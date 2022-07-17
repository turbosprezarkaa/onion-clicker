hpfile = open('Cache/inf.txt', 'r+')
hp = int(hpfile.read())

def func1():
    global root
    global hp
    global hpfile
    global hpbar
    root.grab_set()
    root1 = Toplevel(root)
    root1.geometry('800x800')
    root1.iconbitmap('Cache/Images/icon.ico')
    root1.resizable(0,0)
    root1.config(bg = '#ff8400')
    root1.grab_set()

    def hpminus():
        global hp
        global hpfile
        global hpbar
        hp -= 1
        hpbar.pack_forget()
        hpbar = Label(root1, text = f'{hp} HP', font = ('jetbrains mono bold', 25), width = 15, bg = '#ff0000', bd = 3, relief = SOLID)
        hpbar.pack()
        hpfile.truncate()
        hpfile = open('Cache/inf.txt', 'r+')
        hpfile.write(str(hp))
        hpfile.flush()

    photos = Image.open('Cache/Images/onion.png')
    image = photos.resize((300, 300))
    newimg = ImageTk.PhotoImage(image)

    void1 = Label(root1, text = '\n', bg = '#ff8400')
    void1.pack()

    onion1 = Button(root1, image = newimg, activebackground = '#ff8400', bg = '#ff8400', relief = FLAT, borderwidth = 0, command = hpminus)
    onion1.image = newimg
    onion1.pack()

    void2 = Label(root1, text = '\n', bg = '#ff8400')
    void2.pack()  

    hpbar = Label(root1, text = f'{hp} HP', font = ('jetbrains mono bold', 25), width = 15, bg = '#ff0000', bd = 3, relief = SOLID)
    hpbar.pack()

    root1.mainloop()

def closemsg1():
    global root
    global root2
    root2.destroy()
    exec(open('mgames.py', encoding = 'utf-8').read(), globals())
    mgameswindow()

def func2():
    global root
    global root2
    global licznik
    global liczba
    
    root.destroy()

    root2 = Tk()
    root2.title('Onion Clicker')
    root2.geometry('800x750')
    root2.iconbitmap('Cache/Images/icon.ico')
    root2.resizable(0,0)
    root2.config(bg = '#ff8400')

    photos = Image.open('Cache/Images/drop.png')
    image = photos.resize((800, 400))
    newimg = ImageTk.PhotoImage(image)

    licznik = Label(root2, text = f'KASA:{liczba}$', bg = '#ff8400', font = ('jetbrains mono bold', 30))
    licznik.pack(side = TOP)

    void1 = Label(root2, text = '\n\n', bg = '#ff8400')
    void1.pack()
    
    def opencase():
        global root2
        global case
        global button
        global liczba
        global licznik

        drop = ['SKIN - ONION BRONZE','SKIN - ONION SILVER','SKIN - ONION GOLD','SKIN - ONION DIAMOND','ULEPSZENIE - KASA x2','ULEPSZENIE - KASA x3','ULEPSZENIE - KASA x5','none']
        dropchoice = random.choice(drop)
            
        if int(liczba) >= 4000:
            liczba -= 4000
            variablefile = open('Cache/num.txt', 'r+')
            variablefile.truncate()
            variablefile.write(str(liczba))
            variablefile.flush()

            # licznik.pack_forget()
            licznik.config(text = f'KASA:{liczba}$')
            # licznik.pack(side = TOP)

            def sleep():
                global case
                global button
                if dropchoice == 'none':
                    label.config(text = f'PUSTA SKRZYNIA :(')
                    case.after(3000, lambda:case.destroy())
                else:
                    label.config(text = f'WYLOSOWAŁEŚ:\n{dropchoice}')
                    case.after(3000, lambda:case.destroy())

                    file = open('Cache/data.txt', 'r+')
                    fileread = file.read()

                    if dropchoice == 'SKIN - ONION BRONZE':
                        if 'TIER : BRONZE\n' in fileread:
                            pass
                        else:
                            file.write('TIER : BRONZE\n')

                    if dropchoice == 'SKIN - ONION SILVER':
                        if 'TIER : SILVER\n' in fileread:
                            pass
                        else:
                            file.write('TIER : SILVER\n')

                    if dropchoice == 'SKIN - ONION GOLD':
                        if 'TIER : GOLD\n' in fileread:
                            pass
                        else:
                            file.write('TIER : GOLD\n')

                    if dropchoice == 'SKIN - ONION DIAMOND':
                        if 'TIER : DIAMOND\n' in fileread:
                            pass
                        else:
                            file.write('TIER : DIAMOND\n')

                    if dropchoice == 'ULEPSZENIE - KASA x2':
                        if 'MONEY : x2\n' in fileread:
                            pass
                        else:
                            file.write('MONEY : x2\n')

                    if dropchoice == 'ULEPSZENIE - KASA x3':
                        if 'MONEY : x3\n' in fileread:
                            pass
                        else:
                            file.write('MONEY : x3\n')

                    if dropchoice == 'ULEPSZENIE - KASA x5':
                        if 'MONEY : x5\n' in fileread:
                            pass
                        else:
                            file.write('MONEY : x5\n')

            case = Toplevel(root2)
            case.title('Onion Clicker')
            case.iconbitmap('Cache/Images/icon.ico')
            case.geometry('500x200')
            case.resizable(0, 0)
            case.config(bg = '#ff8400')
            case.grab_set()
            label = Label(case, text = 'LOSOWANIE PRZEDMIOTU...', bg = '#ff8400', font = ('jetbrains mono bold', 25))
            label.pack(expand = True)

            def quit():
                pass
            
            case.after(5000, lambda:sleep())
            case.protocol('WM_DELETE_WINDOW', quit)
            case.mainloop()
        else:
            message = messagebox.showinfo('Onion Clicker', 'NIE STAĆ CIEBIE NA ZAKUP TEGO PRZEDMIOTU!')

    button = Button(root2, 
    text = 'OTWÓRZ SKRZYNIĘ (4000$)', 
    bg = '#ff8400', 
    activebackground = '#ff8400',
    font = ('jetbrains mono bold', 25), 
    relief = SOLID, bd = 2, command = opencase)
    button.pack()

    void2 = Label(root2, text = '\n\n\n\n\n\n\n', bg = '#ff8400')
    void2.pack()

    hint = Label(root2, text = 'PRZEDMIOTY W SKRZYNI:\n', bg = '#ff8400', font = ('jetbrains mono bold', 17))
    hint.pack()

    label = Label(root2, bg = '#ff8400', image = newimg)
    label.image = newimg
    label.pack()

    root2.protocol('WM_DELETE_WINDOW', closemsg1)
    root2.mainloop()

def func3():
    global root
    global text1
    global label1
    global label2
    global button1

    def lv2():
        global text1
        global label1
        global label2
        global button1

        get = text1.get(1.0, END)

        if 'sqrt' in get:
            print('1')
        else:
            messagebox.showinfo('Onion Clicker', 'ZOSTAŁ WPISANY ZŁY KOD')

    def lv1():
        global text1
        global label1
        global label2
        global button1

        photos = Image.open('Cache/Images/code2.png')
        image = photos.resize((750, 500))
        newimg = ImageTk.PhotoImage(image)
        
        get = text1.get(1.0, END)

        if 'while(i<=10)' or 'while(i<11)' in get:
            text1.delete(1.0, END)
            label1.pack_forget()
            label1 = Label(root3, image = newimg)
            label1.image = newimg
            label1.pack(side = TOP)
            label2.config(text = 'Jakiej funkcji trzeba użyć, aby został zapisany\npierwiastek ze zmiennej value')
            button1.config(command = lv2)

        else:
            messagebox.showinfo('Onion Clicker', 'ZOSTAŁ WPISANY ZŁY KOD')

    root.grab_set()
    root3 = Toplevel(root)
    root3.geometry('800x800')
    root3.iconbitmap('Cache/Images/icon.ico')
    root3.resizable(0,0)
    root3.config(bg = '#ff8400')
    root3.grab_set()

    photos = Image.open('Cache/Images/code1.png')
    image = photos.resize((750, 500))
    newimg = ImageTk.PhotoImage(image)

    label2 = Label(root3, text = 'Jak należy uzupełnić powyższy kod,\naby zostało wypisane 10 kolejnych liczb?', bg = '#ff8400', font = ('jetbrains mono bold', 19))
    label2.pack(side = TOP)

    label1 = Label(root3, image = newimg, relief = SOLID, bd = 2)
    label1.image = photos
    label1.pack(side = TOP)

    void1 = Label(root3, bg = '#ff8400', text = '\n')
    void1.pack(side = BOTTOM)

    button1 = Button(root3, bg = '#ff8400', text = 'ZATWIERDŹ', font = ('jetbrains mono bold', 20), activebackground = '#ff8400', width=10, height=1, relief = SOLID, command = lv1)
    button1.pack(side = BOTTOM)

    void2 = Label(root3, bg = '#ff8400', text = '\n')
    void2.pack(side = BOTTOM)

    text1 = Text(root3, wrap = None, bg = '#bd6200', insertbackground = 'white', fg = 'white', bd = 2, relief = SOLID, height = 1, width = 30, font = ('jetbrains mono bold', 25))
    text1.pack(side = BOTTOM)

    root3.mainloop()

def closemsg2():
    global root
    global window
    global liczba
    global licznik
    root.destroy()
    exec(open('main.py', encoding ='utf-8').read(), globals())

def mgames():
    global root
    global window
    global cebula
    global liczba
    global variablefile
    
    variablefile.truncate()
    variablefile = open('Cache/num.txt', 'r+')
    variablefile.write(str(liczba))
    variablefile.flush()

    window.destroy()

    root = Tk()
    root.geometry('700x720')
    root.title('Onion Clicker')
    root.iconbitmap('Cache/Images/icon.ico')
    root.resizable(0, 0)
    root.config(bg = '#ff8400')
    root.grab_set()

    label = Label(root, text = 'M I N I G R Y :', bg = '#ff8400', font = ('jetbrains mono bold', 30))
    label.pack(side = TOP)

    void = Label(root, bg = '#ff8400')
    void.pack()

    button1 = Button(root, text = '#1\n"POKONAJ\nZŁĄ CEBULĘ"', font = ('jetbrains mono bold', 17), height = 4, width = 15, bg = '#ff8400', activebackground = '#ff8400', activeforeground = 'black', relief = SOLID, bd = 2, command = func1)
    button1.pack()

    void = Label(root, bg = '#ff8400')
    void.pack()

    button2 = Button(root, text = '#2\nOTWIERANIE\nSKRZYŃ', font = ('jetbrains mono bold', 17), height = 4, width = 15, bg = '#ff8400', activebackground = '#ff8400', activeforeground = 'black', relief = SOLID, bd = 2, command = func2)
    button2.pack()

    void = Label(root, bg = '#ff8400')
    void.pack()

    button3 = Button(root, text = '#3\nUZUPEŁNIJ\nKOD', font = ('jetbrains mono bold', 17), height = 4, width = 15, bg = '#ff8400', activebackground = '#ff8400', activeforeground = 'black', relief = SOLID, bd = 2, command = func3)
    button3.pack()

    void = Label(root, text = '\n\n\n', bg = '#ff8400')
    void.pack()

    photo4 = Image.open('Cache/Images/wroc.png')
    image4 = photo4.resize((120, 120))
    newimg4 = ImageTk.PhotoImage(image4)

    rbutton = Button(root, image = newimg4, bg = '#ff8400', activebackground = '#ff8400', bd = 0, relief = FLAT, command = closemsg2)
    rbutton.image = newimg4
    rbutton.pack()

    root.protocol('WM_DELETE_WINDOW', closemsg2)
    root.mainloop()

def mgameswindow():
    global root
    global window
    global cebula
    global liczba

    root = Tk()
    root.geometry('700x720')
    root.title('Onion Clicker')
    root.iconbitmap('Cache/Images/icon.ico')
    root.resizable(0, 0)
    root.config(bg = '#ff8400')
    root.grab_set()

    label = Label(root, text = 'M I N I G R Y :', bg = '#ff8400', font = ('jetbrains mono bold', 30))
    label.pack(side = TOP)

    void = Label(root, bg = '#ff8400')
    void.pack()

    button1 = Button(root, text = '#1\n"POKONAJ\nZŁĄ CEBULĘ"', font = ('jetbrains mono bold', 17), height = 4, width = 15, bg = '#ff8400', activebackground = '#ff8400', activeforeground = 'black', relief = SOLID, bd = 2, command = func1)
    button1.pack()

    void = Label(root, bg = '#ff8400')
    void.pack()

    button2 = Button(root, text = '#2\nOTWIERANIE\nSKRZYŃ', font = ('jetbrains mono bold', 17), height = 4, width = 15, bg = '#ff8400', activebackground = '#ff8400', activeforeground = 'black', relief = SOLID, bd = 2, command = func2)
    button2.pack()

    void = Label(root, bg = '#ff8400')
    void.pack()

    button3 = Button(root, text = '#3\nUZUPEŁNIJ\nKOD', font = ('jetbrains mono bold', 17), height = 4, width = 15, bg = '#ff8400', activebackground = '#ff8400', activeforeground = 'black', relief = SOLID, bd = 2, command = func3)
    button3.pack()

    void = Label(root, text = '\n\n\n', bg = '#ff8400')
    void.pack()

    photo4 = Image.open('Cache/Images/wroc.png')
    image4 = photo4.resize((120, 120))
    newimg4 = ImageTk.PhotoImage(image4)

    rbutton = Button(root, image = newimg4, bg = '#ff8400', activebackground = '#ff8400', bd = 0, relief = FLAT, command = closemsg2)
    rbutton.image = newimg4
    rbutton.pack()

    root.protocol('WM_DELETE_WINDOW', closemsg2)
    root.mainloop()
