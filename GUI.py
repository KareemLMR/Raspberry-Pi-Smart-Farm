import tkinter as tk
from tkinter import ttk
from tkinter import Entry
from tkinter import messagebox
from tkinter import *
from PIL import ImageTk, Image

import http.client
import requests
import json

from threading import Thread
from time import sleep

from datetime import datetime

import re

length = 640
width = 480

day = 2

def ReadFile(current_day):
    with open('Data.txt') as f:
        lines = f.read().splitlines()


    rows = [0] * 7

    rows[0] = list(lines[0 + (day - 1)*8].split())
    rows[1] = list(lines[1 + (day - 1)*8].split())
    rows[2] = list(lines[2 + (day - 1)*8].split())
    rows[3] = list(lines[3 + (day - 1)*8].split())
    rows[4] = list(lines[4 + (day - 1)*8].split())
    rows[5] = list(lines[5 + (day - 1)*8].split())
    rows[6] = list(lines[6 + (day - 1)*8].split())

    lst = [rows[0], rows[1], rows[2], rows[3], rows[4], rows[5], rows[6]]

    return lst

lst = ReadFile(day)

class Table:
    def __init__(self,root,list):

        # code for creating table
        def giveControl(var):
            newWindow = Toplevel(root)
            newWindow.title("Controls")
            newWindow.geometry("300x300")
            Zone_adjust = Canvas(
            newWindow,
            height=150,
            width=300,
            bg='white'
            )
            if var == 0:
                Title1 = tk.Label(newWindow, bg = "white", text = "Zone 1 ", font=('Times New Roman',10,'bold')).place(x = 0, y = 0)
                Moisture_adjust1 = tk.Label(newWindow, bg = "white", text = "Moisture Adjust ", font=('Times New Roman',10,'bold')).place(x = 0, y = 20)
                zone1_water = double_slider(newWindow, 10, 200, 100, 0, HORIZONTAL)
                pH1 = tk.Label(newWindow, bg = "white", text = "pH Adjust ", font=('Times New Roman',10,'bold')).place(x = 0, y = 60)
                zone1_pH = double_slider(newWindow, 10, 200, 100, 40, HORIZONTAL)
                EC1 = tk.Label(newWindow, bg = "white", text = "EC Adjust ", font=('Times New Roman',10,'bold')).place(x = 0, y = 100)
                zone1_EC = double_slider(newWindow, 10, 200, 100, 80, HORIZONTAL)
                DO1 = tk.Label(newWindow, bg = "white", text = "DO Adjust ", font=('Times New Roman',10,'bold')).place(x = 0, y = 140)
                zone1_DO = double_slider(newWindow, 10, 200, 100, 120, HORIZONTAL)
            elif var == 1:
                Title1 = tk.Label(newWindow, bg = "white", text = "Zone 2 ", font=('Times New Roman',10,'bold')).place(x = 0, y = 0)
                Moisture_adjust1 = tk.Label(newWindow, bg = "white", text = "Moisture Adjust ", font=('Times New Roman',10,'bold')).place(x = 0, y = 20)
                zone1_water = double_slider(newWindow, 10, 200, 100, 0, HORIZONTAL)
                pH1 = tk.Label(newWindow, bg = "white", text = "pH Adjust ", font=('Times New Roman',10,'bold')).place(x = 0, y = 60)
                zone1_pH = double_slider(newWindow, 10, 200, 100, 40, HORIZONTAL)
                EC1 = tk.Label(newWindow, bg = "white", text = "EC Adjust ", font=('Times New Roman',10,'bold')).place(x = 0, y = 100)
                zone1_EC = double_slider(newWindow, 10, 200, 100, 80, HORIZONTAL)
                DO1 = tk.Label(newWindow, bg = "white", text = "DO Adjust ", font=('Times New Roman',10,'bold')).place(x = 0, y = 140)
                zone1_DO = double_slider(newWindow, 10, 200, 100, 120, HORIZONTAL)
            elif var == 2:
                Title1 = tk.Label(newWindow, bg = "white", text = "Zone 3 ", font=('Times New Roman',10,'bold')).place(x = 0, y = 0)
                Moisture_adjust1 = tk.Label(newWindow, bg = "white", text = "Moisture Adjust ", font=('Times New Roman',10,'bold')).place(x = 0, y = 20)
                zone1_water = double_slider(newWindow, 10, 200, 100, 0, HORIZONTAL)
                pH1 = tk.Label(newWindow, bg = "white", text = "pH Adjust ", font=('Times New Roman',10,'bold')).place(x = 0, y = 60)
                zone1_pH = double_slider(newWindow, 10, 200, 100, 40, HORIZONTAL)
                EC1 = tk.Label(newWindow, bg = "white", text = "EC Adjust ", font=('Times New Roman',10,'bold')).place(x = 0, y = 100)
                zone1_EC = double_slider(newWindow, 10, 200, 100, 80, HORIZONTAL)
                DO1 = tk.Label(newWindow, bg = "white", text = "DO Adjust ", font=('Times New Roman',10,'bold')).place(x = 0, y = 140)
                zone1_DO = double_slider(newWindow, 10, 200, 100, 120, HORIZONTAL)
            elif var == 3:
                Title1 = tk.Label(newWindow, bg = "white", text = "Zone 4 ", font=('Times New Roman',10,'bold')).place(x = 0, y = 0)
                Moisture_adjust1 = tk.Label(newWindow, bg = "white", text = "Moisture Adjust ", font=('Times New Roman',10,'bold')).place(x = 0, y = 20)
                zone1_water = double_slider(newWindow, 10, 200, 100, 0, HORIZONTAL)
                pH1 = tk.Label(newWindow, bg = "white", text = "pH Adjust ", font=('Times New Roman',10,'bold')).place(x = 0, y = 60)
                zone1_pH = double_slider(newWindow, 10, 200, 100, 40, HORIZONTAL)
                EC1 = tk.Label(newWindow, bg = "white", text = "EC Adjust ", font=('Times New Roman',10,'bold')).place(x = 0, y = 100)
                zone1_EC = double_slider(newWindow, 10, 200, 100, 80, HORIZONTAL)
                DO1 = tk.Label(newWindow, bg = "white", text = "DO Adjust ", font=('Times New Roman',10,'bold')).place(x = 0, y = 140)
                zone1_DO = double_slider(newWindow, 10, 200, 100, 120, HORIZONTAL)
            elif var == 4:
                Title1 = tk.Label(newWindow, bg = "white", text = "Zone 5 ", font=('Times New Roman',10,'bold')).place(x = 0, y = 0)
                Moisture_adjust1 = tk.Label(newWindow, bg = "white", text = "Moisture Adjust ", font=('Times New Roman',10,'bold')).place(x = 0, y = 20)
                zone1_water = double_slider(newWindow, 10, 200, 100, 0, HORIZONTAL)
                pH1 = tk.Label(newWindow, bg = "white", text = "pH Adjust ", font=('Times New Roman',10,'bold')).place(x = 0, y = 60)
                zone1_pH = double_slider(newWindow, 10, 200, 100, 40, HORIZONTAL)
                EC1 = tk.Label(newWindow, bg = "white", text = "EC Adjust ", font=('Times New Roman',10,'bold')).place(x = 0, y = 100)
                zone1_EC = double_slider(newWindow, 10, 200, 100, 80, HORIZONTAL)
                DO1 = tk.Label(newWindow, bg = "white", text = "DO Adjust ", font=('Times New Roman',10,'bold')).place(x = 0, y = 140)
                zone1_DO = double_slider(newWindow, 10, 200, 100, 120, HORIZONTAL)
            elif var == 5:
                Title1 = tk.Label(newWindow, bg = "white", text = "Zone 6 ", font=('Times New Roman',10,'bold')).place(x = 0, y = 0)
                Moisture_adjust1 = tk.Label(newWindow, bg = "white", text = "Moisture Adjust ", font=('Times New Roman',10,'bold')).place(x = 0, y = 20)
                zone1_water = double_slider(newWindow, 10, 200, 100, 0, HORIZONTAL)
                pH1 = tk.Label(newWindow, bg = "white", text = "pH Adjust ", font=('Times New Roman',10,'bold')).place(x = 0, y = 60)
                zone1_pH = double_slider(newWindow, 10, 200, 100, 40, HORIZONTAL)
                EC1 = tk.Label(newWindow, bg = "white", text = "EC Adjust ", font=('Times New Roman',10,'bold')).place(x = 0, y = 100)
                zone1_EC = double_slider(newWindow, 10, 200, 100, 80, HORIZONTAL)
                DO1 = tk.Label(newWindow, bg = "white", text = "DO Adjust ", font=('Times New Roman',10,'bold')).place(x = 0, y = 140)
                zone1_DO = double_slider(newWindow, 10, 200, 100, 120, HORIZONTAL)
            elif var == 6:
                Title1 = tk.Label(newWindow, bg = "white", text = "Zone 7 ", font=('Times New Roman',10,'bold')).place(x = 0, y = 0)
                Moisture_adjust1 = tk.Label(newWindow, bg = "white", text = "Moisture Adjust ", font=('Times New Roman',10,'bold')).place(x = 0, y = 20)
                zone1_water = double_slider(newWindow, 10, 200, 100, 0, HORIZONTAL)
                pH1 = tk.Label(newWindow, bg = "white", text = "pH Adjust ", font=('Times New Roman',10,'bold')).place(x = 0, y = 60)
                zone1_pH = double_slider(newWindow, 10, 200, 100, 40, HORIZONTAL)
                EC1 = tk.Label(newWindow, bg = "white", text = "EC Adjust ", font=('Times New Roman',10,'bold')).place(x = 0, y = 100)
                zone1_EC = double_slider(newWindow, 10, 200, 100, 80, HORIZONTAL)
                DO1 = tk.Label(newWindow, bg = "white", text = "DO Adjust ", font=('Times New Roman',10,'bold')).place(x = 0, y = 140)
                zone1_DO = double_slider(newWindow, 10, 200, 100, 120, HORIZONTAL)

            def on_closing():
                if messagebox.askokcancel("Quit", "Do you want to save settings?"):
                    lst[var][6] = zone1_water.getMax()
                    lst[var][7] = zone1_water.getMin()
                    lst[var][8] = zone1_pH.getMax()
                    lst[var][9] = zone1_pH.getMin()
                    lst[var][10] = zone1_EC.getMax()
                    lst[var][11] = zone1_EC.getMin()
                    lst[var][12] = zone1_DO.getMax()
                    lst[var][13] = zone1_DO.getMin()
                    t = Table(canvas_table, lst)
                    EditData(ReadFile(day))
                    url = "https://fertigation.herokuapp.com/zone/setting"

                    payload = json.dumps({
                    "id": str(var + 1),
    			    "minHumidity": str(zone1_water.getMin()),
    			    "maxHumidity": str(zone1_water.getMax()),
    			    "minPH": str(zone1_pH.getMin()),
    			    "maxPH": str(zone1_pH.getMax()),
    			    "minEC": str(zone1_EC.getMin()),
    			    "maxEC": str(zone1_EC.getMax()),
    			    "minOxygen": str(zone1_DO.getMin()),
    			    "maxOxygen": str(zone1_DO.getMax())
                    })
                    headers = {
                      'Content-Type': 'application/json'
                    }

                    response = requests.request("PUT", url, headers=headers, data=payload)

                    print(response.text)
                    newWindow.destroy()
            newWindow.protocol("WM_DELETE_WINDOW", on_closing)

        for i in range(total_rows):
            for j in range(total_columns):
                if j == 0:
                    self.e = Button (root, width=5, fg='blue',font=('Times New Roman',16,'bold'), text = str(lst[i][0]), padx=50, command = lambda i = i : giveControl(i))
                    self.e.grid(row=i, column=j)
                else:
                    self.x = Entry(root, width=5, fg='blue',
                               font=('Times New Roman',16,'bold'))
                    self.x.insert(j, list[i][j])
                    self.x.grid(row=i, column=j)



# take the data


# find total number of rows and
# columns in list
total_rows = len(lst)
total_columns = len(lst[0])

# create root window
root = tk.Tk()
root.title("Tab Widget")
root.geometry("640x480")
tabControl = ttk.Notebook(root)
tabControl.pack(expand = 1, fill ="both")

tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl)
tab4 = ttk.Frame(tabControl)
tab5 = ttk.Frame(tabControl)

tab1.pack(expand = 1, fill ="both")
tab2.pack(expand = 1, fill ="both")
tab3.pack(expand = 1, fill ="both")
tab4.pack(expand = 1, fill ="both")
tab5.pack(expand = 1, fill ="both")

tabControl.add(tab1, text ='My Farm')
tabControl.add(tab2, text ='Zones')
tabControl.add(tab3, text ='irrigation Tank')
tabControl.add(tab4, text ='Setting')
tabControl.add(tab5, text ='House')

text1 = tk.Label(tab1, text = "Smartech", font=('Times New Roman',16,'bold')).place(relx=0.4, rely=0.1, anchor=NW)

# the label for user_password
text2 = tk.Label(tab1, text = "irrigation system", font=('Times New Roman',16,'bold')).place(relx=0.4, rely=0.25, anchor=NW)


main_canvas = Canvas(tab2)
main_canvas.pack(side=LEFT, fill=BOTH, expand=1)

my_scrollbar = ttk.Scrollbar(tab2, orient=HORIZONTAL, command=main_canvas.xview)
my_scrollbar.pack(side=BOTTOM, fill=X)
main_canvas.configure(yscrollcommand=my_scrollbar.set)
main_canvas.bind('<Configure>', lambda e: main_canvas.configure(scrollregion = main_canvas.bbox("all")))

second_frame = Frame(main_canvas)
main_canvas.create_window((0,0), window=second_frame, anchor="nw")
current_day = tk.Label(tab2, text = "Day " + str(day), font=('Times New Roman',10,'bold')).place(relx=0.5, rely=0.05, anchor=CENTER)
def EditData(lst):
    Zone1 = Canvas(
        second_frame,
        height=400,
        width=200,
        bg='yellow'
        )
    Zone1.grid(row=0, column=0)

    Zone1.create_text(100, 50, text = lst[0][0])

    time_zone1 = tk.Label(Zone1, bg = "yellow", text = "Time " + lst[0][1], font=('Times New Roman',10,'bold')).place(x = 0, y = 60)
    Fertilizer_zone1 = tk.Label(Zone1, bg = "yellow", text = "Water " + lst[0][2] + " L\nA = " + lst[0][3] + "\nB = " + lst[0][4] + '\n' + "C = " + lst[0][5], font=('Times New Roman',10,'bold')).place(x = 0, y = 80)
    Moisture_CV = 50
    Moisture_zone1 = tk.Label(Zone1, bg = "yellow", text = "Moisture Current Value " + str(Moisture_CV), font=('Times New Roman',10,'bold')).place(x = 0, y = 160)
    PH_CV = 8
    PH_zone1 = tk.Label(Zone1, bg = "yellow", text = "PH Current Value " + str(PH_CV), font=('Times New Roman',10,'bold')).place(x = 0, y = 180)
    EC_CV = 20
    EC_zone1 = tk.Label(Zone1, bg = "yellow", text = "EC Current Value " + str(EC_CV), font=('Times New Roman',10,'bold')).place(x = 0, y = 200)

    Zone2 = Canvas(
        second_frame,
        height=400,
        width=200,
        bg='orange'
        )
    Zone2.grid(row=0, column=1)

    Zone2.create_text(100, 50, text = lst[1][0])

    time_zone2 = tk.Label(Zone2, bg = "orange", text = "Time " + lst[1][1], font=('Times New Roman',10,'bold')).place(x = 0, y = 60)
    Fertilizer_zone2 = tk.Label(Zone2, bg = "orange", text = "Water " + lst[1][2] + " L\n" + "A = " + lst[1][3] + "\nB = " + lst[1][4] + "\nC = " + lst[1][5], font=('Times New Roman',10,'bold')).place(x = 0, y = 80)
    Moisture_CV = 50
    Moisture_zone2 = tk.Label(Zone2, bg = "orange", text = "Moisture Current Value " + str(Moisture_CV), font=('Times New Roman',10,'bold')).place(x = 0, y = 160)
    PH_CV = 8
    PH_zone2 = tk.Label(Zone2, bg = "orange", text = "PH Current Value " + str(PH_CV), font=('Times New Roman',10,'bold')).place(x = 0, y = 180)
    EC_CV = 20
    EC_zone2 = tk.Label(Zone2, bg = "orange", text = "EC Current Value " + str(EC_CV), font=('Times New Roman',10,'bold')).place(x = 0, y = 200)

    Zone3 = Canvas(
        second_frame,
        height=400,
        width=200,
        bg='red'
        )
    Zone3.grid(row=0, column=2)

    Zone3.create_text(100, 50, text = lst[2][0])

    time_zone3 = tk.Label(Zone3, bg = "red", text = "Time " + lst[2][1], font=('Times New Roman',10,'bold')).place(x = 0, y = 60)
    Fertilizer_zone3 = tk.Label(Zone3, bg = "red", text = "Water " + lst[2][2] + " L\n" + "A = " + lst[2][3] + "\nB = " + lst[2][4] + "\nC = " + lst[2][5], font=('Times New Roman',10,'bold')).place(x = 0, y = 80)
    Moisture_CV = 50
    Moisture_zone3 = tk.Label(Zone3, bg = "red", text = "Moisture Current Value " + str(Moisture_CV), font=('Times New Roman',10,'bold')).place(x = 0, y = 160)
    PH_CV = 8
    PH_zone3 = tk.Label(Zone3, bg = "red", text = "PH Current Value " + str(PH_CV), font=('Times New Roman',10,'bold')).place(x = 0, y = 180)
    EC_CV = 20
    EC_zone3 = tk.Label(Zone3, bg = "red", text = "EC Current Value " + str(EC_CV), font=('Times New Roman',10,'bold')).place(x = 0, y = 200)

    Zone4 = Canvas(
        second_frame,
        height=400,
        width=200,
        bg='blue'
        )
    Zone4.grid(row=0, column=3)

    Zone4.create_text(100, 50, text = lst[3][0])


    time_zone4 = tk.Label(Zone4, bg = "blue", text = "Time " + lst[3][1], font=('Times New Roman',10,'bold')).place(x = 0, y = 60)
    Fertilizer_zone4 = tk.Label(Zone4, bg = "blue", text = "Water " + lst[3][2] + " L\n" + "A = " + lst[3][3] + "\nB = " + lst[3][4] + "\nC = " + lst[3][5], font=('Times New Roman',10,'bold')).place(x = 0, y = 80)
    Moisture_CV = 50
    Moisture_zone4 = tk.Label(Zone4, bg = "blue", text = "Moisture Current Value " + str(Moisture_CV), font=('Times New Roman',10,'bold')).place(x = 0, y = 160)
    PH_CV = 8
    PH_zone4 = tk.Label(Zone4, bg = "blue", text = "PH Current Value " + str(PH_CV), font=('Times New Roman',10,'bold')).place(x = 0, y = 180)
    EC_CV = 20
    EC_zone4 = tk.Label(Zone4, bg = "blue", text = "EC Current Value " + str(EC_CV), font=('Times New Roman',10,'bold')).place(x = 0, y = 200)

    Zone5 = Canvas(
        second_frame,
        height=400,
        width=200,
        bg='green'
        )
    Zone5.grid(row=0, column=4)

    Zone5.create_text(100, 50, text = lst[4][0])

    time_zone5 = tk.Label(Zone5, bg = "green", text = "Time " + lst[4][1], font=('Times New Roman',10,'bold')).place(x = 0, y = 60)
    Fertilizer_zone5 = tk.Label(Zone5, bg = "green", text = "Water " + lst[4][2] + " L\n" + "A = " + lst[4][3] + "\nB = " + lst[4][4] + "\nC = " + lst[4][5], font=('Times New Roman',10,'bold')).place(x = 0, y = 80)
    Moisture_CV = 50
    Moisture_zone5 = tk.Label(Zone5, bg = "green", text = "Moisture Current Value " + str(Moisture_CV), font=('Times New Roman',10,'bold')).place(x = 0, y = 160)
    PH_CV = 8
    PH_zone5 = tk.Label(Zone5, bg = "green", text = "PH Current Value " + str(PH_CV), font=('Times New Roman',10,'bold')).place(x = 0, y = 180)
    EC_CV = 20
    EC_zone5 = tk.Label(Zone5, bg = "green", text = "EC Current Value " + str(EC_CV), font=('Times New Roman',10,'bold')).place(x = 0, y = 200)

    Zone6 = Canvas(
        second_frame,
        height=400,
        width=200,
        bg='white'
        )
    Zone6.grid(row=0, column=5)

    Zone6.create_text(100, 50, text = lst[5][0])

    time_zone6 = tk.Label(Zone6, bg = "white", text = "Time " + lst[5][1], font=('Times New Roman',10,'bold')).place(x = 0, y = 60)
    Fertilizer_zone6 = tk.Label(Zone6, bg = "white", text = "Water " + lst[5][2] + " L\n" + "A = " + lst[5][3] + "\nB = " + lst[5][4] + "\nC = " + lst[5][5], font=('Times New Roman',10,'bold')).place(x = 0, y = 80)
    Moisture_CV = 50
    Moisture_zone6 = tk.Label(Zone6, bg = "white", text = "Moisture Current Value " + str(Moisture_CV), font=('Times New Roman',10,'bold')).place(x = 0, y = 160)
    PH_CV = 8
    PH_zone6 = tk.Label(Zone6, bg = "white", text = "PH Current Value " + str(PH_CV), font=('Times New Roman',10,'bold')).place(x = 0, y = 180)
    EC_CV = 20
    EC_zone6 = tk.Label(Zone6, bg = "white", text = "EC Current Value " + str(EC_CV), font=('Times New Roman',10,'bold')).place(x = 0, y = 200)

    Zone7 = Canvas(
        second_frame,
        height=400,
        width=200,
        bg='violet'
        )
    Zone7.grid(row=0, column=6)

    Zone7.create_text(100, 50, text = lst[6][0])


    time_zone7 = tk.Label(Zone7, bg = "violet", text = "Time " + lst[6][1], font=('Times New Roman',10,'bold')).place(x = 0, y = 60)
    Fertilizer_zone7 = tk.Label(Zone7, bg = "violet", text = "Water " + lst[6][2] + " L\n" + "A = " + lst[6][3] + "\nB = " + lst[6][4] + "\nC = " + lst[6][5], font=('Times New Roman',10,'bold')).place(x = 0, y = 80)
    Moisture_CV = 50
    Moisture_zone7 = tk.Label(Zone7, bg = "violet", text = "Moisture Current Value " + str(Moisture_CV), font=('Times New Roman',10,'bold')).place(x = 0, y = 160)
    PH_CV = 8
    PH_zone7 = tk.Label(Zone7, bg = "violet", text = "PH Current Value " + str(PH_CV), font=('Times New Roman',10,'bold')).place(x = 0, y = 180)
    EC_CV = 20
    EC_zone7 = tk.Label(Zone7, bg = "violet", text = "EC Current Value " + str(EC_CV), font=('Times New Roman',10,'bold')).place(x = 0, y = 200)

EditData(ReadFile(day))
photo = ImageTk.PhotoImage(Image.open("download.png"))
my_label = tk.Label(tab1, image = photo).place(relx=0.5, rely=0.5, anchor=CENTER)

canvas_table = Canvas(
tab4,
height=500,
width=1000,
bg='white'
)
canvas_table.grid(row=0, column=0)

adjustment_table = Canvas(
tab4,
height=500,
width=1000,
bg='white'
)
adjustment_table.grid(row=1, column=0)

t = Table(canvas_table, ReadFile(day))
def loadData():
    print(zone1_water.getMin(), zone1_water.getMax())
    lst[0][6] = zone1_water.getMax()
    lst[0][7] = zone1_water.getMin()
    t = Table(canvas_table, lst)
    EditData(ReadFile(day))

load = Button (canvas_table, text = "Load", padx=50, command=loadData)
load.grid(row=10, column=0)

class double_slider:
    min = 0
    max = 0
    least = 0
    most = 0
    def __init__(self,view, minimum, maximum, X, Y, orientation):
        MIN_slider = Scale(view, from_=minimum, to=minimum, orient=orientation)
        MIN_slider.place(x = X, y = Y)
        MAX_slider = Scale(view, from_=minimum, to=maximum, orient=orientation)
        MAX_slider.place(x = X + 100, y = Y)
        min = minimum
        max = maximum
        flag = 0
        def slide_MIN(var):
            self.least = var

        def slide_MAX(var):
            self.most = var
            MIN_slider = Scale(view, from_=min, to=MAX_slider.get(), orient=orientation, command=slide_MIN)
            MIN_slider.place(x = X, y = Y)


        MIN_slider = Scale(view, from_=min, to=min, orient=orientation, command=slide_MIN)
        MIN_slider.place(x = X, y = Y)
        MAX_slider = Scale(view, from_=min, to=max, orient=orientation, command=slide_MAX)
        MAX_slider.place(x = X + 100, y = Y)

    def getMin(self):
        return self.least
    def getMax(self):
        return self.most


#t = Table(tab4)

PH = Canvas(
    tab3,
    height=200,
    width=200,
    bg='pink'
    )
PH.grid(row=0, column=0)

PH.create_text(100, 10, text = "pH")
PH_Text = tk.Label(PH, bg = "pink", text = "pHValue " , font=('Times New Roman',20,'bold')).place(relx=0.5, rely=0.5,anchor=CENTER)
PH_Unit = tk.Label(PH, bg = "pink", text = "pH " , font=('Times New Roman',10,'bold')).place(relx=0.98, rely=0.98, anchor=SE)

DO = Canvas(
    tab3,
    height=200,
    width=200,
    bg='yellow'
    )
DO.grid(row=0, column=1)

DO.create_text(100, 10, text = "Dissolved Oxygen")
DO_Text = tk.Label(DO, bg = "yellow", text = "DOValue " , font=('Times New Roman',20,'bold')).place(relx=0.5, rely=0.5,anchor=CENTER)
DO_Unit = tk.Label(DO, bg = "yellow", text = "mg/L " , font=('Times New Roman',10,'bold')).place(relx=0.98, rely=0.98, anchor=SE)

EC = Canvas(
    tab3,
    height=200,
    width=200,
    bg='green'
    )
EC.grid(row=0, column=2)

EC.create_text(100, 10, text = "Electric Conductivity")
EC_Text = tk.Label(EC, bg = "green", text = "ECValue " , font=('Times New Roman',20,'bold')).place(relx=0.5, rely=0.5,anchor=CENTER)
EC_Unit = tk.Label(EC, bg = "green", text = "uS " , font=('Times New Roman',10,'bold')).place(relx=0.98, rely=0.98, anchor=SE)


House_readings = Canvas(
    tab5,
    height=400,
    width=200,
    bg='white'
    )
House_readings.grid(row=0, column=0)


ID = tk.Label(House_readings, bg = "white", text = "ID: 1 ", font=('Times New Roman',10,'bold')).place(x = 0, y = 20)
date = tk.Label(House_readings, bg = "white", text = "Time: " + str(datetime.now()), font=('Times New Roman',10,'bold')).place(x = 0, y = 40)
CO2_conc = 25
CO2 = tk.Label(House_readings, bg = "white", text = "CO2: " + str(CO2_conc) + " %", font=('Times New Roman',10,'bold')).place(x = 0, y = 60)
Moisture_percent = 66.5
Moisture_label = tk.Label(House_readings, bg = "white", text = "Moisture: " + str(Moisture_percent) + " %", font=('Times New Roman',10,'bold')).place(x = 0, y = 80)
Air1 = 1
Air2 = 0
Air1_label = tk.Label(House_readings, bg = "white", text = "Air1: " + str(Air1) , font=('Times New Roman',10,'bold')).place(x = 0, y = 100)
Air2_label = tk.Label(House_readings, bg = "white", text = "Air2: " + str(Air2) , font=('Times New Roman',10,'bold')).place(x = 0, y = 120)
Fan = 1
Fan_label = tk.Label(House_readings, bg = "white", text = "Fan: " + str(Fan) , font=('Times New Roman',10,'bold')).place(x = 0, y = 140)
Temp = 66.5
Temp_label = tk.Label(House_readings, bg = "white", text = "Temp: " + str(Temp) + " C", font=('Times New Roman',10,'bold')).place(x = 0, y = 140)

House_settings = Canvas(
    tab5,
    height=400,
    width=400,
    bg='white'
    )
House_settings.grid(row=0, column=1)

Moisture_set = tk.Label(House_settings, bg = "white", text = "Moisture ", font=('Times New Roman',10,'bold')).place(x = 0, y = 20)
Moisture_setSlider = double_slider(House_settings, 0, 100, 100, 20, HORIZONTAL)
Temp_set = tk.Label(House_settings, bg = "white", text = "Temperature ", font=('Times New Roman',10,'bold')).place(x = 0, y = 60)
Temp_setSlider = double_slider(House_settings, 0, 100, 100, 60, HORIZONTAL)

def updateSettings():
    while True:
        conn = http.client.HTTPSConnection("fertigation.herokuapp.com")
        for i in range(1, 3):
            conn.request("GET", "/zone/setting", {}, {'id': str(i)})

            res = conn.getresponse()
            data = str(res.read().decode("utf-8"))
            temp = re.findall(r'\d+', data)
            res = list(map(int, temp))
            lst[i - 1][6] = res[0]
            lst[i - 1][7] = res[1]
            lst[i - 1][8] = res[2]
            lst[i - 1][9] = res[3]
            lst[i - 1][10] = res[4]
            lst[i - 1][11] = res[5]
            lst[i - 1][12] = res[6]
            lst[i - 1][13] = res[7]
            t = Table(canvas_table, lst)
            EditData(ReadFile(day))
            print(res)
        print('\n')
        sleep(30)

thread1 = Thread(target = updateSettings)
thread1.start()
print("thread1 finished...exiting")

def updateData():
    var = 1
    while True:
        print("running")
        url = "https://fertigation.herokuapp.com/zone/"

        payload = json.dumps({
		        "id": '1',
		        "date": str(datetime.now()),
		        "ferta": str(var),
		        "fertb": str(var),
		        "fertc": str(var),
		        "water": str(var),
		        "ph": str(var),
		        "ec": str(var),
		        "moisture1": str(var),
		        "moisture2": str(var),
		        "moisture3": str(var),
		        "valve": '1',
		        "oxygen": str(var)
        })
        headers = {
          'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)
        var = var + 1

        sleep(60)

thread = Thread(target = updateData)
thread.start()
print("thread finished...exiting")

root.mainloop()
