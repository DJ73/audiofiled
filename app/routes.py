from app import app
from flask import request
from app.functions.create import insert_audio

@app.route('/')
def base():
    return "Welcome to AudioFiled"

@app.route('/create', methods=['POST'])
def create_audio():
    """
    Expects JSON data object with two keys:
        - audioFileType: a string representing audiotype
        - audioFileMetaData: a JSON object with the required metadata
    """
    request_data = request.get_json()

    db_insert = insert_audio(request_data)

    return db_insert

@app.route('/delete/<any(song, podcast, audiobook):audioFileType>/<int:audioFileID>')
def delete_audio(audioFileType, audioFileID):
    """
    Deletes the corresponding audio file from database
    Returns 404 if not found
    """

    return f"{audioFileID} has been deleted successfully", 200

@app.route('/update/<any(song, podcast, audiobook):audioFileType>/<int:audioFileID>',
methods = ["POST"])
def update_audio(audioFileType, audioFileID):
    """
    Updates an audio file with new metadata
    Returns 200 if successfully updated
    Returns 404 if file with matching parameters not found
    """
    request_data = request.get_json()

    return f"{audioFileID} updated successfully", 200

@app.route('/get/<any(song, podcast, audiobook):audioFileType>')
def get_all_audio(audioFileType):
    """
    Returns all the audio files in database of given type
    """

    return f"{audioFileType}", 200

@app.route('/get/<any(song, podcast, audiobook):audioFileType>/<int:audioFileID>')
def get_audio(audioFileType, audioFileID):
    """
    Returns JSON formatted details of a specific file
    """

    return f"{audioFileType}-{audioFileID}", 200