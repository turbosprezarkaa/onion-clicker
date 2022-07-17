import os
import sys
import subprocess
import random
import time as time
import webbrowser
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

def install(package):
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

install('pillow')

global box
global liczba
global w
global window
global root
global variablefile

box = True
licznik = True
w = None

variablefile = open('Cache/num.txt', 'r+')
variablefile.flush()

liczba = int(variablefile.read())

exec(open('counter.py', encoding = 'utf-8').read(), globals())
exec(open('functions.py', encoding = 'utf-8').read(), globals())
exec(open('mgames.py', encoding = 'utf-8').read(), globals())

file = open('Cache/data.txt', 'r+')
fileread = file.read()

window = Tk()
window.title('Onion Clicker')
window.geometry('550x800')
window.iconbitmap('Cache/Images/icon.ico')
window.config(bg = '#ff8400')
window.resizable(0, 0)

photo1 = Image.open('Cache/Images/onion.png')
photo2 = Image.open('Cache/Images/hint.png')
photo3 = Image.open('Cache/Images/sklep.png')
photo4 = Image.open('Cache/Images/minigry.png')

image1 = photo1.resize((250, 250))
image2 = photo2.resize((310, 200))
image3 = photo3.resize((120, 120))
image4 = photo4.resize((120, 120))

newimg1 = ImageTk.PhotoImage(image1)
newimg2 = ImageTk.PhotoImage(image2)
newimg3 = ImageTk.PhotoImage(image3)
newimg4 = ImageTk.PhotoImage(image4)

button = Button(window, text = 'WERSJA 2.4', bg = '#ff8400', font = ('jetbrains mono bold', 13, 'underline'), relief = FLAT, bd = 0, activebackground = '#ff8400', command = link)
button.pack(side = BOTTOM, fill=BOTH)

licznik = Label(window, text = f'KASA:{liczba}$', bg = '#ff8400', font = ('jetbrains mono bold', 30))
licznik.pack()

minigames = Button(window, image = newimg4, bg = '#ff8400', activebackground= '#ff8400', relief = FLAT, command = mgames, borderwidth=0)
minigames.pack(side = BOTTOM)

sklep = Button(window, image = newimg3, bg = '#ff8400', activebackground= '#ff8400', command = sklep1, borderwidth=0)
sklep.pack(side = BOTTOM)

hint = Label(window, bg = '#ff8400', image = newimg2)
hint.pack(side = BOTTOM)

cebula = Button(window, bg = '#ff8400', activebackground= '#ff8400', image = newimg1, command = kasa, borderwidth=0)
cebula.pack(side = BOTTOM)

if 'TIER : BRONZE\n' in fileread:
	photo = Image.open('Cache/Images/onionbronze.png')
	image = photo.resize((250, 250))
	newimg = ImageTk.PhotoImage(image)

	cebula.config(image = newimg)
	cebula.image = newimg

if 'TIER : SILVER\n' in fileread:
	photo = Image.open('Cache/Images/onionsilver.png')
	image = photo.resize((250, 250))
	newimg = ImageTk.PhotoImage(image)

	cebula.config(image = newimg)
	cebula.image = newimg

if 'TIER : GOLD\n' in fileread:
	photo = Image.open('Cache/Images/oniongold.png')
	image = photo.resize((250, 250))
	newimg = ImageTk.PhotoImage(image)

	cebula.config(image = newimg)
	cebula.image = newimg

if 'TIER : DIAMOND\n' in fileread:
	photo = Image.open('Cache/Images/oniondiamond.png')
	image = photo.resize((250, 250))
	newimg = ImageTk.PhotoImage(image)

	cebula.config(image = newimg)
	cebula.image = newimg

else:
	pass

if 'MONEY : x2\n' in fileread:
	cebula.config(command = kasax2)

if 'MONEY : x3\n' in fileread:
	cebula.config(command = kasax3)

if 'MONEY : x5\n' in fileread:
	cebula.config(command = kasax5)

window.bind('<Escape>', closeevent)
window.bind('<F1>', helpevent)
window.bind('<F7>', developer)
window.bind('<F8>', autosave)

window.protocol('WM_DELETE_WINDOW', close)
window.mainloop()
