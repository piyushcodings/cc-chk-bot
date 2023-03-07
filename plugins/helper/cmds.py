from pyrogram import Client, filters
from plugins.func.users_sql import *
@Client.on_message(filters.command ('cmds'))
async def cmd_cmds(Client,message):
  try:
    user_id = str(message.from_user.id)
    regdata = fetchinfo(user_id)
    results = str(regdata)
    if results=='None':
      resp = "𝗬𝗢𝗨 𝗔𝗥𝗘 𝗡𝗢𝗧 𝗥𝗘𝗚𝗜𝗦𝗧𝗘𝗥𝗘𝗗 𝗬𝗘𝗧 ⚠️. 𝗥𝗘𝗚𝗜𝗦𝗧𝗘𝗥 𝗙𝗜𝗥𝗦𝗧 𝗕𝗬 𝗨𝗦𝗜𝗡𝗚 /register 𝗧𝗢 𝗨𝗦𝗘 𝗠𝗘."
      await message.reply_text(resp,message.id)
    else:
      user_id = str(message.from_user.id)
      chat_type = str(message.chat.type)
      chat_id = str(message.chat.id)
      #PLAN CHECK 
      await plan_expirychk(user_id)
      texta = f"""
  𝗛𝗲𝘆 <a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a>
  𝗟𝗼𝗮𝗱𝗶𝗻𝗴 𝗮𝗹𝗹 𝗼𝗳 𝗫𝗖𝗖 𝗕𝗢𝗧 𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀..
      """
      msg1 = await message.reply_text(texta,message.id)
      textb = """
𝗫 𝗖𝗖 𝗖𝗛𝗘𝗖𝗞𝗘𝗥 ⚡ 𝗔𝗟𝗟 𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦 -

● 𝗙𝗜𝗥𝗦𝗧 𝗦𝗧𝗔𝗥𝗧 𝗧𝗛𝗘 𝗕𝗢𝗧 𝗖𝗠𝗗
➔ <code>/start@chkmtc_Client</code>
● 𝗖𝗖 𝗔𝗨𝗧𝗛 𝗖𝗛𝗘𝗖𝗞 𝗖𝗠𝗗
➔ <code>/au cc|mm|yy|cvv</code>
● 𝗖𝗖 𝗖𝗛𝗔𝗥𝗚𝗘 𝗖𝗛𝗘𝗖𝗞 𝗖𝗠𝗗
➔ <code>/chk cc|mm|yy|cvv</code>
● 𝗠𝗔𝗦𝗦 𝗔𝗨𝗧𝗛 𝗖𝗖 𝗖𝗛𝗘𝗖𝗞 𝗖𝗠𝗗
➔ <code>/mass cc|mm|yy|cvv</code>
● 𝗠𝗔𝗦𝗦 𝗖𝗛𝗔𝗥𝗚𝗘 𝗖𝗖 𝗖𝗛𝗘𝗖𝗞 𝗖𝗠𝗗
➔ <code>/mchk cc|mm|yy|cvv</code>
● 𝗦𝗖𝗥𝗔𝗣𝗘 𝗖𝗖 𝗙𝗥𝗢𝗠 𝗖𝗛𝗔𝗡𝗡𝗘𝗟
➔ <code>/scr liveccbycp 100</code>
● 𝗖𝗖'𝗦 𝗕𝗜𝗡 𝗖𝗛𝗘𝗖𝗞 𝗖𝗠𝗗
➔ <code>/bin cc|mm|yy|cvv</code>
● 𝗦𝗞 𝗞𝗘𝗬 𝗖𝗛𝗘𝗖𝗞 𝗖𝗠𝗗
➔ <code>/sk sk_live_51kvhhbrfFJrdfTg</code>
● 𝗠𝗔𝗞𝗘 𝗖𝗖 𝗘𝗫𝗧𝗥𝗔𝗣 𝗖𝗠𝗗
➔ <code>/cxt cc|mm|yy|cvv</code>
● 𝗠𝗔𝗞𝗘 𝗕𝗜𝗡 𝗘𝗫𝗧𝗥𝗔𝗣 𝗖𝗠𝗗
➔ <code>/bin cc|mm|yy|cvv</code>
● 𝗖𝗖 𝗚𝗘𝗡𝗔𝗥𝗔𝗧𝗢𝗥 𝗖𝗠𝗗
➔ <code>/gen bin</code>
● 𝗞𝗡𝗢𝗪 𝗨𝗦𝗘𝗥 𝗜𝗗 𝗖𝗠𝗗
➔ <code>/id</code>
● 𝗞𝗡𝗢𝗪 𝗨𝗦𝗘𝗥 𝗣𝗥𝗢𝗙𝗜𝗟𝗘 𝗖𝗠𝗗
➔ <code>/info</code>
● 𝗞𝗡𝗢𝗪 𝗨𝗦𝗘𝗥 𝗖𝗥𝗘𝗗𝗜𝗧 𝗖𝗠𝗗
➔ <code>/credit</code>
● 𝗡𝗘𝗪 𝗨𝗦𝗘𝗥 𝗥𝗘𝗚 𝗖𝗠𝗗
➔ <code>/register</code>
● 𝗞𝗡𝗢𝗪 𝗕𝗢𝗧 𝗖𝗥𝗘𝗗𝗜𝗧 𝗦𝗬𝗦𝗧𝗘𝗠 𝗖𝗠𝗗
➔ <code>/crdsystem</code>
● 𝗔𝗗𝗗 𝗕𝗢𝗧 𝗧𝗢 𝗬𝗢𝗨𝗥 𝗚𝗥𝗢𝗨𝗣 𝗖𝗠𝗗
➔ <code>/howgp</code>
● 𝗖𝗛𝗘𝗖𝗞 𝗬𝗢𝗨𝗥 𝗚𝗔𝗬𝗡𝗘𝗦𝗦 𝗖𝗠𝗗
➔ <code>/gay</code>
● 𝗣𝗨𝗥𝗖𝗛𝗔𝗦𝗘 𝗕𝗢𝗧 𝗣𝗔𝗜𝗗 𝗣𝗟𝗔𝗡 𝗖𝗠𝗗
➔ <code>/buy</code>

𝘼𝙡𝙡 𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨 𝙖𝙧𝙚 𝙣𝙤𝙩 𝙧𝙚𝙖𝙙𝙮 𝙮𝙚𝙩.𝙈𝙤𝙧𝙚 𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨 𝙖𝙣𝙙 𝙂𝙖𝙩𝙚𝙨 𝘼𝙙𝙙𝙞𝙣𝙜 𝙎𝙤𝙤𝙣.𝙄𝙩 𝙞𝙨 𝙪𝙣𝙙𝙚𝙧 𝙙𝙚𝙫𝙤𝙡𝙤𝙥𝙢𝙚𝙣𝙩.
      """
      msg2 = await     Client.edit_message_text(message.chat.id,msg1.id,textb)
  except Exception as e:
      print(e)