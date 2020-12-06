# A python script that calculates you tip.

print('Welcome to my tip calculator!')

how_much_is_the_bill = input('What was the total bill?')
bill = float(how_much_is_the_bill)


tip_choice = (input('What percentage tip would you like to give?')) 
percent_tip = int(tip_choice)

dot_tip = percent_tip / 100 # the tip % divided by 100

tip = bill * dot_tip # To get the actual tip from the tip percentage

total = bill + tip # The original bill + the tip
new_bill = round(total, 2)

print(f'Your new bill, with the tip included is {new_bill}')

split = input('How many people are you splitting the bill with? \nIf it is just yourself please type 1.')
num_of_people = int(split)

splitted = new_bill / num_of_people

final_bill = round(splitted, 2)

print(f'Each person should pay {final_bill}')
