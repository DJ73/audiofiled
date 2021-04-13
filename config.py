import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):

    # Hack to convert postgres to postgresql in Heroku
    DATABASE_URL = os.environ.get("DATABASE_URL")
    i = DATABASE_URL.find("://")
    DATABASE_URL = "postgresql" + DATABASE_URL[i:]
    SQLALCHEMY_DATABASE_URI = DATABASE_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    def __init__(self) -> None:
        super().__init__()
