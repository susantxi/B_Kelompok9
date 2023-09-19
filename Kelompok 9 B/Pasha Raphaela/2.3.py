import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Definisi fungsi untuk mencari akar
def my_bisection(f, a, b, e, iterasi=1):
    if np.sign(f.subs(x, a)) == np.sign(f.subs(x, b)):
        print("Tidak ada akar pada interval [a, b]")
        return None

    # Menghitung titik tengah (m) dari interval [a, b]
    m = (a + b) / 2

    if np.abs(f.subs(x, m)) < e:
        return m, iterasi
    elif np.sign(f.subs(x, a)) == np.sign(f.subs(x, m)):
        return my_bisection(f, m, b, e, iterasi + 1)
    elif np.sign(f.subs(x, b)) == np.sign(f.subs(x, m)):
        return my_bisection(f, a, m, e, iterasi + 1)

# Input fungsi dari pengguna
fungsi_str = input("Masukkan fungsi f(x): ")
x = sp.symbols('x')
f = sp.sympify(fungsi_str)

# Input interval serta tingkat toleransi
a = float(input("Masukkan batas awal interval a: "))
b = float(input("Masukkan batas akhir interval b: "))
e = float(input("Masukkan tingkat toleransi e: "))

# Memanggil fungsi my_bisection untuk mencari akar
akar, iterasi = my_bisection(f, a, b, e)

# Mencetak hasil
print(f"Akar yang ditemukan : {akar:.3f}")
print(f"f(m)                : {f.subs(x, akar):.3f}")
print(f"Jumlah iterasi      : {iterasi}")

# Plot grafik fungsi dan lokasi akar
x_vals = np.linspace(a, b, 100)
y_vals = [f.subs(x, val) for val in x_vals]
plt.plot(x_vals, y_vals, label=f"f(x) = {fungsi_str}")
plt.scatter(akar, f.subs(x, akar), color='red', label="Akar")
plt.legend()
plt.grid()
plt.show()