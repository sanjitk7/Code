# Importing Libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Content HTTP Request
flipkart_cameras = requests.get("https://www.flipkart.com/search?q=cameras&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")
# print(flipkart_cameras)

# Using Beautiful Soap to parse data
soup = BeautifulSoup(flipkart_cameras.text, 'html.parser')
# print(soup.prettify())
# print(soup.title)
# print(soup.a)


# Getting Number of Cards

cards = soup.find_all("div", class_="_4ddWXP") # same syntax as class_
print('Total Number of Cards Found : ', len(cards))

# Getting the Names, Prices, Discounts and Images of the Products

scrape_list = []

for card in cards:
    scrape_dict = {}
    T = card.find(class_="s1Q9rs").text
    P = card.find(class_="_30jeq3")
    D = card.find("div", class_="_3Ay6Sb")
    I = card.find("img",class_="_396cs4 _3exPp9")
    
    scrape_dict["Title"] = T
    scrape_dict["Price"] = P
    scrape_dict["Discount"] = D
    scrape_dict["Image"] = I
    
    scrape_list.append(scrape_dict)

print(scrape_list)

df = pd.DataFrame.from_dict(scrape_list)
df.to_csv('/Users/sanjitkumar/Documents/VIT_DOC/vit_semester_7/C2 - Web Mining/Lab/Lab2/FlipKartCameras.csv', index=False)

print(df)