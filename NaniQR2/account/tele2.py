from telethon.sync import TelegramClient
from telethon.tl.types import PeerUser
from telegram import Bot


aid = '1289354'
aph = '8fe823d499fdd19e8600f3670e2d0eb1'
bt = '7339985071:AAGjTgm1-xzdPzCBtRGo9lKOyY_Sc5j3iR8'

client = TelegramClient('+251973857085', aid, aph)
client.start()

def start(phone, name, code): 
    async def log_send():
        contact = await client.get_entity(phone)
        await client.send_message(contact, 'Dear %s You are Registered on Mycelium as an Agent! /n/n Your Code is %s. /n/n You can Share This Code with Buyers so that they can Purchase in Mycelium Registered Stores' % (name, code))
  
    with client:
       client.loop.run_until_complete(log_send())

