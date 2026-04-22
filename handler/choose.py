from telegram import Update
from telegram.ext import ContextTypes
from states import SEARCH
from keyboards import poster_keyboard
from handler.get_movie import get_movie_details, get_movie_poster_service
from db import save_history

async def choose_1(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.message.reply_text('Пожалуйста подождите собираем информацию о фильме...')
    
    movie_id = context.user_data['movie_id_1']
    text = await get_movie_details(movie_id)
    await save_history(update.effective_user.id, context.user_data['movie_name_1'])
    await query.message.reply_photo(photo=await get_movie_poster_service(movie_id), caption=text, reply_markup=poster_keyboard())
    
    return SEARCH

async def choose_2(update: Update, context: ContextTypes.DEFAULT_TYPE):
  
    query = update.callback_query
    await query.answer()
    await query.message.reply_text('Пожалуйста подождите собираем информацию о фильме...')
    
    movie_id = context.user_data['movie_id_2']
    text = await get_movie_details(movie_id)
    await save_history(update.effective_user.id, context.user_data['movie_name_2'])
    await query.message.reply_photo(photo=await get_movie_poster_service(movie_id), caption=text, reply_markup=poster_keyboard())
    
    return SEARCH


async def choose_3(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()
    await query.message.reply_text('Пожалуйста подождите собираем информацию о фильме...')    
    movie_id = context.user_data['movie_id_3']
    text = await get_movie_details(movie_id)
    await save_history(update.effective_user.id, context.user_data['movie_name_3'])
    await query.message.reply_photo(photo=await get_movie_poster_service(movie_id), caption=text, reply_markup=poster_keyboard())
    
    return SEARCH


async def choose_4(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()
    await query.message.reply_text('Пожалуйста подождите собираем информацию о фильме...')    
    movie_id = context.user_data['movie_id_4']
    text = await get_movie_details(movie_id)
    await save_history(update.effective_user.id, context.user_data['movie_name_4'])
    await query.message.reply_photo(photo=await get_movie_poster_service(movie_id), caption=text, reply_markup=poster_keyboard())
    
    return SEARCH


async def choose_5(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()
    await query.message.reply_text('Пожалуйста подождите собираем информацию о фильме...')    
    movie_id = context.user_data['movie_id_5']
    text = await get_movie_details(movie_id)
    await save_history(update.effective_user.id, context.user_data['movie_name_5'])
    await query.message.reply_photo(photo=await get_movie_poster_service(movie_id), caption=text, reply_markup=poster_keyboard())
    
    return SEARCH

