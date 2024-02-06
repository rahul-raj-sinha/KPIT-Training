# Question 3

sentences = [
    "India is great",
    "Mera Bharath mahan",
    "Go India Go",
    "the quick brown fox jumps over the lazy dog"
]

for n in sentences:

    res = n.split(" ")
    if (res[::-1]==res):
        print(f"{n} is Palindrome")
    else:
        print(f"{n} is not Palindrome")








# for sentence in sentences:
#     reversed_sentence = ' '.join(reversed(sentence.split()))
#     print(f"Original: {sentence}")
#     print(f"Reversed: {reversed_sentence}")
#
#     if is_palindrome(sentence):
#         print("The original sentence is a palindrome.")
#     else:
#         print("The original sentence is not a palindrome.")
#
#     if is_palindrome(reversed_sentence):
#         print("The reversed sentence is a palindrome.\n")
#     else:
#         print("The reversed sentence is not a palindrome.\n")