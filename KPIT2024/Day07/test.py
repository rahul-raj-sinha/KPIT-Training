
from CallDecrClass import Calc, test


@test
def sum(x, y):
    return x * y


sum(2, 10)

c = Calc()
@c.test
def diff(x, y):
    return x - y

diff(10, 7)