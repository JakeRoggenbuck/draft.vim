from datetime import datetime
from typing import Optional
from string import ascii_letters
from random import choice


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
    def __init__(self):
        pass

    def new(self, name: bool = None):
        now = datetime.now()
        draft_name = draft_file_namer(name, now)
        draft_title = draft_titler(name, now)
        print(draft_name)
        print(draft_title)


if __name__ == "__main__":
    draft = Draft()
    draft.new()

    draft.new("Heyy")
