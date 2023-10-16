import numpy as np

def eliminasi_gauss(A, B):
    n = len(A)

    # Langkah 1: Matriks augmentasi
    AB = np.column_stack((A, B))

    # Langkah 2: Eliminasi
    for i in range(n):
        # Pemilihan Pivoting
        baris_pivot = i
        for k in range(i + 1, n):
            if abs(AB[k, i]) > abs(AB[baris_pivot, i]):
                baris_pivot = k
        AB[i], AB[baris_pivot] = AB[baris_pivot].copy(), AB[i].copy()

        # Normalisasi baris i
        pivot = AB[i, i]
        if pivot == 0:
            print("Pivot nol ditemukan. Metode eliminasi Gauss tidak dapat digunakan.")
            return None
        AB[i] = AB[i] / pivot

        # Eliminasi kolom di bawah pivot
        for k in range(i + 1, n):
            faktor = AB[k, i]
            AB[k] = AB[k] - faktor * AB[i]

    # Langkah 3: Substitusi balik
    X = np.zeros(n)
    for i in range(n - 1, -1, -1):
        X[i] = AB[i, -1] - np.sum(AB[i, i+1:n] * X[i+1:n])

    # Menampilkan solusi
    print('Solusi sistem persamaan linear:\n')
    for i in range(n):
        print(f'X{i + 1} = {X[i]}')

# Meminta input matriks A dari pengguna
A = []
n = int(input("Masukkan ukuran matriks (n x n): "))
print(f"Masukkan elemen-elemen matriks A ({n}x{n}):")
for i in range(n):
    baris = []
    for j in range(n):
        elemen = float(input(f"A[{i + 1}][{j + 1}]: "))
        baris.append(elemen)
    A.append(baris)

# Meminta input matriks B dari pengguna
B = []
print("Masukkan elemen-elemen matriks B:")
for i in range(n):
    elemen = float(input(f"B[{i + 1}]: "))
    B.append(elemen)

# Memanggil fungsi eliminasi_gauss dengan matriks A dan B yang dimasukkan oleh pengguna
eliminasi_gauss(np.array(A), np.array(B))
