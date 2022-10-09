from aiogram import types
from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from loader import dp
from video_down_func import tk
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.builtin import CallbackQuery

@dp.message_handler(Text(startswith='https://www.tiktok.com'))
async def test(message:types.Message):
    video_send = tk(message.text)
    video_send_btn_music = video_send['music']
    video_send_btn_watermark = video_send['original_vid']
    video_send_btn = InlineKeyboardMarkup(
        inline_keyboard = [
            [InlineKeyboardButton(text="Musiqani yuklab olish",url="{}".format(video_send_btn_music))],
            [InlineKeyboardButton(text="Tik Tok belgisi bilan yuklash",url="{}".format(video_send_btn_watermark))],
        ]
    )

    await message.answer_audio(video_send['video'],reply_markup=video_send_btn,)

@dp.message_handler(Text)