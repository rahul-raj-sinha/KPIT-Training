# # 1. Find sequences of lowercase letters joined with an underscore:
# import re


# def find_sequences(input_string):
#     pattern = re.compile(r'\b[a-z]+_[a-z]+\b')
#     sequences = re.findall(pattern, input_string)
#     return sequences


# # Example usage:
# input_string = "abc_def xyz_ghi abc_xyz"
# result = find_sequences(input_string)
# print(result)

# ##########################################################################
# # 2. Validate email IDs:
# # import re


# def validate_email(email):
#     pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
#     return re.match(pattern, email) is not None


# # Example usage:
# emails = ["abc@gmail.com", "xyz.k@ibm.com", "abc_get@wipro.com"]
# for email in emails:
#     print(f"{email}: {validate_email(email)}")

# ##########################################################################
# # 3. Regex to find words starting with vowels:
# # import re


# def count_words_starting_with_vowels(input_string):
#     pattern = re.compile(r'\b[aeiouAEIOU]\w*\b')
#     matches = re.findall(pattern, input_string)
#     return len(matches)


# # Example usage:
# input_string = "apple banana orange Elephant Ink"
# count = count_words_starting_with_vowels(input_string)
# print(count)

# ##########################################################################
# # 4. Regex to find words without certain characters:
# # import re


# def count_words_without_chars(input_string):
#     pattern = re.compile(r'\b(?![aect])\w+\b')
#     matches = re.findall(pattern, input_string)
#     return len(matches)


# # Example usage:
# input_string = "cat dog rat hat"
# count = count_words_without_chars(input_string)
# print(count)

# ##########################################################################
# # 5. Filter elements not containing 'e':
# elements = ['apple', 'orange', 'kiwi', 'banana', 'grape']
# filtered_elements = [element for element in elements if 'e' not in element]
# print(filtered_elements)

# or

# import re

# elements = ['apple', 'orange', 'kiwi', 'banana', 'grape']
# filtered_elements = [element for element in elements if not re.search(r'e', element)]
# print(filtered_elements)


# ##########################################################################
# # 6. Display lines not containing 'start':
# input_string = "Line 1\nStart with line 2\nLine 3\nDon't start with start"
# lines_not_containing_start = [line for line in input_string.split(
#     '\n') if 'start' not in line.lower()]
# print(lines_not_containing_start)

# or

# import re

# input_string = "Line 1\nStart with line 2\nLine 3\nDon't start with start"
# lines_not_containing_start = [line for line in input_string.split('\n') if not re.search(r'start', line, re.IGNORECASE)]
# print(lines_not_containing_start)


# ##########################################################################
# # 7. Filter elements containing 4 surrounded by word characters:
# elements = ['word4', '4number', 'word44', 'word4word']
# filtered_elements = [
#     element for element in elements if re.search(r'\b\w*4\w*\b', element)]
# print(filtered_elements)

# or

# import re

# elements = ['word4', '4number', 'word44', 'word4word']
# filtered_elements = [element for element in elements if re.search(r'\b\w*4\w*\b', element)]
# print(filtered_elements)


# ##########################################################################
# # 8. Filter elements starting with 'den' or ending with 'ly':
# elements = ['denial', 'dentist', 'daily', 'weekly']
# filtered_elements = [element for element in elements if element.startswith(
#     'den') or element.endswith('ly')]
# print(filtered_elements)

# or

# elements = ['denial', 'dentist', 'daily', 'weekly']
# filtered_elements = [element for element in elements if re.match(r'den|\w*ly$', element)]
# print(filtered_elements)

# ###########################################################################
# # 9. Replace matching elements from a list:
# input_string = "This is an example string with word1 and word2."
# items_to_replace = ['word1', 'word2']
# for item in items_to_replace:
#     input_string = re.sub(re.escape(item), 'X', input_string)

# print(input_string)

# ############################################################################
# # 10. Extract hex character sequences:
# input_string = "0xabc 0X1aB 123abc"
# hex_sequences = re.findall(r'\b0[xX][0-9a-fA-F]+\b', input_string)
# print(hex_sequences)

# ############################################################################
# # 11. Count words with at least two consecutive repeated alphabets:

# def count_words_with_repeated_alphabets(input_string):
#     pattern = re.compile(r'\b\w*([a-zA-Z])\1\w*\b')
#     matches = re.findall(pattern, input_string)
#     return len(matches)

# # Example usage:
# input_string = "oppressed abandon accommodation bloodless carelessness committed apparition innkeeper occasionally afforded embarrassment foolishness depended successfully succeeded possession cleanliness suppress"
# count = count_words_with_repeated_alphabets(input_string)
# print(count)

###############################################################################
# Extract all whole words only if they are preceded by = or : and followed by : or ..
# import re

# ip = 'Poke,on=-=so_good:ink.to/is(vast)ever2-sit'

# pattern = re.compile(r'(?<=[=:])\b\w+\b(?=[:.])')
# result = re.findall(pattern, ip)

# print(result)

###############################################################################
# Remove the leading and trailing whitespaces from all the individual fields where , is the field separator.
# def clean_csv_fields(csv_string):
#     fields = csv_string.split(',')
#     cleaned_fields = [field.strip() for field in fields]
#     cleaned_csv = ','.join(cleaned_fields)
#     return cleaned_csv

# csv1 = ' comma  ,separated ,values \t\r '
# csv2 = 'good bad,nice  ice  , 42 , ,   stall   small'

# cleaned_csv1 = clean_csv_fields(csv1)
# cleaned_csv2 = clean_csv_fields(csv2)

# print(cleaned_csv1)
# print(cleaned_csv2)

# OR

# import re

# def clean_csv_fields(csv_string):
#     pattern = re.compile(r'\s*,\s*')
#     cleaned_fields = [field.strip() for field in re.split(pattern, csv_string)]
#     cleaned_csv = ','.join(cleaned_fields)
#     return cleaned_csv

# csv1 = ' comma  ,separated ,values \t\r '
# csv2 = 'good bad,nice  ice  , 42 , ,   stall   small'

# cleaned_csv1 = clean_csv_fields(csv1)
# cleaned_csv2 = clean_csv_fields(csv2)

# print(cleaned_csv1)
# print(cleaned_csv2)
