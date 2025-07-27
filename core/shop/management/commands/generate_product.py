import random
from django.core.management.base import BaseCommand
from django.utils.text import slugify
from faker import Faker
from pathlib import Path
from django.core.files import File
from ...models import ProductModels, ProductCategoryModels, ProductStatusModels
from accounts.models import User, UserType

# مسیر اصلی فایل‌ها
BASE_DIR = Path(__file__).resolve().parent


class Command(BaseCommand):
    help = "Generate fake products"

    def handle(self, *args, **options):
        fake = Faker("fa_IR")

        try:
            user = User.objects.get(type=UserType.admin.value)
        except User.DoesNotExist:
            self.stdout.write(self.style.ERROR("Admin user does not exist"))
            return

        # لیست تصاویر موجود
        image_list = [
            "./images/img1.png",
            "./images/img2.png",
            "./images/img3.png",
            "./images/img4.png",
            "./images/img5.png",
            "./images/img6.png",
            "./images/img7.png",
            "./images/img8.png",
            "./images/img9.png",
            "./images/img10.png",
            "./images/img11.png",
            "./images/img12.png",
            "./images/img13.png",
        ]

        # آماده‌سازی تصاویر برای تخصیص غیرتکراری
        shuffled_images = image_list.copy()
        random.shuffle(shuffled_images)

        categories = ProductCategoryModels.objects.all()
        num_products = 13  # به تعداد تصاویر

        for i in range(num_products):
            selected_image = shuffled_images[i % len(shuffled_images)]
            title = " ".join([fake.word() for _ in range(2)])
            slug = slugify(title, allow_unicode=True)
            description = fake.paragraph(nb_sentences=10)
            brief_description = fake.paragraph(nb_sentences=1)
            stock = fake.random_int(min=0, max=10)
            status = random.choice(ProductStatusModels.choices)[0]
            price = fake.random_int(min=10000, max=100000)
            discount_percent = fake.random_int(min=0, max=50)

            num_categories = random.randint(1, min(4, len(categories)))
            selected_categories = random.sample(list(categories), num_categories)

            with open(BASE_DIR / selected_image, "rb") as image_file:
                image_obj = File(image_file, name=Path(selected_image).name)

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
                product.category.set(selected_categories)

        self.stdout.write(
            self.style.SUCCESS(f"Successfully generated {num_products} fake products")
        )
