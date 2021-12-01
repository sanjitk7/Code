import requests
from bs4 import BeautifulSoup

page = requests.get("https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India")

print(page)

# Create a BeautifulSoup object
soup = BeautifulSoup(page.text, 'html.parser')
print(soup.prettify())


print(soup.title)
print(soup.a)

print(soup.find_all("a"))
all_tables = soup.find_all("table")
right_table = soup.find("table", {"class":"wikitable sortable plainrowheaders"})
# right_table = soup.find("table", class_= "wikitable sortable plainrowheaders")



# print(right_table)

#Generate lists
A=[]
B=[]
C=[]
D=[]
E=[]
F=[]
G=[]
for row in right_table.findAll("tr"):
    cells = row.findAll('td')
    states=row.findAll('th') #To store second column data
    if len(cells)==6: #Only extract table body not heading
        A.append(cells[0].find(text=True))
        B.append(states[0].find(text=True))
        C.append(cells[1].find(text=True))
        D.append(cells[2].find(text=True))
        E.append(cells[3].find(text=True))
        F.append(cells[4].find(text=True))
        G.append(cells[5].find(text=True))
        
import pandas as pd
df=pd.DataFrame(A,columns=['Number'])
df['State/UT']=B
df['Admin_Capital']=C
df['Legislative_Capital']=D
df['Judiciary_Capital']=E
df['Year_Capital']=F
df['Former_Capital']=G


print(df)