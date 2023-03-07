from plugins.admin.gc.gc_func import *
from pyrogram import Client, filters
@Client.on_message(filters.command ('getplan3'))
async def cmd_getplan3(Client,message):
  user_id = str(message.from_user.id)
  CEO = "1900986195"
  if user_id != CEO :
    resp = "𝗥𝗲𝗾𝘂𝗶𝗿𝗲 𝗢𝘄𝗻𝗲𝗿 𝗣𝗿𝗶𝘃𝗶𝗹𝗮𝗴𝗲𝘀 ⚠️"
    msg1 = await message.reply_text(resp,message.id)
  else:
    resp = "𝗚𝗲𝗻𝗮𝗿𝗮𝘁𝗶𝗻𝗴.."
    send = await message.reply_text(resp,message.id)
    GC1 = f"XCC-{gcgenfunc()}-{gcgenfunc()}-{gcgenfunc()}"
    insert_plan3(GC1)
    resp = "𝗚𝗲𝗻𝗮𝗿𝗮𝘁𝗶𝗻𝗴 𝟭"
    send = await Client.edit_message_text(message.chat.id,send.id,resp)
    
    resp = "𝗗𝗼𝗻𝗲"
    send = await Client.edit_message_text(message.chat.id,send.id,resp)
    final_resp = f"""
𝗚𝗶𝗳𝘁𝗰𝗼𝗱𝗲 𝗚𝗲𝗻𝗮𝗿𝗮𝘁𝗲𝗱 ✅
𝗔𝗺𝗼𝘂𝗻𝘁: 1

➔ <code>{GC1}</code>
𝗩𝗮𝗹𝘂𝗲 : 𝗚𝗼𝗹𝗱 𝗣𝗹𝗮𝗻 𝟯𝟬 𝗗𝗮𝘆𝘀

𝗙𝗼𝗿 𝗥𝗲𝗱𝗲𝗲𝗺𝘁𝗶𝗼𝗻 
𝗧𝘆𝗽𝗲 /redeem
    """
    send = await Client.edit_message_text(message.chat.id,send.id,final_resp)















