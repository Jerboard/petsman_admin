from django.db import models
from django.contrib.postgres.fields import ArrayField

from datetime import datetime

from bot_admin import maps


# места и события
class Place(models.Model):
    id = models.AutoField ('ID', primary_key=True)
    user_id = models.BigIntegerField ('ID владельца', null=True, blank=True)
    created_at = models.DateTimeField ('Создано', null=True, blank=True)
    updated_at = models.DateTimeField ('Обновлено', null=True, blank=True)
    category_id = models.CharField ('Категория', max_length=64, null=True, blank=True, choices=maps.objects)
    city_id = models.CharField ('Город', max_length=64, null=True, blank=True, choices=maps.cities)
    address = models.TextField ('Адрес', null=True, blank=True)
    phone = models.CharField ('Телефон', max_length=64, null=True, blank=True)
    url = ArrayField (base_field=models.CharField(255), verbose_name='Ссылки', null=True, blank=True)
    # image = models.CharField ('Фото', max_length=255, null=True, blank=True)
    # location = geo_model.PointField('Локация', geography=True, null=True, blank=True)
    # tags = models.TextField ('Теги', null=True, blank=True)
    name_ru = models.CharField ('Название ru', max_length=255, null=True, blank=True)
    # name_en = models.CharField ('Название en', max_length=255, null=True, blank=True)
    # name_uz = models.CharField ('Название uz', max_length=255, null=True, blank=True)
    description_ru = models.TextField ('Описание ru', null=True, blank=True)
    # description_en = models.TextField ('Описание en', null=True, blank=True)
    # description_uz = models.TextField ('Описание uz', null=True, blank=True)
    work_time_ru = models.TextField ('Время работы ru', null=True, blank=True)
    # work_time_en = models.TextField ('Время работы en', null=True, blank=True)
    # work_time_uz = models.TextField ('Время работы uz', null=True, blank=True)
    is_published = models.BooleanField ('Опубликовано', null=True, blank=True)
    photo_path = models.ImageField ('Изменить фото', upload_to="photos_objects/", null=True, blank=True)

    def __str__(self):
        return f"<Place({self.id}, {self.name_ru})>"

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'
        db_table = 'objects'
        managed = False


# животные потерянные и не очень
class Pets(models.Model):
    id = models.AutoField ('ID', primary_key=True)
    created_at = models.DateTimeField('Создана', null=True, blank=True, default=datetime.now())
    update_at = models.DateTimeField ('Обновлено', null=True, blank=True, default=datetime.now())
    user_id = models.BigIntegerField('ID владельца', null=True, blank=True)
    entry_type = models.CharField('Тип объявления', max_length=255, null=True, blank=True, choices=maps.pets_ads_typs)
    city_id = models.CharField('Город', max_length=255, null=True, blank=True, choices=maps.cities)
    shelter_id = models.CharField('Приют', max_length=255, null=True, blank=True)
    pet_name = models.CharField('Кличка питомца', max_length=255, null=True, blank=True)
    pet_type = models.CharField('Тип животного', max_length=255, null=True, blank=True, choices=maps.pets_type)
    pet_gender = models.CharField('Пол', max_length=255, null=True, blank=True, choices=maps.pets_gender)
    pet_breed = models.CharField('Порода', max_length=255, null=True, blank=True)
    description = models.TextField ('Описание', null=True, blank=True)
    photo_id = models.CharField ('Фото', max_length=255, null=True, blank=True)
    date = models.CharField ('Дата', max_length=255, null=True, blank=True)
    address = models.CharField ('Адрес', max_length=255, null=True, blank=True)
    price = models.CharField ('Стоимость', max_length=255, null=True, blank=True)
    phone = models.CharField('Телефон', max_length=255, null=True, blank=True)
    # url = models.TextField ('Ссылки', null=True, blank=True)
    url = ArrayField (base_field=models.CharField (255), verbose_name='Ссылки', null=True, blank=True)
    status = models.CharField('Статус', max_length=255, null=True, blank=True, choices=maps.pets_ads_status)
    view_count = models.IntegerField('Просмотры', null=True, default=0),
    photo_path = models.ImageField ('Изменить фото', upload_to="photos_pets/", null=True, blank=True)
    location = models.CharField ('Локация', max_length=255, null=True, blank=True)

    def __str__(self):
        return f"<Pet({self.id}, {self.pet_type})>"

    class Meta:
        verbose_name = 'Питомцы'
        verbose_name_plural = 'Питомцы'
        db_table = 'pets'
        managed = False


# животные потерянные и не очень
class Profile(models.Model):
    user_id = models.BigIntegerField("ID пользователя", primary_key=True, unique=True)
    full_name = models.CharField("Имя", max_length=255, null=True, blank=True)
    username = models.CharField("Юзернейм", max_length=255, null=True, blank=True)
    language = models.CharField("Язык", max_length=255, null=True, blank=True, default='ru')
    created_at = models.DateTimeField("Первый визит", null=True, blank=True, default=datetime.now())
    last_activity = models.DateTimeField("Последняя активность", null=True, blank=True, default=datetime.now())
    status = models.CharField("Статус", max_length=255, choices=maps.user_status)

    def __str__(self):
        return f"<Profile({self.user_id}, {self.full_name})>"

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
        db_table = 'profiles'
        managed = False


# вопросы и ответы
class Faq(models.Model):
    id = models.AutoField ('ID', primary_key=True)
    category = models.CharField ('Категория', max_length=255, choices=maps.faq_categories)
    subcategory = models.CharField ('Название кнопки', max_length=255, null=True, blank=True)
    url = models.CharField ('Ссылка', max_length=255)
    is_active = models.BooleanField ('Активно', default=True)

    def __str__(self):
        return f"<Faq({self.id}, {self.category})>"

    class Meta:
        verbose_name = 'Вопросы и ответы'
        verbose_name_plural = 'Вопросы и ответы'
        db_table = 'faq'
        managed = False


# чаты для отправки сообщений о питомцах
class MailingChat(models.Model):
    id = models.AutoField ('ID', primary_key=True)
    chat_title = models.CharField ('Название чата', max_length=255)
    chat_id = models.CharField ('ID чата', max_length=255, null=True, blank=True)
    pet_type = models.CharField ('Вид питомца', max_length=255, choices=maps.pets_type_mailing, default='all')
    city_id = models.CharField ('Город', max_length=255, choices=maps.cities)
    is_active = models.BooleanField ('Активно', default=True)

    def __str__(self):
        return f"<MailingChat({self.chat_id}, {self.chat_title})>"

    class Meta:
        verbose_name = 'Чат для питомцев'
        verbose_name_plural = 'Чаты для питомцев'
        db_table = 'mailing_chats'
        managed = False
