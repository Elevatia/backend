#!/usr/bin/env python3

import os
import sys
import requests
import base64

from src.arguments import Arguments

class Client:
    def __init__(self):
        self.data = None
        self.arguments = Arguments()

        self.run()

    def run(self):
        for argument in self.arguments.arguments:
            if (argument != None and argument != False):
                self.commands[argument]

    def check(self):
        return (os.path.isfile(self.image))

    def upload(self):
        r = requests.post("http://localhost/api/upload", data = self.data)
        if (r.status_code == 200):
            print("[+] success")
        else:
            print(f"[-] server returned {r.status_code}")
        print(r.text)

    def convert(self):
        if (self.check() == True):
            print("[.] converting image")
            with open(self.image, "rb") as image_file:
                data = base64.b64encode(image_file.read())
            self.data = data.decode("utf-8")
        else:
            print("[x] image not found")

if (__name__ == "__main__"):
        Client()
