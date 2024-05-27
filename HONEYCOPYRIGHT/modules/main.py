from pyrogram import Client, filters
import os
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, Message
import time
import psutil
import platform
from config import OWNER_ID, BOT_USERNAME
from config import *
from HONEYCOPYRIGHT import HONEYCOPYRIGHT as app

import pyrogram
from pyrogram.errors import FloodWait


# ----------------------------------------------------------------------------------------

start_txt = """<b> ❄️ 𝗖𝗢𝗣𝗬𝗥𝗜𝗚𝗛𝗧 𝗚𝗔𝗨𝗥𝗗 🛡️ </b>

𝖶𝖾𝗅𝖼𝗈𝗆𝖾 𝗍𝗈 𝗖𝗢𝗣𝗒𝗋𝗂𝗀𝗁𝗍 𝗚𝗔𝗨𝗥𝗗 🛡️, ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴄᴏᴘʏʀɪɢʜᴛ ɢᴜᴀʀᴅ ꜱᴇʀᴠɪᴄᴇ
ᴡʜᴀᴛ ᴅᴏᴇꜱ ᴛʜɪꜱ ʙᴏᴛ ᴅᴏ?
ᴛʜɪꜱ ʙᴏᴛ ᴡɪʟʟ ᴘʀᴏᴛᴇᴄᴛ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴄʜᴀᴛ ꜰʀᴏᴍ ᴄᴏᴍᴍᴜɴɪᴛʏ ᴀɴᴅ ꜰʀᴏᴍ ᴄᴏᴘʏʀɪɢʜᴛ ꜱᴛʀɪᴋᴇꜱ ɪᴛ ᴡɪʟʟ ᴘʀᴏᴛᴇᴄᴛ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴄʜᴀᴛ 100% ɴᴏ ᴏɴᴇ ᴄᴀɴ ᴅᴇꜱᴛʀᴏʏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴄʜᴀᴛ ɪꜰ ʏᴏᴜ ʜᴀᴠᴇ ᴛʜɪꜱ ʙᴏᴛ🔐 """

@app.on_message(filters.command("start"))
async def start(_, msg):
    print("Received /start command from user:", msg.from_user.username)  # Debug log
    buttons = [
        [ 
          InlineKeyboardButton("ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ", url=f"http://t.me/Group_securityxbot?startgroup=true")
        ],
        [
          InlineKeyboardButton("• ᴀʙᴏᴜᴛ •", callback_data="dil_back")
        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://graph.org/file/ad0bd6b3491e599d6ec9b.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
    print("Replied to /start command")  # Debug log


gd_buttons = [              
        [
            InlineKeyboardButton("𝐎ᴡɴᴇʀ", user_id=OWNER_ID),
            InlineKeyboardButton("𝐒ᴜᴘᴘᴏʀᴛ", url="https://t.me/mutals_log"),    
        ]
]

@app.on_callback_query(filters.regex("dil_back"))
async def dil_back(_, query: CallbackQuery):
    print(f"Callback query received: {query.data} from user: {query.from_user.username}")  # Debug log
    await query.message.edit_caption(start_txt, reply_markup=InlineKeyboardMarkup(gd_buttons))
    print("Edited message caption for callback query")  # Debug log

start_time = time.time()

def time_formatter(milliseconds: float) -> str:
    seconds, milliseconds = divmod(milliseconds, 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return f"{int(hours)}h {int(minutes)}m {int(seconds)}s"

def size_formatter(bytes: int) -> str:
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes < 1024.0:
            break
        bytes /= 1024.0
    return f"{bytes:.2f} {unit}"

@app.on_message(filters.command("ping"))
async def activevc(_, message: Message):
    print("Received /ping command from user:", message.from_user.username)  # Debug log
    uptime = time_formatter((time.time() - start_time) * 1000)
    cpu = psutil.cpu_percent()
    storage = psutil.disk_usage('/')

    python_version = platform.python_version()

    reply_text = (
        f"➪ᴜᴘᴛɪᴍᴇ: {uptime}\n"
        f"➪ᴄᴘᴜ: {cpu}%\n"
        f"➪ꜱᴛᴏʀᴀɢᴇ: {size_formatter(storage.total)} [ᴛᴏᴛᴀʟ]\n"
        f"➪{size_formatter(storage.used)} [ᴜsᴇᴅ]\n"
        f"➪{size_formatter(storage.free)} [ғʀᴇᴇ]\n"
        f"➪ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ: {python_version},"
    )

    await message.reply(reply_text, quote=True)
    print("Replied to /ping command")  # Debug log

FORBIDDEN_KEYWORDS = ["Porn", "xxx", "sex", "NCERT", "XII", "page", "Ans", "meiotic", "divisions", "System.in", "Scanner", "void", "nextInt"]

@app.on_message()
async def handle_message(client, message):
    print(f"Received message: {message.text} from user: {message.from_user.username} in chat: {message.chat.title}")  # Debug log
    if any(keyword in message.text for keyword in FORBIDDEN_KEYWORDS):
        print(f"Deleting message with ID {message.id} due to forbidden keyword in text")  # Debug log
        await message.delete()
        await message.reply_text(f"@{message.from_user.username} PLEASE DON'T SEND AGAIN!!")
    elif message.caption and any(keyword in message.caption for keyword in FORBIDDEN_KEYWORDS):
        print(f"Deleting message with ID {message.id} due to forbidden keyword in caption")  # Debug log
        await message.delete()
        await message.reply_text(f"@{message.from_user.username} PLEASE DONT SEND AGAIN!!")

@app.on_edited_message(filters.group & ~filters.me)
async def delete_edited_messages(client, edited_message):
    print(f"Deleting edited message with ID {edited_message.id} in chat: {edited_message.chat.title}")  # Debug log
    await edited_message.delete()

def delete_long_messages(_, m):
    return len(m.text.split()) > 10

@app.on_message(filters.group & filters.private & delete_long_messages)
async def delete_and_reply(_, msg):
    print(f"Deleting long message with ID {msg.id} from user: {msg.from_user.username} in chat: {msg.chat.title}")  # Debug log
    await msg.delete()
    user_mention = msg.from_user.mention
    await app.send_message(msg.chat.id, f"Hey {user_mention}, please keep your messages short!")

@app.on_message(filters.animation | filters.audio | filters.document | filters.photo | filters.sticker | filters.video)
async def keep_reaction_message(client, message: Message):
    print(f"Received media message with ID {message.id} from user: {message.from_user.username} in chat: {message.chat.title}")  # Debug log

async def delete_pdf_files(client, message):
    if message.document and message.document.mime_type == "application/pdf":
        print(f"Deleting PDF message with ID {message.id} from user: {message.from_user.username} in chat: {message.chat.title}")  # Debug log
        warning_message = f"@{message.from_user.username} ᴍᴀᴀ ᴍᴀᴛ ᴄʜᴜᴅᴀ ᴘᴅғ ʙʜᴇᴊ ᴋᴇ,\n ʙʜᴏsᴀᴅɪᴋᴇ ᴄᴏᴘʏʀɪɢʜᴛ 
