import art
import game_data
import random

def format_data(account):
    return f"{account['name']}, a {account['description']}, from {account['country']}"

def higher_lower_game():
    temp_list = game_data.data
    #num_of_choices = len(game_data.data)
    iteration_checker = True
    a = random.choice(temp_list)
    score = 0
    print(art.logo)

    while iteration_checker :

        #Front-end
        print(f"Compare A: {format_data(a)}")
        temp_list.remove(a)
        print(art.vs)
        b = random.choice(temp_list)
        print(f"Against B: {format_data(b)}")
        choice = input("Who has more followers? Type 'A' or 'B': ").upper()

        #Logic
        if choice == 'A':
            if a['follower_count'] > b['follower_count']:
                iteration_checker = True
                a = b
                score += 1
                print("\n"*20)
                print(f"You're right! Current score: {score}")
            else:
                iteration_checker = False
                print(f"You were wrong.Your final score: {score}")
        elif choice == 'B':
            if b['follower_count'] > a['follower_count']:
                iteration_checker = True
                a = b
                score +=1
                print("\n"*20)
                print(f"You're right! Current score: {score}")
            else:
                iteration_checker = False
                print(f"You were wrong.Your final score: {score}")
        else:
            print("Invalid choice. Please learn the alphabet, You'll need it to play the game.")
            print(f"Your final score: {score}")

repeat = True
while repeat:
    higher_lower_game()
    check = input("Do you wish to play again? please enter y or n: ").lower()
    if check == 'y':
        repeat = True
    else:
        repeat = False
    print("Thank you for playing.")
