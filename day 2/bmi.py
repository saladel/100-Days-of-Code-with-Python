# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.

# The BMI is a measure of some's weight taking into account their height. 
# e.g. If a tall person and a short person both weigh the same amount, 
# the short person is usually more overweight.

# The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):
# bmi = weight (kg) / height**2 (m^2)

# Example Input
# weight = 80
# height = 1.75
# Example Output
# 80 ÷ 1.75 x 1.75 = 26.122448979591837

# 26

# Hint
# Check the data type of the inputs.
# Try to use the exponent operator in your code.
# Remember PEMDAS.
# Remember to convert your result to a whole number (int).

#######################################

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

h = float(height)
w = int(weight)

result = w / (h * h)

bmi = int(result)

print(bmi)

# https://repl.it/@9T9AD/day-2-2-exercise-2#main.py