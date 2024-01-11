import os
import logging

import get_info
import telegram
from telegram.ext import CommandHandler, Updater

from dotenv import load_dotenv

from menu import (main_buttons,)


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)


load_dotenv()
secret_token = os.getenv("TOKEN")


def wake_up(update, context):
    chat = update.effective_chat
    name = update.message.chat.first_name

    buttons = main_buttons
    keyboard = telegram.InlineKeyboardMarkup(buttons)

    context.bot.send_message(
        chat_id=chat.id,
        text=('📃 Бот визитка Мокрушина Евгения\n'
              f'{name}, выберите что вас интересует:'),
        reply_markup=keyboard,
    )

def main_menu(update, context):
    chat = update.effective_chat
    name = update.message.chat.first_name

    buttons = main_buttons
    keyboard = telegram.InlineKeyboardMarkup(buttons)

    context.bot.send_message(
        chat_id=chat.id,
        text="Выбери категорию.",
        reply_markup=keyboard,
    )

# Очищаем данные
def reset_conversation(update, context):
    context.user_data.clear()
    return wake_up(update, context)

def main():
    updater = Updater(token=secret_token)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', wake_up))

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
