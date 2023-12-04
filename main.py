import openai
from telegram import Update
from telegram.ext import Updater,CommandHandler, CallbackContext, ApplicationBuilder
import logging
import asyncio

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

openai.api_key = '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'

async def start():
    pass

def main():
    application = ApplicationBuilder().token('6858827864:AAECfibqzPrpaEDhQN70z_C9ygBKmMsBBYY').build()
    
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    
    application.run_polling()



messages = []
system_msg = input("What type of chatbot would you like to create?\n")
messages.append({"role": "system", "content": system_msg})

messages = [{"role":"system","content":"Eres un experto en psicologia"}]

def chatbotgpt(input):
    messages.append({"role":"user","content":input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages 
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply


if __name__ == "__main__":
    main()
# print("Your new assistant is ready!")
# while input != "quit()":
#     message = input()
#     messages.append({"role": "user", "content": message})
#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=messages)
#     reply = response["choices"][0]["message"]["content"]
#     messages.append({"role": "assistant", "content": reply})
#     print("\n" + reply + "\n")
        
# updater = Updater(bot=TELEGRAM_TOKEN, use_context=True)

# # Define un manejador de comandos
# def start(update: Update, context: CallbackContext) -> None:
#     update.message.reply_text('¡Hola! Soy un bot de chat alimentado por GPT. Envíame un mensaje y te responderé.')

# # Define un manejador de mensajes
# def handle_message(update: Update, context: CallbackContext) -> None:
#     # Obtén el mensaje del usuario
#     user_message = update.message.text

#     # Utiliza GPT para generar una respuesta
#     gpt_response = openai.Completion.create(
#         engine="text-davinci-003",
#         prompt=user_message,
#         max_tokens=150
#     )

#     # Envía la respuesta al usuario
#     update.message.reply_text(gpt_response['choices'][0]['text'])

# # Configura los manejadores
# updater.dispatcher.add_handler(CommandHandler('start', start))
# updater.dispatcher.add_handler(MessageHandler(filters.Filters.text & ~filters.Filters.command, handle_message))

# # Inicia el bot
# updater.start_polling()
# updater.idle()