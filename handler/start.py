from telegram import Update
from telegram.ext import ContextTypes
from states import MENU
from keyboards import menu_keyboard


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        'Привет! Выбери действие:',
        reply_markup=menu_keyboard()
    )
    return MENU
