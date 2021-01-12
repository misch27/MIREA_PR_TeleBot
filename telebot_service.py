from telebot import TeleBot, types


def display_good_luck_button(self, chat_id):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="👏👏👏 Пожелай мне удачи 👏👏👏", callback_data="good_luck"))
    self._telebot_settings.bot.send_message(chat_id, "Нажми на кнопку 👀", reply_markup=keyboard)


def send_good_luck(self, chat_id, callback_data):
    if callback_data == "good_luck":
        self._telebot_settings.bot.send_message(
            chat_id,
            "😃Руководство МИРЭА от всей души желает тебе сдать всю сессию на отличные оценки!😃"
        )

        self._telebot_settings.bot.send_message(
            chat_id,
            """А если ты еще не решил, куда поступать, то поступай к нам!😘 \n
Тут ты узнаешь, как сделать такого бота, а также много другого! \n
🎉🎉🎉Переходи на сайт приемной комиссии https://priem.mirea.ru/ и подавай документы на наши направления!🎉🎉🎉"""
        )

        self._telebot_settings.bot.send_message(
            chat_id,
            "Встретимся в следующем учебном году!✌"
        )


class Telebot(object):

    def __init__(self, telebot_settngs):
        try:
            self._telebot_settings = telebot_settngs

            @self._telebot_settings.bot.message_handler(commands=["start"])
            def cmd_start(message):
                print(message)
                display_good_luck_button(self, message.chat.id)

            @self._telebot_settings.bot.callback_query_handler(func=lambda call: True)
            def callback_inline(call):
                print(call)
                send_good_luck(self, call.message.chat.id, call.data)

        except Exception as e:
            raise e

    def start_bot(self):
        self._telebot_settings.bot.polling()
