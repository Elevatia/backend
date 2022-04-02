import time
import random
import string

from datetime import date
from pymongo import MongoClient

from src.tools import Tools

class Database:
    def __init__(self):
        self.client = MongoClient("mongodb://mongodb:27017")
        self.database = self.client["database"]
        self.version = "1.0.0"
        self.today = date.today()

        self.tools = Tools()

    def salt(self, size):
        letters = string.digits
        return (''.join(random.choice(letters) for i in range(size)))

    def search(self, id):
        searched = self.database.content.find_one({"id": id})
        content = None

        if (searched != None):
            content = searched["content"]

        return (self.tools.status.builder(self.tools.status.SUCCESS, content))

    def hash(self, content, size):
        raw = ""
        limit = 32

        for i in range(0, size):
            if (i == limit):
                return (raw)
            c = int(hex(content[i]), 0)
            if (c >= 35 and c <= 91):
                raw += chr(c)

        return (raw)

    def id(self, data, size, ip):
        values = "{}{}{}{}".format(
            size,
            self.hash(data, size),
            self.hash(f"{size}", len(f"{size}")),
            self.counter()["content"]
        )

        return (values)

    def counter(self):
        i = 0

        for data in self.database.content.find():
            i += 1
        return (self.tools.status.builder(self.tools.status.SUCCESS, i))

    def upload(self, data, ip):
        size = len(data)
        id = self.id(data, len(data), ip)
        content = self.database.content.insert_one({"id" : id, "content": data, "size" : size})
        status = self.tools.status.builder(self.tools.status.SUCCESS, {"id" : id})

        return (status)

