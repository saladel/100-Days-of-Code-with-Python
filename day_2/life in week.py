# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#First *fork* your copy. Then copy-paste your code below this line 👇
#Finally click "Run" to execute the tests

int_age = int(age)

days = (90 - int_age) * 365
weeks = (90 - int_age) * 52
months = (90 - int_age) * 12

print(f'You have {days} days, {weeks} weeks, and {months} months left.')

# https://repl.it/@9T9AD/lifeinweeks#main.py