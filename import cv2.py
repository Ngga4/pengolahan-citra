import cv2
import matplotlib.pyplot as plt
import numpy as np

# === 1. Input gambar dari user ===
img = cv2.imread("4.jpg")

if img is None:
    print("Gambar tidak ditemukan, cek path!")
    exit()

# === 2. Tanya apakah mau crop ===
choice = input("Apakah ingin crop gambar? (y/n): ").lower()

if choice == "y":
    print("Masukkan koordinat crop (ingat: hasil = (y2-y1) x (x2-x1))")
    y1 = int(input("y1 (baris awal): "))
    y2 = int(input("y2 (baris akhir): "))
    x1 = int(input("x1 (kolom awal): "))
    x2 = int(input("x2 (kolom akhir): "))

    # crop gambar asli
    img = img[y1:y2, x1:x2]

# === 3. Konversi ke grayscale ===
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# === 4. Konversi ke citra biner ===
_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# === 5. Cetak matriks ===
print ("\nMatriks gambar asli (BGR):")
print(img)

print("\nDimensi gambar asli:", img.shape)

print("\nMatriks grayscale:")
print(gray)

print("\nMatriks citra biner (0/1):")
print(binary // 255)

# == 6. Tampilkan gambar ===
plt.figure(figsize=(12,6))
plt.subplot(1,3,1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("Gambar Asli")
plt.axis('off')

plt.subplot(1,3,2)
plt.imshow(gray, cmap='gray')
plt.title("Grayscale")
plt.axis('off')

plt.subplot(1,3,3)
plt.imshow(binary, cmap='gray')
plt.title("Citra Biner")
plt.axis('off')
plt.show()