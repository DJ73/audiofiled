from app.status import Status
from app.models import MODELS, Audio
# , Song, Podcast, Audiobook
from app import db

def insert_audio(audio_data):
    if audio_data["audioFileType"] in MODELS:
        audio = Audio(audio_data["audioFileType"])
        db.session.add(audio)
        db.session.commit()
        afile = MODELS[audio_data["audioFileType"]](id=audio.id, **audio_data["audioFileMetaData"])
        db.session.add(afile)
        db.session.commit()
        return str(afile)
    else:
        return Status(400, "Bad Request: Invalid File Type")