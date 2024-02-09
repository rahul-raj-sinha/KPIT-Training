import re

st = "This is sample string"
if (re.search(r"^This", st)):
    print(True)
else:
    print(False)

if (re.search(r"string$", st)):
    print(True)
else:
    print(False)

st = "bat bat"
pattern = r"b.t"
res = re.search(pattern, st)
if res:
    print(True)
    print(res.group(0))
else:
    print(False)

st = "bt"
res = re.search(r'ba*t', st)    #True because a* means 0 occurance or more
if res:
    print(True)
else:
    print(False)

st = "bat"
# True because a? means 0 occurance or 1 occurance
res = re.search(r'ba?t', st)
if res:
    print(True)
else:
    print(False)

st = "bat"
res = re.search(r'ba+t', st)    # True because a+ means 1 occurance or more
if res:
    print(True)
else:
    print(False)

st = "baaat"
res = re.search(r'ba{3}t', st)    # True because {n} means exact n numbers
if res:
    print(True)
else:
    print(False)

st = "baaaaat"
res = re.search(r'ba{3,}t', st)    # True because {n,} means atleast n numbers
if res:
    print(True)
else:
    print(False)

st = "baaaaaaaat"
res = re.search(r'ba{3,5}t', st)    # True because {n,m} means min n and max m
if res:
    print(True)
else:
    print(False)

st = "bdh9t"
res = re.search(r'b[a-zA-Z0-9]{3}t', st)
if res:
    print(True)
else:
    print(False)

st = "boat"
res = re.search(r'b(oa|a)t', st)
if res:
    print(True)
else:
    print(False)

st = "LCNO-TEL-72-2010-0001"

pattern = r"LCNO-(KAR|KER|APN|TND|TEL|MAH)-([0-6][1-9]|[1-7][0-3])-2[0-9]{3}-(?!0000)[0-9]{4}"
pattern2 = r"LCNO-(KAR|KER|APN|TND|TEL|MAH)-([0-6][1-9]|[1-7][0-3])-2\d{3}-(?!0000)\d{4}"

res = re.search(pattern, st)
if res:
    print("Valid Licensce")
    print(res.group(0))
else:
    print("Invalid Licensce")

st = "asTpr There tHe quick brown fox jumps over the lazy dog"
# res = re.search(r"\w+\s\w+\s\w+\s\w+\s\w+\s\w+\s\w+\s\w+\s\w+\s", st)
# res = re.findall(r"\b(t\w+)", st, re.I)
# print(len(res))
res = re.search(r"dog\Z", st)
if res:
    print(True)
    print(res.group(0))
else:
    print(False)

ptb2 = r"([0-2][1-9]|[1-3][0-1])(/|-)(0[1-9]|1[0-2])(\2)(19[0-9]{2}|2[0-9]{3})"
st = "28/02/1923"
# pattern = r"(\w+)\s(\w+)\s(\w+)\s(\2)"
res = re.search(ptb2, st)
if res:
    print(True)
    print(res.group(0))
else:
    print(False)

st = "The quick brown fox jumps over the lazy dog fox"
res = re.search(r"fox", st)

print("Rejected string: ", st[:res.start()])
print("Matched string: ", res.group(0))
print("Unchecked String: ", st[res.end():])

res2 = re.search(r"fox", st[res.end():])
if res2:
    print(True)
    print(res2.group(0))
else:
    print(False)


function:-
findall
finditer
sub

import re
st = """
the quick brown fox jumps over the lazy dog.
the quick brown fox jumps over the lazy dog.
the quick brown fox jumps over the lazy dog.
the quick brown fox jumps over the lazy dog.
the quick brown fox jumps over the lazy dog.
the quick brown fox jumps over the lazy dog.
the quick brown fox jumps over the lazy dog.
the quick brown fox jumps over the lazy dog.
the quick brown fox jumps over the lazy dog.
the quick brown fox jumps over the lazy dog.
the quick brown fox jumps over the lazy dog.
the quick brown fox jumps over the lazy dog.
"""

pattern = r"t\w+"
# compile convert the string into a regex expression
regex = re.compile(r"t\w+")
res = re.findall(regex, st)
print(f"res: {res}")
print(len(res))

res = re.finditer(r"t\w+", st)
for i in res:
    s = i.start()
    e = i.end()
    print(f"The string found between:{i.start()} and {i.end()} : {st[s:e]}")

st = "the quick brown fox jumps over the lazy dog."
res = re.sub(r"t\w+", "The", st, count=1)
print(res)
res = re.sub(r"fox", "tiger", st, count=1)
print(f"res: {res}")

st = "the quick brown fox jumps over the lazy dog."
res = re.sub(r"fox", lambda word: word.upper(), st)
print(res)








import re

# 6. Validate an IPv4 address
ipv4_address = input("Enter an IPv4 address: ")
ipv4_pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
if re.match(ipv4_pattern, ipv4_address):
    print("Valid IPv4 address.")
else:
    print("Invalid IPv4 address.")

# 7. Extract all URLs from a given text
text = input("Enter text containing URLs: ")
url_pattern = r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+'
urls_found = re.findall(url_pattern, text)
print("URLs found:", urls_found)

# 8. Validate an email address (more comprehensive validation)
email = input("Enter an email address: ")
email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
if re.match(email_pattern, email):
    print("Valid email address.")
else:
    print("Invalid email address.")

# 9. Extract all words containing consecutive vowels from a sentence
sentence = input("Enter a sentence: ")
vowel_pattern = r'\b\w*[aeiou]{2,}\w*\b'
words_with_consecutive_vowels = re.findall(vowel_pattern, sentence)
print("Words with consecutive vowels:", words_with_consecutive_vowels)

# 10. Check if a string is a palindrome (ignoring spaces, punctuation, and case)
string = input("Enter a string to check for palindrome: ")
cleaned_string = re.sub(r'[^a-zA-Z]', '', string.lower())
if cleaned_string == cleaned_string[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")




import re

# 11. Extract all capitalized words from a sentence
sentence = input("Enter a sentence: ")
capitalized_words = re.findall(r'\b[A-Z][a-z]*\b', sentence)
print("Capitalized words:", capitalized_words)

# 12. Validate a MAC address (format: XX:XX:XX:XX:XX:XX)
mac_address = input("Enter a MAC address: ")
mac_pattern = r'^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$'
if re.match(mac_pattern, mac_address):
    print("Valid MAC address.")
else:
    print("Invalid MAC address.")

# 13. Extract all words with numeric digits from a sentence
sentence = input("Enter a sentence: ")
words_with_digits = re.findall(r'\b\w*\d\w*\b', sentence)
print("Words with digits:", words_with_digits)

# 14. Validate a password (criteria: at least 8 characters, containing at least one uppercase letter, one lowercase letter, one digit, and one special character)
password = input("Enter a password: ")
password_pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
if re.match(password_pattern, password):
    print("Valid password.")
else:
    print("Invalid password.")

# 15. Extract all words with a specific length from a sentence
sentence = input("Enter a sentence: ")
word_length = int(input("Enter the word length to extract: "))
words_with_length = re.findall(rf'\b\w{{{word_length}}}\b', sentence)
print(f"Words with length {word_length}:", words_with_length)
