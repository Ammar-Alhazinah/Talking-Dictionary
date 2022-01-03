import tkinter
from tkinter import *
import json
from difflib import get_close_matches
from tkinter import messagebox


# --------------------------------  Functionality Part  --------------------------------

def search():
    textArea.delete(0.0, END)
    data = json.load(open('data.json'))
    word = enterWordEntry.get()
    word = word.lower()
    if word in data:
        meaning = data[word]
        for item in meaning:
            textArea.insert(END, u'\u2022' + item + "\n\n")
    elif len(get_close_matches(word, data.keys())) > 0:
        closeMatch = get_close_matches(word, data.keys())[0]
        if messagebox.askyesno('Confirm', f'Did you mean {closeMatch} instead?'):
            enterWordEntry.delete(0, END)
            textArea.delete(0.0, END)
            enterWordEntry.insert(END, closeMatch)
            meaning = data[closeMatch]
            for item in meaning:
                textArea.insert(END, u'\u2022' + item + "\n\n")
        else:
            messagebox.showerror('Error', 'The Word Does Not Exist, Please Double Check It.')
            enterWordEntry.delete(0, END)
    else:
        messagebox.showinfo('Information', 'The Word does not exist.')
        enterWordEntry.delete(0, END)


# --------------------------------  GUI Part  --------------------------------
# To Create a window using tkinter we need to make an object
root = Tk()

# give size to window and fix position
root.geometry('1000x626+100+30')

# change title of window
root.title('Talking Dictionary created by Ammar Alhazinah')

# remove maximize and minimize window
root.resizable(0, 0)

# add background image to window
bgImage = PhotoImage(file="images/bg123.png")
bgLabel = Label(root, image=bgImage)
bgLabel.place(x=0, y=0)
# ---------------------------------

# Create Enter Word Label
enterWordLabel = Label(root, text="Enter Word", font=('castellar', 30, 'bold',), foreground='red4',
                       background='whitesmoke')
enterWordLabel.place(x=530, y=25)

# Create Entry field
enterWordEntry = Entry(root, font=('arial', 22, 'bold'), justify=CENTER, border=4, relief=RIDGE)
enterWordEntry.place(x=530, y=80)

# Create Search Button
searchImg = PhotoImage(file='images/search.png')
searchBtn = Button(root, text="Search ", background='whitesmoke', border=1.25, height=1, width=7, cursor="hand2",
                   activebackground="whitesmoke", command=search)
searchBtn.place(x=620, y=150)

# Create mic Button
micImg = PhotoImage(file='images/mic.png')
micBtn = Button(root, text='Click to Speak', background='whitesmoke', border=1.25, cursor='hand2',
                activebackground='whitesmoke', height=1)
micBtn.place(x=700, y=150)

# Create Meaning Label
meaningLabel = Label(root, text="Meaning", font=('castellar', 30, 'bold',), foreground='red4', background='whitesmoke')
meaningLabel.place(x=580, y=230)

# Add Text Area to show the result
textArea = Text(root, width=34, height=8, font=('arial', 18, 'bold'), border=4, relief=RIDGE)
textArea.place(x=480, y=300)

# Create mic Button
searchImg = PhotoImage(file='images/search.png')
searchBtn = Button(root, text="Search ", background='whitesmoke', border=1.25, height=1, width=7, cursor="hand2",
                   activebackground="whitesmoke")
searchBtn.place(x=550, y=580)

# Create Clear Button
searchImg = PhotoImage(file='images/clear.png')
searchBtn = Button(root, text="Clear ", background='whitesmoke', border=1.25, height=1, width=7, cursor="hand2",
                   activebackground="whitesmoke")
searchBtn.place(x=680, y=580)

# Create Exit Button
searchImg = PhotoImage(file='images/exit.png')
searchBtn = Button(root, text="Exit ", background='whitesmoke', border=1.25, height=1, width=7, cursor="hand2",
                   activebackground="whitesmoke")
searchBtn.place(x=810, y=580)


# Define enter function
def enter_function(event):
    search()
    # searchBtn.invoke


# Bind your window with keyboard
root.bind('<Return>', enter_function)

# to keep window shown we use mainloop function
root.mainloop()
