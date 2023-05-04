import pytest
from utils.dicts import get_val


@pytest.fixture
def dict_():
    current_dict = {1: "one", 2: "two", 3: "three", 4: "four"}
    return current_dict


def test_get_val(dict_):
    assert get_val(dict_, 2) == "two"
    assert get_val(dict_, 3) == "three"


def test_get_val_not_key(dict_):
    assert get_val(dict_, 9) == "git"
    assert get_val(dict_, 11, default="tig") == "tig"


def test_get_val_default_value(dict_):
    assert get_val(dict_, 1, default="tig") == "one"


def test_get_val_empty_dict():
    current_dict = {}
    assert get_val(current_dict, 5) == "git"

