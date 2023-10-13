def choose_group(message, types, buttons, tg_bot, group_index):
    markup = types.InlineKeyboardMarkup()
    for index, button_text in enumerate(buttons, start=1):
        button = types.InlineKeyboardButton(button_text, callback_data=str(index + group_index))
        markup.add(button)
    tg_bot.send_message(message.chat.id, text=f"Выбери свою группу {message.text}", reply_markup=markup)