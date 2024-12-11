dt = 0.01
num_steps = 5000
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# state = [xyz]

dt = 0.01
m_0 = -1.143
m_1 = -0.714
alpha = 15.6
beta = 27.0
'''
dt = 0.01
m_0 = -1.143
m_1 = -0.714
alpha = 15.6
beta = 24
'''


def nonlin_diode(x, m_0, m_1):
    return m_1 * x + 0.5 * (m_0 - m_1) * (abs( x + 1) - abs(x - 1))

def chua_circuit(state, alpha, beta):
    x = state[0]
    y = state[1]
    z = state[2]
    dx = alpha * (y - x - nonlin_diode(x, m_0, m_1))
    dy = x - y + z
    dz = - beta * y
    return np.array([dx, dy, dz])

def euler(state, d_var):
    res = [0, 0, 0]
    for i in range (3):
        tmp = state[i] + d_var[i] * dt
        res[i] = tmp
    return res

x = []
y = []
z = []
rand = []
initial_state = [1.50001, 0, -1.5]
state = initial_state
for i in range (num_steps):
    tmp = euler(state, chua_circuit(state, alpha, beta))
    x.append(state[0])
    y.append(state[1])
    z.append(state[2])
    print("ITERATION:", i)
    state = tmp

data = {'x': x, 'y': y, 'z': z}
df = pd.DataFrame(data)
df.to_csv('output2.csv', index=False)

# position of equilibrium
x_z_eq = (m_1 - m_0)/(m_1 + 1)

# ploting phase portrait
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
#ax.plot(x, y, z, label='integral curve')
ax.scatter(0, 0, 0, color = 'green', label = r'$E_3$')
ax.scatter(x_z_eq, 0, -x_z_eq, color = 'red', label = r'$E_1$')
ax.scatter(-x_z_eq, 0, x_z_eq, color = 'blue', label = r'$E_2$')

print("EQ:", x_z_eq )
plt.xlabel('X')
plt.ylabel('Y')

# plotting XY projection
fig2, ax2 = plt.subplots()
ax2.plot(z, y)
ax.legend()
plt.xlabel('X')
plt.ylabel('Y')
plt.show()


