# Using random function (i.e:random.choice) take any variable but don't print, the program will ask about your choice
# Use while loop or for loop, do it for 10 times and thus winner will be determined BY HARRY
import random
import pygame
import modulefinder
mychoice=input("Enter your choice:")
yourchoice=["snake","water","gun"]
print(random.choice(yourchoice))
sum1=0
sum2=0
my_wins=0
your_wins=0
rounds=10 
for i in range(1,rounds+1):
    if mychoice==yourchoice:
        print(my_wins,"wins is alloted to both")
        print(mychoice,yourchoice)
    elif mychoice!=yourchoice:
        if mychoice=="snake" and yourchoice=="water":
            my_wins+=1
            your_wins+=0
            print(my_wins, your_wins)
        elif mychoice=="snake" and yourchoice=="gun":
            your_wins+=1
            my_wins+=0
            print(my_wins, your_wins)
        elif mychoice == "water" and yourchoice == "gun":
            my_wins += 1
            your_wins=0
            print(my_wins, your_wins)
        elif mychoice == "water" and yourchoice == "snake":
            your_wins += 1
            my_wins=0
            print(my_wins, your_wins)
        elif mychoice == "gun" and yourchoice == "snake":
            my_wins += 1
            your_wins=0
            print(my_wins, your_wins)
        elif mychoice == "gun" and yourchoice == "water":
            your_wins += 1
            my_wins=0
            print(my_wins, your_wins)



