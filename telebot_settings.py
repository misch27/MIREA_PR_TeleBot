from telebot import TeleBot


class TelebotSettings(object):

    def __init__(self, config):
        self._config = config
        self.bot = TeleBot(self._config.get('bot_token'))
