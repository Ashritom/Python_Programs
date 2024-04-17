print(''' 
 ,d                                                                       
  88                                                                       
MM88MMM 8b,dPPYba,  ,adPPYba, ,adPPYYba, ,adPPYba, 88       88 8b,dPPYba,  
  88    88P'   "Y8 a8P_____88 ""     `Y8 I8[    "" 88       88 88P'   "Y8  
  88    88         8PP""""""" ,adPPPPP88  `"Y8ba,  88       88 88          
  88,   88         "8b,   ,aa 88,    ,88 aa    ]8I "8a,   ,a88 88          
  "Y888 88          `"Ybbd8"' `"8bbdP"Y8 `"YbbdP"'  `"YbbdP'Y8 88                
            
 ,adPPYba,  
a8P_____88  
8PP"""""""  
"8b,   ,aa  
 `"Ybbd8"'  
      
88                                         88                          
88                                   ,d    ""                          
88                                   88                                
88,dPPYba,  88       88 8b,dPPYba, MM88MMM 88 8b,dPPYba,   ,adPPYb,d8  
88P'    "8a 88       88 88P'   `"8a  88    88 88P'   `"8a a8"    `Y88  
88       88 88       88 88       88  88    88 88       88 8b       88  
88       88 "8a,   ,a88 88       88  88,   88 88       88 "8a,   ,d88  
88       88  `"YbbdP'Y8 88       88  "Y888 88 88       88  `"YbbdP"Y8  
                                                           aa,    ,88  
                                                            "Y8bbdP"   

''')
print('''
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
/______/______/______/______/______/______/______/______/______/______/_______/
*******************************************************************************

''')
print("Welcome to Treasure Island.")
print("Your Mission is to find the treasure.")
print('You are at a cross road. Where do you want to go ? Type "Left" or "Right"')
dir = input()
if dir == "Right":
    print("Game Over !!!")
elif dir == "Left": 
    print('You come to a lake. There is an island in the middle of the lake. Type "Wait" to wait for a boat or Type "Swim" to swim across.')
    ch = input()
    if ch == "Swim":
        print("Game Over !!!")
    elif ch == "Wait" : 
        print("You arrive at the island unharmed. There is a house with 3 doors. one Red, one Yellow, one Blue. Which colour do you choose?")
        colour = input()
        if colour == "Red":
            print("Game Over !!!")
        elif colour == "Blue":
            print("Game Over !!!")
        elif colour == "Yellow":
            print("Congratulations !!!  You found the Treasure !!!")
        else : 
            print("Invalid Choice of colour")
    else:
        print("Invalid Choice (Choose only from Wait/Swim)")
else:
    print("Invalid selection of Direction")
