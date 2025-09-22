import numpy as np

# Membuat matriks 5x5 dengan nilai acak 1-9
matriks = np.random.randint(1, 10, (5, 5))
print("Matriks 5x5:")
print(matriks)

# Fungsi untuk mendapatkan tetangga
def get_neighbors(matrix, x, y, mode="4"):
    rows, cols = matrix.shape
    neighbors = []

    if mode == "4":
        arah = [(-1,0),(1,0),(0,-1),(0,1)]  # atas, bawah, kiri, kanan
    elif mode == "D":  
        arah = [(-1,-1),(-1,1),(1,-1),(1,1)]  # diagonal
    elif mode == "8":
        arah = [(-1,0),(1,0),(0,-1),(0,1),
                (-1,-1),(-1,1),(1,-1),(1,1)]  # gabungan
    else:
        raise ValueError("Mode harus '4', 'D', atau '8'.")

    for dx, dy in arah:
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols:  # cek agar tidak keluar batas
            neighbors.append(matrix[nx, ny])
    return neighbors

# Contoh: ambil tetangga dari posisi (2,2) (tengah matriks)
x, y = 2, 2
print(f"\nPosisi pusat ({x},{y}) = {matriks[x,y]}")

print("4-Ketetanggaan:", get_neighbors(matriks, x, y, "4"))
print("Diagonal-Ketetanggaan:", get_neighbors(matriks, x, y, "D"))
print("8-Ketetanggaan:", get_neighbors(matriks, x, y, "8"))
