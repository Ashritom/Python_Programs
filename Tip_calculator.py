print("Welcome to the tip calculator!")
bill = float(input("Whatwas the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
num = int(input("How many people to split the bill? "))
tip_percentage = tip/100
tip_amount = bill * tip_percentage
total_bill = bill + tip_amount
each_person = total_bill / num
print("Each person should pay: ",round(each_person,2))