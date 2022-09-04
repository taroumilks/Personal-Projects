from distutils.cmd import Command
from fileinput import filename
from os import link
from tkinter import *
from tkinter import font
from tkinter.filedialog import *
from tkinter.messagebox import showerror
import webbrowser

fileName = None

def newFile():
    global filename
    filename = "Untitled"
    text.delete(0.0, END)

def saveFile():
    global fileName
    filename = "Untitled"
    t = text.get(0.0, END)
    f = open(fileName, 'w')
    f.write(t)
    f.close()

def saveAs():
    global fileName
    f = asksaveasfile(mode = 'w', defaultextension=".txt")
    t = text.get(0.0, END)
    try:
        f.write(t.rstrip())
    except:
        showerror(title="Oops!", message="Unable to Save File....")
    
def openFile():
    global fileName
    f = askopenfile(mode='r')
    t = f.read()
    text.delete(0.0, END)
    text.insert(0.0, t)

def HelpGitHubLink():
    webbrowser.open("https://github.com/taroumilks")


def FontChangeBigger():
    global FontSize
    FontSize += 2
    Font_tuple = ("Times New Roman", FontSize)
    text.configure(font = Font_tuple )

def FontChangeSmaller():
    global FontSize
    FontSize -=2
    Font_tuple = ("Times New Roman", FontSize)
    text.configure(font = Font_tuple)

        
# Making the Text
root = Tk()
root.title("Python Text Editor")
root.minsize(width=400, height=400)
root.maxsize(width=800, height=800)
FontSize = 10
Font_tuple = ("Times New Roman", FontSize)
text = Text(root, width=400,height=400,font = Font_tuple)
text.pack()

#Making the Menu Bar
menubar = Menu(root)
filemenu = Menu(menubar)
helpmenu = Menu(menubar)
zoommenu = Menu(menubar)
filemenu.add_command(label="New File", command = newFile)
filemenu.add_command(label="Save File", command = saveFile)
filemenu.add_command(label="saveAs" , command = saveAs)
filemenu.add_command(label="openFile" , command = openFile)

zoommenu.add_command(label="FontChangeBigger", command = FontChangeBigger)
zoommenu.add_command(label="FontChangeSmaller", command = FontChangeSmaller)

helpmenu.add_command(label="Help", command=HelpGitHubLink)
filemenu.add_separator()
filemenu.add_command(label="Quit", command=root.quit)
menubar.add_cascade(label="File",menu =filemenu)
menubar.add_cascade(label="Help",menu=helpmenu)
menubar.add_cascade(label="Zoom",menu=zoommenu)

root.config(menu=menubar)
root.mainloop()