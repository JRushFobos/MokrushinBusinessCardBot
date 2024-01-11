from telegram import InlineKeyboardButton

main_buttons = [
    [
        InlineKeyboardButton("🕵️‍♀️ Обо мне", callback_data="aboutme"),
        InlineKeyboardButton("📁 Резюме", callback_data="cv"),
    ],
    [
        InlineKeyboardButton("👩‍🎓 Навыки", callback_data="hardskills"),
        InlineKeyboardButton("💼 Мои проекты", callback_data="myprojects"),
    ],
    [
        InlineKeyboardButton("⛏ Опыт", callback_data="experiance"),
        InlineKeyboardButton("🧒 Фотографии", callback_data="photo"),
    ],
]
