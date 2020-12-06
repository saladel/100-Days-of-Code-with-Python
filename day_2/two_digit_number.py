#Write a program that adds the digits in a 2 digit number. 
#e.g. if the input was 35, then the output should be 3 + 5 = 8

# Example Input
# 39
# Example Output
# 3 + 9 = 12

# Hint
# Try to find out the data type of two_digit_number.
# Think about what you learnt about subscripting.
# Think about type conversion.

####################################

# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

first_number = two_digit_number[0]
second_number = two_digit_number[1]
total_number = int(first_number) + int(second_number)
print(total_number)

# https://repl.it/@9T9AD/day-2-1-exercise#main.py