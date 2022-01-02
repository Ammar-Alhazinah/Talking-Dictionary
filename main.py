from tkinter import *

# To Create a window using tkinter we need to make an object
root = Tk()

# give size to window and fix position
root.geometry('1000x626+100+30')

#change title of window
root.title('Talking Dictionary created by Ammar Alhazinah')

# remove maximize and minimize window
root.resizable(0, 0)


# to keep window shown we use mainloop function
root.mainloop()
