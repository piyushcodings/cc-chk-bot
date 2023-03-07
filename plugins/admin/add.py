from pyrogram import Client, filters
@Client.on_message(filters.command ('add'))
async def cmd_add(Client,message):
  user_id = str(message.from_user.id)
  CEO = "1900986195"
  GROUP = open("plugins/group.txt").read().splitlines()
  if user_id != CEO :
    resp = "𝗥𝗲𝗾𝘂𝗶𝗿𝗲 𝗢𝘄𝗻𝗲𝗿 𝗣𝗿𝗶𝘃𝗶𝗹𝗮𝗴𝗲𝘀 ⚠️"
    msg1 = await message.reply_text(resp,message.id)
  else:
    chat_add = message.text[len('/add '):]
    if len(chat_add) == 0:
      chat_id = str(message.chat.id)
    else:
      chat_id = message.text[len('/add '):]
    groupid = chat_id
    if groupid in GROUP:
      resp = f"""
𝗧𝗵𝗶𝘀 𝗴𝗿𝗼𝘂𝗽 (<code>{groupid}</code>) 𝗶𝘀 𝗮𝗹𝗿𝗲𝗮𝗱𝘆 𝗮𝘂𝘁𝗵𝗼𝗿𝗶𝘇𝗲𝗱 ⚠️.
      """
      await message.reply_text(resp,message.id)
    else:
      with open("plugins/group.txt", "a") as f:
        f.write(f"{groupid}\n")
      resp = f"""
𝗧𝗵𝗶𝘀 𝗴𝗿𝗼𝘂𝗽 (<code>{groupid}</code>) 𝗶𝘀 𝗻𝗼𝘄 𝗮𝘂𝘁𝗵𝗼𝗿𝗶𝘇𝗲𝗱 ✅.
      """
      await message.reply_text(resp,message.id)
  
    