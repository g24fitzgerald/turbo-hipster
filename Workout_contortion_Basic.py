#Copyright(c) 2014 Gina Fitzgerald 
#Contortion workout: provide contortion workouts avoiding injuries 
#base cases from which to expand on monday
#program introduces itself
#user inputs injury
#program returns workout

#global constants

#PROBLEMS: 
#improvement: implimented multiple dictionaries 


import random 
#dictionary


spine_dict= {'cobra progression':'5 minuntes', 'doughnut progression' : '5 minutes',
             'kneeling backbend': '1 minute, 4 reps', 'chair layover' : '1 minute 4 reps',
             'elbow stand' : '1 minute, 4 reps', 'backbend with twist' : '1 minute, 2 reps',
             'standing frontbend' : '2 minutes', 'laying frontbend' : '2 minutes',
             'frontbend with chair' : '1 minute, 4 reps'}

shoulder_dict = {'overhead stretch' : '1 min', 'floor shoulder stretch' : '5 min'}

legs_dict = {'splits (L, R, Center)': '2 min per side', 'splits switch (L-R)' : '10 reps',
             'oversplits (L,R,Center)' : '2 min per side', 'roll through center splits' : '10 reps',
             'legs behind back': '1 min, 3 reps'}

injury = 0
self=[]

#define workout 

def todays_workout(self):
   
    #injured spine 
    if injury == "1":

        #return random sample of exerciese from shoulder and leg dictionaries 
        self= random.sample(shoulder_dict.items(), 2) + random.sample(legs_dict.items(), 4)
        

    #injured shoulders 
    elif injury == "2":
        self= random.sample(spine_dict.items(), 3) + random.sample(legs_dict.items(), 3)

    #injured legs
    elif injury == "3":
        self= random.sample(shoulder_dict.items(), 2) + random.sample(spine_dict.items(), 4)

    #no injuries, return all workouts
    else:
        self= random.sample(shoulder_dict.items(), 2) + random.sample(legs_dict.items(), 3) +random.sample(spine_dict.items(), 3)
        
    return self

#MAIN

#introduction
print("""welcome to your personal guide to the world of contortion"
our program focuses on the following areas:

      "1 - spine
      
      "2 - shoulders
      
      "3 - legs""")

injury = input("""If you are injured in any of the preceeding areas,
               type the corresponding number, otherwise hit enter to continue""")

print(todays_workout(self))

input("press enter to exit")
