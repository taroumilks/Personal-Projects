"""This is a Text Editor. 
Credits to: https://www.youtube.com/watch?v=xqDonHEYPgA&t=265s (Zach King) for the base code.
I have added extra features to make it more like a Text Editor!
-Peter Peng"""

#September 3rd, 2022 - Added a Help button to send to my Github Link
#Added a place to change Font Size
#Added new bars to Menu Bar

#September 4th, 2022 - Added a Date function to print the Date into the Text
#Added a Scroll Bar for Convenience
#Made "enlarged window" take up the entire screen


from distutils.cmd import Command
from fileinput import filename
from msilib.schema import Font
from os import link
from tkinter import *
from tkinter import font
from tkinter.filedialog import *
from tkinter.messagebox import showerror
from typing import Container
import webbrowser
from datetime import date 
import tkinter.messagebox
import tkinter.font

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
    Font_tuple = (FontType, FontSize)
    text.configure(font = Font_tuple )

def FontChangeSmaller():
    global FontSize
    FontSize -=2
    Font_tuple = (FontType, FontSize)
    text.configure(font = Font_tuple)


def DateAndTime():
    today = date.today()
    text.insert(END, today)

def AboutUs():
    tkinter.messagebox.showinfo( "About Us", """Hello! I am (Currently) an Undergraduate Freshman at the University of Texas at Austin! \n 
I am currently an Economics Major that is trying to also major in Computer Science, and this my VERY FIRST ONE! A basic text editor with the help of tkinter \n
I learned the base code from Zach King on youtube, and added some more features to test my knowledge! I hope you enjoyed <3""")


# Making the Text
root = Tk()
root.title("Python Text Editor")
root.minsize(width=400, height=400)
root.maxsize(width=1980, height=1500)
root.state('zoomed')
FontSize = 12
FontType = "Times New Roman"
Font_tuple = (FontType, FontSize)

#Scroll Bar added for convenience 
scrollbar = Scrollbar(root)
scrollbar.pack( side = RIGHT, fill = Y )

text = Text(root, width=400,height=400,yscrollcommand = scrollbar.set, font = Font_tuple, undo = True)
text.pack()
scrollbar.config( command = text.yview )

#Making the Menu Bar
menubar = Menu(root)
filemenu = Menu(menubar)
helpmenu = Menu(menubar)
fontmenu = Menu(menubar)
typemenu = Menu(fontmenu)

#FileMenu - New File, Save File, SaveAs, Open File
filemenu.add_command(label="New File", command = newFile)
filemenu.add_command(label="Save File", command = saveFile)
filemenu.add_command(label="Save As" , command = saveAs)
filemenu.add_command(label="Open File" , command = openFile)
filemenu.add_separator()
filemenu.add_command(label="Quit", command=root.quit)

#Font Menu - Changing the Font Size
fontmenu.add_command(label="Increase Font Size", command = FontChangeBigger)
fontmenu.add_command(label="Decrease Font Size", command = FontChangeSmaller)
fontmenu.add_command(label="Date and Time", command = DateAndTime)




#Help Menu - Click it to go to Github Link
helpmenu.add_command(label="Help", command=HelpGitHubLink)
helpmenu.add_command(label="About Me!" , command = AboutUs)

menubar.add_cascade(label="File",menu =filemenu)
menubar.add_cascade(label="Font",menu=fontmenu)
menubar.add_cascade(label="Help",menu=helpmenu)
fontmenu.add_cascade(label = "Font Type", menu = typemenu)

root.config(menu=menubar)
root.mainloop()