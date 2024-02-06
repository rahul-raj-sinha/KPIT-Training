
class Mynumbers:

    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.n = 1
        return self


    def __next__(self):
        if self.n <= self.max:
            res = self.n
            self.n += 1
            return res
        else:
            raise StopIteration

mynum = Mynumbers(10)
iterObj = mynum.__iter__()

print(next(iterObj))
print(next(iterObj))
print(next(iterObj))
print(next(iterObj))
print(next(iterObj))
print(next(iterObj))
print(next(iterObj))
print(next(iterObj))
print(next(iterObj))
print(next(iterObj))

