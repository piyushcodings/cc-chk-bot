from pyrogram import Client, filters

@Client.on_message(filters.command ('start'))
async def cmd_start(Client,message):
  try:
    user_id = str(message.from_user.id)
    chat_type = str(message.chat.type)
    chat_id = str(message.chat.id)
    #PLAN CHECK 
    
    texta = """
𝗦𝘁𝗮𝗿𝘁𝗶𝗻𝗴 𝗫 𝗖𝗖 𝗖𝗛𝗘𝗖𝗞𝗘𝗥 ⚡ ■□□
      """
    edit = await message.reply_text(texta,message.id)
    textb = """
𝗦𝘁𝗮𝗿𝘁𝗶𝗻𝗴 𝗫 𝗖𝗖 𝗖𝗛𝗘𝗖𝗞𝗘𝗥 ⚡ ■■□
      """
    edit = await Client.edit_message_text(message.chat.id,edit.id,textb)
    textc = """
𝗦𝘁𝗮𝗿𝘁𝗶𝗻𝗴 𝗫 𝗖𝗖 𝗖𝗛𝗘𝗖𝗞𝗘𝗥 ⚡ ■■■
      """
    edit = await Client.edit_message_text(message.chat.id,edit.id,textc)
    textd = f"""
𝗛𝗲𝘆 <a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a> 

𝗪𝗘𝗟𝗖𝗢𝗠𝗘 𝗧𝗢 𝗫 𝗖𝗖 𝗖𝗛𝗘𝗖𝗞𝗘𝗥 ⚡ 𝗕𝗢𝗧. 𝗜 𝗔𝗠 𝗔 𝗖𝗖 𝗖𝗛𝗘𝗖𝗞𝗘𝗥 𝗕𝗢𝗧 𝗪𝗜𝗧𝗛 𝗠𝗔𝗡𝗬 𝗧𝗢𝗢𝗟𝗦 𝗔𝗡𝗗 𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦. 𝗜 𝗖𝗔𝗡 𝗗𝗢 𝗠𝗔𝗡𝗬 𝗪𝗢𝗥𝗞𝗦.

𝗧𝗬𝗣𝗘 /register 𝗧𝗢 𝗖𝗢𝗡𝗧𝗜𝗡𝗨𝗘 𝗨𝗦𝗜𝗡𝗚 𝗠𝗘🥰🥰

"""
    edit = await Client.edit_message_text(message.chat.id,edit.id,textd)
    await plan_expirychk(user_id)
  except Exception as e:
      print(e)
