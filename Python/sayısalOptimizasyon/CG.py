import numpy as np

def conjugate_gradient(A, b, x0=None, tol=1e-10, max_iter=None):
    """
    Conjugate Gradient yöntemi ile Ax = b sistemini çözer.
    
    :param A: Simetrik pozitif tanımlı matris (nxn)
    :param b: Sağ taraf vektörü (n,)
    :param x0: Başlangıç noktası (n,), varsayılan olarak sıfır vektörü
    :param tol: Hata toleransı
    :param max_iter: Maksimum iterasyon sayısı, varsayılan olarak n
    :return: Çözüm vektörü x
    """
    n = len(b)
    if x0 is None:
        x = np.zeros(n)
    else:
        x = x0
    
    r = b - A @ x  # Başlangıç artık vektörü
    p = r.copy()    # İlk doğrultu vektörü
    rs_old = np.dot(r, r)  # r_k^T * r_k
    
    if max_iter is None:
        max_iter = n  # Varsayılan iterasyon sayısı
    
    for _ in range(max_iter):
        Ap = A @ p
        alpha = rs_old / np.dot(p, Ap)  # Adım uzunluğu
        x = x + alpha * p  # Yeni nokta
        r = r - alpha * Ap  # Yeni artık
        
        rs_new = np.dot(r, r)  # Yeni r_k^T * r_k
        if np.sqrt(rs_new) < tol:  # Yakınsama kontrolü
            break
        
        beta = rs_new / rs_old  # Beta katsayısı
        p = r + beta * p  # Yeni doğrultu vektörü
        rs_old = rs_new  # Güncelleme
    
    return x

# Örnek sistem: Ax = b
A = np.array([[4, 1], [1, 3]], dtype=float)  # Simetrik pozitif tanımlı matris
b = np.array([1, 2], dtype=float)  # Sağ taraf vektörü
x0 = np.array([2, 1], dtype=float)  # Başlangıç noktası (isteğe bağlı)

x_cg = conjugate_gradient(A, b)
print("CG ile bulunan çözüm:", x_cg)

# Doğruluk kontrolü
x_exact = np.linalg.solve(A, b)  # NumPy ile karşılaştırma
print("Gerçek çözüm:", x_exact)
