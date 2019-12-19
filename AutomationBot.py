import pandas as pd
import requests
from bs4 import BeautifulSoup
from tkinter import Tk, Label, Button, Entry, IntVar, END, W, E, Text, messagebox

df = pd.read_excel('/Users/anirudhseela/Downloads/ A Vocabulary Quiz Unit #3.A (Responses).xlsx')

new = df['First Name Last Name']
names = []
firstName = []
lastName = []

for i in range(new.size):
    names.append(new[i])

for n in names:
    temp = n.split(" ")
    firstName.append(temp[0])
    lastName.append(temp[1])

for b in range(len(firstName)):
    names[b] = (lastName[b] + ", " + firstName[b])

firstName[0] = 'Anirudh'
lastName[0] = 'Seela'
URL = 'http://www.uschess.org/datapage/player-search.php?name=' + firstName[0] + "+" + lastName[0] + '&state=ANY&ratingmin=&ratingmax=&order=N&rating=R&mode=Find'


data = {'Player Name or ID': 'name'}
r = requests.get(URL)

rating = []
ratings = []
soup = BeautifulSoup(r.content, 'html.parser')
for form in soup.find_all("td"):
    rating.append(form)

str1 = ''.join(rating[15])
ratings.append(str1.strip())
print(str1.strip())
