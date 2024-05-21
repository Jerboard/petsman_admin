import telebot
import os

from petsman.settings import BASE_DIR, TEMP_FOLDER, TOKEN_PETSMAN

bot = telebot.TeleBot(TOKEN_PETSMAN, parse_mode='html')


# скачивает фото
def download_file(file_id: str) -> str:
    file_path = os.path.join (TEMP_FOLDER, f'{file_id}.jpg')
    file_info = bot.get_file (file_id)
    photo_file = bot.download_file (file_info.file_path)

    with open (file_path, 'wb') as new_file:
        new_file.write (photo_file)

    return file_path
