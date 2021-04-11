class Status(object):
    def __init__(self, code, message) -> None:
        super().__init__()
        self.code = code
        self.message = message