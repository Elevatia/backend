from src.lib import Lib

class Status:
    def __init__(self):
        self.SUCCESS = "success"
        self.AUTHORIZED = "authorized"

        self.ERROR = "error"
        self.FAIL = "fail"
        self.NOT_AUTHORIZED = "not authorized"

    def builder(self, code, text):
        return ({
            "code" : code.encode("utf-8").hex(),
            "content" : text
        })

class Tools:
    def __init__(self):
        self.status = Status()
        self.lib = Lib()
