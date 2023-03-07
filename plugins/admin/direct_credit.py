from pyrogram import Client, filters
from plugins.func.users_sql import *
@Client.on_message(filters.command ('ac'))
async def cmd_ac(Client,message):
  user_id = str(message.from_user.id)
  CEO = "1900986195"
  if user_id != CEO :
    resp = "𝗥𝗲𝗾𝘂𝗶𝗿𝗲 𝗢𝘄𝗻𝗲𝗿 𝗣𝗿𝗶𝘃𝗶𝗹𝗮𝗴𝗲𝘀 ⚠️"
    msg1 = await message.reply_text(resp,message.id)
  else:
    try:
      msg = message.text[len('/ac '):]
      splitter = msg.split(' ')
      amt = int(splitter[0])
      user_id = splitter[1]
      module_name = "credit"
      fetch= fetchinfo(user_id)
      credit = int(fetch[5])
      value = credit + amt
      updatedata(user_id,module_name,value)
      resp = f"""
<code>{amt}</code> 𝗖𝗿𝗲𝗱𝗶𝘁 𝗔𝗱𝗱𝗲𝗱 𝗧𝗼 <a href="tg://user?id={user_id}">{user_id}</a> 𝗦𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹𝗹𝘆 ✅
      """
      await message.reply_text(resp,message.id)
      user_sms = f"""
𝗖𝗼𝗻𝗴𝗿𝗮𝘁𝘀 ! 
𝗬𝗼𝘂𝗿 𝗔𝗰𝗰𝗼𝘂𝗻𝘁 𝗝𝘂𝘀𝘁 𝗚𝗼𝘁 {amt} 𝗖𝗿𝗲𝗱𝗶𝘁𝘀 ✅

𝗧𝘆𝗽𝗲 /credits 𝘁𝗼 𝗞𝗻𝗼𝘄 𝗬𝗼𝘂𝗿 𝗖𝘂𝗿𝗿𝗲𝗻𝘁 𝗖𝗿𝗲𝗱𝗶𝘁𝘀
      """
      await Client.send_message(user_id,user_sms)
    except Exception as e:
      print(e)


