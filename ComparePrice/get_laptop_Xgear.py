import csv
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ComparePrice.settings") # Tên app bạn tạo ( QUAN TRỌNG ).
django.setup()
from main.models import Category, Brand, Store, Product, Price
from decimal import Decimal
from datetime import date

with open('E:/PTUD/Project/ComparePrice/data_csv/New_laptopXgear.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    next(reader)
    for row in reader:
        category_name = row['Name Category']
        brand_name = row['Name Brand']
        store_name = row['Name Store']
        product_name = row['Name Product']
        product_url = row['Product URL']
        price_str = row['Price']
        image_url = row['Image URL']
        description = row['Description']
        #xử lí price
        price_str = price_str.replace(',', '.').strip()

        price = price_str
        
        print('tên category:',category_name)
        print('tên brand:',brand_name)
        print('tên store:',store_name)
        print('tên product:',product_name)
        print('tên product_url:',product_url)
        print('tên price:',price)
        print('tên image_url:',image_url)
        print('tên description:',description)
        print('-----------------------------')

        # Kiểm tra xem Category, Brand, Store đã tồn tại trong database chưa
        # Nếu chưa thì tạo mới
        category, _ = Category.objects.get_or_create(name=category_name)
        brand, _ = Brand.objects.get_or_create(name=brand_name)
        store, _ = Store.objects.get_or_create(name=store_name)

        # Tạo một đối tượng Product và lưu vào database
        product=Product.objects.create(
            name=product_name,
            category=category,
            brand=brand,
            image_url=image_url,
            description=description
        )
        # Tạo một đối tượng Price và lưu vào database
        Price.objects.create(
            product=product,
            store=store,
            price=price,
            date=date.today(),
            product_url=product_url
        )