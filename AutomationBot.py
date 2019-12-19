import pandas as pd
import requests
from bs4 import BeautifulSoup
from tkinter import Tk, Label, Button, Entry, IntVar, END, W, E, Text, messagebox

df = pd.read_excel('/Users/anirudhseela/Downloads/ProgramTest.xlsx')

dfFirst = df['First Name']
dfLast = df['Last Name']
dfState = df['State']
dfMin = df['Min']
dfMax = df['Max']

firstName = []
lastName = []
state = []
minRating = []
maxRating = []

ratings = []


for i in range(dfFirst.size):
    firstName.append(dfFirst[i])

for i in range(dfLast.size):
    lastName.append(dfLast[i])

for i in range(dfState.size):
    state.append(dfState[i])

for i in range(dfMin.size):
    minRating.append(dfMin[i])

for i in range(dfMax.size):
    maxRating.append(dfMax[i])

print(len(firstName))

for i in range(len(firstName)):
    URL = 'http://www.uschess.org/datapage/player-search.php?name=' + firstName[i] + "+" + lastName[i] + '&state=' + \
          state[0] + '&ratingmin=' + str(minRating[i]) + ' &ratingmax=' + str(maxRating[i]) + \
          '&order=N&rating=R&mode=Find'

    data = {'Player Name or ID': 'name'}
    r = requests.get(URL)

    rating = []
    soup = BeautifulSoup(r.content, 'html.parser')
    for form in soup.find_all("td"):
        rating.append(form)

    str1 = ''.join(rating[15])
    ratings.append(str1.strip())

for r in range(len(ratings)):
    df['Ratings'][r] = ratings[r]

df.head(5)
df.to_excel('/Users/anirudhseela/Downloads/ProgramTest.xlsx')
print("done")
