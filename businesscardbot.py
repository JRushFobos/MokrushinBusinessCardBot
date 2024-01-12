import logging
import os

import telegram
from dotenv import load_dotenv
from telegram.ext import CallbackQueryHandler, CommandHandler, Updater

import text
from menu import main_buttons

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
        text=(
            "📃 Бот визитка Мокрушина Евгения\n"
            f"{name}, выберите что вас интересует:"
        ),
        reply_markup=keyboard,
    )


def main_menu(update, context):
    chat = update.effective_chat

    buttons = main_buttons
    keyboard = telegram.InlineKeyboardMarkup(buttons)

    context.bot.send_message(
        chat_id=chat.id,
        text="Выберите интересующую вас категорию:",
        reply_markup=keyboard,
    )


def about_me(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat.id, text=text.about_me)
    main_menu(update, context)


def skills(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat.id, text=text.skills)
    main_menu(update, context)


def cv_link(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat.id, text=text.cv_link)
    main_menu(update, context)


def cv_pdf(update, context):
    chat = update.effective_chat
    pdf_file = "cv.pdf"
    context.bot.send_document(chat.id, document=open(pdf_file, "rb"))
    main_menu(update, context)


def work_experience(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat.id, text=text.work_experience)
    main_menu(update, context)


def myprojects(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat.id, text=text.myprojects)
    main_menu(update, context)


def mycontacts(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat.id, text=text.mycontacts)
    main_menu(update, context)


# Очищаем данные
def reset_conversation(update, context):
    context.user_data.clear()
    return wake_up(update, context)


def main():
    updater = Updater(token=secret_token)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", wake_up))
    dp.add_handler(CallbackQueryHandler(about_me, pattern="aboutme"))
    dp.add_handler(CallbackQueryHandler(skills, pattern="skills"))
    dp.add_handler(CallbackQueryHandler(cv_link, pattern="cv_link"))
    dp.add_handler(CallbackQueryHandler(cv_pdf, pattern="cv_pdf"))
    dp.add_handler(CallbackQueryHandler(work_experience, pattern="experiance"))
    dp.add_handler(CallbackQueryHandler(myprojects, pattern="myprojects"))
    dp.add_handler(CallbackQueryHandler(mycontacts, pattern="mycontacts"))

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
