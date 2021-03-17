import os
import requests
from bs4 import BeautifulSoup
import smtplib
import time

#USERS SHOULD FILL THIS PART UP!
emailAddress = os.environ.get('emailAddress')
emailAddressRecipient = os.environ.get('emailAddress')
gmailAppPassword = os.environ.get('gmailAppPassword')
#Add or remove watch objects, there is no limit.
watches = [
    {'watchName': 'Omega Seamaster 2531.80', 'minPrice' : 900, 'maxPrice': 2500,  'recentListingsLimit': 13},
    {'watchName': 'Tudor Black Bay 58', 'minPrice' : 900, 'maxPrice': 2000,  'recentListingsLimit': 13},
    {'watchName': 'Omega Speedmaster', 'minPrice' : 1000, 'maxPrice': 3000,  'recentListingsLimit': 13},
    ] 
frequencyOfChecks = 1 #In days, so this checks every 24 hours.

#Don't need to use an API for this, no point honestly, I don't need exact prices and watch prices fluctuate much more than forex
#honestly
USD_TO_SGD = 1.35
EUR_TO_SGD = 1.60
GBP_TO_SGD = 1.87

def scrapeWatchCharts(watchName, minPrice, maxPrice, recentListingsLimit):
    #We want unsold watches from watchcharts
    URL = "https://watchcharts.com/listings?q={}&page=1&status=unsold".format('%20'.join(watchName.split(' ')))

    #Put your user agent here obviously.
    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'}

    #Extracting prices
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    elements = soup.find_all("h4",{"class" : "m-0"})
    #Putting them in an array
    prices = []
    for element in elements:
        prices.append(element.get_text().strip())

    count = 0
    for price in prices:
        if price[0] == '$':
            convertedPrice = int(price[1:].replace(',', '')) * USD_TO_SGD
        elif price[0] == '€':
            convertedPrice = int(price[1:].replace(',', '')) * EUR_TO_SGD
        elif price[0] == '£':
            convertedPrice = int(price[1:].replace(',', '')) * GBP_TO_SGD

        #rounding one more time after forex conversion
        convertedPrice = round(convertedPrice)

        #If smaller than desired price
        if(convertedPrice < maxPrice and convertedPrice > minPrice):
            send_mail(watchName, maxPrice, URL)
            break #break at the end of it, if one of the watches fits the criteria, we send a notification alerting the user
            #to check out the search page themselves. There the user can find the cheapest watch, if there is a cheaper one
            #than the one we alerted on.

        #Exit after we go through the limit of most recent listings we want.
        count += 1
        if (count >= recentListingsLimit):
            break

def send_mail(watchName, maxPrice, URL):
    global emailAddress, emailAddressRecipient, gmailAppPassword

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(emailAddress, gmailAppPassword)

    subject = 'The price of {} has fallen below {}'.format(watchName, maxPrice)
    body = "There has been a listing below your ideal price, so check out the URL: {}".format(URL)
    msg = f"Subject:{subject}\n\n{body}"

    server.sendmail(
        emailAddress,
        emailAddressRecipient,
        msg
    )
    print("EMAIL HAS BEEN SENT!")

    server.quit()

def searchForWatches():
    for watch in watches:
        scrapeWatchCharts(watch['watchName'],watch['minPrice'],watch['maxPrice'],watch['recentListingsLimit'])

#Added failsafe in case frequency of checks is 0, in which case it will be an infinite loop with 0 breaks.
if frequencyOfChecks != 0:
    while(True):
        searchForWatches()
        #Added this so that there is, at minimum a 1 minute break between each run. Just as another failsafe
        #in case the user accidentally uses too small a number for frequencyOfChecks
        time.sleep(60*60)
        #Checks once a frequencyOfChecks days
        time.sleep(60*60*24*frequencyOfChecks)
else:
    searchForWatches()
