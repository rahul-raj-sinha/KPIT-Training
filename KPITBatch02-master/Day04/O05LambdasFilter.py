
lst = list(range(1, 25))
print(f"lst :{lst}")

even_num = list(filter(lambda x: x % 2 == 0, lst))
print(f"Even Numbers :{even_num}")

print("-" * 60)
sentence = "the quick brown fox jumps over the lazy dog"
words = list(filter(lambda word: word != 'the', sentence.split()))
print(f"words :{words}")
