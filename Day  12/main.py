import random
import art

def restart():
    looper = input("Do you want to play again. Type 'y' or 'n': ").lower()
    if looper == 'y':
        print("\n" * 10)
        game_logic()
    else:
        print("Thank you for playing. Buh-byee")

def game_logic():
    picked_num = random.randint(1, 100)
    #print(picked_num)
    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty: Type 'easy' or 'hard': ").lower()
    a: int = 0
    if difficulty == 'easy':
        a = 10
    if difficulty == 'hard':
        a = 5

    while a != 0:
        print(f"You have {a} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == picked_num:
            print("Yay!! you guessed right. YOU WIN!")
            restart()
        elif guess > picked_num:
            print("Too high")
        else:
            print("Too low")
        if a > 1:
            print("Guess again")
        a -= 1
    print("You ran out of lives.")
    restart()

game_logic()
