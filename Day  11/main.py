import art
import random

def blackjack():
    print(art.logo)
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    player_bust = False
    computer_bust = False
    blackjack_check = False
    #Player
    player_score = 0
    player_hand = random.sample(cards,2)
    for hand in player_hand:
        player_score += hand
    print(f"Your cards: {player_hand}, Player score: {player_score}")
    if player_score == 21:
        print("You win! You got a Blackjack")
        exit(blackjack())

    #Computer
    computer_hand = random.sample(cards,2)
    computer_score = 0
    for hand in computer_hand:
        computer_score += hand
    print(f"Computer's first card: {computer_hand[0]}")


    #Game
    action = input("Type 'y' to get another card, type 'n' to pass: ").lower()
    while action not in ['y','n']:
        print("How can someone mess up one of two letters?")
        action = input("Type 'y' to get another card, type 'n' to pass: ").lower()
    while action == 'y' and player_bust == False:
        additional_player_card = random.choice(cards)
        player_hand.append(additional_player_card)
        player_score += additional_player_card
        if player_score > 21:
            if 11 in player_hand:
                player_hand.remove(11)
                player_hand.append(1)
                player_score = 0
                for hand in player_hand: player_score += hand
                break
            else:
                print(f"Your final hand: {player_hand}, Player score: {player_score}")
                print("You bust. Game over!\n")
                player_bust = True
                break
        elif player_score == 21:
            print(f"Your final hand: {player_hand}, Player score: {player_score}")
            print("You hit a Blackjack!! You win!!")
            blackjack_check = True
            player_bust = True
        else:
            print(f"\nYour cards: {player_hand}, Player score: {player_score}")
            print(f"Computer's first card: {computer_hand[0]}")
            action = input("Type 'y' to get another card, type 'n' to pass: ").lower()
    if action == 'n':
        while computer_score < 17:
            additional_computer_card = random.choice(cards)
            computer_hand.append(additional_computer_card)
            computer_score += additional_computer_card
        if computer_score > 21:
            if 11 in computer_hand:
                computer_hand.remove(11)
                computer_hand.append(1)
                computer_score = 0
                for hand in computer_hand: computer_score += hand
            else:
             #   print(f"Computer's final hand: {computer_hand}, Dealer score: {computer_score}")
                print("Dealer bust. You win!\n")
                computer_bust = True
        elif computer_score == 21:
            #print(f"Computer's final hand: {computer_hand}, Dealer score: {computer_score}")
            print("The dealer hit a Blackjack!! You Lose!!")
            blackjack_check = True
            computer_bust = True
        print(f"Computer's final hand: {computer_hand}, Dealer score: {computer_score}")
    #Game_logic
    if player_score > computer_score and player_bust == False and blackjack_check == False:
        print("You Win!\n")
    elif player_score == computer_score:
        print("It's a draw\n")
    elif player_score < computer_score and computer_bust == False and blackjack_check == False:
        print("You Lose!\n")


while  input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == 'y':
    print("\n"*10)
    blackjack()
else:
    print("No game, womp womp!!")
