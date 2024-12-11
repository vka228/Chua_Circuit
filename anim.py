import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
dt = 0.01
m_0 = -1.143
m_1 = -0.714
alpha = 15.6
beta = 27.0
num_steps = 1000

def nonlin_diode(x, m_0, m_1):
    return m_1 * x + 0.5 * (m_0 - m_1) * (abs(x + 1) - abs(x - 1))

def chua_circuit(state, alpha, beta):
    x = state[0]
    y = state[1]
    z = state[2]
    dx = alpha * (y - x - nonlin_diode(x, m_0, m_1))
    dy = x - y + z
    dz = - beta * y
    return np.array([dx, dy, dz])

def euler(state, d_var):
    return [state[i] + d_var[i] * dt for i in range(3)]

# Prepare variables
x, y, z = [], [], []
initial_state = [1.50001, 0, -1.5]
state = initial_state

# Store the trajectory data
for i in range(num_steps):
    tmp = euler(state, chua_circuit(state, alpha, beta))
    x.append(tmp[0])
    y.append(tmp[1])
    z.append(tmp[2])
    state = tmp

# Save data to CSV
data = {'x': x, 'y': y, 'z': z}
df = pd.DataFrame(data)
df.to_csv('output2.csv', index=False)

# Create animation
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Set up formatting for the movie files
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Set limits based on max values
ax.set_xlim([min(x), max(x)])
ax.set_ylim([min(y), max(y)])
ax.set_zlim([min(z), max(z)])

# Initialize line plot
x_z_eq = (m_1 - m_0)/(m_1 + 1)
line, = ax.plot([], [], [], lw=2)
ax.scatter(0, 0, 0, color = 'green', label = r'$E_3$')
ax.scatter(x_z_eq, 0, -x_z_eq, color = 'red', label = r'$E_1$')
ax.scatter(-x_z_eq, 0, x_z_eq, color = 'blue', label = r'$E_2$')


def init():
    line.set_data([], [])
    line.set_3d_properties([])
    return line,

def update(frame):
    line.set_data(x[:frame], y[:frame])
    line.set_3d_properties(z[:frame])
    return line,

# Increase fps for faster animation
ani = FuncAnimation(fig, update, frames=num_steps, init_func=init, blit=True)

# Save the animation with increased fps
ani.save('chuas_circuit_evolution_lines_close_anot.mp4', writer='ffmpeg', fps=60)

plt.show()