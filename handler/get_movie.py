from telegram import Update, InputMediaPhoto
from telegram.ext import ContextTypes
from services.movie_service import get_movie_service, get_movie_poster_service, get_movie_id_service
from states import GET_MOVIE
from keyboards import choose_movie_keyboard, poster_keyboard
from db import save_user


async def get_movie_details(movie_id):
    data = await get_movie_id_service(movie_id)
    movie_name = data.get('Title')
    year = data.get('Year')
    rating = data.get('imdbRating')
    plot = data.get('Plot')
    text = f'Название: {movie_name}\nГод: {year}\nРейтинг на IMDB: {rating}\nОписание: {plot}'
    return text


async def get_movie_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    movie = update.message.text

    await update.message.reply_text('Пожалуйста подождите мы роемся в библиотеке...')
    data = await get_movie_service(movie)
    if data.get("Response") == "False":
        print(data)
        await update.message.reply_text("Фильм не найден 😢", reply_markup=poster_keyboard())
        return

    movies_name = data["Search"]
    counter = 0
    photos = []
    for movie in movies_name[:5]:
        counter += 1
        photos.append(await get_movie_poster_service(movie['imdbID']))
        context.user_data[f'movie_id_{counter}'] = movie['imdbID']
        context.user_data[f'movie_name_{counter}'] = movie['Title']

    if photos:
        media = [InputMediaPhoto(p) for p in photos[:5]]
        await update.message.reply_media_group(media)
    text = "Найдено:\n\n"
    counter = 0
    for movie in movies_name[:5]:
        counter += 1
        text += f"{counter}) {movie['Title']} ({movie['Year']})\n"
    await update.message.reply_text(text, reply_markup=choose_movie_keyboard())
    await save_user(update.effective_user.id, update.effective_user.username)
    return GET_MOVIE
