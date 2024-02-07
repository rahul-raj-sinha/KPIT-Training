
print(range(1, 10))

l1 = list(range(1, 10))
print(f"l1 :{l1}")

print("-" * 60)
l2 = list(range(1, 11))
print(f"l2 :{l2}")

print("-" * 60)
for i in range(1, 26):
    # if (i > 20):
    #     break
    if (i % 2 == 1):
        continue
    print(i, end=" ")
else:
    print("\nCompleted the generation of even numbers")
print()

