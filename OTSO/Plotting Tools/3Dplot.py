import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

R = 6371.2
Re = 1

data = pd.read_csv("Custom_Location_Name_Trace.csv")
X = data["X"]
Y = data["Y"]
Z = data["Z"]

data2 = pd.read_csv("Custom_Location_Name2_Trace.csv")
X2 = data2["X"]
Y2 = data2["Y"]
Z2 = data2["Z"]

data3 = pd.read_csv("Custom_Location_Name3_Trace.csv")
X3 = data3["X"]
Y3 = data3["Y"]
Z3 = data3["Z"]

xGSM = []
yGSM = []
zGSM = []

fig = plt.figure(figsize=(4,4))

ax = fig.add_subplot(projection='3d')

u = np.linspace(0, 2 * np.pi, 20)
v = np.linspace(0, np.pi, 20)
x = R * np.outer(np.cos(u), np.sin(v))
y = R * np.outer(np.sin(u), np.sin(v))
z = R * np.outer(np.ones(np.size(u)), np.cos(v))

ax.plot_wireframe(x, y, z, color='blue')

ax.set_xlabel("X")

ax.set_ylabel("Y")

ax.set_zlabel("Z")

plt.gca().set_aspect('auto', adjustable='box')

plt.xlim(-10000, 10000)
plt.ylim(-10000, 10000)
ax.set_zlim(-10000, 10000)

ax.plot(X, Y, Z, color = 'black')
ax.plot(X2, Y2, Z2, color = 'green')
ax.plot(X3, Y3, Z3, color = 'red')


plt.show()