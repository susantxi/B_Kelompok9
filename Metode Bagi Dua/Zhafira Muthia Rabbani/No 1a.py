import numpy as np

# Definisi fungsi bisection untuk mencari akar
def my_bisection(f, a, b, e):
    if np.sign(f(a)) == np.sign(f(b)): # Memeriksa apakah f(a).f(b) < 0
        print("Tidak ada akar pada interval [a, b]") # Jika iya, maka interval [a, b] tidak memuat akar
        return None
    
    m = (a + b) / 2 # Menghitung titik tengah (m) dari interval [a, b]
    if np.abs(f(m)) < e:
        return m
    elif np.sign(f(a)) == np.sign(f(m)):
        return my_bisection(f, m, b, e)
    elif np.sign(f(b)) == np.sign(f(m)):
        return my_bisection(f, a, m, e)

# Fungsi yang ingin dicari akarnya
f = lambda x: x**3-2*x+1

# Interval awal [a, b]
a = -2
b = 2

# Tingkat toleransi
e = 0.001

# Panggil fungsi my_bisection untuk mencari akar
akar = my_bisection(f, a, b, e)

# Cetak hasil
if akar is not None:
    print(f"Akar yang ditemukan : {akar:.3f}")
    print(f"f(m)                : {f(akar):.3f}")