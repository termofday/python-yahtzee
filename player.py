class Player:
    """
    The Player Object with Name, Round and Pointfields

    Attributes:
        name (str): The name of Player
        round (int): The number of Round
        points (dict): The keys:values of Games

    """
    def __init__(self, name):
        self.name = name
        self.round = 0
        self.points = {
            "einer": None,
            "zweier": None,
            "dreier": None,
            "vierer": None,
            "fünfer": None,
            "sechser": None,
            "bonus": None,
            "dreierpasch": None,
            "viererpasch": None,
            "full House": None,
            "kleine Straße": None,
            "große Straße": None,
            "kniffel": None,
            "chance": None
        }

    def get_name(self):
        """
        Returns Player names

        Returns: (str) self.name
        """
        return self.name

    def set_points(self, cat, value):
        """

        Sets the field in dictionary (dict) self.points

        :param cat: (str) The value of Category for the points (dict)
        :param value: (int) The value of points
        :return: none
        """
        self.points[cat] = value

    def get_points(self):
        """

        Returns the whole (dict) points dictionary.

        :return: (int) self.points
        """
        return self.points
