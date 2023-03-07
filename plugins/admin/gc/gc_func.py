#RANDOM GEN FUNCTION
def gcgenfunc(len=4):
  import string
  import random
  chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
  return ''.join(random.choice(chars) for _ in range(len))
#insert registration data
def insert_pm(gc):
  import sqlite3
  conn = sqlite3.connect('plugins/xcc_db/giftcard.db')
  db = conn.cursor()
  db.execute(f"INSERT INTO gc VALUES ('{gc}','ACTIVE','PREMIUM')")
  conn.commit()
  conn.close()

def insert_plan1(gc):
  import sqlite3
  conn = sqlite3.connect('plugins/xcc_db/giftcard.db')
  db = conn.cursor()
  db.execute(f"INSERT INTO gc VALUES ('{gc}','ACTIVE','PLAN1')")
  conn.commit()
  conn.close()

def insert_plan2(gc):
  import sqlite3
  conn = sqlite3.connect('plugins/xcc_db/giftcard.db')
  db = conn.cursor()
  db.execute(f"INSERT INTO gc VALUES ('{gc}','ACTIVE','PLAN2')")
  conn.commit()
  conn.close()

def insert_plan3(gc):
  import sqlite3
  conn = sqlite3.connect('plugins/xcc_db/giftcard.db')
  db = conn.cursor()
  db.execute(f"INSERT INTO gc VALUES ('{gc}','ACTIVE','PLAN3')")
  conn.commit()
  conn.close()

# fetch info from userid
def getgc(gc):
  import sqlite3
  conn = sqlite3.connect('plugins/xcc_db/giftcard.db')
  db = conn.cursor()
  db.execute(f"SELECT * FROM gc WHERE id='{gc}'")
  info = db.fetchone()
  conn.commit()
  conn.close()
  return info

# fetch all info from table
def getallgc():
  import sqlite3
  conn = sqlite3.connect('plugins/xcc_db/giftcard.db')
  db = conn.cursor()
  db.execute(f"SELECT * FROM gc")
  info = db.fetchall()
  conn.commit()
  conn.close()
  return info

#UPDATE DATA FROM TABLE
def updategc(gc):
  import sqlite3
  conn = sqlite3.connect('plugins/xcc_db/giftcard.db')
  c = conn.cursor()
  c.execute(f"UPDATE gc SET status='USED' WHERE id='{gc}'")
  conn.commit()
  conn.close()


