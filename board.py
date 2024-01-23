from point_method import *
from tabulate import tabulate

class Board:
    """
    Board for points, addpoints and draw points table.

    Attributes:
        (obj) player
    """
    def __init__(self, player):
        self.player = player

# create table for console
    def table(self):
        """
        Draws the pointtable

        :return: tabulate()
        """
        head = ["Kategorie"]
        head.append("Punkte " + self.player.get_name())

        board = []

        player_points = self.player.get_points()

        for category, points in player_points.items():
                board.append([category, points])

        return (tabulate(board, headers=head, tablefmt="grid"))

    def addpoints(self, cat, dice):
        """
        add points to the player object

        :param cat: (str) the category of (dict) player.points
        :param dice: [] list of dices
        :return: points
        """
        cat = cat.lower()

        if self.player.points[cat] == None:

            if cat == "einer":
                return eyes(dice, 1)

            if cat == "zweier":
                return eyes(dice, 2)

            if cat == "dreier":
                return eyes(dice, 3)

            if cat == "vierer":
                return eyes(dice, 4)

            if cat == "fünfer":
                return eyes(dice, 5)

            if cat == "sechser":
                return eyes(dice, 6)

            if cat == "dreierpasch":
                return pasch(dice, 3)

            if cat == "viererpasch":
                return pasch(dice, 4)

            if cat == "fullhouse":
                return fullhouse(dice)

            if cat == "kleinestraße":
                return kleine_strasse(dice)

            if cat == "großestraße":
                return grosse_strasse(dice)

            if cat == "kniffel":
                return kniffel(dice)

            if cat == "chance":
                return sum(dice)

    def choice_cat(self, dice):
        """

        Choice the category and add points of dices.

        :param self:
        :param dice: [] list of dices
        :return: none
        """
        while True:

            cat_inp = input("Wähle eine Kategorie; gebe 'h' für Hilfe ein: \n")

            cat_inp = cat_inp.lower()

            try:

                if cat_inp == "h":
                    print("Hilfe: Folgende Kategorien stehen zur Wahl (außer 'Bonus'):",  self.player.points.keys())
                    continue

                if self.player.points[cat_inp] is not None:
                    print("Feld bereits gespielt.")
                    continue

                if cat_inp == "bonus":
                    print("Bonus wird ab 63 Punkten freigeschaltet ... Cheater!")
                    self.choice_cat(dice)

                for i in self.player.points.keys():
                    if cat_inp == i:
                        self.player.set_points(cat_inp, self.addpoints(cat_inp, dice))
                        break
            except:
                print("Eingabefehler; versuche es nochmal!")
                self.choice_cat(dice)

            break

    def end(self):
        """
        Calc the player points, add bonus when reach the limit.
        :param self:
        :return: sum points of player
        """
        try:
            if self.player.points["einer"] + self.player.points["zweier"] + self.player.points["dreier"] + self.player.points["vierer"] + self.player.points["fünfer"] + self.player.points["sechser"] >= 63:
                self.player.set_points("bonus", 35)
                print("Bonus von 35 Punkten erhalten, da 63 Punkte. Glückwunsch!")
            else:
                self.player.set_points("bonus", 0)

            total = sum(self.player.points.values())
            return (f"{self.player.name} deine Punkte total: {total}")
        except:
            return ("Fehler in Punkte Total ...")