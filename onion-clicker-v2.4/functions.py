def link():
    webbrowser.open('https://github.com/turbosprezarkaa/onion-clicker')
    webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

def secretlink():
    webbrowser.open('https://onionnft.prv.pl')

def console():
	global box
	global liczba
	global licznik
	global window
	global cebula

	def consolekasa():
		global liczba
		global licznik

		liczba += 2
		licznik.pack_forget()
		licznik = Label(window, text = f'KASA:{liczba}$', bg = '#ff8400', font = ('jetbrains mono bold', 30))
		licznik.pack(side = TOP)

	get = box.get(1.0, END)
	file = open('Cache/data.txt', 'r+')
	fileread = file.read()

	if 'cebulatogigachad' in get:
		if 'CODE : cebulatogigachad\n' in fileread:
			messagebox.showinfo('Onion Clicker', 'KOD BYŁ JUŻ AKTYWOWANY')
		else:
			file.write('CODE : cebulatogigachad\n')
			file.flush()
			liczba += 2000
			licznik.pack_forget()
			licznik = Label(window, text = f'KASA:{liczba}$', bg = '#ff8400', font = ('jetbrains mono bold', 30))
			licznik.pack(side = TOP)
			message = messagebox.showinfo('Onion Clicker', 'DODANO 2000$')
			box.delete(1.0, END)

			if liczba >= 100000:
				window.destroy()
				root = Tk()
				root.title('Onion Clicker')
				root.geometry('500x400')
				root.config(bg = '#ff8400')
				root.resizable(0, 0)
				root.iconbitmap('Cache/Images/icon.ico')
				label1 = Label(root, text = 'OTO KONIEC GRY!', bg = '#ff8400', font = ('jetbrains mono bold', 25, 'underline'), anchor = CENTER)
				label1.pack(side = TOP)
				label2 = Label(root, text = "no chyba, że dodam jakieś update'y\nDZIĘKI ZA ZAGRANIE W ONION CLICKERA! <3\n\n'ONION CLICKER' the Game\nAutor: Ja\nKod gry: Ja\nGrafiki: Ja\nPomysł: Ja\nXDDDD", bg = '#ff8400', font = ('jetbrains mono bold', 15), anchor = CENTER)
				label2.pack()
				root.after(30000, lambda: root.destroy())
				root.mainloop()

	elif 'pythonwcaleniessie' in get:
		if 'CODE : pythonwcaleniessie\n' in fileread:
			messagebox.showinfo('Onion Clicker', 'KOD BYŁ JUŻ AKTYWOWANY')
		else:
			file.write('CODE : pythonwcaleniessie\n')
			file.flush()
			file = open('Cache/data.txt', 'r+')
			fileread = file.read()
			file.write('TIER : BRONZE\n')
			file.flush()
			photo1 = Image.open('Cache/Images/onionbronze.png')
			image1 = photo1.resize((250, 250))
			newimg1 = ImageTk.PhotoImage(image1)
			cebula.config(bg = '#ff8400', activebackground= '#ff8400', image=newimg1, borderwidth=0)
			cebula.image = newimg1
			message = messagebox.showinfo('Onion Clicker', 'DODANO NOWY SKIN CEBULI [TIER BRONZE]')
			box.delete(1.0, END)
        
	elif 'amogus' in get:
		if 'CODE : amogus\n' in fileread:
			messagebox.showinfo('Onion Clicker', 'KOD BYŁ JUŻ AKTYWOWANY')
		else:
			file.write('CODE : amogus\n')
			file.flush()
			file = open('Cache/data.txt', 'r+')
			fileread = file.read()
			file.write('MONEY : x2\n')
			file.flush()
			cebula.config(command = consolekasa)
			message = messagebox.showinfo(
				'Onion Clicker', 'DODANO NOWE ULEPSZENIE [CLICK x2]')
			box.delete(1.0, END)
	else:
            messagebox.showinfo('Onion Clicker', 'NIEPRAWIDŁOWA KOMENDA')
            box.delete(1.0, END)

def autosavedestroy():
    global window
    global root0

    root0.destroy()
    exec(open('main.py', encoding = 'utf-8').read(), globals())

def passevent():
    pass

def barstart():
    global bar
    bar.start

def autosave(event):
    if event:
        global window
        global liczba
        global root0
        global variablefile
        global bar
        
        variablefile.truncate()
        variablefile = open('Cache/num.txt', 'r+')
        variablefile.write(str(liczba))
        variablefile.flush()

        window.destroy()

        root0 = Tk()
        root0.title('Onion Clicker')
        root0.geometry('500x120')
        root0.iconbitmap('Cache/Images/icon.ico')
        root0.resizable(0, 0)
        root0.config(bg = '#ff8400')

        label = Label(root0, text = 'ZAPISYWANIE POSTĘPU...', bg = '#ff8400', font = ('jetbrains mono bold', 25))
        label.pack(expand = True)

        bar = ttk.Progressbar(root0, orient = 'horizontal', mode = 'determinate', length = 280)
        bar.start()
        bar.pack()

        void = Label(root0, bg = '#ff8400')
        void.pack()

        root0.after(4000, autosavedestroy)
        root0.protocol('WM_DELETE_WINDOW', passevent)
        root0.mainloop()

def developer(event):
	global box
	global w

	def developerdestroy():
		global w
		w.destroy()
		w = None

	if event:
		if w is None:
			w = Toplevel()
			w.grab_set()
			w.geometry('450x121')
			w.title('Onion Clicker')
			w.iconbitmap('Cache/Images/icon.ico')

			box = Text(w, wrap = CHAR, relief = SOLID, bd = 10, insertbackground = 'white', bg = 'black', font = ('jetbrains mono bold', 17), fg = 'white', width = 25, height = 1)
			box.place(x = 0, y = 0, relwidth = 1, relheight = 1, width = 1)
			button = Button(w, relief = FLAT, bd = 0, highlightcolor = 'white', highlightbackground = 'white', text = 'ZATWIERDŹ', font = ('jetbrains mono bold', 13), bg = 'black', fg = 'white', activebackground = 'black', activeforeground = 'white', command = console)
			button.pack(fill = BOTH, side = BOTTOM)

			w.protocol('WM_DELETE_WINDOW', developerdestroy)
			w.mainloop()
		else:
			pass

def sklep4():
    global window2
    global label1
    global button0
    global button1
    global button2
    global button3
    global button4
    global button5
    global nextpage
    global nextpage2
    global shop
    global window2
    global npage
    global void1
    global void2
    global void3

    label1.pack_forget()
    button1.pack_forget()
    button2.pack_forget()
    button3.pack_forget()
    button4.pack_forget()
    button5.pack_forget()
    nextpage.pack_forget()
    shop.pack_forget()
    npage.pack_forget()
    void1.pack_forget()
    void2.pack_forget()
    void3.pack_forget()

    shop = Label(window2, text = 'S K L E P :', bg = '#ff8400', font = ('jetbrains mono bold', 30))
    shop.pack(fill = BOTH)

    label1 = Label(window2, text = 'MINIGRY', bg = '#ff8400', activebackground = '#ff8400', height = 1, font = ('jetbrains mono bold', 25))
    label1.pack()

    button2 = Button(window2, text = 'in development', bg = '#ff8400', activebackground = '#ff8400', width = 25, height = 1, font = ('jetbrains mono bold', 19), command = None, relief = SOLID)
    button2.pack()

    void1 = Label(window2, bg = '#ff8400')
    void1.pack()
    
    button3 = Button(window2, text = 'in development', bg = '#ff8400', activebackground = '#ff8400', width = 25, height = 1, font = ('jetbrains mono bold', 19), command = None, relief = SOLID)
    button3.pack()

    void2 = Label(window2, bg = '#ff8400')
    void2.pack()

    button4 = Button(window2, text = 'in development', bg = '#ff8400', activebackground = '#ff8400', width = 25, height = 1, font = ('jetbrains mono bold', 19), command = None, relief = SOLID)
    button4.pack()

    photo6 = Image.open('Cache/Images/poprzednia strona.png')
    image6 = photo6.resize((120, 120))
    newimg6 = ImageTk.PhotoImage(image6)

    nextpage = Button(window2, image = newimg6, bg = '#ff8400', activebackground = '#ff8400', command = sklep2, borderwidth = 0)
    nextpage.pack(side = BOTTOM)
    nextpage.image = newimg6

def sklep2():
    global window2
    global label1
    global button1
    global button2
    global button3
    global button4
    global button5
    global nextpage
    global nextpage2
    global shop
    global window2
    global npage
    global void1
    global void2
    global void3

    label1.pack_forget()
    button2.pack_forget()
    button3.pack_forget()
    button4.pack_forget()
    button5.pack_forget()
    nextpage.pack_forget()
    shop.pack_forget()
    void1.pack_forget()
    void2.pack_forget()
    void3.pack_forget()

    shop = Label(window2, text = 'S K L E P :', bg = '#ff8400', font = ('jetbrains mono bold', 30))
    shop.pack(fill = BOTH)

    label1 = Label(window2, text = 'ULEPSZENIA', bg = '#ff8400', activebackground = '#ff8400', height = 1, font = ('jetbrains mono bold', 25))
    label1.pack()
    
    button1 = Button(window2, text = 'KASA 2x - 500$', bg = '#ff8400', activebackground = '#ff8400', width = 25, height = 1, font = ('jetbrains mono bold', 19), command = x2, relief = SOLID)
    button1.pack()

    void1 = Label(window2, bg = '#ff8400')
    void1.pack()

    button2 = Button(window2, text = 'KASA 3x - 7,000$', bg = '#ff8400', activebackground = '#ff8400', width = 25, height = 1, font = ('jetbrains mono bold', 19), command = x3, relief = SOLID)
    button2.pack()

    void2 = Label(window2, bg = '#ff8400')
    void2.pack()

    button3 = Button(window2, text = 'KASA 5x - 10,000$', bg = '#ff8400', activebackground = '#ff8400', width = 25, height = 1, font = ('jetbrains mono bold', 19), command = x5, relief = SOLID)
    button3.pack()

    photo5 = Image.open('Cache/Images/nastepna strona.png')
    image5 = photo5.resize((120, 120))
    newimg5 = ImageTk.PhotoImage(image5)

    photo6 = Image.open('Cache/Images/poprzednia strona.png')
    image6 = photo6.resize((120, 120))
    newimg6 = ImageTk.PhotoImage(image6)

    npage = Button(window2, image = newimg5, bg = '#ff8400', activebackground = '#ff8400', command = sklep4, borderwidth = 0)
    npage.pack(side = BOTTOM)
    npage.image = newimg5

    nextpage = Button(window2, image = newimg6, bg = '#ff8400', activebackground = '#ff8400', command = sklep3, borderwidth = 0)
    nextpage.pack(side = BOTTOM)
    nextpage.image = newimg6

def sklep3():
    global window2
    global label1
    global button1
    global button2
    global button3
    global button4
    global button5
    global nextpage
    global shop
    global window2
    global npage
    global void1
    global void2
    global void3

    label1.pack_forget()
    button1.pack_forget()
    button2.pack_forget()
    button3.pack_forget()
    button4.pack_forget()
    button5.pack_forget()
    nextpage.pack_forget()
    shop.pack_forget()
    npage.pack_forget()
    void1.pack_forget()
    void2.pack_forget()
    void3.pack_forget()

    shop = Label(window2, text = 'S K L E P :', bg = '#ff8400', font = ('jetbrains mono bold', 30))
    shop.pack(fill = BOTH)

    label1 = Label(window2, text = 'TIERY', bg = '#ff8400', font = ('jetbrains mono bold' , 25))
    label1.pack(fill = BOTH)

    button2 = Button(window2, text = 'TIER BRONZE - 700$', bg = '#ff8400', activebackground = '#ff8400', width = 25, height = 1, font = ('jetbrains mono bold', 19), command = tierbronze, relief = SOLID)
    button2.pack()

    void1 = Label(window2, bg = '#ff8400')
    void1.pack()

    button3 = Button(window2, text = 'TIER SILVER - 5,000$', bg = '#ff8400', activebackground = '#ff8400', width = 25, height = 1, font = ('jetbrains mono bold', 19), command = tiersilver, relief = SOLID)
    button3.pack()

    void2 = Label(window2, bg = '#ff8400')
    void2.pack()

    button4 = Button(window2, text = 'TIER GOLD - 15,000$', bg = '#ff8400', activebackground = '#ff8400', width = 25, height = 1, font = ('jetbrains mono bold', 19), command = tiergold, relief = SOLID)
    button4.pack()

    void3 = Label(window2, bg = '#ff8400')
    void3.pack()

    button5 = Button(window2, text = 'TIER DIAMOND - 30,000$', bg = '#ff8400', activebackground = '#ff8400', width = 25, height = 1, font = ('jetbrains mono bold', 19), command = tierdiamond, relief = SOLID)
    button5.pack()

    photo5 = Image.open('Cache/Images/nastepna strona.png')
    image5 = photo5.resize((120, 120))
    newimg5 = ImageTk.PhotoImage(image5)
    
    nextpage = Button(window2, image = newimg5, bg = '#ff8400', activebackground = '#ff8400', command = sklep2, borderwidth = 0)
    nextpage.pack(side = BOTTOM)
    nextpage.image = newimg5

def sklep1():
    global window2
    global label1
    global button1
    global button2
    global button3
    global button4
    global button5
    global nextpage
    global shop
    global npage
    global liczba
    global variablefile
    global window
    global void1
    global void2
    global void3

    window2 = Toplevel()
    window2.title('Onion Clicker')
    window2.geometry('550x700')
    window2.iconbitmap('Cache/Images/icon.ico')
    window2.config(bg = '#ff8400')
    window2.resizable(0, 0)
    window2.grab_set()

    shop = Label(window2, text = 'S K L E P :', bg = '#ff8400', font = ('jetbrains mono bold', 30))
    shop.pack(fill = BOTH)

    label1 = Label(window2, text = 'TIERY', bg = '#ff8400', font = ('jetbrains mono bold' , 25))
    label1.pack(fill = BOTH)

    button2 = Button(window2, text = 'TIER BRONZE - 700$', bg = '#ff8400', activebackground = '#ff8400', width = 25, height = 1, font = ('jetbrains mono bold', 19), command = tierbronze, relief = SOLID)
    button2.pack()

    void1 = Label(window2, bg = '#ff8400')
    void1.pack()

    button3 = Button(window2, text = 'TIER SILVER - 5,000$', bg = '#ff8400', activebackground = '#ff8400', width = 25, height = 1, font = ('jetbrains mono bold', 19), command = tiersilver, relief = SOLID)
    button3.pack()

    void2 = Label(window2, bg = '#ff8400')
    void2.pack()

    button4 = Button(window2, text = 'TIER GOLD - 15,000$', bg = '#ff8400', activebackground = '#ff8400', width = 25, height = 1, font = ('jetbrains mono bold', 19), command = tiergold, relief = SOLID)
    button4.pack()

    void3 = Label(window2, bg = '#ff8400')
    void3.pack()

    button5 = Button(window2, text = 'TIER DIAMOND - 30,000$', bg = '#ff8400', activebackground = '#ff8400', width = 25, height = 1, font = ('jetbrains mono bold', 19), command = tierdiamond, relief = SOLID)
    button5.pack()

    photo4 = Image.open('Cache/Images/wroc.png')
    image4 = photo4.resize((120, 120))
    newimg4 = ImageTk.PhotoImage(image4)

    photo5 = Image.open('Cache/Images/nastepna strona.png')
    image5 = photo5.resize((120, 120))
    newimg5 = ImageTk.PhotoImage(image5)

    wyjście = Button(window2, image = newimg4, bg = '#ff8400', activebackground = '#ff8400', command = window2.destroy, borderwidth = 0)
    wyjście.pack(side = BOTTOM)

    nextpage = Button(window2, image = newimg5, bg = '#ff8400', activebackground = '#ff8400', command = sklep2, borderwidth = 0)
    nextpage.pack(side = BOTTOM)

    window2.mainloop()

def x2():
    global liczba
    global licznik
    global cebula
    global message

    file = open('Cache/data.txt', 'r+')
    fileread = file.read()

    if 'MONEY : x2\n' in fileread:
        cebula.config(command = kasax2)
    else:
        if int(liczba) >= 500:
            file.write('MONEY : x2\n')
            cebula.config(command = kasax2)
            liczba -= 500
            licznik.pack_forget()
            licznik = Label(window, text = f'KASA:{liczba}$', bg = '#ff8400', font = ('jetbrains mono bold', 30))
            licznik.pack(side = TOP)
            messagebox.showinfo('Onion Clicker', 'ZAKUPIŁEŚ:\n\n- ULEPSZENIE (KASA x2)')

        else:
            message = messagebox.showinfo('Onion Clicker', 'NIE STAĆ CIEBIE NA ZAKUP TEGO PRZEDMIOTU!')

def x3():
    global liczba
    global licznik
    global cebula

    file = open('Cache/data.txt', 'r+')
    fileread = file.read()

    if 'MONEY : x3\n' in fileread:
        cebula.config(command = kasax3)
    else:
        if int(liczba) >= 7000:
            file.write('MONEY : x3\n')
            cebula.config(command = kasax3)
            liczba -= 7000
            licznik.pack_forget()
            licznik = Label(window, text = f'KASA:{liczba}$', bg = '#ff8400', font = ('jetbrains mono bold', 30))
            licznik.pack(side = TOP)
            messagebox.showinfo('Onion Clicker', 'ZAKUPIŁEŚ:\n\n- ULEPSZENIE (KASA x3)')

        else:
            message = messagebox.showinfo('Onion Clicker', 'NIE STAĆ CIEBIE NA ZAKUP TEGO PRZEDMIOTU!')     

def x5():
    global liczba
    global licznik
    global cebula

    file = open('Cache/data.txt', 'r+')
    fileread = file.read()

    if 'MONEY : x5\n' in fileread:
        cebula.config(command = kasax5)
    else:
        if int(liczba) >= 10000:
            file.write('MONEY : x5\n')
            cebula.config(command = kasax5)
            liczba -= 10000
            licznik.pack_forget()
            licznik = Label(window, text = f'KASA:{liczba}$', bg = '#ff8400', font = ('jetbrains mono bold', 30))
            licznik.pack(side = TOP)
            messagebox.showinfo('Onion Clicker', 'ZAKUPIŁEŚ:\n\n- ULEPSZENIE (KASA x5)')

        else:
            message = messagebox.showinfo('Onion Clicker', 'NIE STAĆ CIEBIE NA ZAKUP TEGO PRZEDMIOTU!')        

def tierbronze():
    global liczba
    global licznik
    global cebula

    file = open('Cache/data.txt', 'r+')
    fileread = file.read()

    if 'TIER : BRONZE\n' in fileread:
        photo1 = Image.open('Cache/Images/onionbronze.png')
        image1 = photo1.resize((250, 250))
        newimg1 = ImageTk.PhotoImage(image1)

        cebula.config(bg = '#ff8400', activebackground = '#ff8400', image = newimg1, borderwidth = 0)
        cebula.image = newimg1
    else:
        if int(liczba) >= 700:
            file.write('TIER : BRONZE\n')
            file.flush()
            photo1 = Image.open('Cache/Images/onionbronze.png')
            image1 = photo1.resize((250, 250))
            newimg1 = ImageTk.PhotoImage(image1)

            cebula.config(bg = '#ff8400', activebackground = '#ff8400', image = newimg1, borderwidth = 0)
            cebula.image = newimg1

            liczba -= 700
            licznik.pack_forget()
            licznik = Label(window, text = f'KASA:{liczba}$', bg = '#ff8400', font = ('jetbrains mono bold', 30))
            liczba += 350
            licznik.pack_forget()
            licznik = Label(window, text = f'KASA:{liczba}$', bg = '#ff8400', font = ('jetbrains mono bold', 30))
            licznik.pack(side = TOP)
            messagebox.showinfo('Onion Clicker', 'ZAKUPIŁEŚ:\n\n- TIER (BRONZE)\n\n\n\nOTRZYMAŁEŚ:\n\n- ZWROT CENY (350$)')

        else:
            message = messagebox.showinfo('Onion Clicker', 'NIE STAĆ CIEBIE NA ZAKUP TEGO PRZEDMIOTU!')  

def tiersilver():
    global liczba
    global licznik
    global cebula

    file = open('Cache/data.txt', 'r+')
    fileread = file.read()

    if 'TIER : SILVER\n' in fileread:
        photo1 = Image.open('Cache/Images/onionsilver.png')
        image1 = photo1.resize((250, 250))
        newimg1 = ImageTk.PhotoImage(image1)

        cebula.config(bg = '#ff8400', activebackground = '#ff8400', image = newimg1, borderwidth = 0)
        cebula.image = newimg1
    else:
        if int(liczba) >= 5000:
            file.write('TIER : SILVER\n')
            file.flush()
            photo1 = Image.open('Cache/Images/onionsilver.png')
            image1 = photo1.resize((250, 250))
            newimg1 = ImageTk.PhotoImage(image1)

            cebula.config(bg = '#ff8400', activebackground = '#ff8400', image = newimg1, borderwidth = 0)
            cebula.image = newimg1

            liczba -= 5000
            licznik.pack_forget()
            licznik = Label(window, text = f'KASA:{liczba}$', bg = '#ff8400', font = ('jetbrains mono bold', 30))
            licznik.pack(side = TOP)
            liczba += 500
            licznik.pack_forget()
            licznik = Label(window, text = f'KASA:{liczba}$', bg = '#ff8400', font = ('jetbrains mono bold', 30))
            licznik.pack(side = TOP)
            messagebox.showinfo('Onion Clicker', 'ZAKUPIŁEŚ:\n\n- TIER (SILVER)\n\n\n\nOTRZYMAŁEŚ:\n\n- ZWROT CENY (500$)')

        else:
            message = messagebox.showinfo('Onion Clicker', 'NIE STAĆ CIEBIE NA ZAKUP TEGO PRZEDMIOTU!')  

def tiergold():
    global liczba
    global licznik
    global cebula

    file = open('Cache/data.txt', 'r+')
    fileread = file.read()

    if 'TIER : GOLD\n' in fileread:
        photo1 = Image.open('Cache/Images/oniongold.png')
        image1 = photo1.resize((250, 250))
        newimg1 = ImageTk.PhotoImage(image1)

        cebula.config(bg = '#ff8400', activebackground = '#ff8400', image = newimg1, borderwidth = 0)
        cebula.image = newimg1
    else:
        if int(liczba) >= 15000:
            file.write('TIER : GOLD\n')
            file.flush()
            photo1 = Image.open('Cache/Images/oniongold.png')
            image1 = photo1.resize((250, 250))
            newimg1 = ImageTk.PhotoImage(image1)

            cebula.config(bg = '#ff8400', activebackground = '#ff8400', image = newimg1, borderwidth = 0)
            cebula.image = newimg1

            liczba -= 15000
            licznik.pack_forget()
            licznik = Label(window, text = f'KASA:{liczba}$', bg = '#ff8400', font = ('jetbrains mono bold', 30))
            licznik.pack(side = TOP)
            liczba += 4000
            licznik.pack_forget()
            licznik = Label(window, text = f'KASA:{liczba}$', bg = '#ff8400', font = ('jetbrains mono bold', 30))
            licznik.pack(side = TOP) 
            messagebox.showinfo('Onion Clicker', 'ZAKUPIŁEŚ:\n\n- TIER (GOLD)\n\n\n\nOTRZYMAŁEŚ:\n\n- ZWROT CENY (4,000$)')
            
        else:
            message = messagebox.showinfo('Onion Clicker', 'NIE STAĆ CIEBIE NA ZAKUP TEGO PRZEDMIOTU!')           

def tierdiamond():
    global liczba
    global licznik
    global cebula

    file = open('Cache/data.txt', 'r+')
    fileread = file.read()

    if 'TIER : DIAMOND\n' in fileread:
        photo1 = Image.open('Cache/Images/oniondiamond.png')
        image1 = photo1.resize((250, 250))
        newimg1 = ImageTk.PhotoImage(image1)

        cebula.config(bg = '#ff8400', activebackground = '#ff8400', image = newimg1, borderwidth = 0)
        cebula.image = newimg1
    else:
        if int(liczba) >= 30000:
            file.write('TIER : DIAMOND\n')
            file.flush()
            photo1 = Image.open('Cache/Images/oniondiamond.png')
            image1 = photo1.resize((250, 250))
            newimg1 = ImageTk.PhotoImage(image1)

            cebula.config(bg = '#ff8400', activebackground = '#ff8400', image = newimg1, borderwidth = 0)
            cebula.image = newimg1

            liczba -= 30000
            licznik.pack_forget()
            licznik = Label(window, text = f'KASA:{liczba}$', bg = '#ff8400', font = ('jetbrains mono bold', 30))
            licznik.pack(side = TOP)
            liczba += 6000
            licznik.pack_forget()
            licznik = Label(window, text = f'KASA:{liczba}$', bg = '#ff8400', font = ('jetbrains mono bold', 30))
            licznik.pack(side = TOP)
            messagebox.showinfo('Onion Clicker', 'ZAKUPIŁEŚ:\n\n- TIER (DIAMOND)\n\n\n\nOTRZYMAŁEŚ:\n\n- ZWROT CENY (6,000$)')
            
        else:
            message = messagebox.showinfo('Onion Clicker', 'NIE STAĆ CIEBIE NA ZAKUP TEGO PRZEDMIOTU!')

def close():
    if messagebox.askyesno('Onion Clicker', 'Czy na pewno chcesz teraz wyjść?'):
        variablefile = open('Cache/num.txt', 'r+')
        variablefile.truncate()
        variablefile.write(str(liczba))
        window.destroy()

def closeevent(event):
	if event:
		if messagebox.askyesno('Onion Clicker', 'Czy na pewno chcesz teraz wyjść?'):
			variablefile = open('Cache/num.txt', 'r+')
			variablefile.truncate()
			variablefile.write(str(liczba))
			window.destroy()

def helpevent(event):
    global window
    if event:
        helproot = Toplevel(bg = '#ff8400')
        helproot.title('Onion Clicker')
        helproot.iconbitmap('Cache/Images/icon.ico')
        helproot.resizable(0,0)
        helproot.geometry('400x200')
        label = Label(helproot, text = 'Skróty klawiszowe:', font = ('jetbrains mono bold', 20, 'underline'), bg = '#ff8400')
        label.pack(side = TOP)
        shortcuts = Label(helproot, text = 'F1 - lista skrótów\nF7 - konsola\nF8 - zapis gry\nESC - wyjście', font = ('jetbrains mono bold', 17), bg = '#ff8400')
        shortcuts.pack()
        helproot.mainloop()
