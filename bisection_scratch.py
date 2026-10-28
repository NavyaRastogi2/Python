def func(x):
 return x*x - 4
def bisection(a, b, tol=0.0001):
  if func(a) * func(b) >= 0:
    print("Bisection method fails: f(a) and f(b) must have opposite signs.")
    return None
  while (b - a) >= tol:
    c = (a + b) / 2
    if func(c) == 0.0:
     break
    if func(c) * func(a) < 0:
     b = c
    else:
      a = c
  return c
root = bisection(1, 3)
print(f"The value of the root is: {root:.4f}")
