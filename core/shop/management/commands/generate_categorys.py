from django.core.management.base import BaseCommand
from ...models import ProductCategoryModels
from faker import Faker
from django.utils.text import slugify
# ======================================================================================================================
class Command(BaseCommand):
    help = 'Generate fake product categories'

    def handle(self, *args, **kwargs):
        fake = Faker(locale='fa')
        num_categories = 10

        for _ in range(num_categories):
            title = fake.word().capitalize()
            slug = slugify(title)

            # چک کردن اینکه آیا slug تکراری است
            original_slug = slug
            counter = 1
            while ProductCategoryModels.objects.filter(slug=slug).exists():
                slug = f"{original_slug}-{counter}"
                counter += 1

            # ایجاد دسته‌بندی
            ProductCategoryModels.objects.create(title=title, slug=slug)

        self.stdout.write(self.style.SUCCESS(f'{num_categories} categories generated successfully'))
# ======================================================================================================================