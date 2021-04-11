import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):

    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

    def __init__(self) -> None:
        super().__init__()
