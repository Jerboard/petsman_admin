

# города
cities = (
    ("tashkent", "Ташкент"),
    ("samarkand", "Самарканд"),
    ("almaty", "Алматы"),
    ("astana", "Астана"),
    ("bishkek", "Бишкек"),
    ("karaganda", "Караганда"),
    ("shymkent", "Шымкент"),
    ("pavlodar", "Павлодар"),
    ("ust_kamenogorsk", "Усть-Камнегорск")
)

cities_dict = dict(cities)

# места
objects = (
    ("global_pets_transportation", "✈️ Международные перевозки животны"),
    ("aquarium_services", "🐠 Обслуживание аквариумов 🐟"),
    ("cafes_and_restaurants", "🍰 Кафе и рестораны"),
    ("parks_and_recreation_areas", "🏞 Парки и зоны отдыха"),
    ("shelters_and_volunteers", "🐾 Приюты и волонтёры 🤲"),
    ("pet_shop", "🐶 Зоомагазины 🐱"), 
    ("vet_clinics", "🏥 Ветклиники"), 
    ("vet_pharmacies", "💊 Ветаптеки"),
    ("pet_groomer", "🐩 Грумеры✂"), 
    ("cynologists", "🐕 Кинологи🦮"), 
    ("hotels_for_pets", "🏡 Передержка🐾"), 
    ("pet_taxi", "🚖 Пет-такси"), 
    ("pet_friendly_stores", "🛍 Магазины"),
    ("hotels", "🏨Отели"),
    ("dog_walking_areas", "🦮 Площадки для выгула"),
    ("events", "🎊 События 🎉"),
    ("community", "🌍 Сообщества 👥"),
)


# типы объявлений питомцев
pets_ads_typs = (
    ('found', "Найденные животные"),
    ('lost', "Потерянные животные"),
    ('person', "Взять в добрые руки"),
    ('shelter', "Взять животное из приюта"),
    ('take_pet_home', "Взять животное из семьи"),
    ('get_pet_sitting', "Отдать на передержку"),
    ('take_pet_sitting', "Взять на передержку"),
    ('my_pet', "Мой питомец"),
)

pets_ads_typs_dict = dict(pets_ads_typs)


# типы питомцев
pets_type = (
    ('cat', 'Кошка'),
    ('dog', 'Собака'),
    ('other', 'Другое'),
)

pets_type_dict = dict(pets_type)

# типы питомцев
pets_type_mailing = (
    ('all', 'Все'),
    ('cat', 'Кошки'),
    ('dog', 'Собаки'),
    ('other', 'Другие питомцы'),
)


# пол питомца
pets_gender = (
    ('male', 'Мальчик'),
    ('female', 'Девочка'),
    ('other', 'Другое'),
)

pets_gender_dict = dict(pets_gender)


# статус обявлений питомцев
pets_ads_status = (
    ('moderation', 'На модерации'),
    ('published', 'Опубликовано'),
    ('closed', 'Снято с публикации'),
)


# категории faq
faq_categories = (
    ('❓ Вопросы и ответы 🤔', '❓ Вопросы и ответы 🤔'),
    ('📝 Полезные советы 🧐', '📝 Полезные советы 🧐'),
    ('🚓 Остерегайтесь мошенников 🤨', '🚓 Остерегайтесь мошенников 🤨'),
    ('🌍 Сообщество Petsman 🐾', '🌍 Сообщество Petsman 🐾'),
)

# статус пользователя
user_status = (
    ('user', 'Пользователь'),
    ('admin', 'Администратор'),
    ('volunteer', 'Волонтёр'),
    ('partner', 'Партнёр'),
    ('ban', 'Бан'),
)
