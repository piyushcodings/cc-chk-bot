from plugins.admin.gc.gc_func import *
from pyrogram import Client, filters
@Client.on_message(filters.command ('getplan2'))
async def cmd_getplan2(Client,message):
  user_id = str(message.from_user.id)
  CEO = "1900986195"
  if user_id != CEO :
    resp = "𝗥𝗲𝗾𝘂𝗶𝗿𝗲 𝗢𝘄𝗻𝗲𝗿 𝗣𝗿𝗶𝘃𝗶𝗹𝗮𝗴𝗲𝘀 ⚠️"
    msg1 = await message.reply_text(resp,message.id)
  else:
    resp = "𝗚𝗲𝗻𝗮𝗿𝗮𝘁𝗶𝗻𝗴.."
    send = await message.reply_text(resp,message.id)
    GC1 = f"XCC-{gcgenfunc()}-{gcgenfunc()}-{gcgenfunc()}"
    insert_plan2(GC1)
    resp = "𝗚𝗲𝗻𝗮𝗿𝗮𝘁𝗶𝗻𝗴 𝟭"
    send = await Client.edit_message_text(message.chat.id,send.id,resp)
    GC2 = f"XCC-{gcgenfunc()}-{gcgenfunc()}-{gcgenfunc()}"
    insert_plan2(GC2)
    resp = "𝗚𝗲𝗻𝗮𝗿𝗮𝘁𝗶𝗻𝗴 𝟮"
    send = await Client.edit_message_text(message.chat.id,send.id,resp)
    GC3 = f"XCC-{gcgenfunc()}-{gcgenfunc()}-{gcgenfunc()}"
    insert_plan2(GC3)
    resp = "𝗚𝗲𝗻𝗮𝗿𝗮𝘁𝗶𝗻𝗴 𝟯"
    send = await Client.edit_message_text(message.chat.id,send.id,resp)
    GC4 = f"XCC-{gcgenfunc()}-{gcgenfunc()}-{gcgenfunc()}"
    insert_plan2(GC4)
    resp = "𝗚𝗲𝗻𝗮𝗿𝗮𝘁𝗶𝗻𝗴 𝟰"
    send = await Client.edit_message_text(message.chat.id,send.id,resp)
    GC5 = f"XCC-{gcgenfunc()}-{gcgenfunc()}-{gcgenfunc()}"
    insert_plan2(GC5)
    resp = "𝗚𝗲𝗻𝗮𝗿𝗮𝘁𝗶𝗻𝗴 𝟱"
    send = await Client.edit_message_text(message.chat.id,send.id,resp)
    
    resp = "𝗗𝗼𝗻𝗲"
    send = await Client.edit_message_text(message.chat.id,send.id,resp)
    final_resp = f"""
𝗚𝗶𝗳𝘁𝗰𝗼𝗱𝗲 𝗚𝗲𝗻𝗮𝗿𝗮𝘁𝗲𝗱 ✅
𝗔𝗺𝗼𝘂𝗻𝘁: 𝟱

➔ <code>{GC1}</code>
𝗩𝗮𝗹𝘂𝗲 : 𝗦𝗶𝗹𝘃𝗲𝗿 𝗣𝗹𝗮𝗻 𝟭𝟱 𝗗𝗮𝘆𝘀

➔ <code>{GC2}</code>
𝗩𝗮𝗹𝘂𝗲 : 𝗦𝗶𝗹𝘃𝗲𝗿 𝗣𝗹𝗮𝗻 𝟭𝟱 𝗗𝗮𝘆𝘀

➔ <code>{GC3}</code>
𝗩𝗮𝗹𝘂𝗲 : 𝗦𝗶𝗹𝘃𝗲𝗿 𝗣𝗹𝗮𝗻 𝟭𝟱 𝗗𝗮𝘆𝘀

➔ <code>{GC4}</code>
𝗩𝗮𝗹𝘂𝗲 : 𝗦𝗶𝗹𝘃𝗲𝗿 𝗣𝗹𝗮𝗻 𝟭𝟱 𝗗𝗮𝘆𝘀

➔ <code>{GC5}</code>
𝗩𝗮𝗹𝘂𝗲 : 𝗦𝗶𝗹𝘃𝗲𝗿 𝗣𝗹𝗮𝗻 𝟭𝟱 𝗗𝗮𝘆𝘀


𝗙𝗼𝗿 𝗥𝗲𝗱𝗲𝗲𝗺𝘁𝗶𝗼𝗻 
𝗧𝘆𝗽𝗲 /redeem
    """
    send = await Client.edit_message_text(message.chat.id,send.id,final_resp)















