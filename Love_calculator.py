print("The Love Calculator is calculating your score...")
name1 = input() 
name2 = input() 


combined_name = (name1+name2).lower()


t = combined_name.count("t")
r = combined_name.count("r")
u = combined_name.count("u")
e = combined_name.count("e")
first = t+r+u+e

l = combined_name.count("l")
o = combined_name.count("o")
v = combined_name.count("v")
e = combined_name.count("e")
second = l+o+v+e


score = int(str(first) + str(second))

if score < 10 or score>90:
  print(f"Your score is {score}, you go together like coke and mentos.")

elif score >=40 and score<=50:
  print(f"Your score is {score}, you are alright together.")
  
else:
  print(f"Your score is {score}.")