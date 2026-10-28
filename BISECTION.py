from scipy import optimize
def f(x):
return x**3 - x - 2
root = optimize.bisect(f, 1, 2)
print(f"Approximate root: {root:.6f}")
#we use thi to find roots of a equation 
