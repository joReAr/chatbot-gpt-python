import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler,Filters,CallbackContext
from telegram import Bot
import openai

# Configura el token del bot
TOKEN = '6858827864:AAECfibqzPrpaEDhQN70z_C9ygBKmMsBBYY'

#configura el token de openai
openai.api_key = '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'

# Configura el nivel de logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

logger = logging.getLogger(__name__)

messages = [{"role":"system","content":"eres un experto en psicología"}]

def call_ChatGPT(message):
    if message:
        messages.append(
            {"role": "user", "content": message},
        )
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages 
        )
         
    reply = chat.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})
    return reply;

def handle_text(update: Update,context:CallbackContext):
    message = update.message.text
    chat_id = update.message.chat_id
    try:
        processing_message = context.bot.send_message(chat_id=chat_id,text="consultando..")
        reply = call_ChatGPT(message)
    except:
        reply = "Error llamada de servicio de chatCompletion"
        print(reply)
    context.bot.send_message(chat_id=chat_id,text=reply)
def main():
    updater = Updater(token=TOKEN,use_context=True)

    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text,handle_text))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()