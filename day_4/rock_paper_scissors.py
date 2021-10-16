import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


choice = int(input('Which are you? '))
computer_choice = int(random.randint(0, 2))



if choice == 0:
    choice = rock
    user_choice = 'rock!'
elif choice == 1:
    choice = paper
    user_choice = 'paper!'
elif choice == 2:
    choice = scissors
    user_choice = 'scissors!'
else:
    print('Invalid selection')

#Computer Input, using the random module
if computer_choice == 0:
    computer_choice = rock
    cpu_choice = 'rock!'
elif choice == 1:
    computer_choice = paper
    cpu_choice = 'paper!'
elif computer_choice == 2:
    computer_choice = scissors
    cpu_choice = 'scissors!'
else: 
    print('Computer chose an invalid selection')

print(f'you chose {user_choice} {choice} while computer chose {cpu_choice} {computer_choice}')

# Win or Loose logic
if (choice == rock and computer_choice == rock) or (choice == paper and computer_choice == paper) or (choice == scissors and computer_choice == scissors) :
    print('tie')
elif choice == rock and computer_choice == scissors:
    print('You win')
elif choice == scissors and computer_choice == paper:
    print('You win')
elif choice == paper and computer_choice == rock:
    print('You win')
else:
    print('You lose!')
