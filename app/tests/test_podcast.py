from flask.helpers import url_for
import pytest
from app import app
from flask import jsonify


@pytest.fixture
def client():
    return app.test_client()


PODCAST_ID = 0


def test_create_podcast_ok(client):
    """
    GIVEN a podcast that with data
    WHEN it is created in the database
    THEN check that it was successfully created
    """

    with app.test_request_context():
        response = client.post(
            url_for("create_audio"),
            json={
                "audioFileType": "podcast",
                "audioFileMetaData": {
                    "name": "Inedible plants",
                    "host": "Nestle",
                    "participants": ["Cadbury", "Jimmy"],
                    "duration": 231
                    },
            },
            content_type="application/json",
        )

    assert response.status_code == 200
    res_data = response.data.decode("utf-8")
    assert res_data.startswith("[PODCAST]")
    assert "Inedible plants" in res_data
    global PODCAST_ID
    PODCAST_ID = int(res_data[res_data.find("(") + 1 : res_data.find(")")])


def test_get_all_podcast_ok(client):
    """
    GIVEN a podcast in the database
    WHEN all podcasts are requested
    THEN check that known podcast in database
    """

    with app.test_request_context():
        response = client.get(url_for("get_all_audio", audioFileType="podcast"))

    assert response.status_code == 200
    res_data = response.get_json()
    record = list(filter(lambda x: x["id"] == PODCAST_ID, res_data))
    assert len(record) == 1
    assert record[0]["name"] == "Inedible plants"


def test_update_podcast_ok(client):
    """
    GIVEN a podcast in the database
    WHEN an update request is made
    THEN check that it was successfully updated
    """

    with app.test_request_context():
        response = client.post(
            url_for("update_audio", audioFileType="podcast", audioFileID=PODCAST_ID),
            json={"name": "Hubble Space", "host": "Neil Tyson", "participants": ["NatGeo", "Tangerine"], "duration": 231},
            content_type="application/json",
        )

    assert response.status_code == 200
    res_data = response.data.decode("utf-8")
    assert res_data.startswith("[PODCAST]")
    assert "Hubble Space" in res_data


def test_get_one_podcast_ok(client):
    """
    GIVEN a podcast was updated in the database
    WHEN the specific podcast data is requested
    THEN check that it was successfully updated
    """

    with app.test_request_context():
        response = client.get(
            url_for("get_audio", audioFileType="podcast", audioFileID=PODCAST_ID)
        )

    assert response.status_code == 200
    res_data = response.get_json()
    assert res_data["id"] == PODCAST_ID
    assert res_data["name"] == "Hubble Space"


def test_delete_podcast_ok(client):
    """
    GIVEN a podcast in the database
    WHEN a delete request is made
    THEN check that it was successfully deleted
    """

    with app.test_request_context():
        response = client.get(
            url_for("delete_audio", audioFileType="podcast", audioFileID=PODCAST_ID)
        )

    assert response.status_code == 200
    res_data = response.data.decode("utf-8")
    assert res_data.startswith("[PODCAST]")
    assert "Hubble Space" in res_data
