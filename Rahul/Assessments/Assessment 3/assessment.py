# Ques 1
import re
st="https://www.google.com/search?h/petsexpert/siamese-cat-price-in-india/blog/macaws-prices-purchase-cost-supplies-food-and-more/mynextpet.in/macaw-parrot-price-in-india/"
# m=""
res=re.finditer(r"(.*?)/",st)
for i in res:
    s = i.start()
    e = i.end()
    # (st[s:e])
    print(f"The string found between:{i.start()} and {i.end()} : {st[s:e]}")







# Ques 2

def print_rangoli(n):
    alphabets = 'abcdefghijklmnopqrstuvwxyz'

    for i in range(n-1, -n, -1):
        r = '-'.join(alphabets[n-1:abs(i):-1] + alphabets[abs(i):n])
        print(r.center(4*n-3, '-'))

if __name__ == '__main__':
    size = int(input().strip())
    print_rangoli(size)




# Ques 3
e1 = open("emp1.dat", "r").readlines()
e2 = open("emp2.dat", "r").readlines()
e3 = open("emp3.dat", "r").readlines()
e4 = open("emp4.dat", "r").readlines()
e5 = open("emp5.dat", "r").readlines()
e6 = open("emp6.dat", "r").readlines()
e7 = open("emp7.dat", "r").readlines()
e8 = open("emp8.dat", "r").readlines()

s1 = open("stud1.dat", "r").readlines()
s2 = open("stud2.dat", "r").readlines()
s3 = open("stud3.dat", "r").readlines()
s4 = open("stud4.dat", "r").readlines()
s5 = open("stud5.dat", "r").readlines()
s6 = open("stud6.dat", "r").readlines()
s7 = open("stud7.dat", "r").readlines()

emp = e1[1:]+e2[1:]+e3[1:]+e4[1:]+e5[1:]+e6[1:]+e7[1:]+e8[1:]
stud = s1[1:]+s2[1:]+s3[1:]+s4[1:]+s5[1:]+s6[1:]+s7[1:]

female = 0
male = 0
total = emp + stud
for i in range(len(total)):
    if total[i][9] == "f":
        female += 1
    if total[i][9] == "m":
        male += 1
print("Female employee: ", female)
print("Male employee: ", male)
print("-"*60)
empt = []
for i in emp:
    empt.append(i.split(","))

stdt = []
for i in stud:
    stdt.append(i.split(","))

tot_salary = 0
for i in empt:
    tot_salary += int(i[4])
print("Total Salary: ", tot_salary)
print("-"*60)
uniq_dept = []
for i in empt:
    if i[3] not in uniq_dept:
        uniq_dept.append(i[3])
    else:
        continue
print(uniq_dept)
print("Count of employees: ", len(emp))
print("Count of student: ", len(stud))
print("-"*60)
passtd = 0
failtd = 0
for i in stdt:
    if (int(i[4][0:2]) > 35):
        passtd += 1
    else:
        failtd += 1

print("No. of Passing Student: ", passtd)
print("No. of Failed Student: ", failtd)
print("-"*60)
f1 = open("FruitSales1.dat", "r").readlines()
f2 = open("FruitSales2.dat", "r").readlines()
f3 = open("FruitSales3.dat", "r").readlines()
f4 = open("FruitSales4.dat", "r").readlines()
f5 = open("FruitSales5.dat", "r").readlines()

fruit = f1[1:]+f2[1:]+f3[1:]+f4[1:]+f5[1:]
frt = []
for i in fruit:
    frt.append(i.split(","))
uniq_fruit = []
for i in frt:
    if i[1] not in uniq_fruit:
        uniq_fruit.append(i[1])
    else:
        continue
print(uniq_fruit)
print("-"*60)

org = 0
app = 0
grp = 0
for i in frt:
    if (i[1] == "Orange"):
        org += int(i[3])
    if (i[1] == "Apple"):
        app += int(i[3])
    if (i[1] == "Grapes"):
        grp += int(i[3])
print("Total weight of Orange: ", org)
print("Total weight of Apple: ", app)
print("Total weight of Grapes: ", grp)
print("-"*60)
tot_quant = 0
for i in frt:
    tot_quant += int(i[3])

print("Total Quantity of Fruits: ", tot_quant)
