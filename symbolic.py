import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

al, bt, m1, m0 = sp.symbols('al bt m1 m0')
lm = sp.symbols('lm')
bt = 27
al = 15.6
m0 = -1.143

m1 = -0.714
expr0 = - lm ** 3 + lm ** 2 * (- al * (m0 + 1) - 1) + lm * (- bt - al * m0) - al * bt * (m0 + 1)
expr1 = - lm ** 3 + lm ** 2 * (- al * (m1 + 1) - 1) + lm * (- bt - al * m1) - al * bt * (m1 + 1)

print(sp.solveset(expr0, lm))
print(sp.solveset(expr1, lm))

