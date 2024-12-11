import sympy as sp
import numpy as np
import matplotlib.pyplot as plt


al, bt, m1, m0 = sp.symbols('al bt m1 m0')
lm = sp.symbols('lm')
m1 = -0.714

bt_values = []
al_values = np.linspace(0, 5.5, 20)

for al_value in al_values:
    a = -(al_value * (m1 + 1) - 1)
    b = - (-al_value * m1 - bt)
    c = al_value * bt * (m1 + 1)

    p = b - (a ** 3) / 3
    q = c + (2 * a ** 3) / (27) - (a * b) / 3

    D = (q ** 2) / (4) + (p ** 3) / (27)

    # Solve for bt using D
    bt_solution = sp.solve(D - 1000, bt)

    # Append to bt_values
    bt_values.append(bt_solution[0])

# Output the results
print(bt_values)
plt.plot(al_values, bt_values)
plt.show()
