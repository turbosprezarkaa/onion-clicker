def reset():
    global root
    global file2
    file1 = open('Cache/data.txt', 'r+')
    file2 = open('Cache/num.txt', 'r+')
    file1.truncate()
    file2.truncate()
    file1.flush()
    file2.flush()
    file2.write('0')
    file1.flush()
    file2.flush()
    webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
    messagebox.showinfo('Onion Clicker','ZRESETOWANO WSZYSTKIE DANE GRACZA\n\nWŁĄCZ GRE PONOWNIE')
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
        root.resizable(0, 0)
        root.iconbitmap('Cache/Images/icon.ico')
        label1 = Label(root, text = 'KONIEC GRY!', bg = '#ff8400', font = ('jetbrains mono bold', 30, 'underline'), anchor = CENTER)
        label1.pack(side = TOP)
        label2 = Label(root, text = "\nDZIĘKI ZA ZAGRANIE W\nONION CLICKERA! <3", bg = '#ff8400', font = ('jetbrains mono bold', 25), anchor = CENTER)
        label2.pack()
        button = Button(root, text = '         RESET (OPCJONALNE)         ', font = ('jetbrains mono bold', 20), bg = '#ff8400', activebackground = '#ff8400', height = 1, width = 30, relief = SOLID, command = reset)
        button.pack(expand = True)
        author = Label(root, text = 'game made by turbosprezarkaa', font = ('jetbrains mono bold', 15), bg = '#ff8400')
        author.pack(side = BOTTOM)
        root.mainloop()

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
        root.geometry('620x400')
        root.config(bg = '#ff8400')
        root.resizable(0, 0)
        root.iconbitmap('Cache/Images/icon.ico')
        label1 = Label(root, text = 'KONIEC GRY!', bg = '#ff8400', font = ('jetbrains mono bold', 30, 'underline'), anchor = CENTER)
        label1.pack(side = TOP)
        label2 = Label(root, text = "\nDZIĘKI ZA ZAGRANIE W\nONION CLICKERA! <3", bg = '#ff8400', font = ('jetbrains mono bold', 25), anchor = CENTER)
        label2.pack()
        button = Button(root, text = '         RESET (OPCJONALNE)         ', font = ('jetbrains mono bold', 20), bg = '#ff8400', activebackground = '#ff8400', height = 1, width = 30, relief = SOLID, command = reset)
        button.pack(expand = True)
        author = Label(root, text = 'game made by turbosprezarkaa', font = ('jetbrains mono bold', 15), bg = '#ff8400')
        author.pack(side = BOTTOM)
        root.mainloop()

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
        root.geometry('620x400')
        root.config(bg = '#ff8400')
        root.resizable(0, 0)
        root.iconbitmap('Cache/Images/icon.ico')
        label1 = Label(root, text = 'KONIEC GRY!', bg = '#ff8400', font = ('jetbrains mono bold', 30, 'underline'), anchor = CENTER)
        label1.pack(side = TOP)
        label2 = Label(root, text = "\nDZIĘKI ZA ZAGRANIE W\nONION CLICKERA! <3", bg = '#ff8400', font = ('jetbrains mono bold', 25), anchor = CENTER)
        label2.pack()
        button = Button(root, text = '         RESET (OPCJONALNE)         ', font = ('jetbrains mono bold', 20), bg = '#ff8400', activebackground = '#ff8400', height = 1, width = 30, relief = SOLID, command = reset)
        button.pack(expand = True)
        author = Label(root, text = 'game made by turbosprezarkaa', font = ('jetbrains mono bold', 15), bg = '#ff8400')
        author.pack(side = BOTTOM)
        root.mainloop()

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
        root.geometry('620x400')
        root.config(bg = '#ff8400')
        root.resizable(0, 0)
        root.iconbitmap('Cache/Images/icon.ico')
        label1 = Label(root, text = 'KONIEC GRY!', bg = '#ff8400', font = ('jetbrains mono bold', 30, 'underline'), anchor = CENTER)
        label1.pack(side = TOP)
        label2 = Label(root, text = "\nDZIĘKI ZA ZAGRANIE W\nONION CLICKERA! <3", bg = '#ff8400', font = ('jetbrains mono bold', 25), anchor = CENTER)
        label2.pack()
        button = Button(root, text = '         RESET (OPCJONALNE)         ', font = ('jetbrains mono bold', 20), bg = '#ff8400', activebackground = '#ff8400', height = 1, width = 30, relief = SOLID, command = reset)
        button.pack(expand = True)
        author = Label(root, text = 'game made by turbosprezarkaa', font = ('jetbrains mono bold', 15), bg = '#ff8400')
        author.pack(side = BOTTOM)
        root.mainloop()