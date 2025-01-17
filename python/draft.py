from datetime import datetime
from typing import Optional, List, Tuple
from string import ascii_letters
from random import choice
from os import path, listdir

OUTFILE_PATH = "/tmp/draft-viewer-temp-file"


def name_string_generator(length: int = 16) -> str:
    """Generate a random string for file names"""
    name_string = "".join(choice(ascii_letters) for _ in range(length))
    return name_string


def draft_titler(name: Optional[str], now: datetime) -> str:
    """Make a title for the file with the date"""
    format = "%m/%d/%Y %H:%M:%S"
    day, time = now.strftime(format).split()

    title = f"{day} {time}\n<!-- Using {format} -->"
    if name is not None:
        title = f"{name}\t{title}"

    return title


def draft_file_namer(name: Optional[str], now: datetime) -> str:
    """Make a unique file name for the draft"""
    format = "%d_%m_%Y__%H_%M_%S"
    date = now.strftime(format)

    random_string = name_string_generator()

    file_name = f"{date}_{random_string}"
    if name is not None:
        name = name.lower()

        # Replace characters that should not be in the filename
        for x in ["(", ")", "/", " ", "~"]:
            if x in name:
                name = name.replace(x, "_")

        file_name = f"{name}_{file_name}"

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
        file = open(self.path, "w")
        message = self.draft_title + "\n\n"
        file.write(message)


def search_single_word(directory: str, word: str) -> List[str]:

    matching_paths = []
    paths = listdir(directory)

    for j_path in paths:
        full_path = path.join(directory, j_path)

        with open(full_path) as file:
            try:
                text = file.read()
                num = text.count(word)

                if num > 0:
                    matching_paths.append((num, full_path))
            except UnicodeDecodeError:
                # file is not a text file
                num = 0

    return matching_paths


def open_draft_viewer(outfile_path: str, entries: List[Tuple[int, str]]):
    with open(outfile_path, "w") as file:
        file.write("=== Draft Viewer ===\n\n")

        if len(entries) > 0:
            # Write header
            file.write("#\tcount\tpath\n")

            order = []
            for entry in entries:
                count = str(entry[0]).ljust(5)
                order.append((entry, count,))

            # Sort by count
            order.sort(key=lambda x: int(x[1]), reverse=True)

            for a, o in enumerate(order):
                n = a + 1
                entry, count = o
                file.write(f"{n}.\t{count}\t{entry[1]}\n")
        else:
            file.write("Search term not found\n")


def list_drafts(directory: str) -> list:
    return listdir(directory)
