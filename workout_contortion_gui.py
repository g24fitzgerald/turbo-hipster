from tkinter import*
from tkinter import ttk

def calculate_workout(*args):
    print('yes sir')

root = Tk()
root.title("Contortion Training Program")

#create mainframe, configure methods allow for adjustment when resizing
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column = 0, row = 0, sticky = (N,W,E,S))
mainframe.columnconfigure(0, weight = 1)
mainframe.rowconfigure(0, weight = 1)

#Injuries label
ttk.Label(mainframe, text='Mark if you are injured in either of the following areas, otherwise hit next to return your workout:').grid(column=1, row=1, sticky=W)

#legs button
ttk.Checkbutton(mainframe, text='legs').grid(column=1, row= 2, sticky= W)


#spine button
ttk.Checkbutton(mainframe, text='spine').grid(column=1, row= 3, sticky=W)


#Next button
ttk.Button(mainframe, text="Next", command=calculate_workout).grid(column=3, row=3, sticky=SE)


#children of mainframe adjust to resizing
for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

#hitting return key instead of 'next' button returns same result 
root.bind('<Return>', calculate_workout)

root.mainloop()
