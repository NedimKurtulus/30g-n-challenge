import numpy as np
from scipy.optimize import minimize

# Örnek hedef fonksiyonu: f(x) = (x - 2)^2
def objective_function(x):
    return (x - 2)**2

# Başlangıç tahmini
x0 = [0]

# BFGS algoritması ile optimizasyon
result = minimize(objective_function, x0, method='BFGS')

# Sonuçları yazdır
print("Optimum çözüm:", result.x)
print("Fonksiyon değeri:", result.fun)
