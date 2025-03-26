import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import least_squares

# Gerçek fonksiyon: y = a * exp(b * x) + c
def true_function(x, a, b, c):
    return a * np.exp(b * x) + c

# Hata fonksiyonu: Gerçek değerler ile tahmin arasındaki fark
def residuals(params, x, y_true):
    a, b, c = params
    return true_function(x, a, b, c) - y_true

# Veri oluşturma (Gerçek parametreler: a=2.5, b=-1.3, c=0.5)
np.random.seed(42)
x_data = np.linspace(0, 5, 50)  # 0 ile 5 arasında 50 nokta
y_real = true_function(x_data, 2.5, -1.3, 0.5)
y_noisy = y_real + 0.2 * np.random.randn(*y_real.shape)  # Gürültü ekledik

# Başlangıç tahmini (Rastgele değerler)
initial_guess = [1.0, -1.0, 1.0]

# LM algoritmasını çalıştır
result = least_squares(residuals, initial_guess, args=(x_data, y_noisy), method='lm')

# Optimum parametreleri al
a_opt, b_opt, c_opt = result.x
print(f"Bulunan Parametreler: a = {a_opt:.4f}, b = {b_opt:.4f}, c = {c_opt:.4f}")

# Tahmin edilen fonksiyonu çiz
y_fitted = true_function(x_data, a_opt, b_opt, c_opt)

plt.scatter(x_data, y_noisy, label="Ölçülen Veriler", color="red")
plt.plot(x_data, y_real, label="Gerçek Fonksiyon", linestyle="dashed")
plt.plot(x_data, y_fitted, label="LM Optimizasyonu Sonucu", color="blue")
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.title("Levenberg-Marquardt ile Optimizasyon")
plt.show()
