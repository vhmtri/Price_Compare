
# Create your models here.
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('category_detail', args=[str(self.id)])

class Brand(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('brand_detail', args=[str(self.id)])

class Store(models.Model):
    name = models.CharField(max_length=255, unique=True)
    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('store_detail', args=[str(self.id)])

class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    image_url = models.URLField(max_length=500,blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('product_detail', args=[str(self.id)])

    # def get_latest_price(self):
    #     latest_price = self.price_set.order_by('-date').first()
    #     return latest_price.price if latest_price else None

class Price(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    price = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    product_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.product.name} - {self.store.name} - {self.price}"

    # class Meta:
    #     ordering = ['-date']