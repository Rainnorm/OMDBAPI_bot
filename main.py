from telegram.ext import CallbackQueryHandler, filters, MessageHandler, ConversationHandler, ApplicationBuilder, CommandHandler
from dotenv import load_dotenv
import os
from handler.start import start
from states import GET_MOVIE, MENU, SEARCH
from handler.cancel import cancel
from handler.get_movie import get_movie_handler
from handler.history import history
from db import init_db
from handler.serach import seacrh
from handler.choose import choose_1, choose_2, choose_3, choose_4, choose_5
load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')


async def on_startup(app):
    await init_db()


def main():
    app = ApplicationBuilder().token(TOKEN).post_init(on_startup).build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
                MENU: [CallbackQueryHandler(history, pattern='history'),
                       CallbackQueryHandler(seacrh, pattern='search')],
                SEARCH: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_movie_handler),
                         CallbackQueryHandler(history, pattern='history')],
                GET_MOVIE: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_movie_handler),
                            CallbackQueryHandler(choose_1, pattern='1'),
                            CallbackQueryHandler(choose_2, pattern='2'),
                            CallbackQueryHandler(choose_3, pattern='3'),
                            CallbackQueryHandler(choose_4, pattern='4'),
                            CallbackQueryHandler(choose_5, pattern='5')]
                },
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    app.add_handler(conv_handler)
    app.run_polling()


if __name__ == "__main__":
    main()