from asgiref.sync import async_to_sync
from django.db.models import Q
from shapely import wkb


import typing as t
import re
import os

from petsman.settings import UB_API_ID, UB_API_HAS
from bot_admin.models import Pets, MailingChat
from bot_admin.maps import pets_type_dict, pets_gender_dict
from bot_admin.bot_petsman import download_file


# повторно отправляет сообщения
# async def send_telegram_message(chats_ids: list, text: str, photo_path: t.Union[str, None]):
#     async with Client (
#             name='petsman_user',
#             api_id=UB_API_ID,
#             api_hash=UB_API_HAS,
#     ) as app:
#         app: Client
#         for chat_id in chats_ids:
#             if photo_path:
#                 await app.send_photo(chat_id=chat_id, photo=photo_path, caption=text)
#             else:
#                 await app.send_message (chat_id=chat_id, text=text)


# убирает пустые строки
def clearing_text(text: str) -> str:
    clear_text = ''
    for row in text.split ('\n'):
        if not re.search ('None', row):
            clear_text = f'{clear_text}\n{row}'

    return clear_text.strip()


# def send_telegram_message_sync(ads: list):
#     for ad in ads:
#         ad: Pets
#
#         if ad.location:
#             geometry = wkb.loads (ad.location)
#             lon, lat = geometry.coords [0]
#             location = f'<a href="https://www.google.com/maps?q={lat},{lon}"><b>Локация</b></a>'
#         elif ad.address:
#             location = f'<b>Адрес:</b> {ad.address}'
#         else:
#             location = ''
#
#         pet_type_str = pets_type_dict.get(ad.pet_type)
#         pet_gender_str = pets_gender_dict.get(ad.pet_gender)
#
#         text = (
#             f'<b>Дата потери: {ad.date}</b>\n'
#             f'#{pet_type_str}\n'
#             f'#{pet_gender_str}\n'
#             f'Название приюта: {ad.shelter_id}\n'
#             f'{ad.description}\n'
#             f'<b>Вознаграждение:</b> {ad.price}\n'
#             f'<b>Телефон:</b> {ad.phone}\n'
#             f'<b>Соц. сети:</b> {ad.url}\n'
#             f'{location}'
#         )
#
#         chats = MailingChat.objects.filter (
#             city_id=ad.city_id,
#             is_active=True
#         ).filter (
#             Q (pet_type='all') | Q (pet_type=ad.pet_type)
#         )
#         chats_ids = [chat.chat_id for chat in chats]
#
#         if ad.photo_id:
#             photo_path = download_file(ad.photo_id)
#         else:
#             photo_path = None
#
#         async_to_sync(send_telegram_message)(chats_ids, clearing_text(text), photo_path)
#
#         if photo_path:
#             os.remove(photo_path)
