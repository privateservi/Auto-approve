import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, User, ChatJoinRequest

pr0fess0r_99=Client(
    "𝗕𝗼𝘁 𝗦𝘁𝗮𝗿𝘁𝗲𝗱 𝗣𝗹𝗲𝗮𝘀𝗲 𝗦𝘂𝗯𝘀𝗰𝗿𝗶𝗯𝗲 𝐒𝐌𝐃 𝐏𝐄𝐀𝐂𝐄 𝐋𝐈𝐍𝐊𝐳",
    bot_token = os.environ["BOT_TOKEN",'6186689074:AAE-QC_SF682gMoOcWbgH6OoOeNLOpPSzm0'],
    api_id = int(os.environ["API_ID",'28185220']),
    api_hash = os.environ["API_HASH",'7775088403abbe110d5a38cfc75addce"']
)

CHAT_ID=int(os.environ.get("CHAT_ID", '-1001931700058'))
TEXT=os.environ.get("APPROVED_WELCOME_TEXT", "Hello {mention}\nWelcome To {title}\n\nYour Auto Approved")
APPROVED = os.environ.get("APPROVED_WELCOME", "on").lower()

@pr0fess0r_99.on_message(filters.private & filters.command(["start"]))
async def start(client: pr0fess0r_99, message: Message):
    approvedbot = await client.get_me() 
    button=[[
      InlineKeyboardButton("𝚄𝙿𝙳𝙰𝚃𝙴𝚉", url="https://t.me/SMD_BOTz"),
      InlineKeyboardButton("𝚂𝚄𝙿𝙿𝙾𝚁𝚃", url="https://t.me/SAM_DUB_LEZHa")
      ],[
      InlineKeyboardButton("𝙰𝚄𝚃𝙷𝙾𝚁", url=f"https://t.me/SMD_Owner")
      ]]
    await message.reply_text(text="**𝙷𝙴𝙻𝙻𝙾...⚡\n\n𝙸𝙰𝙼 𝙰 𝚂𝙸𝙼𝙿𝙻𝙴 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼 𝙰𝚄𝚃𝙾 𝚁𝙴𝚀𝚄𝙴𝚂𝚃 𝙰𝙲𝙲𝙴𝙿𝚃 𝙱𝙾𝚃.\n𝙵𝙾𝚁 𝚈𝙾𝚄𝚁 𝙲𝙷𝙰𝚃𝚂 𝙲𝚁𝙴𝙰𝚃𝙴 𝙾𝙽𝙴 𝙱𝙾𝚃... \n𝚅𝙸𝙳𝙴𝙾 𝙾𝙽 𝙼𝚈 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼 𝙲𝙷𝙰𝙽𝙽𝙴𝙻**", reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview=True)

@pr0fess0r_99.on_chat_join_request(filters.chat(CHAT_ID))
async def autoapprove(client: pr0fess0r_99, message: ChatJoinRequest):
    chat=message.chat # Chat
    user=message.from_user # User
    print(f"{user.first_name} 𝙹𝙾𝙸𝙽𝙴𝙳 ⚡") # Logs
    await client.approve_chat_join_request(chat_id=chat.id, user_id=user.id)
    if APPROVED == "on":
        await client.send_message(chat_id=chat.id, text=TEXT.format(mention=user.mention, title=chat.title))       

print("𝗕𝗼𝘁 𝗦𝘁𝗮𝗿𝘁𝗲𝗱 𝗣𝗹𝗲𝗮𝘀𝗲 𝗦𝘂𝗯𝘀𝗰𝗿𝗶𝗯𝗲 𝗦𝗠𝗗𝗣𝗘𝗔𝗖𝗘𝗟𝗜𝗡𝗞𝘇")
pr0fess0r_99.run()
