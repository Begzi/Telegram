from django.shortcuts import render, redirect
import asyncio
import telethon
# from telethon import TelegramClient, events, sync
from telethon.tl.functions.channels import JoinChannelRequest
# from telegram.client import Telegram

import socks


# Create your views here.
api_id = 111111
api_hash = 'apifromtelegram'
# loop = asyncio.new_event_loop()
# asyncio.set_event_loop(loop)
# client = telethon.TelegramClient('anon', api_id, api_hash, loop=loop)

def main(request):
    #
    # async def send_telethon_message(client):
    #     me = await client.get_me()
    #     await client.send_message('me', 'Testing Telethon1')
    # client = TelegramClient('anon', api_id, api_hash, loop=loop)
    # with client:
    #     loop.run_until_complete(send_telethon_message(client))
    # k = 0

    # async def check():
    #     dialogs = await client.get_dialogs()
    #     print('dialogsinner')
    #     print(dialogs)
    #     return dialogs
    # dialogs = check()
    # print('dialogs')
    # print(dialogs)

    # dialogs = client.get_dialogs()
    # for chat in dialogs.chats:
    #     getmessage = client.get_messages(chat.id, limit=400)
    #     for message in getmessage:
    #         print(message.message)

    # client = TelegramClient('@BigZEcheese', api_id, api_hash)
    # client = TelegramClient('@BigZEcheese', api_id, api_hash,  loop=loop)
    # with TelegramClient('anon', api_id, api_hash,  loop=loop) as client:
    #     loop.run_until_complete(client.send_message('me', 'Hello, myself!'))
    # client.start()
    # phone_number = '+79080196349'
    # client.send_code_request(phone_number)
    # myself = client.sign_in(phone_number, input('Enter code: '))
    # async def main():
    #     # Now you can use all client methods listed below, like for example...
    #     await client.send_message('me', 'Hello to myself!')
    #
    # with client:
    #     client.loop.run_until_complete(main())
    # # print(client.get_me().stringify())
    #
    # client.send_message('me', 'Hello! Talking to you from Telethon')
    # client.send_message('@ayasmaa_artyna', 'Hello! Talking to you from Telethon')

    # tg = Telegram(
    #     api_id=api_id,
    #     api_hash=api_hash,
    #     phone='+89080196349',  # you can pass 'bot_token' instead
    #     database_encryption_key='admin',
    # )
    # tg.login()
    #
    # # if this is the first run, library needs to preload all chats
    # # otherwise the message will not be sent
    # result = tg.get_chats()
    # result.wait()
    #
    # print(result)
    # # `tdlib` is asynchronous, so `python-telegram` always returns you an `AsyncResult` object.
    # # You can receive a result with the `wait` method of this object.
    # result.wait()
    # print(result.update)
    #
    # tg.stop()  # you must call `stop` at the end of the script
    # client = TelegramClient('some_name',api_id,api_hash,proxy = (socks.SOCKS5, 'localhost', 8000)  # Настройки прокси
    # ).start()
    # # Some_name здесь - случайное имя, при первом запуске вы сможете ввести свой номер телефона и код подтверждения, а затем будет сгенерирован файл some_name.session, и вам не нужно вводить код подтверждения номера телефона. неоднократно, когда вы запускаете его снова
    # myself = client.get_me()
    # print(myself)  # Проверяем, подключаться ли

    def code_callback():
        while True:
            code = input()
            return code
    async def run():
        try:
            await client.connect()   #From DB check, существует ли файл, если да, то коннектимся, если нет, то создаём
        except:
            await client.start(phone='+79080196349',  code_callback=code_callback)
        # dialogs = await client.get_dialogs()
        # channel = await client.get_entity('me')
        # first = dialogs[0]
        # for i in range(0, 5):
        #     print(dialogs[i].title)
        # # i = 0
        # # async for message in client.iter_messages(channel):
        # #     i = i + 1
        # #     print(str(i))
        # #     print(message)
        # #     if i == 5:
        # #         break
        # result = await client(telethon.functions.messages.GetPeerDialogsRequest(
        #     peers=[first]
        # ))
        # async for message in client.iter_messages(first, limit = 5 ):
        #     print(message.id, message.text)
        # mes = len(await  client.get_messages(first, limit = 1))
        # print(mes)
        # print(result.dialogs[0].read_outbox_max_id)  # Мною отправленное письмо, прочитанное последнее
        # print(result.dialogs[0])
        # if result.dialogs[0].read_outbox_max_id >= mes:
        #     print('the message has been read')
        # else:
        #     print('the message has not been read yet')
        #
        # @client.on(telethon.events.NewMessage(chats=("CANNEL")))
        # async def handler(event):
        #     if 'user_id=2807' in str(event.message):
        #         if 'text' in str(event.message):
        #             await event.reply('MESSAGE')
        # await client.send_message('@gexos', 'Вот это сообщение отправил от Python')
        user_id_list = []
        # @client.on(telethon.events.NewMessage(incoming=True, forwards=None))
        # async def handler(event):
        #     user_info = event.message.to_dict()['from_id']
        #     user_id = user_info['user_id']
        #     count = 0
        #     for i in user_id_list:
        #         if i == user_id:
        #             count += 1
        #         else:
        #             continue
        #     if count == 0:
        #         user_id_list.append(user_id)
        #         await asyncio.sleep(5)
        #         await client.send_message(user_id, 'Техт')
        #     print(user_id_list)
        # response = client.wait_event(telethon.events.NewMessage(
        #     outgoing=True,
        #     forwards=None
        # ))
        # response = await response
        # code = response.message.message.strip()
        # print(code)
    global client
    global loop
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    client = telethon.TelegramClient('anon', api_id, api_hash, loop=loop)
    client.loop.run_until_complete(run())
    print(type(client))
    return redirect('wait')

# @client.on(telethon.events.NewMessage(incoming=True, forwards=None))
#     async def handler(event):
#         # user_info = event.message.to_dict()['from_id']
#         # user_id = user_info['user_id']
#         # count = 0
#         # for i in user_id_list:
#         #     if i == user_id:
#         #         count += 1
#         #     else:
#         #         continue
#         # if count == 0:
#         #     user_id_list.append(user_id)
#         #     await asyncio.sleep(5)
#         #     await client.send_message(user_id, 'Техт')
#         print('asdadsdassaxa')
def notmain(request):
    async def run():
        await  client.disconnect()
    print(type(client))
    client.loop.run_until_complete(run())
    # client.loop.run_until_complete(run())
    return render(request, 'index.html')

def wait(request):

    async def run():
        dialogs = await client.get_dialogs()
        channel = await client.get_entity('me')
        first = dialogs[0]
        for i in range(0, 5):
            print(dialogs[i].title)
        # i = 0
        # async for message in client.iter_messages(channel):
        #     i = i + 1
        #     print(str(i))
        #     print(message)
        #     if i == 5:
        #         break
        result = await client(telethon.functions.messages.GetPeerDialogsRequest(
            peers=[first]
        ))
        async for message in client.iter_messages(first, limit = 5 ):
            print(message.id, message.text)
        mes = len(await  client.get_messages(first, limit = 1))
        print(mes)
        print(result.dialogs[0].read_outbox_max_id)  # Мною отправленное письмо, прочитанное последнее
        print(result.dialogs[0])
        if result.dialogs[0].read_outbox_max_id >= mes:
            print('the message has been read')
        else:
            print('the message has not been read yet')

        # @client.on(telethon.events.NewMessage(chats=("CANNEL")))
        # async def handler(event):
        #     if 'user_id=2807' in str(event.message):
        #         if 'text' in str(event.message):
        #             await event.reply('MESSAGE')
        # # await client.send_message('@gexos', 'Вот это сообщение отправил от Python')
        user_id_list = []


        # response = client.wait_event(telethon.events.NewMessage(
        #     outgoing=True,
        #     forwards=None
        # ))
        # response = await response
        # code = response.message.message.strip()
        # print(code)

    client.loop.run_until_complete(run())
    def write():
        print('asdasd')
    client.add_event_handler(write, telethon.events.NewMessage(incoming=True, forwards=None))
    # client.add_event_handler(handler)
    return render(request, 'index.html')