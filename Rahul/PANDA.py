import pandas as pd
 
mydataset = {
    'cars': ['Tata', 'Mahindra', 'Maruti'],
    'safety': [5, 3, 2]
}
print(mydataset)
 
pdf = pd.DataFrame(mydataset)
print(pdf)
 
print('*' * 60)
cars = ['tata', 'maruti', 'hyundai', 'honda']
print(cars)
 
psrs = pd.Series(cars)
print(psrs[0])
 
print(psrs.values)
print('*' * 60)
 
psrs1 = pd.Series(cars, index=['a', 'b', 'c', 'd'])
print(psrs1)
print('*' * 60)
 
score = {'Sachin: 85', 'Sehwag: 120', 'Dravid: 45', 'Sourav: 60'}
print(f"Scores: {score}")
 
plsrs = pd.Series(score)
print(plsrs)
 
print(f"Dravid: {plsrs['Dravid']}")
