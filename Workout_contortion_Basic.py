#Copyright(c) 2014 Gina Fitzgerald 
#Contortion workout: provide contortion workouts avoiding injuries 
#program introduces itself
#user inputs injury
#program returns workout


#PROBLEMS: 
#improvement: implimented multiple dictionaries 


import random 
#dictionary


Backbend= {'cobra':'5 minuntes',
           'doughnut' : '5 minutes',
           'kneeling backbend': '1 minute, 4 reps',
           'chair layover' : '1 minute 4 reps',
           'elbow stand' : '1 minute, 4 reps'}
           
Frontbend= {'standing frontbend-head to floor' : '3 min',
            'standing frontbend-head through legs':'3 min',
            'laying frontbend' : '2 minutes',
            'frontbend with chair' : '1 minute, 4 reps'}
    
Other = {'overhead stretch' : '1 min', 'floor shoulder stretch' : '5 min','backbend with twist' : '1 minute, 2 reps',}

Splits_side = {'splits (L, R)': '5 min per side',
                'splits switch (L-R)' : '10 reps',
                'oversplits (L,R)' : '5 min per side',
                'legs behind back': '1 min, 3 reps',
                'dislocated splits': '15 reps',
                'split with backbend': '15 reps'}

Splits_center = {'straddle':'5 min',
                 'straddle on back': '5 min',
                 'leg elevated straddle': '15 reps',
                 'oversplit': '5 min',
                 'roll through center splits' : '10 reps',
                 'forward straddle': '15 reps'}
    
injury = 0
self=[]

#create workout class
class Workout(object):
    def __init__():
        self.warm_up = warm_up
        self.splits = splits
        self.spine = spine

    #Maybe include in initialization? 
    def warm_up(self):
        self= Other
        return self

    
    def spine(self):
        #in case of spinal injury 
        if '1' in injury:
            self= {'cobra':'5 minuntes',
           'doughnut' : '5 minutes',
           'standing frontbend-head to floor' : '3 min',
            'laying frontbend' : '2 minutes'}

        #otherwise perform randomly selected pairs of Front/Back exercises 
        else:
            self = random.sample(Backbend.items(), 3) + random.sample(Frontbend.items(), 3)

        return self

    def splits(self):
        #in case of leg injury 
        if '2' in injury:
            self= {'splits (L-R-Center)': '5 min per side'} #only perform basic leg workouts 

        #no leg injury 
        else:
            self = random.sample(Splits_side.items(), 4) + random.sample(Splits_center.items(), 4)
        return self

1

    

#MAIN

#introduction
print("""welcome to your personal guide to the world of contortion"
our program focuses heavily on the following areas:

      "1 - spine
      
      "2 - splits""")

#user inputs injury 
injury = input(
                """\n\nIf you are injured in any of the preceeding areas,
                   type the corresponding number(s)and hit enter,
                   otherwise hit enter to continue
                   if your input is not in field, program will provide full workout""")

#present workout
print("\n\nWarm Up")
print(Workout.warm_up(self))

print("\n\nSpinal work")
print(Workout.spine(self))

print("\n\nLeg work")
print(Workout.splits(self))

input("\n\npress enter to exit")
