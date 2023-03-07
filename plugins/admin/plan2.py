from pyrogram import Client, filters
from plugins.func.users_sql import *
from datetime import date
from datetime import timedelta

@Client.on_message(filters.command ('plan2'))
async def cmd_plan2(Client,message):
  user_id = str(message.from_user.id)
  CEO = "1900986195"
  if user_id != CEO :
    resp = "𝗥𝗲𝗾𝘂𝗶𝗿𝗲 𝗢𝘄𝗻𝗲𝗿 𝗣𝗿𝗶𝘃𝗶𝗹𝗮𝗴𝗲𝘀 ⚠️"
    msg1 = await message.reply_text(resp,message.id)
  else:
    try:
      msg = message.text[len('/plan2 '):]
      splitter = msg.split(' ')
      userid = splitter[0]
      paymnt_method = splitter[1]
      pmid = userid
      pm_chk = fetchinfo(pmid)
      pmresults = str(pm_chk)
      if pmresults=='None':
        resp = "𝗨𝗦𝗘𝗥 𝗜𝗦 𝗡𝗢𝗧 𝗥𝗘𝗚𝗜𝗦𝗧𝗘𝗥𝗘𝗗 𝗧𝗢 𝗧𝗛𝗘 𝗕𝗢𝗧 ❌ "
        await message.reply_text(resp,message.id)
      else:
        module_name = "plan"
        value = "Silver Plan 1.99$"
        updatedata(pmid,module_name,value)
        fetch= fetchinfo(user_id)
        credit = int(fetch[5])
        module_name = "credit"
        deduct = credit + 2000
        value = deduct
        updatedata(pmid,module_name,value)
        today = str(date.today())
        validity = str(date.today()+timedelta(days=30))
        module_name = "expiry"
        value = validity
        updatedata(pmid,module_name,value)
        module_name = "status"
        value = "PREMIUM"
        updatedata(pmid,module_name,value)
        ad_resp = f"""𝗨𝗦𝗘𝗥 <a href="tg://user?id={pmid}">{pmid}</a> 𝗦𝗨𝗖𝗖𝗘𝗦𝗦𝗙𝗨𝗟𝗟𝗬 𝗣𝗨𝗥𝗖𝗛𝗔𝗦𝗘𝗗 𝗦𝗜𝗟𝗩𝗘𝗥 𝗣𝗟𝗔𝗡 𝗔𝗧 1.99$"""
        await message.reply_text(ad_resp,message.id)
        receipt_id = randgen(len=10)
        user_resp = f"""
𝗧𝗵𝗮𝗻𝗸𝘀 𝗬𝗼𝘂 𝗙𝗼𝗿 𝗣𝘂𝗿𝗰𝗵𝗮𝘀𝗶𝗻𝗴 𝗢𝘂𝗿 𝗦𝗶𝗹𝘃𝗲𝗿 𝗣𝗹𝗮𝗻 ✅

𝗜𝗗 : <code>{pmid}</code>
𝗣𝗹𝗮𝗻 : Silver
𝗣𝗿𝗶𝗰𝗲 : 1.99$
𝗣𝘂𝗿𝗰𝗵𝗮𝘀𝗲 𝗗𝗮𝘁𝗲: {today}
𝗘𝘅𝗽𝗶𝗿𝘆 : {validity}
𝗩𝗮𝗹𝗶𝗱𝗶𝘁𝘆: 30 Days
𝗦𝘁𝗮𝘁𝘂𝘀 : Paid ☑️
𝗣𝗮𝘆𝗺𝗲𝗻𝘁 𝗠𝗲𝘁𝗵𝗼𝗱 : {paymnt_method}.
𝗥𝗲𝗰𝗲𝗶𝗽𝘁 𝗜𝗗 : XCC{receipt_id}

𝙏𝙝𝙞𝙨 𝙞𝙨 𝙖 𝙧𝙚𝙘𝙚𝙞𝙥𝙩 𝙛𝙤𝙧 𝙮𝙤𝙪𝙧 𝙥𝙡𝙖𝙣.𝙎𝙖𝙫𝙚𝙙 𝙞𝙩 𝙞𝙣 𝙖 𝙎𝙚𝙘𝙪𝙧𝙚 𝙋𝙡𝙖𝙘𝙚.𝙏𝙝𝙞𝙨 𝙬𝙞𝙡𝙡 𝙝𝙚𝙡𝙥 𝙮𝙤𝙪 𝙞𝙛 𝙖𝙣𝙮𝙩𝙝𝙞𝙣𝙜 𝙜𝙤𝙚𝙨 𝙬𝙧𝙤𝙣𝙜 𝙬𝙞𝙩𝙝 𝙮𝙤𝙪𝙧 𝙥𝙡𝙖𝙣 𝙥𝙪𝙧𝙘𝙝𝙖𝙨𝙚𝙨 .

𝗛𝗮𝘃𝗲 𝗮 𝗚𝗼𝗼𝗱 𝗗𝗮𝘆 .
- @mtctechx
        """
        await Client.send_message(pmid,user_resp)
    except Exception as e:
      print(e)





      


      
    
      