# A python script that calculates you tip.

print('Welcome to the tip calculator!')

bill = float(input('How much is the bill?'))

percent_tip = int((input('What percentage tip would you like to give?')))

dot_tip = percent_tip / 100 # the tip % divided by 100

tip = bill * dot_tip # To get the actual tip from the tip percentage

total = bill + tip # The original bill + the tip
new_bill = round(total, 2)

print(f'Your new bill, with the tip included is {new_bill}')

number_of_people = int(input('How many people are you splitting the bill with? \nIf it is just yourself please type 1.'))

splitted_bill = new_bill / number_of_people

final_bill = round(splitted_bill, 2)

print(f'Each person should pay {final_bill}')

# https://repl.it/@9T9AD/tip-calculator#main.py
