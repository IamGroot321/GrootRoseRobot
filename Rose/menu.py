from Rose import bot as app
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from Rose.utils.lang import *


fbuttons = InlineKeyboardMarkup(
        [
        [
            InlineKeyboardButton(
                text="🧡sᴛɪᴄᴋᴇʀ ᴘᴀᴄᴋs🧡", url="https://t.me/groot_network"
            ),
            InlineKeyboardButton(
                text="💚ғᴜɴɴʏ ɢɪғs💚", url="https://t.me/rjbr0"
            )
        ], 
        [
            InlineKeyboardButton(
                text="💙ᴛᴇʟᴜɢᴜ ɢʀᴏᴜᴘs💙", url="https://t.me/telugulittleworld"
            ),
            InlineKeyboardButton(
                text="💛ᴛᴇʟᴜɢᴜ ᴄᴏᴅᴇʀs💛", url="https://t.me/telugucoders"
            )
        ], 
        [
            InlineKeyboardButton(
                text="💜ᴏᴡɴᴇʀ💜", url="https://t.me/mynameisgroot"
            )
        ], 
        [
            InlineKeyboardButton("« Back", callback_data='startcq')
        ]
        ]
)

keyboard =InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="🇱🇷 ᴇɴɢʟɪsʜ", callback_data="languages_en"
            ),
            InlineKeyboardButton(
                text="🇮🇳 हिन्दी", callback_data="languages_hi"
            ), 
        ],
        [
            InlineKeyboardButton(
                text="🇮🇳 తెలుగు", callback_data="languages_te"
            ),
        ], 
        [   
            InlineKeyboardButton("◁", callback_data='startcq'
            ), 
        ]
    ]
)

@app.on_callback_query(filters.regex("_langs"))
@languageCB
async def commands_callbacc(client, CallbackQuery, _):
    user = CallbackQuery.message.from_user.mention
    await app.send_message(
        CallbackQuery.message.chat.id,
        text= "ᴛʜᴇ ʟɪsᴛ ᴏғ ᴀᴠᴀɪʟᴀʙʟᴇ ʟᴀɴɢᴜᴀɢᴇs:",
        reply_markup=keyboard,
        disable_web_page_preview=True,
    )
    await CallbackQuery.message.delete()
    
@app.on_callback_query(filters.regex("_about"))
@languageCB
async def commands_callbacc(client, CallbackQuery, _):
    await app.send_message(
        CallbackQuery.message.chat.id,
        text=_["menu"],
        reply_markup=fbuttons,
        disable_web_page_preview=True,
    )
    await CallbackQuery.message.delete()

