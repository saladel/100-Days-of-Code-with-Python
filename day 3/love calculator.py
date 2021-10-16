# 🚨 Don't change the code below 👇

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

#Convert to lower case
lowercase_name1 = name1.lower()
lowercase_name2 = name2.lower()

#true love count for name1
firstname_count_T = lowercase_name1.count('t')
firstname_count_R = lowercase_name1.count('r')
firstname_count_U = lowercase_name1.count('u')
firstname_count_E = lowercase_name1.count('e')
#love
firstname_count_L = lowercase_name1.count('l')
firstname_count_O = lowercase_name1.count('o')
firstname_count_V = lowercase_name1.count('v')
firstname_count_E = lowercase_name1.count('e')


#Count true love for name2
secondname_count_T = lowercase_name2.count('t')
secondname_count_R = lowercase_name2.count('r')
secondname_count_U = lowercase_name2.count('u')
secondname_count_E = lowercase_name2.count('e')
#Love
secondname_count_L = lowercase_name2.count('l')
secondname_count_O = lowercase_name2.count('o')
secondname_count_V = lowercase_name2.count('v')
secondname_count_E = lowercase_name2.count('e')


#Calculatiing the love score for 'true'
T = firstname_count_T + secondname_count_T
R = firstname_count_R + secondname_count_R
U = firstname_count_U + secondname_count_U
E = firstname_count_E + secondname_count_E

#Calculatiing the love score for 'true'
L = firstname_count_L + secondname_count_L
O = firstname_count_O + secondname_count_O
V = firstname_count_V + secondname_count_V
E = firstname_count_E + secondname_count_E


total_true = T + R + U + E

total_love = L + O + V + E

love_score = int(str(total_true) + str(total_love))

if love_score < 10 or love_score > 90:
  print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50:
  print(f"Your score is {love_score}, you are alright together.")
else: print(f"Your score is {love_score}.")
