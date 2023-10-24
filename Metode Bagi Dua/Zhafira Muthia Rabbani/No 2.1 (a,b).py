import numpy as np

# Definisi fungsi bisection untuk mencari akar
def my_bisection(f, a, b, e, max_iterations):
    if np.sign(f(a)) == np.sign(f(b)):
        print("Tidak ada akar pada interval [a, b]")
        return None
            
    iteration = 0
    while iteration < max_iterations:
        m = (a + b) / 2
        if np.abs(f(m)) < e:
            return m
        elif np.sign(f(a)) == np.sign(f(m)):
            a = m
        elif np.sign(f(b)) == np.sign(f(m)):
            b = m
        iteration += 1
        
    return m

# A
# Fungsi yang ingin dicari akarnya
f = lambda x: x**3-2*x+1

# Interval awal
a = -2
b = 2

# Tingkat toleransi
e = 0.001

# B
#f = lambda x: np.exp(x) - x
#a = -0.5
#b = 0.5
#e = 0.005

# Jumlah iterasi maksimal (input dari pengguna)
max_iterations = int(input("Masukkan jumlah iterasi maksimal: "))

# Panggil fungsi my_bisection untuk mencari akar
akar = my_bisection(f, a, b, e, max_iterations)

# Cetak hasil
if akar is not None:
    print(f"Akar yang ditemukan : {akar:.3f}")
    print(f"f(m)                : {f(akar):.3f}")