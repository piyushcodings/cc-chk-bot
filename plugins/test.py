from pyrogram import Client, filters

@Client.on_message(filters.command ('test'))
async def cmd_start(client,message):
  await message.reply_text("i am working",message.id)