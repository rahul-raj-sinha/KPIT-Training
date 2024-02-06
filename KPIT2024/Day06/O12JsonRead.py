
import json

JFR = open("C:\\Training\\PycharmProjects\\KPIT2024\\Data\\books.json", "r")
jsonFile = json.load((JFR))

# print(jsonFile)

for book in jsonFile['books']:
    print(book['name'])
    print("-" * len(book['name']))
    for k, v in book.items():
        print(k,  " => ", v)
    print("-" * 60)

