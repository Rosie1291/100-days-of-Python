total_bill = float(input("Welcome to the tip calculator!\nWhat was the total bill? "))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
num_of_ppl = int(input("How many people to split the bill? "))
pay = total_bill / num_of_ppl * (1 + tip/ 100)
print(f"Each person should pay: ${round(pay, 2)}")