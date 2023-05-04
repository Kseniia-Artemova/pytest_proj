from utils import arrs
import pytest


@pytest.fixture
def coll():
    collection = [1, 2, 3, 4, 5, 6]
    return collection


def test_get(coll):
    assert arrs.get(coll, 1, "test") == 2


def test_get_empty_collection():
    assert arrs.get([], 0, "test") == "test"


def test_slice(coll):
    assert arrs.my_slice(coll, 1, 3) == [2, 3]
    assert arrs.my_slice(coll, 1) == [2, 3, 4, 5, 6]
    assert arrs.my_slice(coll, -3, -1) == [4, 5]
    assert arrs.my_slice(coll, -9, 2) == [1, 2]


def test_slice_empty_collection():
    assert arrs.my_slice([], 1, 4) == []
