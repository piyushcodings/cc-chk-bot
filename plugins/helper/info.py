#IMPORT PYROGRAM MODULE
from pyrogram import Client, filters
#Reg Data Import
from plugins.func.users_sql import *
@Client.on_message(filters.command ('info'))
async def cmd_info(Client,message):
  try:
    user_id = str(message.from_user.id)
    regdata = fetchinfo(user_id)
    results = str(regdata)
    if results=='None':
      resp = "𝗬𝗢𝗨 𝗔𝗥𝗘 𝗡𝗢𝗧 𝗥𝗘𝗚𝗜𝗦𝗧𝗘𝗥𝗘𝗗 𝗬𝗘𝗧 ⚠️. 𝗥𝗘𝗚𝗜𝗦𝗧𝗘𝗥 𝗙𝗜𝗥𝗦𝗧 𝗕𝗬 𝗨𝗦𝗜𝗡𝗚 /register 𝗧𝗢 𝗨𝗦𝗘 𝗠𝗘."
      await message.reply_text(resp,message.id)
    else:
      
      if message.reply_to_message:
        user_id = str(message.reply_to_message.from_user.id)
        chat_type = str(message.chat.type)
        chat_id = str(message.chat.id)
        #PLAN CHECK 
        await plan_expirychk(user_id)
        user_id = str(message.reply_to_message.from_user.id)
        username = str(message.reply_to_message.from_user.username)
        first_name = str(message.reply_to_message.from_user.first_name)
        info = fetchinfo(user_id)
        results = str(info)
        if results=="None":
          send_info = f"""
𝗬𝗼𝘂𝗿 𝗜𝗻𝗳𝗼 𝗼𝗻 𝗫 𝗖𝗖 𝗖𝗛𝗘𝗖𝗞𝗘𝗥 ⚡
━━━━━━━━━━━━━━
● 𝗙𝗶𝗿𝘀𝘁𝗻𝗮𝗺𝗲: {first_name}
● 𝗜𝗗: <code>{user_id}</code>
● 𝗨𝘀𝗲𝗿𝗻𝗮𝗺𝗲: {username}
● 𝗣𝗿𝗼𝗳𝗶𝗹𝗲 𝗟𝗶𝗻𝗸: <a href="tg://user?id={message.reply_to_message.from_user.id}">Profile Link</a>
● 𝗧𝗚 𝗥𝗲𝘀𝘁𝗿𝗶𝗰𝘁𝗶𝗼𝗻𝘀: {message.reply_to_message.from_user.is_restricted}
● 𝗧𝗚 𝗦𝗰𝗮𝗺𝘁𝗮𝗴: {message.reply_to_message.from_user.is_scam}
● 𝗧𝗚 𝗣𝗿𝗲𝗺𝗶𝘂𝗺: {message.reply_to_message.from_user.is_premium}
● 𝗦𝘁𝗮𝘁𝘂𝘀: NOT REGISTERED
● 𝗖𝗿𝗲𝗱𝗶𝘁: N/A
● 𝗣𝗹𝗮𝗻: N/A
● 𝗣𝗹𝗮𝗻 𝗘𝘅𝗽𝗶𝗿𝘆: N/A
● 𝗞𝗲𝘆 𝗥𝗲𝗱𝗲𝗲𝗺𝗲𝗱 : N/A
● 𝗥𝗲𝗴𝗶𝘀𝘁𝗲𝗿𝗲𝗱 𝗮𝘁: N/A
"""
          await message.reply_text(send_info,message.id)
        else:
          pid = str(message.reply_to_message.from_user.id)
          await plan_expirychk(pid)
          info = fetchinfo(user_id)
          results = info
          status = results[2]
          plan = results[3]
          expiry = results[4]
          credit = results[5]
          antispam = results[6]
          antispam_time = results[7]
          totalkey = results[8]
          reg_at = results[9]
          send_info = f"""
𝗬𝗼𝘂𝗿 𝗜𝗻𝗳𝗼 𝗼𝗻 𝗫 𝗖𝗖 𝗖𝗛𝗘𝗖𝗞𝗘𝗥 ⚡
━━━━━━━━━━━━━━
● 𝗙𝗶𝗿𝘀𝘁𝗻𝗮𝗺𝗲: {first_name}
● 𝗜𝗗: <code>{user_id}</code>
● 𝗨𝘀𝗲𝗿𝗻𝗮𝗺𝗲: {username}
● 𝗣𝗿𝗼𝗳𝗶𝗹𝗲 𝗟𝗶𝗻𝗸: <a href="tg://user?id={message.reply_to_message.from_user.id}">Profile Link</a>
● 𝗧𝗚 𝗥𝗲𝘀𝘁𝗿𝗶𝗰𝘁𝗶𝗼𝗻𝘀: {message.reply_to_message.from_user.is_restricted}
● 𝗧𝗚 𝗦𝗰𝗮𝗺𝘁𝗮𝗴: {message.reply_to_message.from_user.is_scam}
● 𝗧𝗚 𝗣𝗿𝗲𝗺𝗶𝘂𝗺: {message.reply_to_message.from_user.is_premium}
● 𝗦𝘁𝗮𝘁𝘂𝘀: {status}
● 𝗖𝗿𝗲𝗱𝗶𝘁: {credit}
● 𝗣𝗹𝗮𝗻: {plan}
● 𝗣𝗹𝗮𝗻 𝗘𝘅𝗽𝗶𝗿𝘆: {expiry}
● 𝗞𝗲𝘆 𝗥𝗲𝗱𝗲𝗲𝗺𝗲𝗱 : {totalkey}
● 𝗥𝗲𝗴𝗶𝘀𝘁𝗲𝗿𝗲𝗱 𝗮𝘁: {reg_at}
"""
          await message.reply_text(send_info,message.id)
      else:
        user_id = str(message.from_user.id)
        chat_type = str(message.chat.type)
        chat_id = str(message.chat.id)
        #PLAN CHECK 
        await plan_expirychk(user_id)
        user_id = str(message.from_user.id)
        username = str(message.from_user.username)
        first_name = str(message.from_user.first_name)
        info = fetchinfo(user_id)
        results = str(info)
        if results=="None":
          send_info = f"""
𝗬𝗼𝘂𝗿 𝗜𝗻𝗳𝗼 𝗼𝗻 𝗫 𝗖𝗖 𝗖𝗛𝗘𝗖𝗞𝗘𝗥 ⚡
━━━━━━━━━━━━━━
● 𝗙𝗶𝗿𝘀𝘁𝗻𝗮𝗺𝗲: {first_name}
● 𝗜𝗗: <code>{user_id}</code>
● 𝗨𝘀𝗲𝗿𝗻𝗮𝗺𝗲: {username}
● 𝗣𝗿𝗼𝗳𝗶𝗹𝗲 𝗟𝗶𝗻𝗸: <a href="tg://user?id={message.from_user.id}">Profile Link</a>
● 𝗧𝗚 𝗥𝗲𝘀𝘁𝗿𝗶𝗰𝘁𝗶𝗼𝗻𝘀: {message.from_user.is_restricted}
● 𝗧𝗚 𝗦𝗰𝗮𝗺𝘁𝗮𝗴: {message.from_user.is_scam}
● 𝗧𝗚 𝗣𝗿𝗲𝗺𝗶𝘂𝗺: {message.from_user.is_premium}
● 𝗦𝘁𝗮𝘁𝘂𝘀: NOT REGISTERED
● 𝗖𝗿𝗲𝗱𝗶𝘁: N/A
● 𝗣𝗹𝗮𝗻: N/A
● 𝗣𝗹𝗮𝗻 𝗘𝘅𝗽𝗶𝗿𝘆: N/A
● 𝗞𝗲𝘆 𝗥𝗲𝗱𝗲𝗲𝗺𝗲𝗱 : N/A
● 𝗥𝗲𝗴𝗶𝘀𝘁𝗲𝗿𝗲𝗱 𝗮𝘁: N/A
"""
          await message.reply_text(send_info,message.id)
        else:
          pid = str(message.from_user.id)
          await plan_expirychk(pid)
          info = fetchinfo(user_id)
          results = info
          status = results[2]
          plan = results[3]
          expiry = results[4]
          credit = results[5]
          antispam = results[6]
          antispam_time = results[7]
          totalkey = results[8]
          reg_at = results[9]
          send_info = f"""
𝗬𝗼𝘂𝗿 𝗜𝗻𝗳𝗼 𝗼𝗻 𝗫 𝗖𝗖 𝗖𝗛𝗘𝗖𝗞𝗘𝗥 ⚡
━━━━━━━━━━━━━━
● 𝗙𝗶𝗿𝘀𝘁𝗻𝗮𝗺𝗲: {first_name}
● 𝗜𝗗: <code>{user_id}</code>
● 𝗨𝘀𝗲𝗿𝗻𝗮𝗺𝗲: {username}
● 𝗣𝗿𝗼𝗳𝗶𝗹𝗲 𝗟𝗶𝗻𝗸: <a href="tg://user?id={message.from_user.id}">Profile Link</a>
● 𝗧𝗚 𝗥𝗲𝘀𝘁𝗿𝗶𝗰𝘁𝗶𝗼𝗻𝘀: {message.from_user.is_restricted}
● 𝗧𝗚 𝗦𝗰𝗮𝗺𝘁𝗮𝗴: {message.from_user.is_scam}
● 𝗧𝗚 𝗣𝗿𝗲𝗺𝗶𝘂𝗺: {message.from_user.is_premium}
● 𝗦𝘁𝗮𝘁𝘂𝘀: {status}
● 𝗖𝗿𝗲𝗱𝗶𝘁: {credit}
● 𝗣𝗹𝗮𝗻: {plan}
● 𝗣𝗹𝗮𝗻 𝗘𝘅𝗽𝗶𝗿𝘆: {expiry}
● 𝗞𝗲𝘆 𝗥𝗲𝗱𝗲𝗲𝗺𝗲𝗱 : {totalkey}
● 𝗥𝗲𝗴𝗶𝘀𝘁𝗲𝗿𝗲𝗱 𝗮𝘁: {reg_at}
  """
        await message.reply_text(send_info,message.id)
  except Exception as e:
      print(e)