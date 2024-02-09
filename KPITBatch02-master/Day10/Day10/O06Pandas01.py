import pandas as pd

mydataset = {
    'cars':['Tata', 'Mahinra', 'Maruti'],
    'safety':[5, 3, 2]
}
print(mydataset)

pDf = pd.DataFrame(mydataset)
print(pDf)
print("Pandas Version :", pd.__version__ )

print("-" * 60)
cars = ['tata', 'maruti', 'hyundai', 'honda']
print(cars)
pSrs  = pd.Series(cars)
print(pSrs)
print("-" * 60)
print(pSrs[0])
print("-" * 60)
print(pSrs.values)

print("-" * 60)
pSrs1 = pd.Series(cars, index=['a', 'b', 'c', 'd'])
print(pSrs1)

print("-" * 60)
score = {'Sachin': 85, 'Sehwag': 120, 'Dravid': 45, 'Sourav': 60}
print(f"score :{score}")

plySrs = pd.Series(score)
print(plySrs)

print("-" * 60)
print(f"Dravid :{plySrs['Dravid']}")

print("-" * 60)
print(plySrs[plySrs>90])
print("-" * 60)
print(plySrs[plySrs<90])

print("-" * 60)
print("Sachin" in plySrs)
