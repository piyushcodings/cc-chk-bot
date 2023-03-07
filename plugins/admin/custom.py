from pyrogram import Client, filters
from plugins.func.users_sql import *
@Client.on_message(filters.command ('cs'))
async def cmd_cs(Client,message):
  user_id = str(message.from_user.id)
  CEO = "1900986195"
  if user_id != CEO :
    resp = "𝗥𝗲𝗾𝘂𝗶𝗿𝗲 𝗢𝘄𝗻𝗲𝗿 𝗣𝗿𝗶𝘃𝗶𝗹𝗮𝗴𝗲𝘀 ⚠️"
    msg1 = await message.reply_text(resp,message.id)
  else:
    try:
      msg = message.text[len('/cs '):]
      splitter = msg.split(' ')
      userid = splitter[0]
      module_name = splitter[1]
      value = splitter[2]
      updatedata(userid,module_name,value)
      resp = f"""
  𝗨𝗦𝗘𝗥𝗜𝗗: <code>{userid}</code>
  𝗠𝗢𝗗𝗨𝗟𝗘 𝗡𝗔𝗠𝗘: {module_name}
  𝗠𝗢𝗗𝗨𝗟𝗘 𝗩𝗔𝗟𝗨𝗘: {value}
  
  𝗖𝗵𝗮𝗻𝗴𝗲𝗱
      """
      await message.reply_text(resp,message.id)
    except Exception as e:
      print(e)
      