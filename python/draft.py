from datetime import datetime
from typing import Optional
from string import ascii_letters
from random import choice
from os import path


def name_string_generator(length: int = 16) -> str:
    """Generate a random string for file names"""
    name_string = ""
    for letter in range(length):
        name_string += choice(ascii_letters)
    return name_string


def draft_titler(name: Optional[str], now: datetime.now) -> str:
    """Make a title for the file with the date"""
    format = "%d/%m/%Y %H:%M:%S"
    day, time = now.strftime(format).split()

    title = f"{day} {time}"
    if name is not None:
        title = f"{name}\t{title}"

    return title


def draft_file_namer(name: Optional[str], now: datetime.now) -> str:
    """Make a unique file name for the draft"""
    format = "%d_%m_%Y__%H_%M_%S"
    date = now.strftime(format)

    random_string = name_string_generator()

    file_name = f"{date}_{random_string}"
    if name is not None:
        file_name = f"{name.lower()}_{file_name}"

    return file_name


class Draft:
    def __init__(self, name: str, directory: str):
        self.name = name
        self.directory = directory
        self.now = datetime.now()

        self.draft_name = draft_file_namer(self.name, self.now)
        self.draft_title = draft_titler(self.name, self.now)

        self.path = path.join(self.directory, self.draft_name)

        self.write_file()

    def write_file(self):
        file = open(self.path)
        message = self.title + "\n\n"
        file.write(message)
