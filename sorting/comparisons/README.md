# Sorting: Comparisons

## Challenge

In the first half of this code challenge, you will write functions which sort domain objects. Your functions will receive an array of Movie objects. Each Movie object has a title (string), a year (number), and a list of genres (array of strings). One function will sort the movies by most recent year first. One function will sort the movies, alphabetical by title, but will ignore any leading “A”s, “An”s, or “The”s.

In the second half of the code challenge, you will write tests for your comparator functions. This may necessitate refactoring the code you wrote in part one. Your tests will need to call the comparator functions directly, and make assertions about the response values given test inputs.

## Functions

* `create_movies`
  * Takes in a dictionary of movies and coverts to a `Movie` class
  * The purpose of this function is to simplify handling of the movie data in other functions and to keep all movies formatted the same with access to the same methods
* `class Movie`
  * Creates a `Movie` with the following attributes:
    * `title`
    * `year`
    * `genres`
  * To represent the `Movie` class in a printed value to the user, we use the following `__str__` method:

    ```py
    def __str__(self):
      return self.title
    ```

    * This will return the title of the movie to the user in printed form
* `sort_by_year`
  * Takes in a dictionary of movies and passes them to `create_movies`
  * Sorts `Movies` by `year` in descending order (most recent first), then by `title`
* `sort_by_title`
  * Takes in a dictionary of movies and passes them to `create_movies`
  * Sorts `Movies` by `title` in alphabetical order
  * Function ignores leading `A`, `An`, and `The` in the `title` of the movie

## Tests

* To test, we create a `movies_fixture` using `pytest`
* This fixture gives us the dictionary of movies from our `movies.py` file and makes it available to all test functions
* `test_sort_by_year`
  * Confirms that the function correctly sorts the `movies_fixture` first by the most recent year, then by title of the movie
* `test_sort_by_title`
  * Confirms that the function correctly sorts the `movies_fixture` by title, ignoring any leading `A`, `An`, and `The` words in the title

## Whiteboard

![Whiteboard](./wb.JPG)
