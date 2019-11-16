import numpy as np
import sympy as sp


l1, l2, l3 = sp.symbols("l1 l2 l3")

t01 = sp.Matrix([[np.cos(np.pi/4), -np.sin(np.pi/4), 0, 0],
                [np.sin(np.pi/4), np.cos(np.pi/4), 1, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1]])

t12 = sp.Matrix([[np.cos(np.pi/2), -np.sin(np.pi/2), 0, l1],
                [np.sin(np.pi/2), np.cos(np.pi/2), 1, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1]])
t23 = sp.Matrix([[np.cos(np.pi/6), -np.sin(np.pi/6), 0, l2],
                [np.sin(np.pi/6), np.cos(np.pi/6), 1, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1]])

t34 = sp.Matrix([[1, 0, 0, l3], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])


ans = t01.multiply(t12).multiply(t23).multiply(t34)

print(ans)

