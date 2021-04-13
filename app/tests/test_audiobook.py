from flask.helpers import url_for
import pytest
from app import app
from flask import jsonify


@pytest.fixture
def client():
    return app.test_client()


AUDIOBOOK_ID = 0


def test_create_audiobook_ok(client):
    """
    GIVEN a audiobook that with data
    WHEN it is created in the database
    THEN check that it was successfully created
    """

    with app.test_request_context():
        response = client.post(
            url_for("create_audio"),
            json={
                "audioFileType": "audiobook",
                "audioFileMetaData": {
                    "title": "Tale of two cities",
                    "author": "Christopher Walkin",
                    "narrator": "Tom Hiddleston",
                    "duration": 3411
                },
            },
            content_type="application/json",
        )

    assert response.status_code == 200
    res_data = response.data.decode("utf-8")
    assert res_data.startswith("[AUDIOBOOK]")
    assert "Tale of two cities" in res_data
    global AUDIOBOOK_ID
    AUDIOBOOK_ID = int(res_data[res_data.find("(") + 1 : res_data.find(")")])


def test_get_all_audiobook_ok(client):
    """
    GIVEN a audiobook in the database
    WHEN all audiobooks are requested
    THEN check that known audiobook in database
    """

    with app.test_request_context():
        response = client.get(url_for("get_all_audio", audioFileType="audiobook"))

    assert response.status_code == 200
    res_data = response.get_json()
    record = list(filter(lambda x: x["id"] == AUDIOBOOK_ID, res_data))
    assert len(record) == 1
    assert record[0]["title"] == "Tale of two cities"


def test_update_audiobook_ok(client):
    """
    GIVEN a audiobook in the database
    WHEN an update request is made
    THEN check that it was successfully updated
    """

    with app.test_request_context():
        response = client.post(
            url_for("update_audio", audioFileType="audiobook", audioFileID=AUDIOBOOK_ID),
            json={
                "title": "Winery Dawn",
                "author": "J C Penny",
                "narrator": "Micheal Andrew",
                "duration": 3141
            },
            content_type="application/json",
        )

    assert response.status_code == 200
    res_data = response.data.decode("utf-8")
    assert res_data.startswith("[AUDIOBOOK]")
    assert "Winery Dawn" in res_data


def test_get_one_audiobook_ok(client):
    """
    GIVEN a audiobook was updated in the database
    WHEN the specific audiobook data is requested
    THEN check that it was successfully updated
    """

    with app.test_request_context():
        response = client.get(
            url_for("get_audio", audioFileType="audiobook", audioFileID=AUDIOBOOK_ID)
        )

    assert response.status_code == 200
    res_data = response.get_json()
    assert res_data["id"] == AUDIOBOOK_ID
    assert res_data["title"] == "Winery Dawn"


def test_delete_audiobook_ok(client):
    """
    GIVEN a audiobook in the database
    WHEN a delete request is made
    THEN check that it was successfully deleted
    """

    with app.test_request_context():
        response = client.get(
            url_for("delete_audio", audioFileType="audiobook", audioFileID=AUDIOBOOK_ID)
        )

    assert response.status_code == 200
    res_data = response.data.decode("utf-8")
    assert res_data.startswith("[AUDIOBOOK]")
    assert "Winery Dawn" in res_data
