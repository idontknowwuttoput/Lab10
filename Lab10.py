import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ps1 = pd.Series( [1,3,5,7,9] )
ps2 = pd.Series( [ 2,4,6,8,10] )
ps = ps1 + ps2
print(ps)
ps = ps2 - ps1
print(ps)
ps = ps2 * ps1
print(ps)
ps = ps2 / ps1
print(ps)

print(ps2 == ps1)
print(ps2 > ps1)
print(ps2 < ps1)

dict= {'a': 10, 'b': 20, 'c':30, 'd':40, 'e':50}
psd = pd.Series(dict)
psd



np_array = np.array([10, 20, 30, 40, 50])
print(np_array)
ps_numArray = pd.Series(np_array)
ps_numArray

s1 = pd.Series([10, '20', 'python', '40', '50'])
print(s1)

s2 = pd.to_numeric(s1, errors='coerce')
print(s2)

s2 = s2.append(pd.Series([60,70]))
print(s2)

sorted_s2 = s2.sort_values()
print(sorted_s2)

sorted_s2.index = [1,2,3,4,5,6,7]
print(sorted_s2)

sorted_s2.mean()
format_sorted_s2 = "{:.2f}".format(sorted_s2.mean())
print(format_sorted_s2)

sorted_s2.median()
format_sorted_s2 = "{:.2f}".format(sorted_s2.median())
print(format_sorted_s2)

sorted_s2.std()
format_sorted_s2 = "{:.2f}".format(sorted_s2.std())
print(format_sorted_s2)


var1 = s2.values.tolist()
print(var1)
print(type(var1))

npArray = np.array(var1)
print(npArray)
print(type(npArray))


import pandas as pd
colorList = pd.Series([['Red', 'Blue', 'Yellow'], ['Red', 'White'], ['Black']])
print(colorList)

s = colorList.apply(pd.Series).stack().reset_index(drop=True)
print(s)


list = [1,2,3,4,5]
df = pd.DataFrame(list)
print(df)

import pandas as pd
listofList = [['Mike',5],['Peter',10],['Thomas',15]]
df = pd.DataFrame(listofList,columns=['Name','Age'])
print(df)


dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"], "capital": ["Brasilia", "Moscow", "New Dehil", "Beijing", "Bloemfontein"], "area": [8.516, 17.10, 3.286, 9.597, 1.221], "population": [200.4, 143.5, 1252, 1357, 52.98]}
brics = pd.DataFrame(dict)
print(brics)

brics.index = ["BR", "RU", "IN", "CH", "SA"]
print(brics)

cars = pd.read_csv('mtcars.csv')
print(cars)

print(cars.head())
print(cars.tail())

print(cars.columns)

print(cars.index)

car = cars['model'].str.split(' ', n = 1, expand = True)
print(car.head())


cars = cars.assign(car_brand = car[0])
cars = cars.assign(car_model = car[1])
cars[cars['car_brand'] == 'Mazda']

cars.index = cars['model']
del cars['model']
print(cars.index)

print(cars.iloc[:,:6].describe())

print(cars.head(10))

print(cars.mean())


plt.scatter(cars['mpg'], cars['hp'])
plt.savefig("graph")
plt.show()

ax = cars[['car_model', 'hp']].plot(kind='bar', title="Horse Powder Comparison", figsize=(10, 10), legend=True, fontsize=12)
plt.savefig("barChart1")
plt.show()

ax = cars['hp'].plot(kind='hist', title="Range in HP", figsize=(10, 10), legend=True, fontsize=12)
plt.show()
my_fig = ax.get_figure()
my_fig.savefig("Car_Range_HP.png")

ps = cars['mpg'].sort_values()
index = np.arange(len(ps.index))
plt.xlabel('Models', fontsize=5)
plt.ylabel('Miles per gallon', fontsize=10)
plt.xticks(index, ps.index, fontsize=10, rotation=90)
plt.title('Miles per gallon of Cars')
plt.bar(ps.index, ps.values)
plt.savefig("barChart2")
plt.show();

from scipy.stats import linregress
stats = linregress(cars['mpg'], cars['hp'])
m = stats.slope
b = stats.intercept
plt.figure(figsize=(5,5))
plt.scatter(cars['mpg'], cars['hp'])
plt.plot(cars['mpg'], m * cars['mpg'] + b, color="red", linewidth=3)
plt.savefig("LinearGraph")
plt.show()