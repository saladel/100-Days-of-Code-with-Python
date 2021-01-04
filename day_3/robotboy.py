print('''◖(◣☩◢)◗  ◖(◣☩◢)◗ ◖(◣☩◢)◗ ◖(◣☩◢)◗ ◖(◣☩◢)◗''')

print("Welcome to Trivia Island.")
excitement = input("Are you excited?! Y or N\n")

if excitement == 'y' or excitement == 'Y':
  print("Let's go! 💪")

  #Question1
  print('Question 1\n')
  Quest1 = input('Have you watched robotboy? Y or N\n')
  if Quest1 == 'y' or Quest1 == 'Y':
    print('Awesome!')

    #Question 2
    Quest2 = input('What is the name of the professor that made robotboy?\n')
    #making question 2 lower case 
    Quest2.lower()
    if Quest2 == 'professor moshimo' or Quest2 == 'moshimo' or Quest2 == 'prof moshimo':
      print("That is correct!")

      #Question 3
      print('Question3\n')
      Quest3 = input("What is the name of Tommys' best friend?\n")
      #making question 3 lower case 
      Quest3.lower()
      if Quest3 == 'gus turner' or Quest3 == 'gus' or Quest3 == 'g-man' or Quest3 == 'the g-man':
        print('Superb! 👏')

        #Question 4
        Quest4 = int(input('How many assassination attempt has Tommy survived?\n'))
        
        if Quest4 == 14:
          print('OMG!! You are definitely a fan! 😱🤯')
        elif Quest4 >= 10 and Quest4 < 14:
          print('That was close! The answer is 14')
        elif Quest4 > 14 or Quest4 < 10:
          print('The answer is: 14\n\nGame Over 😭😭')
          #End of Question 4

      else: print("The name of Tommys' bestfriend is Gus Turner AKA The G-Man.\n\nTry again.")
      #End of Question 3

    else: print('The name of the Professor is Moshimo.\n\nTry again.')
    #End of Question 2

  else: print('Game Over!\nTo participate in this trivia you need to have seen robotboy.')
  #End of Question 1

else: print('Game Over!\nGood vibes only 🙏')
#The End
#Ende
#Fin
