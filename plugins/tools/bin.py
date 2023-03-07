from pyrogram import Client, filters
import requests
import json
import re
import time
from plugins.func.users_sql import *
import requests
import json
session = requests.session()
@Client.on_message(filters.command ('bin'))
async def cmd_bin(Client,message):
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
      #CMD SENT NOW CHECKING VALID IF OR NOT CC#
        if message.reply_to_message:
          bin = message.reply_to_message.text
      
        else:
          bin = message.text[len('/bin '):]
        if len(bin) == 0:
            nocc = """
𝗚𝗜𝗩𝗘 𝗔 𝗩𝗔𝗟𝗜𝗗 𝗕𝗜𝗡 ❌
          """
            return await message.reply_text(nocc,message.id)
        fbin = bin[:6]
        session = requests.session()
        bin = session.get(f"https://lookup.binlist.net/{fbin}").json()
        try:
          brand = bin["scheme"].upper()
        except:
          brand = "N/A"
        try:
          type = bin["type"].upper()
        except:
          type = "N/A"
        try:
          level = bin["brand"].upper()
        except:
          level = "N/A"
        try:
          bank_data= bin["bank"]
        except:
          bank_data = "N/A"
        try:
          bank = bank_data["name"].upper()
        except:
          bank = "N/A"
        try:
          country_data = bin["country"]
        except:
          country_data = "N/A"
        try:
          country = country_data["name"].upper()
        except:
          country = "N/A"
        try:
          flag = country_data["emoji"]
        except:
          flag = "N/A"
        try:
          currency = country_data["currency"].upper()
        except:
          currency = "N/A"
        resp = f"""
𝗩𝗮𝗹𝗶𝗱 𝗕𝗜𝗡 ✅

𝗕𝗜𝗡:  <code>{fbin}</code>
𝗕𝗿𝗮𝗻𝗱: {brand}
𝗟𝗲𝘃𝗲𝗹: {level}
𝗧𝘆𝗽𝗲: {type}
𝗕𝗮𝗻𝗸: {bank}
𝗖𝗼𝘂𝗻𝘁𝗿𝘆: {country} - {flag} - {currency}

𝗖𝗵𝗲𝗰𝗸𝗲𝗱 𝗕𝘆 <a href="tg://user?id={message.from_user.id}"> {message.from_user.first_name}</a> [ {role} ]
𝗕𝗼𝘁 𝗕𝘆 <a href="tg://user?id=1386134927">[ 🇧🇩 ] ＭＴＣＴＥＣＨＸ 👑</a>
        """
        await message.reply_text(resp,message.id)
  except Exception as e:
      print(e)