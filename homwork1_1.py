

from aiogram import Bot, Dispatcher, types, executor
from config import token



logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item = types.KeyboardButton("Угадай число")
    markup.add(item)
    
    await message.answer("Привет! Я загадал число от 1 до 3. Попробуйте угадать.", reply_markup=markup)

@dp.message_handler(func=lambda message: True)
async def guess_number(message: types.Message):
    if message.text == "Угадай число":
        random_number = random.randint(1, 3)
        
        markup = types.ReplyKeyboardRemove()
        
        await message.answer("Я загадал число от 1 до 3. Введите ваш вариант:", reply_markup=markup)
    else:
        try:
            guess = int(message.text)
            if guess == random_number:
                await message.answer("Правильно! Вы отгадали.")
                await message.answer_photo(photo=InputFile("https://media.makeameme.org/created/you-win-nothing-b744e1771f.jpg"))
            else:
                await message.answer("Извините, вы не угадали. Я загадал число {}.".format(random_number))
                await message.answer_photo(photo=InputFile("https://media.makeameme.org/created/sorry-you-lose.jpg"))
        except ValueError:
            await message.answer("Пожалуйста, введите число.")

if __name__ == '__main__':
    from aiogram import executor

    executor.start_polling(dp, skip_updates=True)
