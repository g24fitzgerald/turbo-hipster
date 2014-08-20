#Copyright(c) 2014 Gina Fitzgerald 
#Contortion workout: provide contortion workouts avoiding injuries 
#base cases from which to expand on monday
#program introduces itself
#user inputs injury
#program returns workout

#global constants

#PROBLEMS: 
#improvement: increase scope of dict (option 2 looks best now-1 dict 9 k/v pairs

#dictionary
workout_dictionary = {'spine': 'w1', 'shoulders': 'w2', 'legs' : 'w3'}

injury = 0
self=[]

#define workout 

def todays_workout(self):
   
    #injured spine 
    if injury == "1":
        self= workout_dictionary['shoulders'] + workout_dictionary['legs']

    #injured shoulders 
    elif injury == "2":
        self= workout_dictionary['spine'] + workout_dictionary['legs']

    #injured legs
    elif injury == "3":
        self= workout_dictionary['spine']+ workout_dictionary['shoulders']

    #no injuries, return all workouts
    else:
        self= workout_dictionary
        
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
