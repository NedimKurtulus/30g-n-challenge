import sympy as sp

def gradient_vector(func, variables):
    grad = [sp.diff(func, var) for var in variables]
    return grad

# Örnek: f(x, y) = x**2 + 3*y**2
x, y = sp.symbols('x y')
f = x**2 + 3*y**2

grad = gradient_vector(f, [x, y])
print("Gradyan Vektörü:", grad)
