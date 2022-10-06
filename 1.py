# import asyncio
import configparser
import telethon

# Импортируем конфигурационный файл
config = configparser.ConfigParser()
config.read("config.ini")

# Присваиваем значения внутренним переменным
api_id = 1111111
api_hash = 'heshfromtelegram'
username = 'anon'

# Массив для хранения ID пользователей, отправивших сообщение
user_id_list = []

# Создание объекта клиента Telegram
client = telethon.TelegramClient(username, api_id, api_hash)

# Запуск клиента
client.start()

# Событие на новое входящее сообщение
@client.on(telethon.events.NewMessage(incoming=True, forwards=None))
async def handler(event):
    user_info = event.message.to_dict()['from_id']
    print(user_info)
    user_id = user_info['user_id']
    count = 0
    for i in user_id_list:
        if i == user_id:
           count += 1
        else:
            continue
    if count == 0:
        user_id_list.append(user_id)
        # await asyncio.sleep(5)
        await client.send_message('me', 'Техт')
    print(user_id_list)


print('asdasdasdasds')
print(type(client))
for i in range(1,5):
    print(i)
client.run_until_disconnected()
for i in range(6,10):
    print(i)