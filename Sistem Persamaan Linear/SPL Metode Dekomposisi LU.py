import numpy as np

def lu_decomposition(A, B):
    n = len(A)
    L = np.zeros((n, n))
    U = np.zeros((n, n))
    X = np.zeros(n)
    Y = np.zeros(n)

    # Langkah 1: Pastikan Det(A) != 0
    if np.linalg.det(A) == 0:
        print("Determinan matriks A sama dengan 0.")
        return None

    # Langkah 2: Cari matriks L dan U
    for j in range(n):
        # a) Untuk j = 1, 2, ..., n
        for i in range(n):
            P1 = 0
            for k in range(i):
                P1 += L[i, k] * U[k, j]
            U[i, j] = A[i, j] - P1
            if i < j:
                L[i, j] = 0
            elif i == j:
                L[i, j] = 1

        # b) Untuk i = j + 1, ..., n
        for i in range(j + 1, n):
            U[i, j] = 0
            P2 = 0
            for k in range(j):
                P2 += L[i, k] * U[k, j]
            L[i, j] = (A[i, j] - P2) / U[j, j]
    
    # Menampilkan matriks L
    print('\n\nMatriks L:')
    print(L)

    # Menampilkan matriks U
    print('\nMatriks U:')
    print(U)

    # Langkah 3: Cari nilai y
    I = 0
    while I < n:
        P = 0
        k = 0
        while k < I:
            P += L[I, k] * Y[k]
            k += 1
        Y[I] = B[I] - P
        I += 1
    
     # Menampilkan nilai y
    print('\nNilai y:')
    for i in range(n):
        print(f'Y{i + 1} = {Y[i]}')

    # Langkah 4: Cari nilai x
    I = n - 1
    while I >= 0:
        P = 0
        k = I + 1
        while k < n:
            P += U[I, k] * X[k]
            k += 1
        X[I] = (Y[I] - P) / U[I, I]
        I -= 1

    # Menampilkan solusi
    print('\nNilai x (Solusi SPL):')
    for i in range(n):
        print(f'X{i + 1} = {X[i]}')

# Meminta input matriks A dari pengguna
A = []
n = int(input("Masukkan ukuran matriks (n x n): "))
print(f"Masukkan elemen-elemen matriks A ({n}x{n}):")
for i in range(n):
    row = []
    for j in range(n):
        elem = float(input(f"A[{i + 1}][{j + 1}]: "))
        row.append(elem)
    A.append(row)

# Meminta input matriks B dari pengguna
B = []
print("Masukkan elemen-elemen matriks B:")
for i in range(n):
    elem = float(input(f"B[{i + 1}]: "))
    B.append(elem)

# Memanggil fungsi lu_decomposition dengan matriks A dan B yang dimasukkan oleh pengguna
lu_decomposition(np.array(A), np.array(B))
