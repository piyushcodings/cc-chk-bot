from pyrogram import Client, filters
from plugins.func.users_sql import *
@Client.on_message(filters.command ('id'))
async def cmd_id(Client,message):
  try:
    user_id = str(message.from_user.id)
    chat_type = str(message.chat.type)
    chat_id = str(message.chat.id)
    #PLAN CHECK 
    if message.reply_to_message:
      texta = f"""
𝗛𝗲𝘆 <a href="tg://user?id={message.reply_to_message.from_user.id}"> {message.reply_to_message.from_user.first_name}</a> !
𝗬𝗼𝘂𝗿 𝗨𝘀𝗲𝗿 𝗜𝗗: <code>{message.reply_to_message.from_user.id}</code> 
𝗧𝗵𝗶𝘀 𝗖𝗵𝗮𝘁 𝗜𝗗: <code>{message.chat.id}</code>
"""
      msg1 = await message.reply_text(texta,message.id)
    else:
      texta = f"""
𝗛𝗲𝘆 <a href="tg://user?id={message.from_user.id}"> {message.from_user.first_name}</a> !
𝗬𝗼𝘂𝗿 𝗨𝘀𝗲𝗿 𝗜𝗗: <code>{message.from_user.id}</code> 
𝗧𝗵𝗶𝘀 𝗖𝗵𝗮𝘁 𝗜𝗗: <code>{message.chat.id}</code>
"""
      msg1 = await message.reply_text(texta,message.id)
      await plan_expirychk(user_id)
  except Exception as e:
      print(e)