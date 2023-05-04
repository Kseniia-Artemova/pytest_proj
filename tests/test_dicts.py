import pytest
from utils.dicts import get_val


def test_get_val():
    current_dict = {1: "one", 2: "two", 3: "three", 4: "four"}
    assert get_val(current_dict, 2) == "two"
    assert get_val(current_dict, 3) == "three"


def test_get_val_not_key():
    current_dict = {1: "one", 2: "two", 3: "three", 4: "four"}
    assert get_val(current_dict, 9) == "git"
    assert get_val(current_dict, 11, default="tig") == "tig"


def test_get_val_default_value():
    current_dict = {1: "one", 2: "two", 3: "three", 4: "four"}
    assert get_val(current_dict, 1, default="tig") == "one"


def test_get_val_empty_dict():
    current_dict = {}
    assert get_val(current_dict, 5) == "git"

