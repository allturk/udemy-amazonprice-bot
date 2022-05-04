from decimal import Decimal
import requests
from bs4 import BeautifulSoup as bs
import lxml
import re

M_USER="algoritmatest@gmail.com"
M_SEC=""
headers = {"Accept-Language": "tr,en;q=0.9,en-GB;q=0.8,en-US;q=0.7",
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36 Edg/101.0.1210.32"}
response = requests.get(
    "https://www.amazon.com.tr/Apple-%C3%A7ekirdekli-14-%C3%A7ekirdekli-GPUya-sahip-Apple-M1/dp/B09JR725DK?ref_=Oct_d_omwf_d_12601898031&pd_rd_w=5rB6v&pf_rd_p=b12ee757-72bc-41fe-a493-67b5c042e229&pf_rd_r=N9TZJZSWAVES3MD53V45&pd_rd_r=6bce771b-e5ca-411a-b70f-f29600f1290a&pd_rd_wg=lt0PO&pd_rd_i=B09JR725DK",headers=headers)
# with open("amazon_res.txt","w",encoding="utf-8") as file:
#     file.write(response.text)
# with open("amazon_res.txt", "r", encoding="utf-8") as file:
#     response = file.read()
soup = bs(response.text, "lxml")
# with open("amazon.txt","w",encoding="utf-8") as file:
#     file.write(soup.prettify())
product = soup.title.getText()
price1 = (soup.find(name="div", class_="a-section aok-hidden twister-plus-buying-options-price-data")).text
pricve1 = price1.strip('[]{}')
price = pricve1.replace('"', "")
price = price.replace(":", " :")
print(price)
stri = "\xa0TL"
price = re.split(':|(?<!\.,),(?!\,)(?!64)', price)
print(price)

for item in price:
    if stri in item:
        price[price.index(item)] = item.rstrip(stri)
# print(price)
# price_list = [pri.getText().strip('{"[}"]').spl(":|,") for  pri in price]
# print(price_list)
price_dict = {pri.strip(): price[price.index(pri) + 1] for pri in price if " " in pri}
price_text = price_dict["priceAmount"]
price_float = Decimal(price_text)
print(price_float)

