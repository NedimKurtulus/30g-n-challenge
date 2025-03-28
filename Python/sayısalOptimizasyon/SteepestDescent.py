import numpy as np

# Test fonksiyonu: Rosenbrock fonksiyonu
def rosenbrock(x):
    """Rosenbrock fonksiyonu"""
    return sum(100.0 * (x[i + 1] - x[i] ** 2) ** 2 + (1 - x[i]) ** 2 for i in range(len(x) - 1))

# Gradient (Türev) fonksiyonu
def rosenbrock_gradient(x):
    """Rosenbrock fonksiyonunun gradienti"""
    grad = np.zeros_like(x)
    for i in range(len(x) - 1):
        grad[i] = -400.0 * x[i] * (x[i + 1] - x[i] ** 2) - 2.0 * (1 - x[i])
        grad[i + 1] = 200.0 * (x[i + 1] - x[i] ** 2)
    return grad

# Steepest Descent Algoritması
def steepest_descent(grad_func, initial_point, learning_rate=0.001, max_iterations=1000, tolerance=1e-6):
    """Steepest Descent algoritması"""
    x = initial_point
    for i in range(max_iterations):
        grad = grad_func(x)
        x_new = x - learning_rate * grad  # Yeni nokta, gradient yönünde hareket
        if np.linalg.norm(x_new - x) < tolerance:  # Eğer fark çok küçükse, sonlandır
            break
        x = x_new
    return x

# Başlangıç noktası
initial_point = np.array([1.5, -1.5])

# Steepest Descent ile optimizasyonu yap
optimal_point = steepest_descent(rosenbrock_gradient, initial_point)

# Sonuçları yazdır
print("Optimum Nokta:", optimal_point)
print("Fonksiyon Değeri:", rosenbrock(optimal_point))
