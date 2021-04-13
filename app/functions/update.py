from flask import abort
from app import db
from app.models import MODELS, Audio


def modify_audio(audio_type, audio_id, audio_data):
    if audio_type in MODELS:
        audio = Audio.query.filter_by(id=audio_id, type=audio_type).first()
        if audio is None:
            abort(404, description=f"ID {audio_id} not found")
        afile = MODELS[audio_type].query.filter_by(id=audio_id).first()
        if afile is None:
            abort(404, description=f"{audio_type} with ID {audio_id} not found")
        afile.update(**audio_data)
        db.session.commit()
        return f"{afile} updated"
    else:
        abort(400, description="Bad Request: Invalid File Type")
