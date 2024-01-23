from board import *
from dice import *
from player import *

"""
description: Kniffel, also known as Yahtzee. This was written as a final project for the first term of my reskilling.
author: hendrik haustein
date: 22.01.2024
"""
def state(player):
    """

    The game logic

    :param player: the player object
    :return:  none
    """
    # point board init
    board = Board(player)
    # dice init
    dice = Dice()

    rolling = input("Enter oder Eingabe für Würfeln! oder 'p' für Punkteanzeige oder 'q' zum Beenden")

    if rolling == 'p':
        # show point board for player
        print(board.table())
        state(player)
    elif rolling == 'q':
        print("Bis bald!")
        exit()
    else:
        # round 1
        dice.throw(5)
        # rounds 2 - 3
        for i in range(2):
            print("Deine Würfel Spieler", player.name, ": ", " ".join(map(str, dice.eyes)))

            reroll = dice.rethrow()

            for index in reroll:
                dice.eyes[index - 1] = random.randint(1, 6)
        # final eyes
        print("Endliches Ergebnis", player.name, ": ", " ".join(map(str, dice.eyes)), "\n")

        # insert points
        board.choice_cat(dice.eyes)
        print(board.table())

        return

def game_loop():
    """
    The game loop

    :return: none
    """

    player_list = []
    current_player_id = 0

    """
    init the game; create player
    """
    while True:
        player_name = input("Spielernamen einfügen oder 'q' zum Beenden der Spielereingabe: ")

        if len(player_name) <= 0:
            print("Spielername muss Zeichen enthalten ...")
            game_loop()

        if (player_name.lower() == "q"):
            if len(player_list) <= 0:
                print("Sicher, dass Sie die Eingabe beenenden wollen? Es wurden keine Spieler eingetragen.")
                wahl = input("y/n")
                if wahl == "y":
                    print("Bis bald!")
                    break
                else:
                    game_loop()
            else:
                break

        # instance player obj
        player = Player(player_name)
        player_list.append(player)

    """
    manage the rounds
    """
    while any(player.round < 13 for player in player_list):
        current_player = player_list[current_player_id]

        print("Runde von: ", player_list[current_player_id].name, "Runde: ", player_list[current_player_id].round)

        # roll dice, reroll dice, insert points -> game logic
        state(current_player)

        # finally the last round: get bonus, calc ...
        if current_player.round == 12:
            board = Board(current_player)
            print(board.end())

        # win list
        winlist = []

        # reachs the last player the end ? then calc the winner ...
        if player_list.index(current_player) == len(player_list) - 1:
            if current_player.round == 12:
                print("\n Letzter Spieler beendete Runde 13 ... Gewinner ist ... \n ")

                """
                calc the winning player or it's a tie?
                """
                while True:

                    for i in range(len(player_list)):
                        winlist.append([player_list[i].name, sum(player_list[i].points.values())])

                    sorted_data = sorted(winlist, key=lambda x: x[1], reverse=True)

                    headwin = ["Name", "Punkte"]

                    print("Punkteliste \n", tabulate(sorted_data, headers=headwin, tablefmt="grid"))

                    for i in range(len(sorted_data)):
                        if sorted_data[i][1] == sorted_data[i + 1][1]:
                            print("Unentschieden!")
                            break
                        else:
                            print("Gewinner ist: ", sorted_data[0][0], "mit ", sorted_data[0][1], " Punkten!")
                            break
                    break

        # increase the player round
        current_player.round += 1
        # player id, % len() do that id is moving within player_list[]
        current_player_id = (current_player_id + 1) % len(player_list)

game_loop()
