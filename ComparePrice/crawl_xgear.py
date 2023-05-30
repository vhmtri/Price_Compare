from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import pandas as pd

s=Service('C:/Users/acer/Downloads/chromedriver_win32/chromedriver.exe')
driver = webdriver.Chrome(service=s) 
link_laptops =[]
for i in range(1,17):
    url="https://xgear.net/product-category/laptop/page/"+str(i)+"/"
    driver.get(url)
    link_laptop=driver.find_elements(By.XPATH,"//a[@class='woocommerce-LoopProduct-link woocommerce-loop-product__link']")
    for link in link_laptop:
        link = link.get_attribute("href")
        link_laptops.append(link)
print(len(link_laptops))
name_caterorys=[]
name_stores=[]
name_products=[]
name_brands=[]
image_urls=[]
descriptions=[]
prices=[]
product_urls=[]
for i in link_laptops:
    driver.get(i)
    driver.execute_script("document.querySelectorAll('del').forEach(el => el.remove());");
    name_caterory=driver.find_element(By.XPATH,"/html/body/div[3]/div[1]/div/div[1]/div[1]/div/div/nav/p/a[1]")
    name_store='Xgear'
    name_product=driver.find_element(By.XPATH,"/html/body/div[3]/div[1]/div/div[1]/div[2]/div/h1")
    name_brand=driver.find_element(By.XPATH,"/html/body/div[3]/div[1]/div/div[2]/div[1]/div/div[2]/div/span[1]/span/a")
    image_url=driver.find_element(By.XPATH,"/html/body/div[3]/div[2]/div/div[1]/div/div/div/div/figure/div[1]/a")
    description=driver.find_element(By.XPATH,"//div[@class='elementor-element elementor-element-dd2a586 elementor-widget elementor-widget-woocommerce-product-content']//div//p[not(descendant::img)]")
    price=driver.find_element(By.XPATH,"//p[@class='price']//span[@class='woocommerce-Price-amount amount']//bdi")
    product_url=i
    print('Name Category:',name_caterory.text)
    print('Name Store:',name_store)
    print('Name Product:',name_product.text)
    print('Name Brand:',name_brand.text)
    print('Image URL:',image_url.get_attribute("href"))
    print('Description:',description.text)
    print('Price:',price.text)
    print('Product URL:',product_url)
    name_caterorys.append(name_caterory.text)
    name_stores.append(name_store)
    name_products.append(name_product.text)
    name_brands.append(name_brand.text)
    image_urls.append(image_url.get_attribute("href"))
    descriptions.append(description.text)
    prices.append(price.text)
    product_urls.append(product_url)
    print('--------------------------------------')

driver.close()
data={"Name Category":name_caterorys,"Name Store":name_stores,"Name Product":name_products,"Name Brand":name_brands,"Image URL":image_urls,"Description":descriptions,"Price":prices,"Product URL":product_urls}
df=pd.DataFrame(data)
print(df)
df.to_csv('New_laptopXgear.csv.csv',index=False)