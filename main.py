from bs4 import BeautifulSoup
import datetime
import tkinter as tk
from tkinter import ttk
from constants import *
import requests

window = tk.Tk()
window.title("Конвентер курса валют")

window.geometry("670x400")
window.minsize(width=670, height=350)
window.maxsize(width=670, height=400)

style = ttk.Style()
style.configure('W.TButton', font=('Bahnschrift Light SemiCondensed', 19, 'underline'))

today = datetime.datetime.now()
date = ""
date += today.strftime("%b") + " " + today.strftime("%d") + " " + today.strftime("%I") + ":" + \
        today.strftime("%M") + " " + today.strftime("%p") + " " + today.strftime("%Z")
dates = tk.Label(text=str(date), font=('Bahnschrift Light SemiCondensed', 19))
dates.grid(row=1, column=1)

currname = tk.Label(text="Название валюты", font=('Bahnschrift Light SemiCondensed', 19))
currname.grid(row=3, column=2)

combobox = ttk.Combobox(window, values=currency_list, state='readonly', font=('Bahnschrift Light SemiCondensed', 19))
combobox.grid(row=4, column=2)
combobox.current(0)

combobox_two = ttk.Combobox(window, values=currency_list, state='readonly', font=('Bahnschrift Light SemiCondensed', 19))
combobox_two.grid(row=5, column=2)
combobox_two.current(0)

currval = tk.Label(text="Количество валюты", font=('Bahnschrift Light SemiCondensed', 19))
currval.grid(row=3, column=0)

val = tk.Entry(window, justify='center', font=('Bahnschrift Light SemiCondensed', 19))
val.grid(row=4, column=0)

def converter():
    curr_temp = combobox.get()
    curr_temp_two = combobox_two.get()

    curr1 = ""
    curr2 = ""

    for i in range(len(curr_temp)):
        if curr_temp[i] == " ":
            curr1 += "+"

        else:
            curr1 += curr_temp[i]

    for i in range(len(curr_temp_two)):
        if curr_temp_two[i] == " ":
            curr2 += "+"

        else:
            curr2 += curr_temp_two[i]

    url = f"https://www.google.com/search?q={curr1}+to+{curr2}"
    data = requests.get(url)

    soup = BeautifulSoup(data.text, 'html.parser')

    values = soup.get_text()

    index = values.find("=")
    index2 = values.find(" ", index)

    value = values[index + 1: index2]

    x = val.get()

    if curr1 == curr2:
        final = tk.Label(text=str(x), font=('Bahnschrift Light SemiCondensed', 19))

    else:
        new_curr = float(value.replace(",",".")) * float(x.replace(",","."))
        final = tk.Label(text=str(new_curr), font=('Bahnschrift Light SemiCondensed', 19))

    final.grid(row=5, column=0)

button = ttk.Button(window,
    style='W.TButton',
    text="Конвертировать!",
    command=converter)

button.grid(row=8, column=1)

window.mainloop()
