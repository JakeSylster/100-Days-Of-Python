#Rock Paper Scissors game
import random
print("Welcome to the Rock Paper Scissors game.")

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

game_art = [f"Rock\n{rock}",f"Paper\n{paper}",f"Scissors\n{scissors}"]

user_choice = int(input("What do you choose? \nType 0 for Rock, 1 for Paper or 2 for Scissors\n"))
if 0 <= user_choice <= 3:
    print(f"You Chose: {game_art[user_choice]}")
    computer_choice = random.randint(0, 2)
    print(f"Computer Chose: {game_art[computer_choice]}")
else:
    print("Wrong input. You don't deserve to play this game. Learn to read")

# if user_choice == 0:
#     print("You Chose: 'Rock'\n",rock)
# elif user_choice == 1:
#     print("You Chose: 'Paper'\n",paper)
# elif user_choice == 2:
#     print("You Chose: 'Scissor'\n",scissors)


# if computer_choice == 0:
#     print("Computer Chose: 'Rock'\n",rock)
# elif computer_choice == 1:
#     print("Computer Chose: 'Paper'\n",paper)
# elif computer_choice == 2:
#     print("Computer Chose: 'Scissor'\n",scissors)

if user_choice == 0:
    if computer_choice == 0:
        print("Draw")
    elif computer_choice == 1:
        print("You Lose!")
    elif computer_choice == 2:
        print("You Win!!")
    else:
        print("Wrong input. How can you mess up three numbers? Learn to read.\nGAME OVER")
elif user_choice == 1:
    if computer_choice == 0:
        print("You Win!!")
    elif computer_choice == 1:
        print("Draw")
    elif computer_choice == 2:
        print("You Lose!")
    else:
        print("Wrong input. First finish 1st standard. Learn to read and then come back to play\nGAME OVER")
elif user_choice == 2:
    if computer_choice == 0:
        print("You Lose!")
    elif computer_choice == 1:
        print("You Win!!")
    elif computer_choice == 2:
        print("Draw")
    else:
        print("Wrong input. Go back to school. Learn to read.\nGAME OVER")
else:
    print("You're Adopted!!\nGAME OVER")
