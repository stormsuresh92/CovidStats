import requests
from bs4 import BeautifulSoup
import pandas as pd


url = 'https://www.worldometers.info/coronavirus/countries-where-coronavirus-has-spread/'
head = {'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36'}
all = []
r = requests.get(url, headers=head)
s = BeautifulSoup(r.text, 'html.parser')
data = iter(s.find_all('td'))
while True:
  try:
    country = next(data).text
    Cases = next(data).text
    Deathes = next(data).text
    Continent = next(data).text
    all.append([country, int(Cases.replace(',','')), int(Deathes.replace(',', '')), Continent])
    all.sort(key = lambda row: row[1], reverse = True)
    df = pd.DataFrame(all)
    df.to_csv('covidstats.csv', index=False)
  except:
    break  
print('fin')


