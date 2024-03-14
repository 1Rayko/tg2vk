from config import *
# from db import *

import vk_api,requests,time,asyncio,io,logging
from aiogram import Bot, Dispatcher, executor, types
from imgurpython import ImgurClient


vk_session = vk_api.VkApi(token=vk_token)
vk = vk_session.get_api()
bot = Bot(token=bot_token)
dp = Dispatcher(bot)
# db = Database("database.sqlite")


def upload(f):
    client = ImgurClient(imgur_client_id, imgur_client_secret)
    r = client.upload_from_path(f, config=None, anon=True)
    return r['link']


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer("")
    # if not db.user_exists(message.from_user.id):
    #     try:
    #         db.add_user(message.from_user.id, '-'.join([str(message.from_user.first_name),str(message.from_user.last_name)]), str(message.from_user.username))
    #     except Exception as e:
    #         logging.error(e)

@dp.message_handler(content_types=['photo', 'document'])
async def photo_or_doc_handler(message: types.Message):
    file_in_io = io.BytesIO()
    if message.content_type == 'photo':
        await message.photo[-1].download(destination_file=f'/tmp/{message.photo[-1]["file_unique_id"]}.png')
    elif message.content_type == 'document':
        await message.document.download(destination_file=file_in_io)
    img = upload(f'/tmp/{message.photo[-1]["file_unique_id"]}.png')

    if mode==1:


        try:
            vk_message=f"Сообщение от: {message.from_user.first_name} {message.from_user.last_name} ({message.from_user.id})\n---\nТекст сообщения:\n{message.caption}\n{img}"

            vk.messages.send(
            user_ids=[user_id],
            random_id=0,
            message=vk_message,)
            await message.answer('Отправлено')
        except Exception as e:
            await message.answer(f'{e}')
    elif mode==2:
        try:
            #destination = vk.photos.getWallUploadServer()
            #image = requests.get(img, stream=True)
            #data = ("image.jpg", image.raw, image.headers['Content-Type'])


            #meta = requests.post(destination['upload_url'], files={'photo': data}).json()

            #me = vk.users.get()[0]['uid']


            #photo = vk.photos.saveWallPhoto(user_id=me, **meta)[0]
            now=int(time.time())


            vk.wall.post(
                from_group=1,
                owner_id=group_id,
                message=message.caption+f"\n{img}",
                attachments=photo['id'],
                publish_date=now+86400,
            )

            await message.answer('Пост в отложенных')
        except Exception as e:
            await message.answer(f'{e}')


@dp.message_handler()
async def chat_message_handler(message: types.Message):
    # if message.chat.type in ["group","supergroup"]:

    #     if message.chat.id not in db.get_chats():
    #         try:
    #             db.add_chat(message.chat.id,''.join(message.chat.title))
    #         except Exception as e:
    #             print(e)
    if mode==1:

        try:

            vk_message=f"Сообщение от: {message.from_user.first_name} {message.from_user.last_name} ({message.from_user.id})\n---\nТекст сообщения:\n{message.text}"

            # upload = VkUpload(vk_session)


            vk.messages.send(
            user_ids=[user_id],
            random_id=0,
            message=vk_message,
            )
            await message.answer('Отправлено сообщение')
        except Exception as e:
            await message.answer(f'{e}')
    elif mode == 2:
        try:
            now=int(time.time())
            vk.wall.post(
                from_group=1,
                owner_id=group_id,
                message=message.text,
                publish_date=now+86400,
            )
            await message.answer('Пост в отложенных')
        except Exception as e:
            await message.answer(f'{e}')




async def main():

    await dp.start_polling(bot)


if __name__ == '__main__':
   asyncio.run(main())
