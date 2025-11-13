from aiogram import Bot, Dispatcher, F  
from aiogram.types import CallbackQuery, Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command, CommandStart
from aiogram.enums import ChatType
from aiogram.utils.keyboard import InlineKeyboardBuilder
import asyncio

API_TOKEN = ''
CHANNEL = ''
bot = Bot(API_TOKEN)
dp = Dispatcher()

@dp.message(F.chat.type.in_({ChatType.GROUP, ChatType.SUPERGROUP}))
async def group_message_hander(message: Message):
	if message.from_user is None or message.from_user.is_bot:
		return

	member = await bot.get_chat_member(CHANNEL, message.from_user.id)
	subscribed = member.status in ['member', 'administrator', 'creator']

	if not subscribed:
		await message.delete()
		kb = InlineKeyboardBuilder()
		kb.button(
			text="Подписаться на канал",
			url=''
		)
		kb.adjust(1)

		await message.answer(
			f"{message.from_user.full_name} чтобы писать в группе подпишись на канал",
			reply_markup=kb.as_markup()
		)

async def main():
	await dp.start_polling(bot)

if __name__ == "__main__":
	asyncio.run(main())
