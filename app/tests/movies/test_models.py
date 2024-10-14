import pytest

from movies.models import Movie

@pytest.mark.django_db
def test_movie_model():
    movie = Movie(title="The Big Lebowski", genre="comedy", year="1998")
    movie.save()
    assert movie.title == "The Big Lebowski"
    assert movie.genre == "comedy"
    assert movie.year == "1998"
    assert movie.created_date
    assert movie.updated_date
    assert str(movie) == movie.title
