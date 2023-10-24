import numpy as np

def interpolasi_newton(x, y, interpolasi_x):
    n = len(x)
    if len(y) != n:
        print("Panjang x dan y harus sama")
        return None

    # Matriks tabel divided differences
    f = np.zeros((n, n))
    f[:, 0] = y

    for j in range(1, n):
        for i in range(n - j):
            f[i, j] = (f[i+1, j-1] - f[i, j-1]) / (x[i+j] - x[i])
            
    hasil = f[0, 0]
    for j in range(1, n):
        term = f[0, j]
        for i in range(j):
            term *= (interpolasi_x - x[i])
        hasil += term

    return hasil

# Meminta input dari pengguna
n = int(input("Masukkan jumlah titik data: "))
x = np.zeros(n)
y = np.zeros(n)

print('\n')
for i in range(n):
    x[i] = float(input(f"Masukkan nilai x{str(i)}: "))
    y[i] = float(input(f"Masukkan nilai y{str(i)}: "))

interpolasi_x = float(input("\nMasukkan nilai x untuk interpolasi: "))

# Menghitung interpolasi dan mencetak hasilnya
hasil = interpolasi_newton(x, y, interpolasi_x)
if hasil is not None:
    nilai_hasil = "{:.6f}".format(hasil)
    print(f"Hasil Interpolasi Polinom Newton P({interpolasi_x}) adalah {nilai_hasil}")
