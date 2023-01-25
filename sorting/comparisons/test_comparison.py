import pytest
from comparison import sort_by_title, sort_by_year
from movies import movies


# Expected test output of test #1
expected_year = ["The Intouchables", "Valkyrie", "Stardust", "Ratatouille", "City of God", "Memento", "The Shawshank Redemption", "Beetlejuice", "Crocodile Dundee", "The Cotton Club"]

# Expected test output of test #2
expected_title = ["Beetlejuice", "City of God", "The Cotton Club", "Crocodile Dundee", "The Intouchables", "Memento", "Ratatouille", "The Shawshank Redemption", "Stardust", "Valkyrie"]

def test_sort_by_year(movies_fixture):
    movies = sort_by_year(movies_fixture)
    actual = [movie.__str__() for movie in movies]
    expected = expected_year
    assert actual == expected

def test_sort_by_title(movies_fixture):
    movies = sort_by_title(movies_fixture)
    actual = [movie.__str__() for movie in movies]
    expected = expected_title
    assert actual == expected

@pytest.fixture
def movies_fixture():
    movie_data = movies
    return movie_data
