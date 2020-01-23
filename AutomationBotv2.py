import traceback
import pandas as pd
import requests
from bs4 import BeautifulSoup
from tkinter import Tk, Label, Button, Entry, IntVar, END, W, E, Text, messagebox

# /Users/anirudhseela/Downloads/ProgramTest.xlsx

excelSheet = []
sections = []
minRating = []
maxRating = []
toNext = [True]


class ExcelSheet:

    def __init__(self, master):
        self.master = master
        master.title("Chess Tourney Management System")

        self.title = Label(master, text="Chess Tourney Management System")
        self.dir = Label(master, text="Enter the path of the Excel Sheet.")

        self.excelName = Label(master, text="Excel Sheet Name:")

        self.excelName_text = Entry(master)
        self.excelName_text.focus_set()

        self.next_button = Button(master, text="Next", command=lambda: self.Enter())
        self.exit_button = Button(master, text="Exit", command=lambda: self.Exit())

        self.title.grid(row=0, column=0, sticky=W)
        self.dir.grid(row=1, column=0, sticky=W)

        self.excelName.grid(row=2, column=0, sticky=W)
        self.excelName_text.grid(row=2, column=1, sticky=W)

        self.next_button.grid(row=4, column=0)
        self.exit_button.grid(row=4, column=1, sticky=W)

    def Enter(self):
        if (len(excelSheet)) > 0:
            excelSheet[0] = str(self.excelName_text.get())
        else:
            excelSheet.append(str(self.excelName_text.get()))

        bool = messagebox.askyesno('Excel Sheet', "Your excel sheet is \'" + excelSheet[0] +
                                   "\'. If this is incorrect reenter your excel sheet. If it is not correct click no and "
                                   "reenter the information.")
        if not bool:
            excelSheet.clear()
            self.excelName_text.delete(0, len(str(self.excelName_text)))
            self.excelName_text.focus_set()

        else:
            root.destroy()

    def Exit(self):
        root.destroy()
        toNext[0] = False


if toNext[0]:
    root = Tk()
    my_gui = ExcelSheet(root)
    root.mainloop()


# ----------------------------------------------------------------------------------------------------------------------

class Sections:

    def __init__(self, master):
        self.master = master
        master.title("Chess Tourney Management System")

        self.title = Label(master, text="Chess Tourney Management System")
        self.dir = Label(master, text="Enter the path of the Excel Sheet.")

        self.sectionName = Label(master, text="Section Name:")
        self.min = Label(master, text="Min Rating: ")
        self.max = Label(master, text="Max Rating: ")

        self.sectionName_text = Entry(master)
        self.min_text = Entry(master)
        self.max_text = Entry(master)
        self.sectionName_text.focus_set()

        self.add_button = Button(master, text="Add", command=lambda: self.Add())
        self.next_button = Button(master, text="NEXT", command=lambda: self.Next())
        self.exit_button = Button(master, text="Exit", command=master.quit)

        self.title.grid(row=0, column=0, sticky=W)
        self.dir.grid(row=1, column=0, sticky=W)

        self.sectionName.grid(row=2, column=0, sticky=W)
        self.sectionName_text.grid(row=2, column=1, sticky=W)

        self.min.grid(row=3, column=0, sticky=W)
        self.min_text.grid(row=3, column=1, sticky=W)

        self.max.grid(row=4, column=0, sticky=W)
        self.max_text.grid(row=4, column=1, sticky=W)

        self.add_button.grid(row=5, column=0)
        self.next_button.grid(row=5, column=1, sticky=W)
        self.exit_button.grid(row=5, column=2, sticky=W)

    def Add(self):

        minRating.append(self.min_text.get())
        maxRating.append(self.max_text.get())

        sections.append(self.sectionName_text.get())

        self.min_text.delete(0, len(str(self.min_text)))
        self.max_text.delete(0, len(str(self.max_text)))
        self.sectionName_text.delete(0, len(str(self.sectionName_text)))

        self.sectionName_text.focus_set()

    def Next(self):
        sectionsStr = "Please verify that the sections info is correct \n"
        if len(sections) < 1:
            sectionsStr += "Section: None Min Rating: None Max Rating: None"
        else:
            for i in range(0, len(sections)):
                sectionsStr += "Section " + sections[i] + " Min Rating: " + minRating[i] + " Max Rating: " + maxRating[
                    i] \
                               + "\n"

        sectionsStr += "If not click no and reenter the information."
        bool = messagebox.askyesno('Excel Sheet', sectionsStr)
        if not bool:
            minRating.clear()
            maxRating.clear()
            sections.clear()
            self.sectionName_text.focus_set()
        else:
            root.destroy()


if toNext[0]:
    root = Tk()
    my_gui = Sections(root)
    root.mainloop()
# ----------------------------------------------------------------------------------------------------------------------
try:
    df = pd.read_excel(str(excelSheet[0]))
    dfFirst = df['First Name']
    dfLast = df['Last Name']
    dfState = df['State']
    dfSection = df['Section']
    dfPlayUp = df['Play Up']

    firstName = []
    lastName = []
    state = []
    playUp = []
    ratings = []

    for i in range(dfFirst.size):
        firstName.append(dfFirst[i])

    for i in range(dfLast.size):
        lastName.append(dfLast[i])

    for i in range(dfState.size):
        state.append(dfState[i])
    for i in range(dfPlayUp.size):
        playUp.append(dfPlayUp[i])

    for i in range(len(firstName)):
        try:
            a = sections.index(str(dfSection[i]))

            print(str(playUp[i]) == "Yes")

            if (str(playUp[i]) == "Yes"):
                #     sortMin = []
                #     sortMax = []
                searchMin = str(minRating[a])
                searchMax = str(maxRating[a])
                #
                #     for m in minRating:
                #         if m != "":
                #             sortMin.append(int(m))
                #
                #     for m in maxRating:
                #         if m != "":
                #             sortMax.append(int(m))

                sortMin = []
                sortMax = []

                for m in minRating:
                    sortMin.append(m)

                for m in maxRating:
                    sortMax.append(m)

                sortMin.sort()
                sortMax.sort()

                b = sortMin.index(str(minRating[a])) - 1
                print(b)

                if minRating[i] != "":
                    searchMin = str(sortMin[b])

                if maxRating[i] != "":
                    searchMax = str(sortMax[b])

                URL = 'http://www.uschess.org/datapage/player-search.php?name=' + firstName[i] + "+" + lastName[
                    i] + '&state=' + \
                      state[i] + '&ratingmin=' + searchMin + ' &ratingmax=' + searchMax + \
                      '&order=N&rating=R&mode=Find'
            else:
                URL = 'http://www.uschess.org/datapage/player-search.php?name=' + firstName[i] + "+" + lastName[
                    i] + '&state=' + \
                      state[i] + '&ratingmin=' + str(minRating[a]) + ' &ratingmax=' + str(maxRating[a]) + \
                      '&order=N&rating=R&mode=Find'

            data = {'Player Name or ID': 'name'}
            r = requests.get(URL)

            rating = []
            soup = BeautifulSoup(r.content, 'html.parser')
            for form in soup.find_all("td"):
                rating.append(form)

            if (len(rating) > 39):
                str1 = ''.join(rating[15])
                ratings.append("review " + str1.strip())
            else:
                str1 = ''.join(rating[15])
                ratings.append(str1.strip())

        except Exception:
            traceback.print_exc()
            ratings.append("None")

    for r in range(len(ratings)):
        df['Ratings'][r] = ratings[r]

    df.to_excel(str(excelSheet[0]))

    messagebox.showinfo('Chess Tourney Management System', "The process has been completed! " +
                        "Please refresh your excel sheet to see the changes.")
except Exception:
    messagebox.showinfo("Thank You!", "Your excel sheet wasn't found. Thank you for using the Tourney Managemnt Sytem!")



