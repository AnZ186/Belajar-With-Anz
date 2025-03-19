import numpy as np

def input_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            while True:
                try:
                    element = float(input(f"Masukkan elemen [{i+1}, {j+1}]: "))
                    row.append(element)
                    break
                except ValueError:
                    print("Input tidak valid. Masukkan angka.")
        matrix.append(row)
    return np.array(matrix)

def matrix_operations():
    while True:
        try:
            rows_a = int(input("Masukkan jumlah baris matriks A: "))
            cols_a = int(input("Masukkan jumlah kolom matriks A: "))
            rows_b = int(input("Masukkan jumlah baris matriks B: "))
            cols_b = int(input("Masukkan jumlah kolom matriks B: "))
            break
        except ValueError:
            print("Input tidak valid. Masukkan angka.")

    print("\nMasukkan elemen matriks A:")
    matrix_a = input_matrix(rows_a, cols_a)
    print("\nMasukkan elemen matriks B:")
    matrix_b = input_matrix(rows_b, cols_b)

    print("\nMatriks A:")
    print(matrix_a)
    print("\nMatriks B:")
    print(matrix_b)

    if cols_a != rows_b:
        print("\nPerkalian matriks tidak dapat dilakukan karena jumlah kolom matriks A tidak sama dengan jumlah baris matriks B.")
    else:
        try:
            print("\nHasil perkalian matriks A x B:")
            result = np.dot(matrix_a, matrix_b)
            print(result)
        except ValueError as e:
            print(f"Terjadi kesalahan saat perkalian matriks: {e}")

    print("\nHasil penjumlahan matriks A + B:")
    if matrix_a.shape == matrix_b.shape:
        try:
            print(np.add(matrix_a, matrix_b))
        except ValueError as e:
            print(f"Terjadi kesalahan saat penjumlahan matriks: {e}")
    else:
        print("Penjumlahan matriks tidak dapat dilakukan karena ukuran matriks berbeda.")

    print("\nHasil pengurangan matriks A - B:")
    if matrix_a.shape == matrix_b.shape:
        try:
            print(np.subtract(matrix_a, matrix_b))
        except ValueError as e:
            print(f"Terjadi kesalahan saat pengurangan matriks: {e}")
    else:
        print("Pengurangan matriks tidak dapat dilakukan karena ukuran matriks berbeda.")

if __name__ == "__main__":
    matrix_operations()