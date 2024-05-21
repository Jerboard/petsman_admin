from django.contrib import admin
from .models import Profile, Place, Pets, Faq, MailingChat
from bot_admin import maps
from django.utils.html import format_html, mark_safe

from bot_admin.bot_user import send_telegram_message_sync


@admin.register(Profile)
class ViewAdminProfile(admin.ModelAdmin):
    list_display = ['user_id', 'full_name', 'username', 'language', 'created_at', 'last_activity', 'status']
    search_fields = ['user_id', 'user_id', 'username']
    list_filter = ['status']
    ordering = ['-last_activity']


# Владелец/Город/Имя объекта/Адрес/Создано/Статус объекта(Опубликовано)
@admin.register (Place)
class ViewAdminPlace (admin.ModelAdmin):
    list_display = ['user_full_name', 'city_str', 'name_ru', 'address', 'created_at', 'is_published', 'cover_image_preview']
    search_fields = ['user_id', 'tags']
    list_filter = ['city_id', 'category_id']
    readonly_fields = ['cover_image_preview_in']

    def cover_image_preview(self, obj):
        if obj.photo_path:
            return mark_safe(f'<img src="{obj.photo_path.url}" style="max-width:100px; max-height:100px;">')
        else:
            return "No image"

    def cover_image_preview_in(self, obj):
        if obj.photo_path:
            return mark_safe(f'<img src="{obj.photo_path.url}" style="max-width:300px; max-height:300px;">')
        else:
            return "No image"

    def user_full_name(self, obj):
        user = Profile.objects.filter(user_id=obj.user_id).first()
        if user:
            return user.full_name
        else:
            return 'admin'

    def city_str(self, obj):
        return maps.cities_dict.get(obj.city_id)

    user_full_name.short_description = 'Владелец'
    city_str.short_description = 'Город'
    cover_image_preview.short_description = 'Фото'
    cover_image_preview_in.short_description = 'Фото'


#  Пользователь/Город/Тип объявления/Описание/Создано/Статус объекта(Опубликовано)/
@admin.register (Pets)
class ViewAdminSearchPets (admin.ModelAdmin):
    # list_display = ['user_full_name', 'city_str', 'entry_type', 'description_short', 'created_at', 'status',
    #                 'cover_image_preview']
    list_display = ['user_full_name', 'city_str', 'entry_type', 'description_short', 'created_at', 'status']
    search_fields = ['user_id']
    list_filter = ['pet_type', 'city_id', 'entry_type', 'status']
    # readonly_fields = ['cover_image_preview_in']
    actions = ['repeat_mailing']  # Добавляем кастомное действие
    exclude = ['photo_id', 'location']

    # def cover_image_preview(self, obj):
    #     if obj.photo_path:
    #         return mark_safe(f'<img src="{obj.photo_path.url}" style="max-width:100px; max-height:100px;">')
    #     else:
    #         return "No image"
    #
    # def cover_image_preview_in(self, obj):
    #     if obj.photo_path:
    #         return mark_safe(f'<img src="{obj.photo_path.url}" style="max-width:300px; max-height:300px;">')
    #     else:
    #         return "No image"

    def user_full_name(self, obj):
        user = Profile.objects.filter(user_id=obj.user_id).first()
        if user:
            return user.full_name
        else:
            return str(obj.user_id)

    def city_str(self, obj):
        return maps.cities_dict.get(obj.city_id)

    def entry_type_str(self, obj):
        return maps.pets_ads_typs_dict.get(obj.entry_type)

    def description_short(self, obj):
        if obj.description:
            return obj.description[:50]
        else:
            return '-'

    def repeat_mailing(self, request, queryset):
        # print('\n\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        # print(type(queryset), len(queryset))
        #
        # for i in queryset:
        #     print(i)
        send_telegram_message_sync(queryset)
        # for chat in queryset:
        #     re_mailing_ad(chat)  # Вызываем функцию повторной отправки
        self.message_user(request, "Повторная отправка выполнена успешно")

    repeat_mailing.short_description = "Повторная отправка"
    user_full_name.short_description = 'Пользователь'
    city_str.short_description = 'Город'
    entry_type_str.short_description = 'Тип объявления'
    description_short.short_description = 'Описание'
    # cover_image_preview.short_description = 'Фото'
    # cover_image_preview_in.short_description = 'Фото'


@admin.register (Faq)
class ViewAdminFaq (admin.ModelAdmin):
    list_display = ['category', 'subcategory', 'url', 'is_active']
    search_fields = ['category']
    ordering = ['id']


@admin.register(MailingChat)
class ViewAdminMailingChat(admin.ModelAdmin):
    list_display = ['chat_id', 'chat_title', 'city_str', 'pet_type', 'is_active']
    search_fields = ['chat_id', 'chat_title']
    list_filter = ['city_id', 'pet_type', 'is_active']

    def city_str(self, obj):
        return maps.cities_dict.get(obj.city_id)
    city_str.short_description = 'Город'
