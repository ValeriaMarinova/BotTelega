import telebot
import config

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['website'])
def open_website(message):
	markup = types.InlineKeyboardMarkup()
	markup.add(types.InlineKeyboardButton(url = "https://hd.kinopoisk.ru/?utm_source=google_search&utm_medium=paid_performance&utm_campaign=9781770628|GA_[KP-P]_{WS:S}_RU-225_goal-HD_Category-Generic&utm_term=%D0%BA%D0%B8%D0%BD%D0%BE%20%D0%BE%D0%BD%D0%BB%D0%B0%D0%B9%D0%BD%20%D1%81%D0%BC%D0%BE%D1%82%D1%80%D0%B5%D1%82%D1%8C%20%D0%B1%D0%B5%D1%81%D0%BF%D0%BB%D0%B0%D1%82%D0%BD%D0%BE.[e]&utm_content=INTid|kwd-306397509342|cid|9781770628|gid|99024766279|aid|446700930422|pos||src|g_|dvc|c|kpid|0&source=kinopoisk_paid_performance_google_search_9781770628|ucnt_INTid|kwd-306397509342|cid|9781770628|gid|99024766279|aid|446700930422|pos||src|g_|dvc|c|kpid|0&gclid=Cj0KCQjw0rr4BRCtARIsAB0_48MqxcUhc7s8Y7J5DqV9Zro8n5TP20Ail0qzg-m5Aulffc8rwlzoDakaArX_EALw_wcB"))
	bot.send_message(message.chat.id, )

keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('фильмы', 'сериалы')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, выбери фильм или сериал', reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'фильмы':
        bot.send_message(message.chat.id,  "Выберите жанр:  \nБоевики \nhttps://www.kinopoisk.ru/lists/navigator/action/?limit=20&tab=best \nУжасы \nhttps://www.kinopoisk.ru/lists/editorial/top_100_horrors_by_best_horror_movies/?tab=all \nТриллеры \n https://www.filmpro.ru/amp/materials/62600")
       
    elif message.text.lower() == 'сериалы':
        bot.send_message(message.chat.id, "Выберите жанр:  \nКомедии \nhttps://www.kinopoisk.ru/lists/navigator/comedy/?quick_filters=serials&limit=20&tab=best \nДрамы \nhttps://www.filmpro.ru/series/selections/69400 \nБоевики \nhttps://www.filmpro.ru/materials/selections/71990")
    

bot.polling(none_stop=True)