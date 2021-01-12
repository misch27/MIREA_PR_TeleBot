from dependency_injector import providers, containers
from telebot_settings import TelebotSettings
from telebot_service import Telebot


class Configs(containers.DeclarativeContainer):
    config = providers.Configuration('config')


class Clients(containers.DeclarativeContainer):
    telebot_settings = providers.Singleton(TelebotSettings, Configs.config)


class Readers(containers.DeclarativeContainer):
    telebot_service = providers.Factory(Telebot, telebot_settngs=Clients.telebot_settings)
