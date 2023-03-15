import asyncio
from pyrogram import Client, compose, filters, enums
import re
from pathlib import Path
from defs import getcards
from plugins.func.users_sql import *

plugins = dict(root="plugins")


async def main():
  user = Client("scrapper",
                api_id="24578407",
                api_hash="5f711fbe013fd0d20147f62728118510")
  bot = Client("my_bot",
               api_id="24578407",
               api_hash="5f711fbe013fd0d20147f62728118510",
               bot_token="6127557847:AAEGXigaZIS4MHoxOudREzxZnNQKtu4TjD8",
               plugins=plugins)
  clients = [user, bot]
  bot.set_parse_mode(enums.ParseMode.HTML)

  print("Done Bot Active ✅")

  await compose(clients)


