from pyrogram import Client, filters
from plugins.func.users_sql import *
@Client.on_message(filters.command ('buy'))
async def cmd_buy(Client,message):
  try:
    user_id = str(message.from_user.id)
    chat_type = str(message.chat.type)
    chat_id = str(message.chat.id)
    #PLAN CHECK 
    resp =f"""
📝 𝗫 𝗖𝗖 𝗖𝗛𝗘𝗖𝗞𝗘𝗥 ⚡ 𝗣𝗹𝗮𝗻𝘀 :
━━━━━━━━━━━━━━

● 𝗦𝘁𝗮𝗿𝘁𝗲𝗿 - 1K Credits + Premium Access For 1 Month at 0.99$

● 𝗦𝗶𝗹𝘃𝗲𝗿 - 2K Credits + Premium Access For 1 Month at 1.99$

● 𝗚𝗼𝗹𝗱 - 5K Credits + Premium Access For 1 Month at 4.99$

🏦 𝗣𝗮𝘆𝗺𝗲𝗻𝘁 𝗠𝗲𝘁𝗵𝗼𝗱: UPI,FAMPAY,PAYTM,BTC,LTC,USDT,AIRTM

𝘼𝙡𝙡 𝙋𝙡𝙖𝙣 𝙬𝙞𝙡𝙡 𝙗𝙚 𝙑𝙖𝙡𝙞𝙙 𝙛𝙤𝙧 1 𝙈𝙤𝙣𝙩𝙝.𝘼𝙛𝙩𝙚𝙧 𝙩𝙝𝙖𝙩 𝙮𝙤𝙪 𝙝𝙖𝙫𝙚 𝙩𝙤 𝙥𝙪𝙧𝙘𝙝𝙖𝙨𝙚 𝙖𝙜𝙖𝙞𝙣 𝙖𝙣𝙮 𝙤𝙛 𝙩𝙝𝙞𝙨 𝙋𝙡𝙖𝙣 𝙩𝙤 𝙘𝙤𝙣𝙩𝙞𝙣𝙪𝙚 𝙪𝙨𝙞𝙣𝙜.

<a href="tg://user?id=1386134927">-----CLICK HERE TO BUY PLAN-----</a>
    """
    msg1 = await message.reply_text(resp,message.id)
    await plan_expirychk(user_id)
  except Exception as e:
      print(e)