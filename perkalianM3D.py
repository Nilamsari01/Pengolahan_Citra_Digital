import numpy as np

print("=== PROGRAM PERKALIAN MATRIKS ARRAY 3 DIMENSI ===")

# Input jumlah layer
layer = int(input("\nMasukkan jumlah layer: "))

# Input ukuran Matriks A
print("\n--- Ukuran Matriks A ---")
baris_A = int(input("Masukkan jumlah baris Matriks A: "))
kolom_A = int(input("Masukkan jumlah kolom Matriks A: "))

# Input ukuran Matriks B
print("\n--- Ukuran Matriks B ---")
baris_B = int(input("Masukkan jumlah baris Matriks B: "))
kolom_B = int(input("Masukkan jumlah kolom Matriks B: "))

# Validasi syarat perkalian matriks
if kolom_A != baris_B:
    print("\nERROR!")
    print("Jumlah kolom Matriks A harus sama dengan jumlah baris Matriks B.")
    print(f"Matriks A memiliki {kolom_A} kolom.")
    print(f"Matriks B memiliki {baris_B} baris.")
    print("\nPerkalian matriks tidak dapat dilakukan.")

else:
    # INPUT MATRIKS A
    A = []

    print("\n=== Masukkan Elemen Matriks A ===")

    for l in range(layer):
        print(f"\nLayer {l + 1}")
        data_layer = []

        for i in range(baris_A):
            data_baris = []

            for j in range(kolom_A):
                nilai = int(
                    input(f"Elemen A[{l + 1}][{i + 1}][{j + 1}]: ")
                )
                data_baris.append(nilai)

            data_layer.append(data_baris)

        A.append(data_layer)

    # INPUT MATRIKS B
    B = []

    print("\n=== Masukkan Elemen Matriks B ===")

    for l in range(layer):
        print(f"\nLayer {l + 1}")
        data_layer = []

        for i in range(baris_B):
            data_baris = []

            for j in range(kolom_B):
                nilai = int(
                    input(f"Elemen B[{l + 1}][{i + 1}][{j + 1}]: ")
                )
                data_baris.append(nilai)

            data_layer.append(data_baris)

        B.append(data_layer)

    # UBAH KE NUMPY ARRAY
    A = np.array(A)
    B = np.array(B)


    # PERKALIAN MATRIKS
    hasil = np.matmul(A, B)

    # OUTPUT
    print("\n================================")
    print("        HASIL PERHITUNGAN")
    print("================================")

    print("\nMatriks A:")
    print(A)

    print("\nMatriks B:")
    print(B)

    print("\nHasil Perkalian Matriks:")
    print(hasil)