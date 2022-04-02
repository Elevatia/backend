import argparse

class Arguments:
    def __init__(self):
        self.version = "1.0.0"

        self.build()
        self.args = self.parser.parse_args()

    def build(self):
        self.parser = argparse.ArgumentParser(description = "All commands availables")
        self.settings = self.parser.add_argument(
            "-v",
            "--version",
            action = "store_true",
            help = "Display current version",
            required = False
        )

        self.settings = self.parser.add_argument(
            "-s",
            "--search",
            action = "store",
            help = "Search id in database",
            required = False
        )

        self.settings = self.parser.add_argument(
            "-u",
            "--upload",
            action = "+",
            help = "Upload content in database",
            default=[],
            required = False
        )
