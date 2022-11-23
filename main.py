#!/usr/bin/python3
# -*- coding: utf-8 -*-

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests as rq
from tkinter import *
from tkinter import ttk
import classes

VERSION = 5.131
TOKEN = 'fcf784d2fcf784d2fcf784d206ffe7472fffcf7fcf784d29fdf12d1cff39e144bbbaa42'


def check_id(newval):
    if not newval.isdigit():
        errmsg.set('ID группы должно состоять только из чисел')
    else:
        pass


root = Tk()
root.title('SMM-парсер')
root.geometry("300x250")

label = Label(text="Введите ID группы")
label.pack()


check = (root.register(check_id), "%P")
vk_group_id_input = ttk.Entry(validate="key", validatecommand=check)
vk_group_id_input.pack()

errmsg = StringVar()
error_label = ttk.Label(foreground="red", textvariable=errmsg, wraplength=250)
error_label.pack()

output = ttk.Label()
output.pack()

root.mainloop()

