
import time 
from typing import Text
from telethon import TelegramClient, events #,Button
from telethon.tl.custom import Button
from datetime import timedelta
import logging
import asyncio

from telethon.tl.types import InputPeerChannel
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                   level=logging.INFO)



# client telegram api
api_id = 4407795
api_hash = '7774cfea690ea5ba39ed1b15c9a5f0f6'


GAME_ID = None
REWARD_ID = None
HOF_ID = None
FAQ_ID = None


INPUT1 = 1168502525
INPUT2 = InputPeerChannel(channel_id=1168502525, access_hash=-765990212819668249)
token = '1840281216:AAFzyYbybV2UtLcjclgV0a2jGvzPS9yTB0E'

client1 = TelegramClient("bot", api_id, api_hash).start(bot_token=token)
client2 = TelegramClient("dev", api_id, api_hash)
def main():

    client1.start()
    client2.start()
    print("Userbot on!")
    client1.run_until_disconnected()
    client2.run_until_disconnected()
    






@client2.on(events.NewMessage(chats=INPUT1, from_users='me'))
async def set_game(event):


    global GAME_ID, REWARD_ID, HOF_ID, FAQ_ID
    my_message = event.original_update.message.message # This will get every message from admin
    if my_message == '/setgame': # Check if the message is '/setgame'
        get_game = event.original_update.message.reply_to # Will try to get the message which was replay 
        if get_game is not None: # Work if there is any replied to message 
            replyed_to = await client1.get_messages(INPUT2, ids=get_game.reply_to_msg_id)
            if replyed_to.media.game:
                GAME_ID = get_game.reply_to_msg_id
                await client1.send_message(entity=INPUT2, message = f'{replyed_to.media.game.short_name} is set as game')
            else:
                await client1.send_message(entity=INPUT2, message = f'Please use this command replaying to game' )
        else:
            await client1.send_message(entity=INPUT2, message = 'Please use this command replaying to game ')

    elif my_message == '/setreward':
        get_reward = event.original_update.message.reply_to
        REWARD_ID = get_reward.reply_to_msg_id
        await client1.send_message(entity=INPUT2, message = f'Reward message is set' )

    elif my_message == '/setfaq':
        get_faq = event.original_update.message.reply_to
        FAQ_ID = get_faq.reply_to_msg_id
        await client1.send_message(entity=INPUT2, message = f'FAQ message is set' )

    elif my_message == '/sethalloffame':
        get_HOF = event.original_update.message.reply_to
        HOF_ID = get_HOF.reply_to_msg_id
        await client1.send_message(entity=INPUT2, message = f'HALL OF FAME message is set' )







        
        



@client1.on(events.ChatAction)
async def user_add(event):
    if event.user_joined:
        user = await client1.get_entity(event.action_message.from_id)
    elif event.user_added:
        user = await client1.get_entity(event.action_message.action.users[0])
        await client1.send_message(entity=INPUT2,  message=f'''

Hi {user.first_name} Welcome to Cloud City ™ Click the Group Profile for information. 
Enjoy your stay! 🌇''')



@client1.on(events.CallbackQuery)
async def callback_bot(event):
    print(event)
    global GAME_ID, REWARD_ID, HOF_ID, FAQ_ID
    if event.data == b'1':
        replyed_to = await client2.get_messages(INPUT1, ids=GAME_ID)
        GAME_ID_message =  await client2.send_message(entity=INPUT1, message = replyed_to)
        GAME_ID = GAME_ID_message.id
    if event.data == b'2':
        replyed_to = await client2.get_messages(INPUT1, ids=GAME_ID)
        if replyed_to.message == '':
            await client2.send_message(entity=INPUT1, message = 'Nobody has played yet')
        else:
            await client2.send_message(entity=INPUT1, message = replyed_to.message)
    if event.data == b'3':
        replyed_to = await client2.get_messages(INPUT1, ids=REWARD_ID)
        await client2.send_message(entity=INPUT1, message = replyed_to)
    if event.data == b'4':
        replyed_to = await client2.get_messages(INPUT1, ids=FAQ_ID)
        await client2.send_message(entity=INPUT1, message = replyed_to)
    if event.data == b'5':
        replyed_to = await client2.get_messages(INPUT1, ids=HOF_ID)
        await client2.send_message(entity=INPUT1, message = replyed_to)



if __name__ == '__main__':
    main()
