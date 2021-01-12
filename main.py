from containers import Readers, Clients, Configs

if __name__ == "__main__":
    Configs.config.override({
        "bot_token": '1518692021:AAEPJ_2MYUpbNmM4GBFrlF_M2YFoFhtF3uw'
    })

    telebot_service = Readers.telebot_service()
    telebot_service.start_bot()
