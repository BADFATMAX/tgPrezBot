from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo

bot = Bot('6132155227:AAF6BCvohNUMSWvc3OPaCDh8WV6MlUCkpxY')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Ознакомиться с информацией', web_app=WebAppInfo(url='https://badfatmax.github.io/tgPrezBot/')))
    await message.answer('Успешное подключение!', reply_markup=markup)

executor.start_polling(dp)