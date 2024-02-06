

letters = ['a', 'b', 'c', 'd', 'e']
print(letters)

for letter in letters:
    print(letter, end=" ")
print()

print("-" * 60)
for letter in enumerate(letters):
    print(letter[0], letter[1])

print("-" * 60)
print(list(enumerate(letters)))

print("-" * 60)
for index, letter in enumerate(letters):
    print(f"{index} \t {letter}")

print("-" * 60)
my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(my_list)

print("-" * 60)

for ind, lst in enumerate(my_list):
    print(f"{ind} \t {lst}")

print("-" * 60)
for ind, lst in enumerate(my_list):
    print(f"List({ind})")
    for id, lt in enumerate(lst):
        print(f"\t {id} \t {lt}")

print("-" * 60)