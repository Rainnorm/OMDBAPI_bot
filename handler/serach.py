from telegram import Update
from telegram.ext import ContextTypes
from keyboards import poster_keyboard
from states import SEARCH


async def seacrh(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    await query.edit_message_text('Введи название фильма или сериала', reply_markup=poster_keyboard())
    return SEARCH