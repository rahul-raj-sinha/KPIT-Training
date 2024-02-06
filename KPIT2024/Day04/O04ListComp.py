
l1 = list(range(1, 11))
print(f"l1 :{l1}")

squares = [x ** 2 for x in l1]
print(f"squares :{squares}")

print("-" * 60)

fruits = [
    ('apple', 285),
    ('orange', 60),
    ('pineapple', 150),
    ('grapes', 140),
    ('gauva', 110),
    ('watermelon', 75),
    ('banana', 50),
    ('strawberry', 350)
]

print(f"fruits :{fruits}")

print("-" * 60)
prices = ["fruit" for fruit in fruits]
print(f"prices :{prices}")

print("-" * 60)
prices = [fruit for fruit in fruits]
print(f"prices :{prices}")

print("-" * 60)
prices = [fruit[0] for fruit in fruits]
print(f"prices :{prices}")

print("-" * 60)
prices = [fruit[1] for fruit in fruits]
print(f"prices :{prices}")

print("-" * 60)
prices = [fruit[1] * 0.9 for fruit in fruits]
print(f"prices :{prices}")

print("-" * 60)
prices = [fruit[1] * 0.75 for fruit in fruits]
print(f"prices :{prices}")

print("-" * 60)
prices  = [fruit[1] for fruit in fruits if fruit[1] < 100]
print(f"prices :{prices}")

print("-" * 60)
prices = [[fruit[0], fruit[1], fruit[1] * 0.9, fruit[1] * 0.75]
          for fruit in fruits if fruit[1] > 100]
print(f"prices :{prices}")

print("-" * 60)
sentence = "the quick brown fox jumps over the lazy dog"
print(f"sentence :{sentence}")

print("-" * 60)
words = [word for word in sentence.split()]
print(f"words :{words}")

print("-" * 60)
words = [word for word in sentence.split() if word != 'the']
print(f"words :{words}")
