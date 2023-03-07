from pyrogram import Client, filters
import requests
import json
import re
import time
from plugins.func.users_sql import *
import concurrent.futures
from plugins.gates.func.mass_charge_func import charge_func
session = requests.session()
@Client.on_message(filters.command ('mchk'))
async def cmd_mchk(Client,message):
  try:
    user_id = str(message.from_user.id)
    chat_type = str(message.chat.type)
    chat_id = str(message.chat.id)
    regdata = fetchinfo(user_id)
    results = str(regdata)
    if results=='None':
      resp = "𝗬𝗢𝗨 𝗔𝗥𝗘 𝗡𝗢𝗧 𝗥𝗘𝗚𝗜𝗦𝗧𝗘𝗥𝗘𝗗 𝗬𝗘𝗧 ⚠️. 𝗥𝗘𝗚𝗜𝗦𝗧𝗘𝗥 𝗙𝗜𝗥𝗦𝗧 𝗕𝗬 𝗨𝗦𝗜𝗡𝗚 /register 𝗧𝗢 𝗨𝗦𝗘 𝗠𝗘."
      await message.reply_text(resp,message.id)
    else:
      #PLAN CHECK 
      await plan_expirychk(user_id)
      #PM AND AUTH CHECK
      pm = fetchinfo(user_id)
      status = pm[2]
      role = status
      GROUP = open("plugins/group.txt").read().splitlines()
      if chat_type=="ChatType.PRIVATE" and status=="FREE" :
        resp = "𝗢𝗡𝗟𝗬 𝗣𝗥𝗘𝗠𝗜𝗨𝗠 𝗠𝗘𝗠𝗕𝗘𝗥𝗦 𝗔𝗥𝗘 𝗔𝗟𝗟𝗢𝗪𝗘𝗗 𝗧𝗢 𝗨𝗦𝗘 𝗕𝗢𝗧 𝗜𝗡 𝗣𝗘𝗥𝗦𝗢𝗡𝗔𝗟 ⚠️."
        await message.reply_text(resp,message.id)
      
      elif chat_type=="ChatType.GROUP" or   chat_type=="ChatType.SUPERGROUP" and chat_id not in GROUP:
        resp = "𝗨𝗡𝗔𝗨𝗧𝗛𝗢𝗥𝗜𝗭𝗘𝗗 𝗖𝗛𝗔𝗧 ❌. 𝗖𝗢𝗡𝗧𝗔𝗖𝗧 @mtctechx 𝗧𝗢 𝗔𝗨𝗧𝗛𝗢𝗥𝗜𝗭𝗘."
        await message.reply_text(resp,message.id)
      else:
        #CREDIT CHECK
        chk_credit = fetchinfo(user_id)
        credit = int(chk_credit[5])
        if credit < 5:
          resp = "𝗬𝗢𝗨 𝗛𝗔𝗩𝗘 𝗜𝗡𝗦𝗨𝗙𝗙𝗜𝗖𝗜𝗘𝗡𝗧 𝗖𝗥𝗘𝗗𝗜𝗧 𝗧𝗢 𝗨𝗦𝗘 𝗠𝗘 ⚠️ . 𝗥𝗘𝗖𝗛𝗔𝗥𝗚𝗘 𝗖𝗥𝗘𝗗𝗜𝗧 𝗨𝗦𝗜𝗡𝗚 /buy 𝗢𝗥 𝗪𝗔𝗜𝗧 𝗙𝗢𝗥 𝗙𝗥𝗘𝗘 𝗖𝗥𝗘𝗗𝗜𝗧 𝗨𝗦𝗜𝗡𝗚 𝗚𝗜𝗙𝗧𝗖𝗢𝗗𝗘 ."
          await message.reply_text(resp,message.id)
        else:
          #ANTISPAM MODULE
          user_id = str(message.from_user.id)
          results = fetchinfo(user_id)
          antispam = int(results[6])
          antispam_time = int(results[7])
          now = int(time.time())
          count_antispam = now - antispam_time
          if count_antispam < 180 and role=='FREE':
            after = 180 - count_antispam
            resp = f"""
𝗔𝗡𝗧𝗜𝗦𝗣𝗔𝗠 ⚠️
𝗧𝗥𝗬 𝗔𝗚𝗔𝗜𝗡 𝗔𝗙𝗧𝗘𝗥 {after} 𝗦𝗘𝗖𝗢𝗡𝗗𝗦
            """
            await message.reply_text(resp,message.id)
          elif count_antispam < 120 and role=='PREMIUM':
            after = 120 - count_antispam
            resp = f"""
𝗔𝗡𝗧𝗜𝗦𝗣𝗔𝗠 ⚠️
𝗧𝗥𝗬 𝗔𝗚𝗔𝗜𝗡 𝗔𝗙𝗧𝗘𝗥 {after} 𝗦𝗘𝗖𝗢𝗡𝗗𝗦
            """
            await message.reply_text(resp,message.id)
          else:
            if message.reply_to_message:
              all_cards = message.reply_to_message.text
          
            else:
              all_cards = message.text.split('\n')
              stresp = "𝗦𝗧𝗔𝗥𝗧𝗘𝗗 𝗖𝗛𝗘𝗖𝗞𝗜𝗡𝗚.."
              stchk=  await message.reply_text(stresp,message.id)
              len_cards = len(all_cards)
              if len(all_cards) > 6 and role=="FREE":
                resp = "𝗦𝗢𝗥𝗥𝗬 𝗙𝗥𝗘𝗘 𝗨𝗦𝗘𝗥 𝗔𝗥𝗘 𝗟𝗜𝗠𝗜𝗧𝗘𝗗 𝗧𝗢 5 𝗖𝗖 𝗖𝗛𝗘𝗖𝗞 𝗟𝗜𝗠𝗜𝗧 ❌"
                free = await Client.edit_message_text(message.chat.id,stchk.id,resp)
          
              elif len(all_cards) > 11 and role=="PREMIUM":
                resp = "𝗦𝗢𝗥𝗥𝗬 𝗣𝗥𝗘𝗠𝗜𝗨𝗠 𝗠𝗘𝗠𝗕𝗘𝗥𝗦 𝗛𝗔𝗦 10 𝗖𝗖 𝗖𝗛𝗘𝗖𝗞 𝗟𝗜𝗠𝗜𝗧 ❌"
                PREMIUM = await Client.edit_message_text(message.chat.id,stchk.id,resp)
              else:
                resp = "𝗚𝗘𝗧𝗧𝗜𝗡𝗚 𝗩𝗔𝗟𝗜𝗗 𝗜𝗡𝗣𝗨𝗧..."
                okst = await Client.edit_message_text(message.chat.id,stchk.id,resp)
                cards = []
                for x in all_cards:
                  input = re.findall(r"[0-9]+", x)
                  if not input or len(input) < 3:
                    continue
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
                  else:
                   continue
                len_cards = len(cards)
                if not len_cards:
                  resp = "𝗡𝗢𝗧 𝗙𝗢𝗨𝗡𝗗 𝗔𝗡𝗬 𝗩𝗔𝗟𝗜𝗗 𝗖𝗔𝗥𝗗"
                  nov =  await Client.edit_message_text(message.chat.id,okst.id,resp)
                else:
                  resp = f"𝗜 𝗝𝗨𝗦𝗧 𝗙𝗢𝗨𝗡𝗗 {len_cards} 𝗖𝗔𝗥𝗗 𝗙𝗥𝗢𝗠 𝗬𝗢𝗨𝗥 𝗜𝗡𝗣𝗨𝗧.𝗜 𝗔𝗠 𝗖𝗛𝗘𝗖𝗞𝗜𝗡𝗚..."
                  nov =  await Client.edit_message_text(message.chat.id,okst.id,resp)
                  
                  text = f"""
<b>↯ MASS CHARGE</b> \n
  """
                  r = requests.Session()
                  for inp in cards:
                    time.sleep(0.5)
                    with concurrent.futures.ThreadPoolExecutor() as executor:
                      future = executor.submit(charge_func, r, inp[0], inp[3], inp[1], inp[2])
                      return_value = future.result()
                      text += return_value
                      done = await Client.edit_message_text(message.chat.id,nov.id,text)
          
                  text += f"""
<b>－－－－－－－－－－－－－－－－
[ CHECK INFO ]
⌧ Proxy  - Live! 🌐 
⌧ Total CC Checked - {len_cards}
⌧ Credit Deducted - {len_cards}
⌧ Checked by: <a href="tg://user?id={message.from_user.id}"> {message.from_user.first_name}</a> ♻️ [ {role}]
⌧ Client by - <a href="tg://user?id=1386134927">[ 🇧🇩 ] ＭＴＣＴＥＣＨＸ 👑</a>
－－－－－－－－－－－－－－－－</b>
          """
                  await Client.edit_message_text(message.chat.id,nov.id,text)
                  #ANTISPAM TIME SET
                  module_name = "antispam_time"
                  value = int(time.time())
                  updatedata(user_id,module_name,value)
                  #CREDIT DEDUCT SECTION
                  fetch= fetchinfo(user_id)
                  credit = int(fetch[5])
                  module_name = "credit"
                  amt = len_cards * 1
                  deduct = credit - amt
                  value = deduct
                  updatedata(user_id,module_name,value)
  except Exception as e:
      print(e)