def play():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    user_cards = []
    computer_cards = []
    import random
    def deal_card_user():
        card = random.choice(cards)
        user_cards.append(card)

    def deal_card_computer():
        cardd = random.choice(cards)
        computer_cards.append(cardd)

    deal_card_user()
    deal_card_user()
    deal_card_computer()
    deal_card_computer()
    user_win = False
    computer_win = False
    user_score = user_cards[0] + user_cards[1]
    computer_score = computer_cards[0] + computer_cards[1]
    print(f"Your hand: {user_cards}")
    while computer_win != True and user_win != True:
        user_score = sum(user_cards)
        computer_score = sum(computer_cards)
        if user_score == 21:
            user_win = True
        elif computer_score == 21:
            computer_win = True
        elif user_score > 21:
            if 11 in user_cards:
                user_cards.remove(11)
                user_cards.append(1)
                user_score = sum(user_cards)
        if user_score > 21:
            computer_win = True
        told = 0
        while told == 0:
            first = computer_cards[1]
            print(f"Computer's first card is {first}")
            told = 1
        while user_score < 21:
            hit = input("do you want another card\n")
            if hit == "yes":
                deal_card_user()
                user_score = sum(user_cards)
                print(f"Your hand: {user_cards}")
            if user_score > 21:
                computer_win = True
            else:
                if computer_score < 17:
                    deal_card_computer()
                    computer_score = sum(computer_cards)
                if computer_score > 21:
                    user_win = True

                else:
                    if user_score == computer_score:
                        print("Draw")
                        break
                    elif user_score > computer_score:
                        user_win = True
                    else:
                        computer_win = True

    print(f"Computer hand: {computer_cards}")
    if computer_win:
        print("computer wins")
    if user_win:
        print("user wins")
    again = input("do you want to play again?\n")
    if again == "yes":
        import os
        def clear_console():
            os.system('cls' if os.name == 'nt' else 'clear')

        clear_console()
        play()



