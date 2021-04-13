from flask.helpers import url_for
import pytest
from app import app
from flask import jsonify


@pytest.fixture
def client():
    return app.test_client()


SONG_ID = 0


def test_create_song_ok(client):
    """
    GIVEN a song that with data
    WHEN it is created in the database
    THEN check that it was successfully created
    """

    with app.test_request_context():
        response = client.post(
            url_for("create_audio"),
            json={
                "audioFileType": "song",
                "audioFileMetaData": {"name": "To the moon and back", "duration": 231},
            },
            content_type="application/json",
        )

    assert response.status_code == 200
    res_data = response.data.decode("utf-8")
    assert res_data.startswith("[SONG]")
    assert "To the moon and back" in res_data
    global SONG_ID
    SONG_ID = int(res_data[res_data.find("(") + 1 : res_data.find(")")])


def test_get_all_song_ok(client):
    """
    GIVEN a song in the database
    WHEN all songs are requested
    THEN check that known song in database
    """

    with app.test_request_context():
        response = client.get(
            url_for("get_all_audio", audioFileType="song")
        )

    assert response.status_code == 200
    res_data = response.get_json()
    record = list(filter(lambda x: x["id"]==SONG_ID, res_data))
    assert len(record) == 1
    assert record[0]["name"] == "To the moon and back"


def test_update_song_ok(client):
    """
    GIVEN a song in the database
    WHEN an update request is made
    THEN check that it was successfully updated
    """

    with app.test_request_context():
        response = client.post(
            url_for("update_audio", audioFileType="song", audioFileID=SONG_ID),
            json={"name": "November remember", "duration": 231},
            content_type="application/json",
        )

    assert response.status_code == 200
    res_data = response.data.decode("utf-8")
    assert res_data.startswith("[SONG]")
    assert "November remember" in res_data

def test_get_one_song_ok(client):
    """
    GIVEN a song was updated in the database
    WHEN the specific song data is requested
    THEN check that it was successfully updated
    """

    with app.test_request_context():
        response = client.get(
            url_for("get_audio", audioFileType="song", audioFileID=SONG_ID)
        )

    assert response.status_code == 200
    res_data = response.get_json()
    assert res_data["id"] == SONG_ID
    assert res_data["name"] == "November remember"


def test_delete_song_ok(client):
    """
    GIVEN a song in the database
    WHEN a delete request is made
    THEN check that it was successfully deleted
    """

    with app.test_request_context():
        response = client.get(
            url_for("delete_audio", audioFileType="song", audioFileID=SONG_ID)
        )

    assert response.status_code == 200
    res_data = response.data.decode("utf-8")
    assert res_data.startswith("[SONG]")
    assert "November remember" in res_data