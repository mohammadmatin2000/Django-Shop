import random
from django.core.management.base import BaseCommand
from django.utils.text import slugify
from faker import Faker
from ...models import ProductModels, ProductCategoryModels, ProductStatusModels
from accounts.models import User, UserType
from pathlib import Path
from django.core.files import File

# ======================================================================================================================
BASE_DIR = Path(__file__).resolve().parent

class Command(BaseCommand):
    help = 'Generate fake products'

    def handle(self, *args, **options):
        fake = Faker(locale="fa_IR")

        try:
            user = User.objects.get(type=UserType.admin.value)
        except User.DoesNotExist:
            self.stdout.write(self.style.ERROR('Admin user does not exist'))
            return

        # لیست تصاویر
        image_list = [
            "./images/img1.jpg",
            "./images/img2.jpg",
            "./images/img3.jpg",
            "./images/img4.jpg",
            "./images/img5.jpg",
            "./images/img6.jpg",
            "./images/img7.jpg",
            "./images/img8.jpg",
        ]

        categories = ProductCategoryModels.objects.all()

        for _ in range(10):  # Generate 10 fake products
            num_categories = random.randint(1, 4)
            num_categories = min(num_categories, len(categories))  # محدود کردن تعداد انتخاب به تعداد موجود دسته‌بندی‌ها
            # انتخاب دسته‌بندی‌های رندوم
            selected_categories = random.sample(list(categories), num_categories)

            title = ' '.join([fake.word() for _ in range(1, 3)])
            slug = slugify(title, allow_unicode=True)
            selected_image = random.choice(image_list)

            # استفاده از open در حالت امن
            with open(BASE_DIR / selected_image, "rb") as image_file:
                image_obj = File(image_file, name=Path(selected_image).name)

                description = fake.paragraph(nb_sentences=10)
                brief_description = fake.paragraph(nb_sentences=1)
                stock = fake.random_int(min=0, max=10)
                status = random.choice(ProductStatusModels.choices)[0]  # استفاده از ProductStatusModels به جای ProductStatusType
                price = fake.random_int(min=10000, max=100000)
                discount_percent = fake.random_int(min=0, max=50)

                product = ProductModels.objects.create(
                    user=user,
                    title=title,
                    slug=slug,
                    image=image_obj,
                    description=description,
                    brief_description=brief_description,
                    stock=stock,
                    status=status,
                    price=price,
                    discount_percent=discount_percent,
                )

                # اضافه کردن دسته‌بندی‌های انتخاب شده به محصول
                product.category.set(selected_categories)

        self.stdout.write(self.style.SUCCESS('Successfully generated 10 fake products'))
