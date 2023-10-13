
def onegroup(message):
    buttons = groups.buttons_course_1
    markup = types.InlineKeyboardMarkup()
    for index, button_text in enumerate(buttons, start=1):
        button = types.InlineKeyboardButton(button_text, callback_data=str(index))
        markup.add(button)

    bot.send_message(message.chat.id, text="Выбери свою группу 1 курса", reply_markup=markup)


def twogroup(message):

    buttons = groups.buttons_course_2
    markup = types.InlineKeyboardMarkup()
    for index, button_text in enumerate(buttons, start=1):
        button = types.InlineKeyboardButton(button_text, callback_data=str(index + 21))
        markup.add(button)

    bot.send_message(message.chat.id, text="Выбери свою группу 2 курса", reply_markup=markup)


def onegroup(message):

    buttons = groups.buttons_course_3
    markup = types.InlineKeyboardMarkup()
    for index, button_text in enumerate(buttons, start=1):
        button = types.InlineKeyboardButton(button_text, callback_data=str(index + 43))
        markup.add(button)

    bot.send_message(message.chat.id, text="Выбери свою группу 3 курса", reply_markup=markup)


def onegroup(message):

    buttons = groups.buttons_course_4
    markup = types.InlineKeyboardMarkup()
    for index, button_text in enumerate(buttons, start=1):
        button = types.InlineKeyboardButton(button_text, callback_data=str(index + 63))
        markup.add(button)
        print(index + 63) 

    bot.send_message(message.chat.id, text="Выбери свою группу 4 курса", reply_markup=markup)


def onegroup(message):

    buttons = groups.buttons_course_5
    markup = types.InlineKeyboardMarkup()
    for index, button_text in enumerate(buttons, start=1):
        button = types.InlineKeyboardButton(button_text, callback_data=str(index + 77))
        markup.add(button)

    bot.send_message(message.chat.id, text="Выбери свою группу 5 курса", reply_markup=markup)