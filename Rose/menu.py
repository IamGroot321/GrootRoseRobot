from Rose import bot as app
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from Rose.utils.lang import *


fbuttons = InlineKeyboardMarkup(
        [
        [
            InlineKeyboardButton(
                text="🧡sɪᴄᴋᴇʀ ᴘᴀᴄᴋs🧡", url="https://t.me/groot_network"
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
                text="💛sᴜᴘᴘᴏʀᴛᴇʀs💛", url="https://telegra.ph/file/b9046390e87cbc3c5b6f0.jpg"
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
                text="🇱🇷 English", callback_data="languages_en"
            ),
            InlineKeyboardButton(
                text="🇱🇰 සිංහල", callback_data="languages_si"
            )
        ],
        [
            InlineKeyboardButton(
                text="🇮🇳 हिन्दी", callback_data="languages_hi"
            ),
            InlineKeyboardButton(
                text="🇮🇹 Italiano", callback_data="languages_it"
            )
        ],
        [
            InlineKeyboardButton(
                text="🇮🇳 తెలుగు", callback_data="languages_ta"
            ),
            InlineKeyboardButton(
                text="🇮🇩 Indonesia", callback_data="languages_id"
            ),
        ],
        [
            InlineKeyboardButton(
                text="🇦🇪 عربي", callback_data="languages_ar"
            ),
            InlineKeyboardButton(
                text="🇮🇳 മലയാളം", callback_data="languages_ml"
            ), 
        ],
        [
            InlineKeyboardButton(
                text="🇲🇼 chichewa", callback_data="languages_ny"
            ), 
            InlineKeyboardButton(
                text="🇩🇪 german", callback_data="languages_ge"
            ), 
        ], 
        [  
            InlineKeyboardButton("« Back", callback_data='startcq')
        ]
    ]
)

@app.on_callback_query(filters.regex("_langs"))
@languageCB
async def commands_callbacc(client, CallbackQuery, _):
    user = CallbackQuery.message.from_user.mention
    await app.send_message(
        CallbackQuery.message.chat.id,
        text= "The list of available languages:",
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

