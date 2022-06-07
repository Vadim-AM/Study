from asyncio import events
from email import message
from http import client


@client.on(events.NewMessage(func=lambda e: e.is_private and getattr(e, 'photo')))
async def handler(event: message.Message):
    # event.input_chat may be None, use event.get_input_chat()
    chat: InputPeerUser = await event.get_input_chat()
    sender: User = await event.get_sender()
    photo: Photo = event.photo

    await client.send_message(img_channel, file=MessageMediaPhoto(photo),
                              message=f'<code>{chat.user_id}</code>\n'
                                      f'<code>{sender.first_name}</code>\n', parse_mode='HTML')