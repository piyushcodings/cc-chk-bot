from pyrogram import Client, filters
from plugins.func.users_sql import *
@Client.on_message(filters.command ('crdsystem'))
async def cmd_crdsystem(Client,message):
  try:
    user_id = str(message.from_user.id)
    chat_type = str(message.chat.type)
    chat_id = str(message.chat.id)
    #PLAN CHECK 
    resp =f"""
𝗫 𝗖𝗖 𝗖𝗛𝗘𝗖𝗞𝗘𝗥 ⚡𝗖𝗥𝗘𝗗𝗜𝗧 𝗦𝗬𝗦𝗧𝗘𝗠 -

● 𝗔𝗨𝗧𝗛 𝗚𝗔𝗧𝗘𝗦
➔ 1 credit Per CC check

● 𝗖𝗛𝗔𝗥𝗚𝗘 𝗚𝗔𝗧𝗘𝗦
➔ 1 credit Per CC check

● 𝗠𝗔𝗦𝗦 𝗔𝗨𝗧𝗛 𝗚𝗔𝗧𝗘𝗦
➔ 1 credit Per CC check

● 𝗠𝗔𝗦𝗦 𝗖𝗛𝗔𝗥𝗚𝗘 𝗚𝗔𝗧𝗘𝗦
➔ 1 credit Per CC check

● 𝗖𝗖 𝗦𝗖𝗥𝗔𝗣𝗘𝗥 𝗚𝗔𝗧𝗘𝗦
➔ 1 credit Per Scraping
    """
    msg1 = await message.reply_text(resp,message.id)
    await plan_expirychk(user_id)
  except Exception as e:
      print(e)