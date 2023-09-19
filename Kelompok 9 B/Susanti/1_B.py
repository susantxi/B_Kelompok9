import numpy as np

# definisikan fungsi yang akan dicari akarnya
def f(x):
    return np.exp(x) - x

# definisikan fungsi bisection
def bisection(a, b, e):
    # periksa apakah tanda interval (a dan b) sama
    if np.sign(f(a)) == np.sign(f(b)):
        print(f"Tidak ada akar pada interval [{a}, {b}]")
        return None
    
    # hitung titik tengah interval
    c = (a + b) / 2
    if np.abs(f(c)) < e:
        return c
    elif np.sign(f(a)) == np.sign(f(c)):
        return bisection(c, b, e)
    elif np.sign(f(b)) == np.sign(f(c)):
        return bisection(a, c, e)

# interval awal
a = -0.5
b = 0.5

# tingkat toleransi
e = 0.005

# panggil fungsi bisection
akar = bisection(a, b, e)

# Cetak hasil
if akar is not None:
    print(f"Akar hampiran = {akar: .3f} ")
    print((f"f(c) = {f(akar):.3f}"))
