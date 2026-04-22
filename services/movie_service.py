import httpx
import os
from dotenv import load_dotenv
load_dotenv()
OMDB_API_TOKEN = os.getenv('OMDB_API_TOKEN')
DEFAULT_POSTER = 'https://wku.edu.kz/images/noimage.jpg'

async def get_movie_service(movie_name: str):
    url = "https://www.omdbapi.com/?"  # лучше https

    params = {
        "apikey": OMDB_API_TOKEN,
        "s": movie_name
    }
    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)

        return response.json()


async def get_movie_id_service(movie_id: str):
    url = "https://www.omdbapi.com/?"  # лучше https

    params = {
        "apikey": OMDB_API_TOKEN,
        "i": movie_id
    }
    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)
        return response.json()


async def get_movie_poster_service(imdbID: str):
    url = "http://img.omdbapi.com/?"  # лучше https

    params = {
        "apikey": OMDB_API_TOKEN,
        "i": imdbID
    }
    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)
        if response.status_code != 200:
            response = DEFAULT_POSTER
        
        return response
