#IMPORT PYROGRAM MODULE
from pyrogram import Client, filters
#Reg Data Import
from plugins.func.users_sql import *
@Client.on_message(filters.command ('credits'))
async def cmd_credit(Client,message):
  try:
    user_id = str(message.from_user.id)
    regdata = fetchinfo(user_id)
    credit = regdata[5]
    status = regdata[2]
    plan = regdata[3]
    results = str(regdata)
    first_name = str(message.from_user.first_name)
    if results=='None':
      resp = "𝗬𝗢𝗨 𝗔𝗥𝗘 𝗡𝗢𝗧 𝗥𝗘𝗚𝗜𝗦𝗧𝗘𝗥𝗘𝗗 𝗬𝗘𝗧 ⚠️. 𝗥𝗘𝗚𝗜𝗦𝗧𝗘𝗥 𝗙𝗜𝗥𝗦𝗧 𝗕𝗬 𝗨𝗦𝗜𝗡𝗚 /register 𝗧𝗢 𝗨𝗦𝗘 𝗠𝗘."
      await message.reply_text(resp,message.id)
    else:
      resp = f"""
𝗡𝗮𝗺𝗲: {first_name}
𝗖𝗿𝗲𝗱𝗶𝘁: {credit}
𝗦𝘁𝗮𝘁𝘂𝘀: {status}
𝗣𝗹𝗮𝗻: {plan}

𝗪𝗮𝗻𝘁 𝗠𝗼𝗿𝗲 ? 𝗧𝘆𝗽𝗲 /buy 𝘁𝗼 𝗚𝗲𝘁 𝗺𝗼𝗿𝗲.
      """
      await message.reply_text(resp,message.id)
      await plan_expirychk(user_id)
  except Exception as e:
      print(e)