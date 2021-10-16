# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random

# Dummy names: Ade, Abdul, Wale, Azeez

# 1st, get the names using the names Variable
print(names)

#2nd, get the length of the list of names
name_length = len(names)

#3rd,subtract 1 from the name_length because of indexing
new_name_length = name_length - 1

#4th, randomise the names using randint and store the index number
index_of_person_paying = random.randint(0, new_name_length) 

#5th, get the name of the person through the index; index_of_person_paying
person_paying = names[index_of_person_paying]

#6th, finish up
print(f"{person_paying} is going to buy the meal today!")

