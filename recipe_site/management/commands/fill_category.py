from django.core.management.base import BaseCommand

from recipe_site.models import Category


class Command(BaseCommand):
    help = "Fill Category"

    def handle(self, *args, **kwargs):
        cat1 = Category(title='Салаты')
        cat1.save()
        cat2 = Category(title='Супы')
        cat2.save()
        cat3 = Category(title='Блюда из мяса')
        cat3.save()
        cat4 = Category(title='Блюда из рыбы')
        cat4.save()
        cat5 = Category(title='Блюда из птицы')
        cat5.save()
        cat6 = Category(title='Гарниры')
        cat6.save()
        cat7 = Category(title='Выпечка')
        cat7.save()
        return self.stdout.write('ok')