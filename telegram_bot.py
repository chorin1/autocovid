import os
from log_helper import set_logger
import telegram

from moe_fill import sign_moe

log = set_logger("telegram-bot")

CHAT_ID = os.environ['CHAT_ID']
bot = telegram.Bot(token=os.environ['TELEGRAM_TOKEN'])


def handle_bot_msg(req):
    # retrieve the message in JSON and then transform it to Telegram object
    update = telegram.Update.de_json(req.get_json(force=True), bot)

    chat_id = update.message.chat.id
    msg_id = update.message.message_id
    text = update.message.text.encode('utf-8').decode()
    log.info(f"got text message : {text}")

    if text == "/start":
        bot_welcome = "Welcome to Kinderbot, this bot will sign covid health certificates for you."
        bot.sendMessage(chat_id=chat_id, text=bot_welcome, reply_to_message_id=msg_id)
    elif text == "/sign" and chat_id == CHAT_ID:
        try:
            bot.sendChatAction(chat_id=chat_id, action="upload_photo")
            bot.send_photo(chat_id, photo=sign_moe())
        except Exception:
            bot.sendMessage(chat_id=chat_id, text="sorry, there was a problem", reply_to_message_id=msg_id)

    return 'ok'
