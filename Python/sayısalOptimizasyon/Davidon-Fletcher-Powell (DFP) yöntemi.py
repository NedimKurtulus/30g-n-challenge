import numpy as np

# Amaç fonksiyonu (örnek): f(x) = x1^2 + 2*x2^2 + 3*x1*x2
def func(x):
    return x[0]**2 + 2*x[1]**2 + 3*x[0]*x[1]

# Gradient (Eğimi Hesapla): ∇f = [∂f/∂x1, ∂f/∂x2]
def gradient(x):
    df_dx1 = 2*x[0] + 3*x[1]  # ∂f/∂x1
    df_dx2 = 4*x[1] + 3*x[0]  # ∂f/∂x2
    return np.array([df_dx1, df_dx2])

# DFP Optimizasyon Algoritması
def dfp_optimization(func, grad, x0, tol=1e-6, max_iter=100):
    n = len(x0)
    x = x0  # Başlangıç noktası
    H = np.eye(n)  # Başlangıçta Hesse matrisinin tersi birim matris
    grad_x = grad(x)

    for i in range(max_iter):
        if np.linalg.norm(grad_x) < tol:  # Durdurma kriteri
            break

        # Arama yönü hesaplama: d_k = - H_k * ∇f(x_k)
        d = -H @ grad_x

        # Adım büyüklüğünü belirleme (Basit Line Search: α_k)
        alpha = 0.1  # Genellikle bir optimizasyon yapılır ama burada sabit
        x_new = x + alpha * d

        # Güncellenmiş Gradient
        grad_new = grad(x_new)

        # Güncelleme için gerekli değişkenler
        s = x_new - x
        y = grad_new - grad_x

        # Hesse matrisinin tersini DFP formülüyle güncelle
        rho = 1.0 / (y @ s) if (y @ s) != 0 else 1e-8  # Sıfır bölme hatasını önlemek için
        Hy = H @ y
        H = H + rho * np.outer(s, s) - (rho * np.outer(Hy, Hy) / (y @ Hy))

        # Güncellemeleri kaydet
        x = x_new
        grad_x = grad_new

        # Çıktıyı yazdır
        print(f"Iter {i+1}: x = {x}, f(x) = {func(x)}")

    return x

# Başlangıç noktası
x0 = np.array([2.0, -1.0])

# Optimizasyonu çalıştır
optimum_x = dfp_optimization(func, gradient, x0)
print(f"Optimum Çözüm: x = {optimum_x}, f(x) = {func(optimum_x)}")
