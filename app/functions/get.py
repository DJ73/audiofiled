from flask import abort, jsonify
from app import db
from app.models import MODELS, Audio


def get_file(audio_type, audio_id):
    if audio_type not in MODELS:
        abort(400, description="Bad Request: Invalid File Type")
    if Audio.query.filter_by(id=audio_id).first() is None:
        abort(404, description=f"ID {audio_id} not found")
    afile = MODELS[audio_type].query.filter_by(id=audio_id).first()
    if afile is None:
        abort(404, description=f"{audio_type} with ID {audio_id} not found")
    else:
        return jsonify(afile.serialize())


def get_all_files(audio_type):
    if audio_type not in MODELS:
        abort(400, description="Bad Request: Invalid File Type")
    afiles = MODELS[audio_type].query.all()
    return jsonify([a.serialize() for a in afiles])
