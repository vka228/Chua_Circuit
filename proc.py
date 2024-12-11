import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from main import dt
from main import num_steps
import random

#timestep = int(num_steps / 10000)
timestep = 2000
fileName = 'output.csv'
data = pd.read_csv(fileName)
x = np.array(data['x'].dropna())
y = np.array(data['y'].dropna())
z = np.array(data['z'].dropna())

# forming array of ones and zeros
restxt = 'restxt.txt'
file = open(restxt, 'w')
res = []
i = 0
while (i < len(x)):
    if (x[i] * y[i] * z[i] > 0):
        res.append(0)
        file.write('0')
    else:
        res.append(1)
        file.write('1')
    i += timestep
file.close()


b = 0
num_bin = 10
res_dec = []
while ( b + num_bin < len(res)):
    tmp = ''
    for j in range (num_bin):
        tmp += str(res[b + j])
    b += num_bin
    res_dec.append(int(tmp, 2))
print(res_dec)

# plotting decimal histogramm
fig4, ax4 = plt.subplots()
n_bins = 512
plt.hist(res_dec, bins = n_bins)

# plotting binary map
fig, ax = plt.subplots()
res_cut = res
u = []
i = 0
for b in range (int(len(res_cut) ** 0.5)):
    i_1 = i + int(len(res_cut) ** 0.5)
    tmp = res_cut[i: i_1]
    i = i_1
    u.append(tmp)
print(res_cut)
pcm = ax.pcolormesh(u, cmap=plt.cm.jet)
plt.colorbar(pcm, ax=ax)
ax.set_title("Chua PRNG")


fig3, ax3 = plt.subplots()
plt.scatter(np.linspace(0, len(res), len(res)),res )
print(len(x))

fig4, ax4 = plt.subplots()
plt.plot(x, y)

# plotting binary map of random values from python
u_2 = []
for i in range (len(u)):
    tmp = []
    for j in range (len(u)):
        tmp.append(random.randint(0, 1))
    u_2.append(tmp)

fig5, ax5 = plt.subplots()
pcm = ax5.pcolormesh(u_2, cmap=plt.cm.jet)
ax5.set_title('Python PRNG')





print("RESULTS:", len(res))
plt.show()