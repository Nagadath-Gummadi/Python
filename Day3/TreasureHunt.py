print("Enter to the Tresure Island.\nYour job is to find the tresure.")
ans=input('Do you want to goto left or right?')
if(ans=='left' or ans=='LEFT' or ans=='Left'):
    print("Game Over")
if(ans=='Right' or ans=='RIGHT' or ans=='right'):
    ans=input('Do you want to swim or wait?')
    if(ans=='Swim' or ans=='SWIM' or ans=='swim'):
        print('Game Over')
    if(ans=='Wait' or ans=='WAIT' or ans=='wait'):
        door=int(input('Which Door you want to choose:(1,2,3) ?'))
        if(door==2):
            print("You found the tressure..")
            treasure='''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/________/
*******************************************************************************

            
            '''
            print(treasure)

        else:
            print('Game Over')
