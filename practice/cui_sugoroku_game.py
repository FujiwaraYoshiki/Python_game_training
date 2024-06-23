import random

player_position = 1
com_position = 1


def sugoroku_board():
    print("・" * (player_position - 1) + "Ｐ" + "・" * (30 - player_position) + "Goal")
    print("・" * (com_position - 1) + "Ｃ" + "・" * (30 - com_position) + "Goal")


sugoroku_board()
print("Let's play sugoroku!")
while True:
    input("Press Enter to advance your piece")
    player_position = player_position + random.randint(1, 6)
    if player_position > 30:
        player_position = 30
    sugoroku_board()
    if player_position == 30:
        print("You win!!")
        break
    input("Press Enter to advance Com piece")
    com_position = com_position + random.randint(1, 6)
    if com_position > 30:
        com_position = 30
    sugoroku_board()
    if com_position == 30:
        print("Com win!!")
        break
