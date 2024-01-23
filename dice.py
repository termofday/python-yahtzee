import random

class Dice:

    """
    The dice object

    Attributes:
        ---
    """

    def __init__(self):
        self.eyes = []
    def throw(self, n):
        """

        Throws (int) n dice objects and append them to the [] eyes, then returns them to work with them.

        :param n: (int) the number of dices
        :return: (int) self.eyes
        """
        for i in range(n):
            self.eyes.append(random.randint(1, 6))
        return self.eyes

    def rethrow(self):
        """

        Rethrows the dices

        :return: [] or ? []
        """
        while True:

            rethrow_inp = input("\n Wähle Würfel zum neu Würfeln. Gebe Zahlen von 1 bis 5 mit Leerzeichen ein, Beispiel -> '1 2 3' für die ersten drei Würfel. \n Oder drücke Enter, um alle zu halten.\n")

            if rethrow_inp:
                try:
                    return list(map(int, rethrow_inp.split()))
                except ValueError:
                    print("Hier nur Zahlen eingeben. Deine Würfelreihe war: ", " ".join(map(str, self.eyes)))
            else:
                return []


