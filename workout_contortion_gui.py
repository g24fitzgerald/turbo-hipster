from tkinter import*
from tkinter import ttk

def calculate_workout(*args):
    if bla bla bla 

root = Tk()
root.title("Contortion Training Program")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column = 0, row = 0, sticky = (N,W,E,S))
mainframe.columnconfigure(0, weight = 1)
mainframe.rowconfigure(0, weight = 1)

ttk.Button(mainframe, text="Next", command=calculate_workout).grid(column=3, row=3, sticky=W)


for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

root.bind('<Return>', calculate_workout)

root.mainloop()
