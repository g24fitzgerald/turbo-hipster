import random

from tkinter import *
from tkinter.ttk import *

class Exercises():
    def __init__(self):
        self.legsHard = []
        self.legsEasy = []
        self.spineHard = []
        self.spineEasy = []

        self.generated = []

    def initialize(file):
        self.legsHard = [] # TODO
        self.legsEasy = [] # TODO
        self.spineHard = [] # TODO
        self.spineEasy = [] # TODO

    def setupNormal():
        self.generated.append(self.legsHard)
        self.generated.append(self.spineHard)

    def setupLegsEasy():
        self.generated.append(self.legsEasy)
        self.generated.append(self.spineHard)

    def setupSpineEasy():
        self.generated.append(self.legsHard)
        self.generated.append(self.spineEasy)

    def shuffle():
        random.shuffle(self.generated)

class Disclaimer(Frame):
    def __init__(self, master):
        super(Disclaimer, self).__init__(master)
        
        self.grid()
        
        self["borderwidth"] = 5
        
        self.title = Label(self, text = "WARNING!")
        self.title.grid(row = 0, column = 0)
        
        self.text = Label(self, text = "this workout is not intended for those without previous training. Under no circumstances should these exercises be performed without first having recieved proper training from an instructor. This is not a tutorial on becoming a contortionist, rather this is a workout generator for contortionists seeking to vary their personal training. By clicking 'ok' you assume responsibility for any and all injuries aquired while following this program.")
        self.text.grid(row= 1, column = 0)
        self.text.config(wraplength = 500)
            
        self.agree = Button(master, text = "I have read and understand the preceeding information", command = self.agreeClicked)
        self.agree.grid(row = 2, column = 0)

    def agreeClicked(self):
        chooser.tkraise()
    
class Chooser(Frame):
    def __init__(self, master):
        super(Chooser, self).__init__(master)
        
        self.grid()
        
        self["borderwidth"] = 5
        
        self.title = Label(self, text = "Contortion Program")
        self.title.grid(row = 0, column = 0)

        self.question = Label(self, text = "Do you have injuries in any of the following areas?")
        self.question.grid(row = 1, column = 0)

        self.problem = StringVar()
        self.problem.set(None)

        self.problem_legs = Radiobutton(self, text = "legs", variable = self.problem, value= 'legs')
        self.problem_legs.grid(row = 2, column = 0)

        self.problem_spine = Radiobutton(self, text = "spine", variable = self.problem, value= 'spine')
        self.problem_spine.grid(row = 3, column = 0)

        self.next = Button(self, text = "calculate workout", command = self.next)
        self.next.grid(row = 4, column = 0)

    def nextClicked(self):
        if self.problem == 'legs':
            exercises.setupLegsEasy()

        elif self.problem == 'spine':
            exercises.setupSpineEasy()

        else:
            exercises.setupNormal()

        workout.tkraise()

class Workout(Frame):
    def __init__(self, master):
        super(Workout, self).__init__(master)
        

    def disp_workout(self):
        if self.diff.get() != 'None':
            self.interpret_image()

            self.timer(self, 300)
            self.timer.grid(row= 3, column= 1, columnspan = 2, pady= 20)

    def interpret_image(self):
        if self.timer != 0:
            img = PhotoImage(file='myPicture.gif')
            panel = Label(root, image = img)
            panel.pack()

        else:
            self.callback
            
    def callback(self):
        img2 = PhotoImage(Image.open(path2))
        panel.configure(image = img2)
        panel.image = img
        
class Timer(Frame):
    # Generates and displayes timer used in the game frame

    def __init__(self, master, remaining):
        super(Timer, self).__init__(master)
        self.remaining = remaining
        self["padx"] = 20
        
        # Make clock and message labels
        self.clock = Label(self)
        self.message = Label(self, font = ("Helvetica", 18))
        self.clock.grid(row = 0, sticky = W)
        self.message.grid(row = 1, sticky = W)


    def countdown(self):
        # Show clock counting down after every second

        # make minute and second calculations so clock can be shown in minutes 
        self.t_min = self.remaining // 60
        self.t_sec = self.remaining % 60
        if self.remaining > 0:
            if self.t_sec < 10:
                self.clock["text"] = str(self.t_min) + ":0" + str(self.t_sec) 
            else:
                self.clock["text"] = str(self.t_min) + ":" + str(self.t_sec) 

            self.remaining -= 1

            # Recursively run every second
            self.after(1000, self.countdown)

        # Change label texts and button states when time runs out
        else:
            self.clock["text"] = "0:00" 
            self.message["text"] = "Time is up!"

# initialize excercises
exercises = Exercises()

exercises.initialize('...') # TODO

# initalize gui
root = Tk()

# set title
root.title("Contortion Workout")

# calculate geometry
sw = (root.winfo_screenwidth() // 2) - (585 // 2)
sh = (root.winfo_screenheight() // 2) - (410 // 2)

root.geometry("585x410+" + str(sw) + "+" + str(sh))

# initialize container
container = Frame(root)

container.grid(sticky = NSEW)
container.rowconfigure(0)
container.columnconfigure(0)

# initialize frames
disclaimer = Disclaimer(container)
disclaimer.grid(row = 0, column = 0, sticky = NSEW)
                       
chooser = Chooser(container)
chooser.grid(row = 0, column = 0, sticky = NSEW)
                       
workout = Workout(container)
workout.grid(row = 0, column = 0, sticky = NSEW)

# bring disclaimer to the front
disclaimer.tkraise()

# initialize main loop
root.mainloop()

                          
    
