#Copyright (c) 2014 Gina Fitzgerald
#New Beginnings Project
#Contortion workout generator
#program opens with the warning page which isntructs to maximize window, and brings next page to the front
#2nd page (Chooser) opens to include injury buttons which generate workouts. next button brings 3rd page to front
#3rd page (Workout) displays images for 5 minutes, displaying seconds countdown, and automatically changes to the next random workout as the timer hits zero
#program runs until user exits-This protects against continuing the workout after sustaining a new injury-due to the personal nature of contortion, user may continue as long as necessary
#This project allowed me to gain a deeper understanding of the structure of object oriented programmming, importing files, understanding the scope of a command, and the dangers of over-complicating code 



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
        
        self.text = Label(self, text = "this workout is not intended for those without previous training. Under no circumstances should these exercises be performed without first having recieved proper training from an instructor. This is not a tutorial on becoming a contortionist. This is a workout generator for contortionists seeking to vary their personal training. Contortionists should warmup BEFORE STARTING this workout; Neglecting to do so will result in injury. By clicking 'ok' you assume responsibility for any and all injuries aquired while following this program. Take a moment to maximize this window.")
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
        self.image.grid(row = 0, column = 0)

        self.tip1 = Label(self, text = "Do not dislocate until you are a complete contotionist")
        self.tip1.grid(row= 1, column = 1)
        self.tip1.config(wraplength = 250)

        self.tip2 = Label(self, text = "Do the exercises for 3 hours a day. Repeat them 10-25 times once you have them down. Do this every day. It takes years to become a true contortionist. Never miss a day.")
        self.tip2.grid(row= 2, column = 1)
        self.tip2.config(wraplength = 250)

        self.tip3 = Label(self, text = "Remember to breathe. Be gentle coming in and out of positions")
        self.tip3.grid(row= 0, column = 1)
        self.tip3.config(wraplength = 250)
        

        self.tip4 = Label(self, text = "This generator will loop foever. Exit the program manually when you've repeated the exerciese to your satisfaction. If you feel unusual pain, discontinue workout immidiately.")
        self.tip4.grid(row= 3, column = 1)
        self.tip4.config(wraplength = 250)
        
        self.countdown = Label(self, text = "Time remaining: 0", font =('Helvetica', 20))
        self.countdown.grid(row = 2, column = 0)

        self.exercise = 0
        self.elapsed = 0
        
    

    def tick(self):
        self.elapsed = self.elapsed + 1
        if self.elapsed == 300:
            self.elapsed = 0
            self.exercise = (self.exercise + 1) % len(exercises.generated)
                            
        self.image.config(image = exercises.generated[self.exercise])
        
        countdown = "time left: " + str(300 - self.elapsed)
        self.countdown.config(text = countdown)

        timer = Timer(1.0, self.tick)
        timer.start()
        
                    

# initalize gui
root = Tk()

# set title
root.title("Contortion Workout")

# calculate geometry
s_width = (root.winfo_screenwidth() // 2) - (500 // 2)
s_height = (root.winfo_screenheight() // 2) - (400 // 2)

root.geometry("585x410+" + str(s_width) + "+" + str(s_height))

# initialize exercises
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
