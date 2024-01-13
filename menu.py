from telegram import InlineKeyboardButton

main_buttons = [
    [
        InlineKeyboardButton('🕵️‍♀️ Обо мне', callback_data='aboutme'),
        InlineKeyboardButton('👩‍🎓 Навыки', callback_data='skills'),
    ],
    [
        InlineKeyboardButton('👆 Резюме(Link)', callback_data='cv_link'),
        InlineKeyboardButton('📁 Резюме(PDF)', callback_data='cv_pdf'),
    ],
    [
        InlineKeyboardButton('⛏ Опыт', callback_data='experiance'),
        InlineKeyboardButton('💼 Мои проекты', callback_data='myprojects'),
    ],
    [
        InlineKeyboardButton('☎️ Мои контакты', callback_data='mycontacts'),
    ],
]
