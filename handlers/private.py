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
        caption=f"""** 𝐈,𝐌 𝐓𝐇𝐄 𝐁𝐄𝐒𝐓 𝐌𝐔𝐒𝐈𝐂 💙𝐏𝐋𝐀𝐘𝐄𝐑 𝐈𝐍 𝐓𝐄𝐋𝐄𝐆𝐑𝐀𝐌 🎧 𝐕𝐂 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐝 𝐁𝐲 = [𝐁𝐇𝐀𝐓𝐀𝐊𝐓𝐈 👻❤️](https://t.me/ZINDA_H_TU_MERE_LIYE_HEART_HACK)
👑━━━━━━━━━━━━━━━━━━━━
┏━━━━━━━━━━━━━━━━━┓ 
┣★𝐂𝐫𝐞𝐚𝐭𝐨𝐫👑 :-  [👑𝐁𝐇𝐀𝐓𝐀𝐊𝐓𝐈👻](https://t.me/ZINDA_H_TU_MERE_LIYE_HEART_HACK)
┣★𝐒𝐮𝐩𝐩𝐨𝐫𝐭 :-  [✨𝐁𝐎𝐓,𝐒🎸](https://t.me/BHATAKTI_ATMA_SUPPORT)
┣★𝐃𝐢𝐬𝐜𝐮𝐬𝐬 :-   [✨𝐁𝐇𝐀𝐓𝐀𝐊𝐓𝐈](https://t.me/ABOUT_BHATAKTI)
┣★𝐒𝐨𝐮𝐫𝐜𝐞  :-   [✨𝐂𝐋𝐈𝐂𝐊↩️](https://t.me/A_BUT)
┣★𝐂𝐨𝐦𝐦𝐚𝐧𝐝 :- [↗️𝐂𝐋𝐈𝐂𝐊↗️](https://t.me/BHATAKTI_ATMA_SUPPORT)
┣★𝐆𝐈𝐕𝐄 𝐀 :-  [✨𝐇𝐄𝐀𝐑𝐓💜](https://t.me/A_BUT/32)
┗━━━━━━━━━━━━━━━━━┛
𝐈𝐟 𝐘𝐨𝐮 𝐇𝐚𝐯𝐞 𝐀𝐧𝐲 𝐐𝐮𝐞𝐬𝐭𝐢𝐨𝐧𝐬 𝐀𝐧𝐝 𝐇𝐞𝐥𝐩 𝐓𝐡𝐞𝐧 𝐃𝐦 𝐌𝐲 𝐁𝐨𝐬𝐬 = [𝐁𝐇𝐀𝐓𝐀𝐊𝐓𝐈 𝐀𝐓𝐌𝐀 👻](https://t.me/ZINDA_H_TU_MERE_LIYE_HEART_HACK)**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🥀 Jᴏɪɴ Hᴇʀᴇ & Sᴜᴘᴘᴏʀᴛ ✨", url=f"https://t.me/BHATAKTI_ATMA_MUSIC_bot")
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
                        "💥 Cʟɪᴄᴋ Mᴇ Tᴏ Gᴇᴛ Rᴇᴘᴏ 💞", url=f"https://t.me/A_BUT")
                ]
            ]
        ),
    )
