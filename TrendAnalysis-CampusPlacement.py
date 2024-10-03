#Campus Placement- Trend Analysis
import numpy as np
import matplotlib.pyplot as plt

x=np.array(["2017-18", "2018-19", "2019-20", "2020-21", "2021-22"])
y=np.array([45, 43, 80, 85, 92])
mylabels= np.array([45, 43, 80, 85, 92])
f1 = {
    "size":"15", 
    "color": "r"
}
f2 = {
    "size": 20, 
    "color": "darkgreen"
}
plt.title("Campus Placements- Trend Analysis", fontdict = f2, weight= "bold")
plt.xlabel("Years-------->", fontdict = f1, loc="right")
plt.ylabel("Percentage----->", fontdict= f1, loc ="top")
plt.plot(x, y, color= "darkblue")
plt.grid(axis= "y")
plt.show()
