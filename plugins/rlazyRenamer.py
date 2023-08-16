"""
Apache License 2.0
Copyright (c) 2023 @LazyDeveloper
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
Dev Channel Link : https://t.me/LazyDeveloper 
Repo Link : https://github.com/LazyDeveloperr/LazyPrincess
License Link : https://github.com/LazyDeveloperr/LazyPrincess/blob/main/LICENSE
# Removing this is strictly prohibited ! Don't remove this all without the 
permission of LazyDeveloperr
"""
    # Credit @LazyDeveloper.
    # Please Don't remove credit.
        # Born to make history @LazyDeveloper !

    # Thank you LazyDeveloper for helping us in this Journey
import asyncio
from asyncio import sleep
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import FloodWait,UserNotParticipant
import humanize
from info import *
# from utils import humanbytes
# import random
# from pyshorteners import Shortener
# from lazybot import StreamBot




@Client.on_message( filters.private & (filters.document | filters.audio | filters.video))
async def rename_start(client, message):
    if (LAZY_MODE==True):
        if message.from_user.id in ADMINS :
            file = getattr(message, message.media.value)
            filesize = humanize.naturalsize(file.file_size) 
            filename = file.file_name
            text = f"""\n⨳ *•.¸♡ L҉ΛＺ𝐲 ＭⓄｄ𝓔 ♡¸.•* ⨳\n\n**Please tell, what should i do with this file.?**\n\n**🎞File Name** :- `{filename}`\n\n⚙️**File Size** :- `{filesize}`"""
            buttons = [[ InlineKeyboardButton("📝✧✧ S𝚝ar𝚝 re𝚗aᗰi𝚗g ✧✧📝", callback_data="rename") ],
                       [ InlineKeyboardButton("⨳  C L Ф S Ξ  ⨳", callback_data="cancel") ]]
            await message.reply_text(text=text, reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup(buttons))

        elif message.from_user.id in LAZY_RENAMERS :
            file = getattr(message, message.media.value)
            filesize = humanize.naturalsize(file.file_size) 
            filename = file.file_name
            try:
                text = f"""\n⨳ *•.¸♡ L҉ΛＺ𝐲 ＭⓄｄ𝓔 ♡¸.•* ⨳\n\n**Please tell, what should i do with this file.?**\n\n**🎞File Name** :- `{filename}`\n\n⚙️**File Size** :- `{filesize}`"""
                buttons = [[ InlineKeyboardButton("📝✧✧ S𝚝ar𝚝 re𝚗aᗰi𝚗g ✧✧📝", callback_data="rename") ],
                           [ InlineKeyboardButton("⨳  C L Ф S Ξ  ⨳", callback_data="cancel") ]]
                await message.reply_text(text=text, reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup(buttons))
                await sleep(FLOOD)
            except FloodWait as e:
                await sleep(e.value)
                text = f"""\n⨳ *•.¸♡ L҉ΛＺ𝐲 ＭⓄｄ𝓔 ♡¸.•* ⨳\n\n**Please tell, what should i do with this file.?**\n\n**🎞File Name** :- `{filename}`\n\n⚙️**File Size** :- `{filesize}`"""
                buttons = [[ InlineKeyboardButton("📝✧✧ S𝚝ar𝚝 re𝚗aᗰi𝚗g ✧✧📝", callback_data="rename") ],
                           [ InlineKeyboardButton("⨳  C L Ф S Ξ  ⨳", callback_data="cancel") ]]
                await message.reply_text(text=text, reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup(buttons))
            except:
                pass
        else:
            file = getattr(message, message.media.value)
            filesize = humanize.naturalsize(file.file_size) 
            filename = file.file_name
            text = f"""\n⨳ *•.¸♡ L҉ΛＺ𝐲 ＭⓄｄ𝓔 ♡¸.•* ⨳\n\n**Please tell, what should i do with this file.?**\n\n**🎞File Name** :- `{filename}`\n\n⚙️**File Size** :- `{filesize}`"""
            buttons = [[ InlineKeyboardButton("📝✧✧ S𝚝ar𝚝 re𝚗aᗰi𝚗g ✧✧📝", callback_data="requireauth") ],
                        [ InlineKeyboardButton("⨳  C L Ф S Ξ  ⨳", callback_data="cancel") ]]
            await message.reply_text(text=text, reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup(buttons))
    else:
        return



# def get_shortlink(url):
#    shortlink = False 
#    try:
#       shortlink = Shortener().dagd.short(url)
#    except Exception as err:
#        print(err)
#        pass
#    return shortlink

# # @StreamBot.on_message(filters.private & (filters.document | filters.video | filters.audio) & ~filters.edited, group=4)
# @StreamBot.on_message(filters.private & filters.command('streamit'))
# async def private_receive_handler(c: Client, m: Message):
#     try:
#         log_msg = await m.forward(chat_id=LOG_CHANNEL)
#         stream_link = URL + 'watch/' + str(log_msg.message_id)
#         shortlink = get_shortlink(stream_link) 
#         if shortlink:
#             stream_link = shortlink
#         online_link = URL + 'download/'+ str(log_msg.message_id) 
#         shortlinka = get_shortlink(online_link)
#         if shortlinka:
#             online_link = shortlinka
        
#         file_size = None
#         if m.video:
#             file_size = f"{humanbytes(m.video.file_size)}"
#         elif m.document:
#             file_size = f"{humanbytes(m.document.file_size)}"
#         elif m.audio:
#             file_size = f"{humanbytes(m.audio.file_size)}"

#         file_name = None
#         if m.video:
#             file_name = f"{m.video.file_name}"
#         elif m.document:
#             file_name = f"{m.document.file_name}"
#         elif m.audio:
#             file_name = f"{m.audio.file_name}"

#         msg_text ="""
# <i><u>𝗬𝗼𝘂𝗿 𝗟𝗶𝗻𝗸 𝗚𝗲𝗻𝗲𝗿𝗮𝘁𝗲𝗱 !</u></i>

# <b>📂 Fɪʟᴇ ɴᴀᴍᴇ :</b> <i>{}</i>

# <b>📦 Fɪʟᴇ ꜱɪᴢᴇ :</b> <i>{}</i>

# <b>📥 Dᴏᴡɴʟᴏᴀᴅ :</b> <i>{}</i>

# <b> 🖥 WATCH    :</b> <i>{}</i>

# <b>🚸 Nᴏᴛᴇ : LINK WON'T EXPIRE  </b>

# """

#         await log_msg.reply_text(text=f"**RᴇQᴜᴇꜱᴛᴇᴅ ʙʏ :** [{m.from_user.first_name}](tg://user?id={m.from_user.id})\n**Uꜱᴇʀ ɪᴅ :** `{m.from_user.id}`\n**Dᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ :** {stream_link}", disable_web_page_preview=True, parse_mode="Markdown", quote=True)
#         await m.reply_text(
#             text=msg_text.format(file_name, file_size, online_link, stream_link),
#             parse_mode="HTML", 
#             quote=True,
#             disable_web_page_preview=True,
#             reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🖥STREAM", url=stream_link), #Stream Link
#                                                 InlineKeyboardButton('Dᴏᴡɴʟᴏᴀᴅ📥', url=online_link)]]) #Download Link
#         )
#     except FloodWait as e:
#         print(f"Sleeping for {str(e.x)}s")
#         await asyncio.sleep(e.x)
#         await c.send_message(chat_id=LOG_CHANNEL, text=f"Gᴏᴛ FʟᴏᴏᴅWᴀɪᴛ ᴏғ {str(e.x)}s from [{m.from_user.first_name}](tg://user?id={m.from_user.id})\n\n**𝚄𝚜𝚎𝚛 𝙸𝙳 :** `{str(m.from_user.id)}`", disable_web_page_preview=True, parse_mode="Markdown")
#     except Exception as e:
#         print("Error:", str(e))

# Born to make history @LazyDeveloper !

