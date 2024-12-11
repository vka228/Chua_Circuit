import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

fileName = 'output2.csv'
data = pd.read_csv(fileName)
y = np.array(data['y'].dropna())
z = np.array(data['z'].dropna())

plt.plot(y, z)
plt.show()