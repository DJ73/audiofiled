from app.models import MODELS, Audio
from app import db
from flask import abort


def remove_audio(audio_type, audio_id):
    if audio_type in MODELS:
        audio = Audio.query.filter_by(id=audio_id, type=audio_type).first()
        if audio is None:
            abort(404, description=f"ID {audio_id} not found")
        afile = MODELS[audio_type].query.filter_by(id=audio_id).first()
        if afile is None:
            abort(404, description=f"{audio_type} with ID {audio_id} not found")
        db.session.delete(afile)
        db.session.commit()
        db.session.delete(audio)
        db.session.commit()
        return f"{afile} deleted"
    else:
        abort(400, description="Bad Request: Invalid File Type")
