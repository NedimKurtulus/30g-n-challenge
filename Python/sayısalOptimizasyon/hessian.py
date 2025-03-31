import sympy as sp

def hessian_matrix(f, vars):
    """
    Verilen skaler fonksiyon f'in Hessian matrisini hesaplar.
    
    :param f: Skaler fonksiyon
    :param vars: Bağımsız değişkenlerin listesi
    :return: Hessian matrisi
    """
    hessian = sp.hessian(f, vars)
    return hessian

# Örnek: f(x, y) = x**2 + 3*x*y + y**2
x, y = sp.symbols('x y')
f = x**2 + 3*x*y + y**2

# Hessian matrisini hesaplayalım
hessian = hessian_matrix(f, [x, y])
print("Hessian Matrisi:")
sp.pprint(hessian)
