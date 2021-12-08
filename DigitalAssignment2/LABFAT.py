# Importing Libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd


url = "https://www.oyorooms.com/search?location=East%20Coast%20Road%2C%20Chennai%2C%20Tamil%20Nadu&latitude=12.9877504&longitude=80.25573020000002&searchType=locality&checkin=08%2F12%2F2021&checkout=09%2F12%2F2021&roomConfig%5B%5D=2&country=india&guests=2&rooms=1" 
headers = { 'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36" } 
response = requests.request("GET", url, headers=headers) 
data = BeautifulSoup(response.text, 'html.parser') 

room_data = data.find_all('div', attrs={'class': 'hotelCardListing__descriptionWrapper'})

print(len(room_data))


scrape_list = []

for room in room_data:
    scrape_dict = {}
    hotel_name = room.find(class_="listingHotelDescription__hotelName d-textEllipsis").text
    hotel_rating = room.find(class_="hotelRating__rating").text
    hotel_rent = room.find(class_="listingPrice__finalPrice").text
    hotel_offer = room.find(class_="listingPrice__percentage").text
    # I = room.find("img",class_="_396cs4 _3exPp9")
    
    scrape_dict["hotel_name"] = hotel_name
    scrape_dict["hotel_rating"] = hotel_rating
    scrape_dict["hotel_rent"] = hotel_rent
    scrape_dict["hotel_offer"] = hotel_offer
    
    scrape_list.append(scrape_dict)

print(scrape_list)

df = pd.DataFrame.from_dict(scrape_list)
df.to_csv('.\Oyo.csv', index=False)

print(df)