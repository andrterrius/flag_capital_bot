from config import *
from aiogram import types
from aiogram import executor
@dp.inline_handler()
async def inline_postbot(query: types.InlineQuery):
    country = query.query.lower() or None
    result = db.get_country(country)
    if result:
        articles = [
        types.InlineQueryResultPhoto(
        	id = country,
            photo_url=result[2],
            thumb_url=result[2],
            ),
        types.InlineQueryResultArticle(
        	id = result[1],
        	title=f"{result[1]} - cтолица страны {query.query}",
        	input_message_content=types.InputTextMessageContent(
                message_text=result[1]
            )
        )
        ]
        await query.answer(articles, cache_time=1)
    else:
    	articles = [types.InlineQueryResultArticle(
    		id = "not_found",
    		title="Страна не найдена",
    		input_message_content=types.InputTextMessageContent(
    			message_text="Не знаю такую страну"
    			)
    		)]
    	return await query.answer(articles, cache_time=1)#Если страна не нашлась в базе, отправляем ответ "Страна не найдена"
@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
		await message.answer("Добро пожаловать! Напишите @flag_capital_bot и страну в поле для ввода текста. \nПример:\n@flag_capital_bot Россия")
if __name__ == '__main__':
	executor.start_polling(dp)