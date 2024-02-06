
for i in range(5, 0, -1):
    for k in range(1, 6-i):
        print(" ", end="")
    for j in range(1, i+1):
        print(j, end=" ")
    print()

for i in range(2, 6):
    for k in range(1, 6-i):
        print(" ", end="")
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()



"""

1 2 3 4 5
 1 2 3 4
  1 2 3
   1 2
    1
   2 1
  3 2 1
 4 3 2 1
5 4 3 2 1
  

"""
width = 50
price_width = 10
item_width = width - price_width

header_fmt = '{{:{}}}{{:>{}}}'.format(item_width, price_width)
fmt = '{{:{}}}{{:>{}.2f}}'.format(item_width, price_width)
print('=' * width)
print(header_fmt.format('Item', 'Price'))
print('=' * width)

print(fmt.format('Apples', 0.4))
print(fmt.format('Pears', 0.5))
print(fmt.format('Cantaloupes', 1.92))
print(fmt.format('Dried Apricots (16 oz.)', 8))
print(fmt.format('Prunes (4 lbs.)', 12))
print('=' * width)

