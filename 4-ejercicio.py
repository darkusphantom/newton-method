import numpy as np

def f(x):
    return x - np.tan(x)

def df(x):
    return 1 - (1/np.cos(x))**2

def newton_method(x0, f, df, tol=1e-7, max_iter=100):
    x = x0
    for _ in range(max_iter):
        x1 = x - f(x)/df(x)
        if abs(x1 - x) < tol:
            return x1
        x = x1
    return None

roots = []
x0 = 0.1
for _ in range(10):
    root = newton_method(x0, f, df)
    roots.append(root)
    x0 = root + 0.1

print("Las primeras 10 raíces positivas son:")
for i, root in enumerate(roots, 1):
    print(f"Raíz {i}: {root}")
