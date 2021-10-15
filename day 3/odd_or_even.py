# An application that checks if a number is odd or even.

number = float(input("Which number do you want to check? "))

test = number % 2

if test == 0:
  print('This is an even number.')
else:
  print('This is an odd number.')
