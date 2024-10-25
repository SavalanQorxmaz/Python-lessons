# import asyncio
# from aiogram import Bot, Dispatcher, F
# from aiogram.types import Message
# from aiogram.filters import CommandStart


# token = '7748829971:AAE_FFwxi4jzFcew7atc_kCCz0NopzoFUIk'
# bot = Bot(token=token)
# dp = Dispatcher()

# @dp.message(CommandStart())
# async def cmd_start(message: Message):
#     await message.answer("Salam Aleykum. Yegin ne demek istediyimi anladin. 😂")

# @dp.message(F.text == 'Necesen?')
# async def answer_to_necesen(message: Message):
#     await message.reply("Wukur, sen necesen? 😂")

# async def main():
#     await dp.start_polling(bot)


# if __name__ == "__main__":
#     asyncio.run(main())