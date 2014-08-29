import random

from os import listdir
from threading import Timer

from tkinter import *
from tkinter.ttk import *

class Exercises():
    def __init__(self):
        self.legsHard = []
        self.legsEasy = []
        self.spineHard = []
        self.spineEasy = []

        self.generated = []

    def initialize(self):
        self.initializeArray(self.legsHard, './Legs_hard')
        self.initializeArray(self.legsEasy, './Legs_easy')
        self.initializeArray(self.spineHard, './Spine_hard')
        self.initializeArray(self.spineEasy, './Spine_easy')

    def initializeArray(self, array, directory):
        for filename in listdir(directory):
            if filename.endswith('.gif'):
                array.append(PhotoImage(file = directory + '/' + filename))

    def setupNormal(self):
        self.generated.extend(self.legsHard)
        self.generated.extend(self.spineHard)
        
        random.shuffle(self.generated)
        
    def setupLegsEasy(self):
        self.generated.extend(self.legsEasy)
        self.generated.extend(self.spineHard)
        
        random.shuffle(self.generated)

    def setupSpineEasy(self):
        self.generated.extend(self.legsHard)
        self.generated.extend(self.spineEasy)
        
        random.shuffle(self.generated)

class Disclaimer(Frame):
    def __init__(self, master):
        super(Disclaimer, self).__init__(master)
        
        self["borderwidth"] = 10
        
        self.title = Label(self, text = "WARNING!", )
        self.title.grid(row = 0, column = 0)
        
        self.text = Label(self, text = "this workout is not intended for those without previous training. Under no circumstances should these exercises be performed without first having recieved proper training from an instructor. This is not a tutorial on becoming a contortionist, rather this is a workout generator for contortionists seeking to vary their personal training. By clicking 'ok' you assume responsibility for any and all injuries aquired while following this program.")
        self.text.grid(row= 2, column = 0)
        self.text.config(wraplength = 500)
            
        self.agree = Button(self, text = "I have read and understand the preceeding information", command = self.agreeClicked)
        self.agree.grid(row = 3, column = 0)

    def agreeClicked(self):
        chooser.tkraise()
    
class Chooser(Frame):
    def __init__(self, master):
        super(Chooser, self).__init__(master)
        
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

        self.next = Button(self, text = "calculate workout", command = self.nextClicked)
        self.next.grid(row = 4, column = 0)

    def nextClicked(self):
        if self.problem == 'legs':
            exercises.setupLegsEasy()

        elif self.problem == 'spine':
            exercises.setupSpineEasy()

        else:
            exercises.setupNormal()

        workout.tkraise()
        workout.tick()

class Workout(Frame):
    def __init__(self, master):
        super(Workout, self).__init__(master)

        self.title = Label(self, text = "Contortion Routine")
        self.title.grid(row = 0, column = 0)

        self.image = Label(self)
        self.image.grid(row = 1, column = 0)

        self.countdown = Label(self, text = "time left: 0")
        self.countdown.grid(row = 2, column = 0)

        self.exercise = 0
        self.elapsed = 0

    def tick(self):
        self.elapsed = self.elapsed + 1

        if self.elapsed == 10:
            self.elapsed = 0
            self.exercise = (self.exercise + 1) % len(exercises.generated)
        
        self.image.config(image = exercises.generated[self.exercise])

        countdown = "time left: " + str(300 - self.elapsed)
        self.countdown.config(text = countdown)

        timer = Timer(1.0, self.tick)
        timer.start()
        
    def disp_routine(self):
            print("where's the workout?")
            self.interpret_image()
            self.timer= Timer(self, 300)
            self.timer.grid(row= 3, column= 1, columnspan = 2, pady= 20)



    def interpret_image(self):
        while self.timer != 0:
            for i in Exercises.generated:
                img = PhotoImage(file ='split-c-02.gif') ###
                panel = Label(root, image = img)
                panel.pack()

        else:
            self.callback
            
    def callback(self):
        img2 = PhotoImage(Image.open()) ###
        panel.configure(image = img2)
        panel.image = img
        
class Timer2(Frame):
    # Generate and display countdown

    def __init__(self, master, remaining):
        super(Timer, self).__init__(master)
        self.remaining = remaining
        self["padx"] = 10
        
        # Make clock and message labels
        self.clock = Label(self)
        self.message = Label(self)
        self.clock.grid(row = 0, sticky = W)
        self.message.grid(row = 1, sticky = W)


    def countdown(self):
        # Display countdown 0:00
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
            self.message["text"] = "Slowly come out of last position and enter next"
            

# initalize gui
root = Tk()

# set title
root.title("Contortion Workout")

# calculate geometry
s_width = (root.winfo_screenwidth() // 2) - (500 // 2)
s_height = (root.winfo_screenheight() // 2) - (400 // 2)

root.geometry("585x410+" + str(s_width) + "+" + str(s_height))

# initialize excercises
exercises = Exercises()
exercises.initialize()

# initialize container
container = Frame(root)

container.grid(sticky = NSEW)
container.rowconfigure(0)
container.columnconfigure(0)

container.pack(side = 'top', fill = 'both', expand = True)

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
