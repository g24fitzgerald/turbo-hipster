from tkinter import *
from tkinter.ttk import *


#create warning page
class page_one(Frame):
    def __init__(self, master):
        super(page_one, self).__init__(master)
        self.grid()
        self.widgets
        self['boarder width'] = 5

    def widgets(self):
        self.title1 = Label(self, text="WARNING!", font= t_font)
        self.title1.grid(row = 0, column = 1, columnspan = 3)
        self.title2 = Label(self, text= "this workout is not intended for those without previous training. Under no circumstances should these exercises be performed without first having recieved proper training from an instructor. This is not a tutorial on becoming a contortionist, rather this is a workout generator for contortionists seeking to vary their personal training. By clicking 'ok' you assume responsibility for any and all injuries aquired while following this program.", font=t_font)
        self.title2.grid(row= 1, column = 1, columnspan = 3)

        #must hit a_button to procede 
        self.a_button= Button(master, text="I have read and understand the preceeding information", command = enable)
        self.a_button.grid()

    def enable(self):
        self.destroy()
        return page_two(root)
    
    
class page_two(Frame):
    
    # page 2 (after warning) 
    def __init__(self, master):
        super(page_two, self).__init__(master)
        self.grid()
        self.widgets()
        self["borderwidth"] = 5

    def widgets(self):
        # Titles 
        self.title1 = Label(self, text = "Contortion Program", font = t_font)
        self.title1.grid(row = 0, column = 1, columnspan = 3)
        self.title2 = Label(self, text = "Do you have injuries in any of the following areas?", font = ("Helvetica", 24), pady = 8)
        self.title2.grid(row = 1, column = 1, columnspan = 3)

        #Radiobuttons
        self.entry = StringVar()
        self.entry.set(None)

        #leg button
        self.leg_button= Radiobutton(self, text="legs", variable = self.entry, value= 'a')
        self.leg_button.grid(row = 3, column = 3, sticky = W)

        #spine button
        self.spine_button= Radiobutton(self, text = "spine", variable = self.entry, value= 'b')
        self.spine_button.grid(row = 4, column = 3, sticky = W)

        #continue
        self.next_button= Button(self, text = "calculate workout", command = calculate_workout)
        self.next_button.grid(row = 4, column = 4, sticky = E)

        #workout categories
        self.W1= [] #hard legs
        self.W2= [] #easy legs
        self.W1= [] #hard spine
        self.W2= [] #easy spine 

        self.workout = []

        

    def calculate_workout(self):
        
        if self.leg_button == 'a' and self.spine_button =='b':
            self.workout = self.W1

        elif self.leg_button != 'a' and self.spine_button =='b':
            workout = self.W2

        elif self.leg_button == 'a' and self.spine_button !='b':
            workout = self.W3

        else:
            workout = self.W4

        return workout
        self.destroy()
        return page_three(root)

class page_three(page_two):
    
    def __init__(self, master):
        super(page_two, self).__init__(master)
        


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
        self.clock = Label(self, font = t_font)
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

root=Tk()
root.bind("<Return>", callback)
root.mainloop()

                          
    
