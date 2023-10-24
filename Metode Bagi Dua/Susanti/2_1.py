import numpy as np

# definisi fungsi yang akan dicari akarnya
def f(x):
    return x**3-2*x+1

# definisi fungsi bisection untuk mencari akar dari fungsi
def bisection(a, b, e, max_iterations):
    if np.sign(f(a)) == np.sign(f(b)):
        print(f"Tidak ada akar pada interval [{a}, {b}]")
        return None

    i = 0
    while i < max_iterations:
        c = (a + b) / 2
        if np.abs(f(c)) < e:
            return c
        elif np.sign(f(a)) == np.sign(f(c)):
            a = c
        elif np.sign(f(b)) == np.sign(f(c)):
            b = c
        i += 1
    return c

# interval
a = -2
b = 2

# galat
e = 0.001

# user menginput jumlah iterasi maksimal
max_iterations = int(input("Masukkan jumlah iterasi maksimal: "))

# panggil fungsi bisection
akar = bisection(a, b, e, max_iterations)

# cetak hasil
if akar is not None:
    print(f"Akar yang ditemukan (c) = {akar:.3f}")
    print(f"f(c) = {f(akar):.3f}")
