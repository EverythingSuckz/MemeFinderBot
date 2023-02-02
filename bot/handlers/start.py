from bot import dp
from aiogram import types, filters

from bot.fym import BASE_URL

@dp.message_handler(filters.Command(commands=["start", "help"], prefixes="!/", ignore_case=False))
@dp.throttled(
    lambda msg, loop, *args, **kwargs: loop.create_task(
        msg.answer(
            "Too many requests, relax!",
            parse_mode=types.ParseMode.MARKDOWN
        )
    ),
    rate=2,
)
async def start(message: types.Message):
    markup = types.InlineKeyboardMarkup()
    markup.row(
        types.InlineKeyboardButton(
                text="Try me",
                switch_inline_query_current_chat=""
        ),
        types.InlineKeyboardButton(
                text="Powered By",
                url=BASE_URL
        )
    )
    await message.answer(f"**Hi {message.from_user.get_mention(as_html=False)}**,\nI can **search memes** for you ;)",
                         parse_mode=types.ParseMode.MARKDOWN_V2,
                         reply_markup=markup)