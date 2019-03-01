from slackclient import SlackClient
from datetime import date
import calendar
from random import randint
import os
import schedule
import time
import logging

f = open('authtoken.txt', 'r')

authtoken = f.read()

my_date = date.today()
weekday = calendar.day_name[my_date.weekday()] 


bobaurls = ["https://www.ezcater.com/catering/pvt/urban-ritual-san-francisco (highly recommend creme brulee)",
            "https://sweetalittle.com",
            "https://sweetalittle.com"]

url = bobaurls[randint(0, len(bobaurls) -1)]

token = authtoken      # found at https://api.slack.com/web#authentication
sc = SlackClient(token)

def sendMessage(sc):
  # make the POST request through the python slack client
  updateMsg = sc.api_call(
    "chat.postMessage",
    channel='#hatch-bot-testing',
    text="Happy " + weekday + "! Would you like some boba today? \n" + url + " :parrot: (testing)",
    username='bobabot', 
    icon_emoji=':boba:'
  )

  # check if the request was a success
  if updateMsg['ok'] is not True:
    logging.error(updateMsg)
  else:
    logging.debug(updateMsg)

schedule.every(10).seconds.do(lambda: sendMessage(sc))
logging.info("entering loop")


# schedule.every().friday.at("11:15").do(lambda: sendMessage(sc))
while True:
    schedule.run_pending()
    time.sleep(5) # sleep for 5 seconds between checks on the scheduler