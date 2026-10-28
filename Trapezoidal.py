import numpy as np
from scipy.integrate import trapezoid
def f(x):
  return x**2
a, b, n = 0, 4, 8
x = np.linspace(a, b, n+1)
y = f(x)
result = trapezoid(y, x)
print(f"Approximate value of the integral: {result:.6f}")
