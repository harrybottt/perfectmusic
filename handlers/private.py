import asyncio
from time import time
from datetime import datetime
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/fbedb8914a5f60edf9eec.jpg",
        caption=f"""** ð,ð ððð ðððð ððððð ððððððð ðð ðððððððð ð§ ðð ððð¯ðð¥ð¨ð©ðð ðð² = [ðððððððð ð»â¤ï¸](https://t.me/ZINDA_H_TU_MERE_LIYE_HEART_HACK)
ðââââââââââââââââââââ
âââââââââââââââââââ 
â£âðð«ððð­ð¨ð«ð :-  [ðððððððððð»](https://t.me/ZINDA_H_TU_MERE_LIYE_HEART_HACK)
â£âðð®ð©ð©ð¨ð«ð­ :-  [â¨ððð,ðð¸](https://t.me/BHATAKTI_ATMA_SUPPORT)
â£âðð¢ð¬ðð®ð¬ð¬ :-   [â¨ðððððððð](https://t.me/ABOUT_BHATAKTI)
â£âðð¨ð®ð«ðð  :-   [â¨ðððððâ©ï¸](https://t.me/A_BUT)
â£âðð¨ð¦ð¦ðð§ð :- [âï¸ðððððâï¸](https://t.me/BHATAKTI_ATMA_SUPPORT)
â£âðððð ð :-  [â¨ðððððð](https://t.me/A_BUT/32)
âââââââââââââââââââ
ðð ðð¨ð® ððð¯ð ðð§ð² ðð®ðð¬ð­ð¢ð¨ð§ð¬ ðð§ð ððð¥ð© ðð¡ðð§ ðð¦ ðð² ðð¨ð¬ð¬ = [ðððððððð ðððð ð»](https://t.me/ZINDA_H_TU_MERE_LIYE_HEART_HACK)**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ð¥ Já´ÉªÉ´ Há´Êá´ & Sá´á´á´á´Êá´ â¨", url=f"https://t.me/BHATAKTI_ATMA_MUSIC_bot")
                ]
                
           ]
        ),
    )
    

@Client.on_message(command(["repo"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/fbedb8914a5f60edf9eec.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ð¥ CÊÉªá´á´ Má´ Tá´ Gá´á´ Rá´á´á´ ð", url=f"https://t.me/A_BUT")
                ]
            ]
        ),
    )
