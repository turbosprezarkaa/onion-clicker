def reset():
    global root
    global file2
    file1 = open('Cache/data.txt', 'r+')
    file2 = open('Cache/num.txt', 'r+')
    file3 = open('Cache/inf.txt', 'r+')
    file1.truncate()
    file2.truncate()
    file3.truncate()
    file2.write('0')
    file2.write('6000')
    file2.flush()
    file3.flush()
    messagebox.showinfo('Onion Clicker','ZRESETOWANO WSZYSTKIE INFORMACJE\n\nWŁĄCZ GRE PONOWNIE')
    root.destroy()

def endgame():
    global root
    global liczba

    liczba -= 1
    variablefile = open('Cache/num.txt', 'r+')
    variablefile.truncate()
    variablefile.write(str(liczba))
    root.destroy()

def kasa():
    global root
    global liczba
    global licznik

    liczba += 1
    licznik.pack_forget()
    licznik = Label(window, text = f'KASA:{liczba}$', bg = '#ff8400', font = ('jetbrains mono bold', 30))
    licznik.pack(side = TOP)

    if liczba >= 10:
        window.destroy()
        root = Tk()
        root.title('Onion Clicker')
        root.geometry('620x400')
        root.config(bg = '#ff8400')
        # root.resizable(0, 0)
        root.iconbitmap('Cache/Images/icon.ico')
        images = Image.open('Cache/Images/onion.png')
        newimgs = ImageTk.PhotoImage(images)
        onion = Label(root, image = newimgs)
        onion.pack(side = LEFT)
        label1 = Label(root, text = 'OTO KONIEC GRY!', bg = '#ff8400', font = ('jetbrains mono bold', 30, 'underline'), anchor = CENTER)
        label1.pack(side = TOP)
        label2 = Label(root, text = "\nDZIĘKI ZA ZAGRANIE W\nONION CLICKERA! <3", bg = '#ff8400', font = ('jetbrains mono bold', 25), anchor = CENTER)
        label2.pack()
        button = Button(root, text = '         RESET (opcjonalne)         ', font = ('jetbrains mono bold', 20), bg = '#ff8400', activebackground = '#ff8400', height = 1, width = 30, relief = SOLID, command = reset)
        button.pack(expand = True)
        author = Label(root, text = 'made by @turbosprezarkaa', font = ('jetbrains mono bold', 15), bg = '#ff8400')
        author.pack(side = BOTTOM)
        root.protocol('WM_DELETE_WINDOW', endgame)

def kasax2():
    global root
    global liczba
    global licznik
    global variablefile

    liczba += 2
    licznik.pack_forget()
    licznik = Label(window, text = f'KASA:{liczba}$', bg = '#ff8400', font = ('jetbrains mono bold', 30))
    licznik.pack(side = TOP)

    if liczba >= 100000:
        window.destroy()
        root = Tk()
        root.title('Onion Clicker')
        root.geometry('620x500')
        root.config(bg = '#ff8400')
        root.resizable(0, 0)
        root.iconbitmap('Cache/Images/icon.ico')
        label1 = Label(root, text = 'OTO KONIEC GRY!', bg = '#ff8400', font = ('jetbrains mono bold', 35, 'underline'), anchor = CENTER)
        label1.pack(side = TOP)
        label2 = Label(root, text = "no chyba, że dodam jakieś\nupdate'y w przyszłości\n¯\_(ツ)_/¯\n\nDZIĘKI ZA ZAGRANIE W\nONION CLICKERA! <3", bg = '#ff8400', font = ('jetbrains mono bold', 25), anchor = CENTER)
        label2.pack()
        button = Button(root, text = '         RESET (opcjonalne)         ', font = ('jetbrains mono bold', 20), bg = '#ff8400', activebackground = '#ff8400', height = 1, relief = SOLID, command = reset)
        button.pack(expand = True)
        author = Label(root, text = 'made by @turbosprezarkaa', font = ('jetbrains mono bold', 15), bg = '#ff8400')
        author.pack(side = BOTTOM)
        root.protocol('WM_DELETE_WINDOW', endgame)

def kasax3():
    global root
    global liczba
    global licznik
    global variablefile

    liczba += 3
    licznik.pack_forget()
    licznik = Label(window, text = f'KASA:{liczba}$', bg = '#ff8400', font = ('jetbrains mono bold', 30))
    licznik.pack(side = TOP)

    if liczba >= 100000:
        window.destroy()
        root = Tk()
        root.title('Onion Clicker')
        root.geometry('620x500')
        root.config(bg = '#ff8400')
        root.resizable(0, 0)
        root.iconbitmap('Cache/Images/icon.ico')
        label1 = Label(root, text = 'OTO KONIEC GRY!', bg = '#ff8400', font = ('jetbrains mono bold', 35, 'underline'), anchor = CENTER)
        label1.pack(side = TOP)
        label2 = Label(root, text = "no chyba, że dodam jakieś\nupdate'y w przyszłości\n¯\_(ツ)_/¯\n\nDZIĘKI ZA ZAGRANIE W\nONION CLICKERA! <3", bg = '#ff8400', font = ('jetbrains mono bold', 25), anchor = CENTER)
        label2.pack()
        button = Button(root, text = '         RESET (opcjonalne)         ', font = ('jetbrains mono bold', 20), bg = '#ff8400', activebackground = '#ff8400', height = 1, relief = SOLID, command = reset)
        button.pack(expand = True)
        author = Label(root, text = 'made by @turbosprezarkaa', font = ('jetbrains mono bold', 15), bg = '#ff8400')
        author.pack(side = BOTTOM)
        root.protocol('WM_DELETE_WINDOW', endgame)

def kasax5():
    global root
    global liczba
    global licznik
    global variablefile

    liczba += 5
    licznik.pack_forget()
    licznik = Label(window, text = f'KASA:{liczba}$', bg = '#ff8400', font = ('jetbrains mono bold', 30))
    licznik.pack(side = TOP)

    if liczba >= 100000:
        window.destroy()
        root = Tk()
        root.title('Onion Clicker')
        root.geometry('620x500')
        root.config(bg = '#ff8400')
        root.resizable(0, 0)
        root.iconbitmap('Cache/Images/icon.ico')
        label1 = Label(root, text = 'OTO KONIEC GRY!', bg = '#ff8400', font = ('jetbrains mono bold', 35, 'underline'), anchor = CENTER)
        label1.pack(side = TOP)
        label2 = Label(root, text = "no chyba, że dodam jakieś\nupdate'y w przyszłości\n¯\_(ツ)_/¯\n\nDZIĘKI ZA ZAGRANIE W\nONION CLICKERA! <3", bg = '#ff8400', font = ('jetbrains mono bold', 25), anchor = CENTER)
        label2.pack()
        button = Button(root, text = '         RESET (opcjonalne)         ', font = ('jetbrains mono bold', 20), bg = '#ff8400', activebackground = '#ff8400', height = 1, relief = SOLID, command = reset)
        button.pack(expand = True)
        author = Label(root, text = 'made by @turbosprezarkaa', font = ('jetbrains mono bold', 15), bg = '#ff8400')
        author.pack(side = BOTTOM)
        root.protocol('WM_DELETE_WINDOW', endgame)
