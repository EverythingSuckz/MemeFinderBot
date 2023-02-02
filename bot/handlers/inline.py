from aiogram import types

from bot import dp
from bot.fym import get_memes



@dp.inline_handler()
async def inline_query_filer(iq: types.InlineQuery):
    user_query = iq.query.strip()
    offset =  int(iq.offset) if iq.offset else 0
    results = []
    text = f"Results for '{user_query}'" if user_query else "Type Something.."
    data = await get_memes(user_query, offset=offset)
    if data:
        for i in data:
            markup = types.InlineKeyboardMarkup()
            markup.row(types.InlineKeyboardButton(
                        text=i.source_site.title(),
                        url=i.source_page_url
            ))
            if i.meme_type == "IMAGE":
                results.append(
                    types.InlineQueryResultPhoto(
                        id=i.file_hash,
                        title=i.meme_file_size,
                        photo_url=i.image_path_url,
                        thumb_url=i.image_path_url,
                        reply_markup=markup
                    )
                )
            else:
                results.append(
                    types.InlineQueryResultVideo(
                        id=i.file_hash,
                        title="Video Result",
                        description="UI looking weird? desktop user? cry about it.",
                        mime_type="video/mp4",
                        thumb_url=i.thumbnail_url,
                        video_url=i.image_path_url,
                        reply_markup=markup
                    )
            )
        await iq.answer(
            results=results,
            cache_time=10,
            switch_pm_text=text,
            switch_pm_parameter="inline",
            next_offset=str(offset + len(results)),
            is_personal=False
        )
    else:
        await iq.answer(
            results=[],
            cache_time=30,
            switch_pm_text="No Results Found",
            switch_pm_parameter="inline",
            is_personal=False
        )