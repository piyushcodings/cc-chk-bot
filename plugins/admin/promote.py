from pyrogram import Client, filters
from plugins.func.users_sql import *
@Client.on_message(filters.command ('pm'))
async def cmd_pm(Client,message):
  try:
    user_id = str(message.from_user.id)
    CEO = "1900986195"
    if user_id != CEO :
      resp = "𝗥𝗲𝗾𝘂𝗶𝗿𝗲 𝗢𝘄𝗻𝗲𝗿 𝗣𝗿𝗶𝘃𝗶𝗹𝗮𝗴𝗲𝘀 ⚠️"
      msg1 = await message.reply_text(resp,message.id)
    else:
      if message.reply_to_message:
        userpm = message.reply_to_message.from_user.id
      else:
        userpm = message.text[len('/pm '):]
      pmid=userpm
      pm_chk = fetchinfo(pmid)
      status = str(pm_chk[2])
      if status !='FREE':
        resp = f"""
  <a href="tg://user?id={pmid}">{pmid}</a> 𝗶𝘀 𝗮𝗹𝗿𝗲𝗮𝗱𝘆 𝗮 𝗣𝗥𝗘𝗠𝗜𝗨𝗠 𝗠𝗲𝗺𝗯𝗲𝗿 ⚠️.
        """
        await message.reply_text(resp,message.id)
      else:
        module_name = "status"
        value = "PREMIUM"
        updatedata(pmid,module_name,value)
        resp = f"""
  <a href="tg://user?id={pmid}">{pmid}</a> 𝗶𝘀 𝗽𝗿𝗼𝗺𝗼𝘁𝗲𝗱 𝘁𝗼 𝗮 𝗣𝗥𝗘𝗠𝗜𝗨𝗠 𝗠𝗲𝗺𝗯𝗲𝗿 ✅.
        """
        await message.reply_text(resp,message.id)
        user_resp = """𝗛𝗘𝗬 𝗗𝗨𝗗𝗘 ! 
𝗬𝗢𝗨𝗥 𝗔𝗖𝗖𝗢𝗨𝗡𝗧 𝗦𝗨𝗖𝗖𝗘𝗦𝗦𝗙𝗨𝗟𝗟𝗬 𝗣𝗥𝗢𝗠𝗢𝗧𝗘𝗗 𝗧𝗢 '𝗣𝗥𝗘𝗠𝗜𝗨𝗠' 𝗨𝗦𝗘𝗥 ✅"""
        await Client.send_message(pmid,user_resp)


  except Exception as e:
    print(e)
    
  
  
    