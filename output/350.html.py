import requests
                
def get_all_products():
    api_url = f"https://fakestoreapi.com/products"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_all_products()

import requests
                
def get_product_by_id(id):
    api_url = f"https://fakestoreapi.com/products/1"
    querystring = {'id': id, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_product_by_id(1)

import requests
                
def get_product_categories():
    api_url = f"https://fakestoreapi.com/products/categories"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_product_categories()

import requests
                
def get_products_by_category(category):
    api_url = f"https://fakestoreapi.com/products/category/jewelery"
    querystring = {'category': category, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_products_by_category('jewelery')

import requests
                
def get_cart_by_user_id(userId):
    api_url = f"https://fakestoreapi.com/carts?userId=1"
    querystring = {'userId': userId, }
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_cart_by_user_id(1)

import requests
                
def get_limited_products():
    api_url = f"https://fakestoreapi.com/products?limit=5"
    querystring = {}
    response = requests.get(url=api_url, params=querystring, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
get_limited_products()

import requests
                
def create_product(title, price, description, image, category):
    api_url = f"https://fakestoreapi.com/products"
    payload = {'title': title, 'price': price, 'description': description, 'image': image, 'category': category, }
    response = requests.post(url=api_url, json=payload, timeout=50)
    if response.status_code != 200:
        print("--------------------------------------------")
        print(response.status_code)
        print(response.text)
    # print(response.json())
create_product('New Product', 29.99, 'This is a new product.', 'https://example.com/image.jpg', 'electronics')

