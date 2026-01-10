from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from Script import script
from info import temp


# ABOUT BUTTON
@Client.on_callback_query(filters.regex("^about$"))
async def about_callback(client, cq):
    await cq.answer()

    buttons = [
        [InlineKeyboardButton("🔙 BACK", callback_data="start")]
    ]

    await cq.message.edit_text(
        text=script.ABOUT_TXT,
        reply_markup=InlineKeyboardMarkup(buttons),
        disable_web_page_preview=True
    )


# BACK TO START
@Client.on_callback_query(filters.regex("^start$"))
async def start_callback(client, cq):
    await cq.answer()

    buttons = [
        [
            InlineKeyboardButton("💳 ABOUT", callback_data="about"),
            InlineKeyboardButton("🛡 GROUP", callback_data="group_info")
        ]
    ]

    await cq.message.edit_text(
        text=script.START_TXT.format(
            cq.from_user.mention,
            "WELCOME 👋",
            temp.U_NAME,
            temp.B_NAME
        ),
        reply_markup=InlineKeyboardMarkup(buttons)
    )
