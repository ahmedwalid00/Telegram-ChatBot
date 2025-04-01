from dotenv import load_dotenv
import os
from aiogram import Bot, Dispatcher, executor, types
import openai
import sys

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

class Refrenece :
    def __init__(self) -> None:
        self.response =""

refrenece = Refrenece()

bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher(bot)

def clear_past():
    refrenece.response = ""

@dp.message_handler(commands=['clear'])
async def clear(message : types.Message):

    clear_past()
    await message.reply("wello has cleared the past conversation and context !")

@dp.message_handler(commands=['start'])
async def start(message : types.Message):

    await message.reply("Hi\nI am Wello Bot!\Created by Ahmed Walid. How can i assist you?")

@dp.message_handler(commands=['help'])
async def help(message :types.Message):

    help_command = """
    Hi There, I'm Wello bot created by Ahmed walid! Please follow these commands - 
    /start - to start the conversation
    /clear - to clear the past conversation and context.
    /help - to get this help menu.
    I hope this helps. :)
    حصوة في عين الميصلي ع نبي
    """

    await message.reply(help_command)

@dp.message_handler(commands=['who are you'])
async def informing(message : types.Message):
    await message.reply("I am Wello bot \n How can i help you?")

@dp.message_handler()
async def gpt(message :types.Message):

    print(f" USER: \n\t{message.text}")

    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo" , 
        messages = [
            {"role" : "assistant" , "content" : refrenece.response},
            {"role" : "user" , "content" : message.text}
        ]
    )
    refrenece.response = response['choices'][0]['message']['content']

    await bot.send_message(chat_id = message.chat.id, text = refrenece.response)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=False)

