import pytest
from data_structures.hashtable import Hashtable


def test_exists():
    assert Hashtable


# @pytest.mark.skip("TODO")
def test_get_apple():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    actual = hashtable.get("apple")
    expected = "Used for apple sauce"
    assert actual == expected

# @pytest.mark.skip("TODO")
def test_hashtable():
    hashtable = Hashtable(1024)
    hashtable.set("ahmad", 30)
    hashtable.set("silent", True)
    hashtable.set("listen", "to me")

    assert hashtable.get("ahmad") == 30
    assert hashtable.get("silent") == True
    assert hashtable.get("listen") == "to me"

    assert hashtable.has("ahmad") == True
    assert hashtable.has("silent") == True
    assert hashtable.has("listen") == True
    assert hashtable.has("unknown") == False

    assert set(hashtable.keys()) == {"ahmad", "silent", "listen"}
