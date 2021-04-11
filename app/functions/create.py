from app.models import MODELS, Audio
from app import db
from flask import abort


def insert_audio(audio_data):
    if audio_data["audioFileType"] in MODELS:
        audio = Audio(audio_data["audioFileType"])
        db.session.add(audio)
        db.session.commit()
        afile = MODELS[audio_data["audioFileType"]](
            id=audio.id, **audio_data["audioFileMetaData"]
        )
        db.session.add(afile)
        db.session.commit()
        return f"{afile.name} inserted"
    else:
        return abort(400, description="Bad Request: Invalid File Type")
