import os
from telegram import Bot

def sendMessage(data):
    tg_bot = Bot(token=os.environ['5101431961:AAG2JeVnA0R4BKpTbbc3WgpN-violnjgBOU'])
    channel = os.environ['-1001786420647']

    try:
        print('--->Sending message to telegram')
        tg_bot.sendMessage(
            channel,
            data,
            parse_mode="MARKDOWN",
        )
        return True
    except KeyError:
        print('--->Key error - sending error to telegram')
        tg_bot.sendMessage(
            channel,
            data,
            parse_mode="MARKDOWN",
        )
    except Exception as e:
        print("[X] Telegram Error:\n>", e)
    return False
