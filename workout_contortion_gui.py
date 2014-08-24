from tkinter import*
from tkinter import ttk
import tkinter.messagebox 

w1= 'hey'
w2= 'hoe'
w3= 'now'
w4= 'go'
workout= None

messagebox.showwarning("show warning", "this workout is not intended for those without previous training. Under no circumstances should these exercises be performed without first having recieved proper training from an instructor. This is not a tutorial on becoming a contortionist, rather this is a workout generator for contortionists seeking to vary their personal training. By clicking 'ok' you assume responsibility for any and all injuries aquired while following this program.")

checkvar1= IntVar()
checkvar2= IntVar()

def calculate_workout(*args):
    
    #4 cases 
    if checkvar1 == 1 and checkvar2 == 1:
        workout= w4
        return workout

    elif checkvar1 == '1' and checkvar2 != '1':
        workout= w2
        return workout

    elif checkvar1 !='1' and checkvar2 == '1':
        workout= w3
        return workout

    else:
        workout= w1
        return workout
    

def report_workout(*args):
    print(workout)


    


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
b_legs=ttk.Radiobutton(mainframe, text='legs', variable= checkvar1, value= 1, command= calculate_workout)
b_legs.grid(column=1, row= 2, sticky= W)


#spine button
b_spine=ttk.Radiobutton(mainframe, text='spine', variable= checkvar2, value= 1, command= calculate_workout)
b_spine.grid(column=1, row= 3, sticky=W)


#Next button
ttk.Button(mainframe, text="Next", command=calculate_workout).grid(column=3, row=3, sticky=SE)


#children of mainframe adjust to resizing
for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

#hitting return key instead of 'next' button returns same result 
root.bind('<Return>', calculate_workout)

root.mainloop()
