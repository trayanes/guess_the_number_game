import random
computer_move = random.randint(0, 100)
print("RULES AND WELCOME PRINT")
guess_found = False
another_try = False
while True:
    if another_try:
        player_move = input("Enter a number between 1 and 100, please: ")
    else:
        player_move = input("Please enter your guess (number between 1 and 100) here: ")
    if player_move.isnumeric():
        player_move = int(player_move)
        if player_move > 100:
            print("That is not a valid number, please try with another one!")
            continue
        elif player_move == computer_move:
            guess_found = True
            break
        else:
            if player_move > computer_move:
                print("Try with a smaller number, please!")
                another_try = True
                continue
            else:
                print("Try with a bigger number, please!")
                another_try = True
            continue
    else:
        print("Invalid guess, please type a number next time!")
        another_try = True
        continue
if guess_found:
    print("YOU guess it! CONGRATS")