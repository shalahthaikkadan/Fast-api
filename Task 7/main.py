from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


# Temporary storage
movies = [
    {"id": 1, "name": "Inception", "rating": 9},
    {"id": 2, "name": "Interstellar", "rating": 10}
]


# Data model
class Movie(BaseModel):
    name: str
    rating: int


# CREATE
@app.post("/movies")
def create_movie(movie: Movie):

    # Check rating
    if movie.rating < 1 or movie.rating > 10:
        raise HTTPException(
            status_code=400,
            detail="Rating must be between 1 and 10"
        )

    new_id = len(movies) + 1

    new_movie = {
        "id": new_id,
        "name": movie.name,
        "rating": movie.rating
    }

    movies.append(new_movie)

    return new_movie


# READ - Get all movies
@app.get("/movies")
def get_movies():
    return movies


# READ - Get movie by ID
@app.get("/movies/{movie_id}")
def get_movie(movie_id: int):

    for movie in movies:

        if movie["id"] == movie_id:
            return movie

    raise HTTPException(
        status_code=404,
        detail="Movie not found"
    )


# UPDATE
@app.put("/movies/{movie_id}")
def update_movie(movie_id: int, movie: Movie):

    if movie.rating < 1 or movie.rating > 10:
        raise HTTPException(
            status_code=400,
            detail="Rating must be between 1 and 10"
        )

    for existing_movie in movies:

        if existing_movie["id"] == movie_id:

            existing_movie["name"] = movie.name
            existing_movie["rating"] = movie.rating

            return existing_movie

    raise HTTPException(
        status_code=404,
        detail="Movie not found"
    )


# DELETE
@app.delete("/movies/{movie_id}")
def delete_movie(movie_id: int):

    for movie in movies:

        if movie["id"] == movie_id:

            movies.remove(movie)

            return {
                "message": "Movie deleted successfully"
            }

    raise HTTPException(
        status_code=404,
        detail="Movie not found"
    )