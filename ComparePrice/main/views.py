from django.shortcuts import render, get_object_or_404,HttpResponseRedirect
from .models import Category, Brand, Store, Product, Price
from django.core.paginator import Paginator
import random
from django.db.models import Min
from .product_utils import sort_products


# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    laptop_list = Product.objects.annotate(lowest_price=Min('price__price')).order_by('?')[:10]
    product_info = []
    for product in laptop_list:
        num_stores = Price.objects.filter(product=product).count()
        lowest_price = Price.objects.filter(product=product).aggregate(Min('price'))['price__min']
        image_url=product.image_url
        product_info.append({
            'product_name': product.name,
            'num_stores': num_stores,
            'lowest_price': lowest_price,
            'image_url':image_url
        })
    context={'laptop_list': laptop_list,
             'product_info': product_info}
    return render(request, 'main/index.html', context)

def product_list(request):
    products_list = Product.objects.all() # Lấy tất cả các sản phẩm từ database
    # Phân trang danh sách sản phẩm
    paginator = Paginator(products_list, 10)
    page_number = request.GET.get('page',1)
    if page_number == None:
        # Nếu page_number không tồn tại, đặt giá trị mặc định là 1
        page_number = 1
    
    page_obj = paginator.get_page(page_number)
    product_info = []
    for product in page_obj:
        num_stores = Price.objects.filter(product=product).count()
        lowest_price = Price.objects.filter(product=product).aggregate(Min('price'))['price__min']
        image_url=product.image_url
        product_info.append({
            'product_name': product.name,
            'num_stores': num_stores,
            'lowest_price': lowest_price,
            'image_url':image_url

            
        })
    context = {'page_obj': page_obj, 'product_info': product_info}
    return render(request, 'main/product_list.html', context)

def product_search(request):
    query = request.GET.get('q')
    
    # Tìm kiếm sản phẩm
    products = Product.objects.filter(name__icontains=query)
    
    # Phân trang danh sách sản phẩm
    paginator = Paginator(products, 10)
    page_number = request.GET.get('page',1)
    if page_number == None:
        # Nếu page_number không tồn tại, đặt giá trị mặc định là 1
        page_number = 1
    
    page_obj = paginator.get_page(page_number)
    product_info = []
    for product in page_obj:
        num_stores = Price.objects.filter(product=product).count()
        lowest_price = Price.objects.filter(product=product).aggregate(Min('price'))['price__min']
        image_url=product.image_url
        product_info.append({
            'product_name': product.name,
            'num_stores': num_stores,
            'lowest_price': lowest_price,
            'image_url':image_url

            
        })
    sort_option = request.GET.get('sort')
    if sort_option == 'low_to_high':
        product_info = sorted(product_info, key=lambda x: x['lowest_price'])
    elif sort_option == 'high_to_low':
        product_info = sorted(product_info, key=lambda x: x['lowest_price'], reverse=True)
    
    context = {'page_obj': page_obj, 'query': query,'product_info': product_info}
    return render(request, 'main/product_search.html', context)
def base(request):
    return render(request, 'main/base.html')
def product_detail(request, product_name):
    product = get_object_or_404(Product, name=product_name)
    prices = product.price_set.all()
    lowest_price = product.price_set.aggregate(lowest_price=Min('price'))['lowest_price']
    return render(request, 'main/product_detail.html', {'product': product, 'prices': prices,'lowest_price': lowest_price})
