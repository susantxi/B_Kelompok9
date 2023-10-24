import numpy as np

# Definisi fungsi untuk mencari akar
def my_bisection(f, a, b, e, iterasi=1):
    if np.sign(f(a)) == np.sign(f(b)):
        print("Tidak ada akar pada interval [a, b]")
        return None

    # Menghitung titik tengah (m) dari interval [a, b]
    m = (a + b) / 2

    if np.abs(f(m)) < e:
        return m, iterasi
    elif np.sign(f(a)) == np.sign(f(m)):
        return my_bisection(f, m, b, e, iterasi + 1)
    elif np.sign(f(b)) == np.sign(f(m)):
        return my_bisection(f, a, m, e, iterasi + 1)

# Input fungsi dari pengguna
fungsi = input("Masukkan fungsi f(x): ")
f = lambda x: eval(fungsi)

# Input interval serta tingkat toleransi
a = float(input("Masukkan batas awal interval a: "))
b = float(input("Masukkan batas akhir interval b: "))
e = float(input("Masukkan tingkat toleransi e: "))

# Memanggil fungsi my_bisection untuk mencari akar
akar, iterasi = my_bisection(f, a, b, e)

# Mencetak hasil
print(f"Akar yang ditemukan : {akar:.3f}")
print(f"f(m)                : {f(akar):.3f}")
print(f"Jumlah iterasi      : {iterasi}")