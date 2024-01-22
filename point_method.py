# methods for addpoints in Board

# def eyes for addpoints()
def eyes(dice, n):
    points = 0
    for i in dice:
        if i == int(n):
            points += int(n)
    return points

# def pasch for addpoints()
def pasch(dice, n):
    points = 0
    for i in dice:
        if dice.count(i) >= n:
            points += sum(dice)
            return points
        else:
            return points

# def fullhouse for addpoints()
def fullhouse(dice):
    points = 0
    # Full House == Dreier o. Viererpasch + Zwei Gleiche
    # Also set() -> allowed only unique items
    # so an dice [] with len of two will be a full house ... or?
    dice = sorted(set(dice))
    if len(dice) == 2:
        points = 25
        return points
    else:
        return points

# def small street for addpoints()
def kleine_strasse(dice):
    points = 0
    dice = str(sorted(dice))
    if "1, 2, 3, 4" in dice:
        points = 30
        return points
    elif "2, 3, 4, 5" in dice:
        points = 30
        return points
    elif "3, 4, 5, 6" in dice:
        points = 30
        return points
    else:
        return points

# def big street for addpoints()
def grosse_strasse(dice):
    points = 0
    dice = str(sorted(set(dice)))
    if "[1, 2, 3, 4, 5]" in dice:
        points = 40
        return points
    elif "[2, 3, 4, 5, 6]" in dice:
        score = 40
        return points
    else:
        return points

# def kniffel for addpoints()
def kniffel(dice):
    points = 0
    count = 1
    for i in range(0, 4):
        if dice[i] == dice[i + 1]:
            count += 1
    if count == 5:
        points = 50
        return points
    else:
        return points
