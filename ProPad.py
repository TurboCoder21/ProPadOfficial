# ProPad By Harshil Parikh
# An enhanced text Editor


# Import necessary imports
from tkinter import *
from tkinter import colorchooser
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os
import sqlite3


# Creates a new file
def newFile():
    global file
    window.title = ("Unsaved       ~ProPad")
    file = None
    TextArea.delete(1.0, END)

# Opens a file
def openFile():
    global file
    file = askopenfilename(defaultextension=".txt",
                           filetype=[
                               ("Text file", ".txt"),
                               ("HTML file", ".html"),
                               ("Python file", ".py"),
                               ("Java file", ".java"),
                               ("All files", ".*")
                           ]
                           )
    if file == "":
        file = None
    else:
        window.title(os.path.basename(file)+"       ~ProPad")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()


# Saves file
def saveFile():
    global file

    if file == None:
        file = asksaveasfilename(initialfile="Unitled.txt",
                                 filetype=[("Text file", ".txt"),
                                           ("All files", ".*")]
                                 )
        if file == "":
            file = None
        else:
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

            window.title(os.path.basename(file)+"       -ProPad")
    else:
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()


# Quits the program
def quitApp():
    window.destroy()

# Clears screen
def clear():
    TextArea.delete(1.0, END)

# Cut text
def cut():
    TextArea.event_generate(("<<Cut>>"))

# Copy text
def copy():
    TextArea.event_generate(("<<Copy>>"))

# Paste text
def paste():
    TextArea.event_generate(("<<Paste>>"))

# Changes font configuration ~ color,style and size
def change_font():

    def fcol():
        global col
        fco = colorchooser.askcolor()
        k = fco[1]
        conn = sqlite3.connect("themes.db")
        c = conn.cursor()
        c.execute(f" UPDATE theme SET f_col='{k}' WHERE table_name='root' ")
        c.execute("SELECT * FROM theme")
        values = c.fetchall()
        conn.commit()
        conn.close()
        for i in values:
            col = i[2]

        TextArea.config(fg=col)

    def fsize():

        def changeFontFinally():
            global font
            global size
            conn = sqlite3.connect("themes.db")
            c = conn.cursor()
            size = scale.get()
            c.execute(
                f" UPDATE theme SET f_size='{size}' WHERE table_name='root' ")
            c.execute("SELECT * FROM theme")
            values = c.fetchall()
            conn.commit()
            conn.close()
            for i in values:
                size = i[4]

            TextArea.config(font=(font, size))

        sizeWin = Toplevel(fontCostomizeWin)
        sizeWin.geometry("300x150")
        sizeWin.title("Font Size")
        sizeWin.iconbitmap("ProPadIcon.ico")

        scale = Scale(sizeWin, from_=10, to=70, length=500, orient=HORIZONTAL,
                      font="Cambria 15", tickinterval=10, troughcolor="#414540")
        scale.pack()

        btmSize = Button(sizeWin, text="CHANGE", command=changeFontFinally,
                         bg="#ffffff", font="Cambria 15 bold", padx=5, pady=5, bd=5, relief=SOLID)
        btmSize.pack(side=BOTTOM)

    def fstyle():

        def changeStyleFinally():
            global font
            global size
            conn = sqlite3.connect("themes.db")
            c = conn.cursor()
            font = entry.get()
            c.execute(
                f" UPDATE theme SET f_style='{font}' WHERE table_name='root' ")
            c.execute("SELECT * FROM theme")
            values = c.fetchall()
            conn.commit()
            conn.close()
            for i in values:
                font = i[3]

            TextArea.config(font=(font, size))

        styleWin = Toplevel(fontCostomizeWin)
        styleWin.geometry("400x180")
        styleWin.title("Font Style")
        styleWin.resizable(False, False)
        styleWin.iconbitmap("ProPadIcon.ico")

        sl = Label(styleWin, text="Please Enter The Font Name",
                   font="Cambria 20 bold", pady=10)
        sl.pack()

        entry = Entry(styleWin,
                      font=("Cambria", 19),
                      bg="#ffffff",
                      )
        entry.pack()

        btnStyle = Button(styleWin, text="CHANGE", font="Cambria 15 bold", bg="#ffffff",
                          padx=5, pady=5, bd=5, relief=SOLID, command=changeStyleFinally)
        btnStyle.pack(side=BOTTOM)

    fontCostomizeWin = Toplevel(window)
    fontCostomizeWin.geometry("300x228")
    fontCostomizeWin.title("Font")
    fontCostomizeWin.resizable(False, False)
    fontCostomizeWin.iconbitmap("ProPadIcon.ico")

    changeFontStyle = Button(fontCostomizeWin, text="Font Style ", bg="#ffffff",
                             font="Cambria 15 bold", padx=5, pady=5, bd=5, relief=SOLID, command=fstyle)
    changeFontStyle.place(x=90, y=5)

    changeFontColor = Button(fontCostomizeWin, text="Font Color", bg="#ffffff",
                             font="Cambria 15 bold", padx=5, pady=5, bd=5, relief=SOLID, command=fcol)
    changeFontColor.place(x=90, y=85)

    changeFontSize = Button(fontCostomizeWin, text=" Font Size  ", bg="#ffffff",
                            font="Cambria 15 bold", padx=5, pady=5, bd=5, relief=SOLID, command=fsize)
    changeFontSize.place(x=90, y=170)


# Changes background color
def change_theme():
    global background
    conn = sqlite3.connect("themes.db")
    c = conn.cursor()
    color = colorchooser.askcolor()
    hex = color[1]
    c.execute(f" UPDATE theme SET bg_col='{hex}' WHERE table_name='root' ")
    c.execute("SELECT * FROM theme")
    values = c.fetchall()
    for i in values:
        background = i[1]
    TextArea.config(bg=background)
    conn.commit()
    conn.close()


# About ProPad
def about():
    aboutWindow = Toplevel(window)
    aboutWindow.resizable(False, False)
    aboutWindow.geometry("500x150")
    aboutWindow.title("ProPad~ Enhanced Text Editor")
    aboutWindow.iconbitmap("ProPadIcon.ico")

    label = Label(aboutWindow, text="Welcome To ProPad",
                  font="Cambria 25 bold", bg="#f5f5f5", pady=2, compound='top')
    label.pack()

    label2 = Label(aboutWindow, text="An enhanced text editor",
                   font="Cambria 25 bold", bg="#f5f5f5", pady=2, compound='top')
    label2.pack()

    label3 = Label(aboutWindow, text="By~ Harshil Parikh",
                   font="Cambria 25 bold", bg="#f5f5f5")
    label3.pack()

    aboutWindow.config(background="#f5f5f5")


# Main Code
if __name__ == '__main__':

    conn = sqlite3.connect("themes.db")
    c = conn.cursor()

    c.execute("SELECT * FROM theme")

    values = c.fetchall()

    for i in values:
        font = i[3]
        size = i[4]
        col = i[2]
        background = i[1]

    window = Tk()
    window.title("Unsaved       ~ProPad (Version-2.0)")
    window.geometry("800x600")

    window.iconbitmap("ProPadIcon.ico")

    conn.commit()
    conn.close()

    TextArea = Text(window, font=(font, size), bg=background, fg=col)
    file = None
    TextArea.pack(expand=True, fill=BOTH)

    MenuBar = Menu(window)
    FileMenu = Menu(MenuBar, tearoff=0, font="Cambria 15", bg="#d9dbd9")

    FileMenu.add_command(label="New", command=newFile)
    FileMenu.add_command(label="Open", command=openFile)
    FileMenu.add_command(label="Save", command=saveFile)
    FileMenu.add_separator()
    FileMenu.add_command(label="Exit", command=quitApp)
    MenuBar.add_cascade(label="File", menu=FileMenu)

    EditMenu = Menu(MenuBar, tearoff=0, font="Cambria 15", bg="#d9dbd9")
    EditMenu.add_command(label="Clear", command=clear)
    EditMenu.add_command(label="Cut", command=cut)
    EditMenu.add_command(label="Copy", command=copy)
    EditMenu.add_command(label="Paste", command=paste)
    MenuBar.add_cascade(label="Edit", menu=EditMenu)

    CustomizeMenu = Menu(MenuBar, tearoff=0, font="Cambria 15", bg="#d9dbd9")
    CustomizeMenu.add_command(label="Font", command=change_font)
    CustomizeMenu.add_command(label="Theme", command=change_theme)
    MenuBar.add_cascade(label="Customize", menu=CustomizeMenu)

    HelpMenu = Menu(MenuBar, tearoff=0, font="Cambria 15", bg="#d9dbd9")
    HelpMenu.add_command(label="About ProPad", command=about)
    MenuBar.add_cascade(label="About", menu=HelpMenu)

    window.config(menu=MenuBar)

    Scroll = Scrollbar(TextArea)
    Scroll.pack(side=RIGHT, fill=Y)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)

    window.mainloop()
