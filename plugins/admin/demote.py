from pyrogram import Client, filters
from plugins.func.users_sql import *
@Client.on_message(filters.command ('fr'))
async def cmd_fr(Client,message):
  user_id = str(message.from_user.id)
  CEO = "1900986195"
  if user_id != CEO :
    resp = "𝗥𝗲𝗾𝘂𝗶𝗿𝗲 𝗢𝘄𝗻𝗲𝗿 𝗣𝗿𝗶𝘃𝗶𝗹𝗮𝗴𝗲𝘀 ⚠️"
    msg1 = await message.reply_text(resp,message.id)
  else:
    try:
      if message.reply_to_message:
        userpm = message.reply_to_message.from_user.id
      else:
        userpm = message.text[len('/fr '):]
      pmid=userpm
      pm_chk = fetchinfo(pmid)
      status = str(pm_chk[2])
      if status !='PREMIUM':
        resp = f"""
<a href="tg://user?id={pmid}">{pmid}</a> 𝗶𝘀 𝗮𝗹𝗿𝗲𝗮𝗱𝘆 𝗮 𝗙𝗥𝗘𝗘 𝗠𝗲𝗺𝗯𝗲𝗿 ⚠️.
        """
        await message.reply_text(resp,message.id)
      else:
        module_name = "status"
        value = "FREE"
        updatedata(pmid,module_name,value)
        resp = f"""
<a href="tg://user?id={pmid}">{pmid}</a> 𝗶𝘀 𝗗𝗘𝗠𝗢𝗧𝗘𝗗 𝘁𝗼 𝗮 𝗙𝗥𝗘𝗘 𝗠𝗲𝗺𝗯𝗲𝗿 ✅.
        """
        await message.reply_text(resp,message.id)
        user_resp = """𝗛𝗘𝗬 𝗗𝗨𝗗𝗘 ! 
𝗬𝗢𝗨𝗥 𝗔𝗖𝗖𝗢𝗨𝗡𝗧 𝗦𝗨𝗖𝗖𝗘𝗦𝗦𝗙𝗨𝗟𝗟𝗬 𝗗𝗘𝗠𝗢𝗧𝗘𝗗 𝗧𝗢 '𝗙𝗥𝗘𝗘' 𝗨𝗦𝗘𝗥 ✅"""
        await Client.send_message(pmid,user_resp)
  
    except Exception as e:
      print(e)