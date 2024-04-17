import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user = int(input("Enter Number to play the game of Rock_Paper_Scissor\n1.Rock\n2.Paper\n3.Scissor\n\n\nEnter Here: "))
bot = random.randint(1,3)

print("\n\n\n")
if user <=3 and user >=1:


    #Draw Situations
    if user == 1 and bot == 1 : 
        print(f"User Choice : Rock\n {rock}\n")
        print(f"Bot Choice :  Rock\n {rock}\n")
        print("Draw")
    if user == 2 and bot == 2 : 
        print(f"User Choice : Paper\n {paper}\n")
        print(f"Bot Choice : Paper\n {paper}\n")
        print("Draw")
    if user == 3 and bot == 3 : 
        print(f"User Choice : Scissors\n {scissors}\n")
        print(f"Bot Choice : Scissors\n {scissors}\n")
        print("Draw")

    #User Winning Situations
    if user == 1 and bot == 3 : 
        print(f"User Choice : Rock\n {rock}\n")
        print(f"Bot Choice : Scissors\n {scissors}\n")
        print("User Win")
    if user == 2 and bot == 1 : 
        print(f"User Choice : Paper\n {paper}\n")
        print(f"Bot Choice : Rock\n {rock}\n")
        print("User Win")
    if user == 3 and bot == 2 : 
        print(f"User Choice : Scissors\n {scissors}\n")
        print(f"Bot Choice : Paper\n {paper}\n")
        print("User Win")


    #Bot Winning Situation
    if user == 3 and bot == 1 : 
        print(f"User Choice : \n {scissors}\n")
        print(f"Bot Choice : \n {rock}\n")
        print("Bot Win")
    if user == 1 and bot == 2 : 
        print(f"User Choice : \n {rock}\n")
        print(f"Bot Choice : \n {paper}\n")
        print("Bot Win")
    if user == 2 and bot == 3 : 
        print(f"User Choice : \n {paper}\n")
        print(f"Bot Choice : \n {scissors}\n")
        print("Bot Win")
else:
    print("Invalid Choice")