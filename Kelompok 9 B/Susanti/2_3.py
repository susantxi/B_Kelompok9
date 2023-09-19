import numpy as np
import matplotlib.pyplot as plt 

def f(x):
    return eval(fungsi)

def bisection(f, a, b, e, iterasi=1):
    if np.sign(f(a)) == np.sign(f(b)):
        print(f"Tidak ada akar pada interval [{a}, {b}]")
        return None

    c = (a + b) / 2
    if np.abs(f(c)) < e:
        return c, iterasi
    elif np.sign(f(a)) == np.sign(f(c)):
        return bisection(f, c, b, e, iterasi+1)
    elif np.sign(f(b)) == np.sign(f(c)):
        return bisection(f, a, c, e, iterasi+1)
 
fungsi = input("Masukkan fungsi f(x): ")

a = float(input("Masukkan batas awal interval a: "))
b = float(input("Masukkan batas akhir interval b: "))
e = float(input("Masukkan galat: "))

# Panggil fungsi bisection
akar, iterasi = bisection(f, a, b, e)

print(f"Akar yang ditemukan (c) = {akar:.3f}")
print(f"f(c) = {f(akar)}")
print(f"Jumlah iterasi = {iterasi}")

x = np.linspace(a, b, 100)
plt.plot(x, f(x), label="f(x)")
plt.scatter(akar, f(akar), color='red', label="Akar")
plt.legend()
plt.grid()
plt.show()