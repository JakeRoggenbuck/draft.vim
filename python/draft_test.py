import pytest
from draft import name_string_generator, draft_titler, draft_file_namer
from datetime import datetime


def test_name_string_generator():
    # Check for repeats
    names = []
    for _ in range(20):
        names.append(name_string_generator())

    assert len(set(names)) == len(names)


def test_draft_titler():
    a = draft_titler("test", datetime.now())
    assert "test" in a

    b = draft_titler(None, datetime.now())
    assert "test" not in b


def test_draft_file_namer():
    a = draft_file_namer("a)b", datetime.now())
    assert "a)b" not in a
    assert "a_b" in a

    b = draft_file_namer("))((~~", datetime.now())
    assert "))((~~" not in b
    assert "______" in b
