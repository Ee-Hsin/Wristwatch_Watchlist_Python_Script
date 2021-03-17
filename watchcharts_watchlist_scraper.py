import requests
from bs4 import BeautifulSoup

#TODO: Add Query to URL with the desired watch as a variable, add the minimum and maximum price criteria

#Don't need to use API for this, no point, I don't need exact prices and watch prices fluctuate much more than forex
#honestly
USD_TO_SGD = 1.35
EUR_TO_SGD = 1.60
GBP_TO_SGD = 1.87

URL = "https://watchcharts.com/listings/watch/125?page=1"

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

elements = soup.find_all("h4",{"class" : "m-0"})

prices = []

for element in elements:
    prices.append(element.get_text().strip())

for price in prices:
    if price[0] == '$':
        convertedPrice = int(price[1:].replace(',', '')) * USD_TO_SGD
    elif price[0] == '€':
        convertedPrice = int(price[1:].replace(',', '')) * EUR_TO_SGD
    elif price[0] == '£':
        convertedPrice = int(price[1:].replace(',', '')) * GBP_TO_SGD

    convertedPrice = round(convertedPrice)

    #If smaller than desired price
    #if():
        #send email




