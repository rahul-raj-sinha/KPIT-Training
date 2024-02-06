
class TooYoung(Exception):
    pass


class TooOld(Exception):
    pass


class TooTiny(Exception):
    pass

try:
    age = 9
    if age < 18:
        raise TooYoung("You are young to vote......")
    elif age <= 6:
        raise TooTiny("You are too tiny to vote")
    elif age >100:
        raise TooOld("You are too old to vote")
except TooYoung as y:
    print(y)
except TooTiny as t:
    print(t)
except TooOld as o:
    print(o)
finally:
    print("The process of voting completed.......")

