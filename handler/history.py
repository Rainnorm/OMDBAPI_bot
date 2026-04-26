from telegram import Update
from telegram.ext import ContextTypes
from db import get_history
from states import SEARCH
from keyboards import search_keyboard

async def history(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query

    await query.answer()
    pool = context.application.bot_data["pool"]
    history = await get_history(pool, update.effective_user.id)
    if not history:
        await query.message.reply_text('История пуста', reply_markup=search_keyboard())
        return
    
    text = "Твоя история запросов:\n\n"

    for row in history:
        movie = row[2]
        created_at = row[3]

        text += f'- {movie} --- {created_at}\n'
    await query.message.reply_text(f'{text}\n\n\nЧтобы продолжить поиск просто ввведи название фильма')
    return SEARCH
