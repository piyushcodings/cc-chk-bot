from plugins.admin.gc.gc_func import *
from pyrogram import Client, filters
from plugins.func.users_sql import *
from datetime import date
from datetime import timedelta
@Client.on_message(filters.command ('redeem'))
async def cmd_gc(Client,message):
  try:
    user_id = str(message.from_user.id)
    regdata = fetchinfo(user_id)
    results = str(regdata)
    if results=='None':
      resp = "𝗬𝗢𝗨 𝗔𝗥𝗘 𝗡𝗢𝗧 𝗥𝗘𝗚𝗜𝗦𝗧𝗘𝗥𝗘𝗗 𝗬𝗘𝗧 ⚠️. 𝗥𝗘𝗚𝗜𝗦𝗧𝗘𝗥 𝗙𝗜𝗥𝗦𝗧 𝗕𝗬 𝗨𝗦𝗜𝗡𝗚 /register 𝗧𝗢 𝗨𝗦𝗘 𝗠𝗘."
      await message.reply_text(resp,message.id)
    else:
      user_id = str(message.from_user.id)
      gc = message.text[len('/redeem '):]
      resp = f"{gc}"
      get = getgc(gc)
      t = str(get)
      if t=='None':
        resp = "𝗜𝗡𝗩𝗔𝗟𝗜𝗗 𝗚𝗜𝗙𝗧𝗖𝗢𝗗𝗘 ❌"
        await message.reply_text(resp,message.id)
      else:
        t = getgc(gc)
        status = t[1]
        plan = t[2]
        
      
        if status=='ACTIVE':
          if plan=='PREMIUM':
            fetch= fetchinfo(user_id)
            tkey = int(fetch[8])
            value = tkey + 1
            module_name = "totalkey"
            updatedata(user_id,module_name,value)
            credit = int(fetch[5])
            value = credit + 100
            module_name = "credit"
            updatedata(user_id,module_name,value)
            module_name = "status"
            value = "PREMIUM"
            updatedata(user_id,module_name,value)
            updategc(gc)
            resp = "𝗥𝗲𝗱𝗲𝗲𝗺 𝗦𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹𝗹𝘆 𝗚𝗶𝗳𝘁𝗰𝗮𝗿𝗱 𝘁𝗼 𝗬𝗼𝘂𝗿 𝗔𝗰𝗰𝗼𝘂𝗻𝘁 ✅. 𝗧𝗬𝗣𝗘 /credits 𝗧𝗢 𝗞𝗡𝗢𝗪 𝗖𝗥𝗘𝗗𝗜𝗧𝗦"
            await message.reply_text(resp,message.id)
          elif plan=='PLAN1':
            fetch= fetchinfo(user_id)
            tkey = int(fetch[8])
            value = tkey + 1
            module_name = "totalkey"
            updatedata(user_id,module_name,value)
            credit = int(fetch[5])
            value = credit + 1000
            module_name = "credit"
            updatedata(user_id,module_name,value)
            module_name = "status"
            value = "PREMIUM"
            updatedata(user_id,module_name,value)
            module_name = "plan"
            value = "Starter Plan 0.99$"
            updatedata(user_id,module_name,value)
            module_name = "expiry"
            today = str(date.today())
            value = str(date.today()+timedelta(days=7))
            updatedata(user_id,module_name,value)
            updategc(gc)
            resp = "𝗬𝗢𝗨 𝗛𝗔𝗩𝗘 𝗦𝗨𝗖𝗖𝗘𝗦𝗦𝗙𝗨𝗟𝗟𝗬 𝗥𝗘𝗗𝗘𝗘𝗠𝗘𝗗 '𝗦𝗧𝗔𝗥𝗧𝗘𝗥 𝗣𝗟𝗔𝗡' 𝗨𝗦𝗜𝗡𝗚 𝗚𝗜𝗙𝗧𝗖𝗢𝗗𝗘 ✅.𝗧𝗬𝗣𝗘 /info 𝗧𝗢 𝗞𝗡𝗢𝗪 𝗠𝗢𝗥𝗘"
            await message.reply_text(resp,message.id)
      
          elif plan=='PLAN2':
            fetch= fetchinfo(user_id)
            tkey = int(fetch[8])
            value = tkey + 1
            module_name = "totalkey"
            updatedata(user_id,module_name,value)
            credit = int(fetch[5])
            value = credit + 2000
            module_name = "credit"
            updatedata(user_id,module_name,value)
            module_name = "status"
            value = "PREMIUM"
            updatedata(user_id,module_name,value)
            module_name = "plan"
            value = "Silver Plan 1.99$"
            updatedata(user_id,module_name,value)
            module_name = "expiry"
            today = str(date.today())
            value = str(date.today()+timedelta(days=15))
            updatedata(user_id,module_name,value)
            updategc(gc)
            resp = "𝗬𝗢𝗨 𝗛𝗔𝗩𝗘 𝗦𝗨𝗖𝗖𝗘𝗦𝗦𝗙𝗨𝗟𝗟𝗬 𝗥𝗘𝗗𝗘𝗘𝗠𝗘𝗗 '𝗦𝗜𝗟𝗩𝗘𝗥 𝗣𝗟𝗔𝗡' 𝗨𝗦𝗜𝗡𝗚 𝗚𝗜𝗙𝗧𝗖𝗢𝗗𝗘 ✅.𝗧𝗬𝗣𝗘 /info 𝗧𝗢 𝗞𝗡𝗢𝗪 𝗠𝗢𝗥𝗘"
            await message.reply_text(resp,message.id)
            
          elif plan=='PLAN3':
            fetch= fetchinfo(user_id)
            tkey = int(fetch[8])
            value = tkey + 1
            module_name = "totalkey"
            updatedata(user_id,module_name,value)
            credit = int(fetch[5])
            value = credit + 5000
            module_name = "credit"
            updatedata(user_id,module_name,value)
            module_name = "status"
            value = "PREMIUM"
            updatedata(user_id,module_name,value)
            module_name = "plan"
            value = "Gold Plan 4.99$"
            updatedata(user_id,module_name,value)
            module_name = "expiry"
            today = str(date.today())
            value = str(date.today()+timedelta(days=30))
            updatedata(user_id,module_name,value)
            updategc(gc)
            resp = "𝗬𝗢𝗨 𝗛𝗔𝗩𝗘 𝗦𝗨𝗖𝗖𝗘𝗦𝗦𝗙𝗨𝗟𝗟𝗬 𝗥𝗘𝗗𝗘𝗘𝗠𝗘𝗗 '𝗚𝗢𝗟𝗗 𝗣𝗟𝗔𝗡' 𝗨𝗦𝗜𝗡𝗚 𝗚𝗜𝗙𝗧𝗖𝗢𝗗𝗘 ✅.𝗧𝗬𝗣𝗘 /info 𝗧𝗢 𝗞𝗡𝗢𝗪 𝗠𝗢𝗥𝗘"
            await message.reply_text(resp,message.id)
      
          else:
            ok = "NONE HAPPENNED"
            print(ok)
            
            
            
            
            
          
        elif status=='USED':
          resp = "𝗚𝗜𝗙𝗧𝗖𝗢𝗗𝗘 𝗔𝗟𝗥𝗘𝗔𝗗𝗬 𝗥𝗘𝗗𝗘𝗘𝗠𝗘𝗗 ⚠️"
          await message.reply_text(resp,message.id)
        elif status=='None':
          resp = "𝗜𝗡𝗩𝗔𝗟𝗜𝗗 𝗚𝗜𝗙𝗧𝗖𝗢𝗗𝗘 ❌"
          await message.reply_text(resp,message.id)
        else:
          resp = "𝗜𝗡𝗩𝗔𝗟𝗜𝗗 𝗚𝗜𝗙𝗧𝗖𝗢𝗗𝗘 ❌"
          await message.reply_text(resp,message.id)
  except Exception as e:
      print(e)
    
    
    
      
    
    
      