# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#First *fork* your copy. Then copy-paste your code below this line 👇
#Finally click "Run" to execute the tests

age = int(age)

dead_line = input("At what age do you want to die? ")

age_left = dead_line - age

days_left = age_left * 365

weeks_left = age_left * 52

months_left = age_left * 12

print(f'You have {days_left} days, {weeks_left} weeks, and {months_left} months left.')

# https://repl.it/@9T9AD/lifeinweeks#main.py