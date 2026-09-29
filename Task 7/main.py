from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

movies = []


# Movie data
class Movie(BaseModel):
    name: str
    rating: int


# Add movie
@app.post("/addmovie")
def add_movie(movie: Movie):

    # Check rating
    if movie.rating < 1 or movie.rating > 10:
        raise HTTPException(
            status_code=400,
            detail="Rating must be between 1 and 10"
        )

    movies.append(movie)

    return {
        "message": "Movie added successfully",
        "movie": movie
    }


# Get all movies
@app.get("/getmovies")
def get_movies():
    return {
        "movies": movies
    }


# Update movie
@app.put("/updatemovie/{index}")
def update_movie(index: int, movie: Movie):

    if index < 0 or index >= len(movies):
        raise HTTPException(
            status_code=404,
            detail="Movie not found"
        )

    # Check rating
    if movie.rating < 1 or movie.rating > 10:
        raise HTTPException(
            status_code=400,
            detail="Rating must be between 1 and 10"
        )

    movies[index] = movie

    return {
        "message": "Movie updated successfully",
        "movie": movie
    }


# Delete movie
@app.delete("/deletemovie/{index}")
def delete_movie(index: int):

    if index < 0 or index >= len(movies):
        raise HTTPException(
            status_code=404,
            detail="Movie not found"
        )

    deleted_movie = movies.pop(index)

    return {
        "message": "Movie deleted successfully",
        "movie": deleted_movie
    }


# JSON format for adding a movie:
#
# {
#     "name": "Inception",
#     "rating": 9
# }
#
# Rating must be between 1 and 10.