#Analysis of the highest packages-placements from 2017-2022 of ABC College
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

x=np.array(["2017-18", "2018-19", "2019-20", "2020-21", "2021-22"])
y=np.array([6, 7, 9, 10, 10])
colors= np.array(["g", 'k', "g", "k", "g"])
plt.bar(x, y, color=colors)
plt.grid(axis="y")
plt.plot(x, y, "_--r")
f1= {
    "family":"serif", 
    "color":"darkblue", 
    "size":20
}
f2= {
    "family":"serif", 
    "color":"purple", 
    "size":16
}
plt.title("Highest salary package in ABC college throughout the years 2017-22", fontdict= f1)
plt.xlabel("Years-------->", fontdict= f2)
plt.ylabel("Packages in lakhs(*1,00,000)--------->", fontdict=f2)
plt.show()
