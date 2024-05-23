from bot_admin.models import Pets


# помечает объекты на переотправку
def mark_pet_remailing(ads: list):
    ids = [ad.id for ad in ads]
    Pets.objects.filter(id__in=ids).update(remailing=True)
