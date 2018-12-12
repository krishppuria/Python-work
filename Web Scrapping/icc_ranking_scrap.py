import pandas as pd
from bs4 import BeautifulSoup
import requests
import unicodedata
icc="https://www.icc-cricket.com/rankings/mens/team-rankings/odi"

icc_response=requests.get(icc).text
soup=BeautifulSoup(icc_response)

print(soup.prettify())

#all_tables=soup.find_all('table')
right_table=soup.find('table',class_='table')
A=[]
B=[]
C=[]
D=[]
E=[]

for row in right_table.findAll("tr"):
    cell=row.findAll("td")
    if len(cell)>0:
        E.append(str(cell[0].find(text=True)))
        A.append(str(cell[1].find(text=True)))
        B.append(str(cell[2].find(text=True)))
        C.append(str(cell[3].find(text=True)))
        D.append(str(cell[4].find(text=True)))
df=pd.DataFrame()
df['Position']=E
df['Team Name']=A
df['Matches']=B
df['Points']=C
df['Rating']=D