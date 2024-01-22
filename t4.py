
# "dev"

def main():
    # init obj
    dice = Dice()
    # round 1
    dice.throw(5)
    print(dice.eyes)
    # dice.rethrow()

    # rounds
    for i in range(2):
        print(" ".join(map(str, dice.eyes)))
        reroll = dice.rethrow()

        for index in reroll:
            dice.eyes[index - 1] = random.randint(1, 6)
    # final eyes
    print("Final", " ".join(map(str, dice.eyes)))

#main()

def test():

    player1 = Player("Adler")
    player1.set_points("Einer", 15)
    print(player1.get_points())

    player2 = Player("Baron")
    player2.set_points("Zweier", 30)
    print(player2.get_points())

#test()

def test2():

    player1 = Player("Jerome")
    board1 = Board(player1)

    player1.set_points("Einer", 3)
    player1.set_points("Zweier", 6)

    board1.table()

    player2 = Player("Ko")
    board2 = Board(player2)

    player2.set_points("Einer", 5)
    player2.set_points("Zweier", 9)

    board2.table()

#test2()

def test3():
    player_list = []
    board_list = []

    # init
    while True:
        player_name = input("Spielernamen einfügen oder 'q' zum Beenden der Spielereingabe: ")

        if len(player_name) <= 0:
            print("Spielername muss Zeichen enthalten ...")
            test3()

        if (player_name.lower() == "q"):
            if len(player_list) <= 0:
                print("Sicher, dass Sie die Eingabe beenenden wollen? Es wurden keine Spieler eingetragen.")
                wahl = input("y/n")
                if wahl == "y":
                    print("Good Bye")
                    break
                else:
                    test3()
            else:
                break

        player = Player(player_name)
        player_list.append(player)

        board = Board(player)
        board_list.append(board)

        #points test fill
        for player in player_list:
            player.set_points("Einer", 8)
            player.set_points("Zweier", 12)

        print("name", player.get_name())
        print("punkte", player.get_points())
        # Bonus test

        print(board.table())
        print(board.end())
#test3()

def test4():

    player = Player("Tim")

    board = Board(player)

    dice = Dice()

    #x = dice.throw(5)

    x = [1, 2, 3, 4, 5]

    board.choice_cat(x)

    print(board.table())

#test4()


