# from plugins.func.users_sql import *
# # CREATE USERS TABLE
# import sqlite3
# conn = sqlite3.connect('plugins/xcc_db/users.db')
# db = conn.cursor()
# db.execute("""CREATE TABLE users(
#     id TEXT NOT NULL UNIQUE,
#     username TEXT,
#     status TEXT,
#     plan TEXT,
#     expiry TEXT,
#     credit TEXT,
#     antispam TEXT,
#     antispam_time TEXT,
#     totalkey TEXT,
#     reg_at TEXT
# )""")
# conn.commit()
# conn.close()
# print("TASK 1/4 COMPLETED")
# import sqlite3
# conn = sqlite3.connect('plugins/xcc_db/giftcard.db')
# db = conn.cursor()
# db.execute("""CREATE TABLE gc(
#     id TEXT NOT NULL UNIQUE,
#     status TEXT,
#     plan TEXT
# )""")
# conn.commit()
# conn.close()
# print("TASK 2/4 COMPLETED")
# print("NOW THE BOT DATABASE IS CREATED AND BOT CAN EASILY RUN NOW ✅.NOW RUN run.py FILE")
