def choose_group(message, types, buttons, tg_bot, group_index):
    markup = types.InlineKeyboardMarkup()
    for index, button_text in enumerate(buttons, start=1):
        button = types.InlineKeyboardButton(button_text, callback_data=str(index + group_index))
        markup.add(button)
    tg_bot.send_message(message.chat.id, text=f"Выбери свою группу {message.text}", reply_markup=markup)

def choose_day(message, types, tg_bot):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("1 курс", "2 курс", "3 курс", "4 курс", "5 курс")
    tg_bot.send_message(message.chat.id, text="Привет, Я бот для просмотра расписания.\n\nКакой у тебя курс?", reply_markup=markup)