from app.functions.get import get_all_files, get_file
import re
from app.functions.delete import remove_audio
from app import app
from flask import request
from app.functions.create import insert_audio
from app.functions.delete import remove_audio
from app.functions.update import update_audio


@app.route("/")
def base():
    return "Welcome to AudioFiled"


@app.route("/create", methods=["POST"])
def create_audio():
    """
    Expects JSON data object with two keys:
        - audioFileType: a string representing audiotype
        - audioFileMetaData: a JSON object with the required metadata
    """
    request_data = request.get_json()

    db_insert = insert_audio(request_data)

    return db_insert


@app.route("/delete/<any(song, podcast, audiobook):audioFileType>/<int:audioFileID>")
def delete_audio(audioFileType, audioFileID):
    """
    Deletes the corresponding audio file from database
    Returns 404 if not found
    """

    db_remove = remove_audio(audioFileType, audioFileID)

    return db_remove


@app.route(
    "/update/<any(song, podcast, audiobook):audioFileType>/<int:audioFileID>",
    methods=["POST"],
)
def update_audio(audioFileType, audioFileID):
    """
    Updates an audio file with new metadata
    Returns 200 if successfully updated
    Returns 404 if file with matching parameters not found
    """
    request_data = request.get_json()

    db_update = update_audio(audioFileType, audioFileID, request_data)

    return db_update


@app.route("/get/<any(song, podcast, audiobook):audioFileType>")
def get_all_audio(audioFileType):
    """
    Returns all the audio files in database of given type
    """

    db_get_all = get_all_files(audioFileType)

    return db_get_all


@app.route("/get/<any(song, podcast, audiobook):audioFileType>/<int:audioFileID>")
def get_audio(audioFileType, audioFileID):
    """
    Returns JSON formatted details of a specific file
    """

    db_get_audio = get_file(audioFileType, audioFileID)

    return db_get_audio
