#Pyrogrm Import
from pyrogram import Client, filters
#Reg Data Import
import time
from datetime import date
from datetime import timedelta
from plugins.func.users_sql import *
@Client.on_message(filters.command ('register'))
async def cmd_register(Client,message):
  try:
    user_id = str(message.from_user.id)
    username = str(message.from_user.username)
    chat_id = str(message.chat.id)
    antispam_time = int(time.time())
    reg_at = str(date.today())
    regdata = fetchinfo(user_id)
    results = str(regdata)
    if results=='None':
      registration = insert_reg_data(user_id,username,antispam_time,reg_at)
      resp = "𝗨𝗦𝗘𝗥 𝗥𝗘𝗚𝗜𝗦𝗧𝗘𝗥𝗘𝗗 𝗦𝗨𝗖𝗖𝗘𝗦𝗦𝗙𝗨𝗟𝗟𝗬 ✅ . 𝗧𝗬𝗣𝗘 /cmds 𝗧𝗢 𝗞𝗡𝗢𝗪 𝗠𝗬 𝗪𝗢𝗥𝗞 𝗔𝗕𝗜𝗟𝗜𝗧𝗬 🥰"
      await message.reply_text(resp,message.id)
  
    else:
      resp = "𝗔𝗟𝗥𝗘𝗔𝗗𝗬 𝗥𝗘𝗚𝗜𝗦𝗧𝗘𝗥𝗘𝗗 ⚠️ .𝗧𝗬𝗣𝗘 /cmds 𝗧𝗢 𝗞𝗡𝗢𝗪 𝗠𝗬 𝗪𝗢𝗥𝗞 𝗔𝗕𝗜𝗟𝗜𝗧𝗬 🥰"
      await message.reply_text(resp,message.id)
      await plan_expirychk(user_id)
    
  except Exception as e:
      print(e)
  
  