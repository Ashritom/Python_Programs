import random
names_string = input("Enter names with ',' seperator: ")
names = names_string.split(",")
num = len(names)
print(names[random.randint(0,num-1)]+" is going to buy the meal today!")
