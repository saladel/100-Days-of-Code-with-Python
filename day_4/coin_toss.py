#Write your code below this line 👇
#Hint: Remember to import the random module first. 🎲

import random

code_seed = int(input("Put in a random number: "))
random.seed(code_seed)


Head = random.randint(0,1)
#Tail = random.randint(0,1)

print(Head)

if Head == 1:
  print("Head")
else: print('Tail')








