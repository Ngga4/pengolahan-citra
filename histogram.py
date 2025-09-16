import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
import os

def grayscaleHistogram():
    root = os.getcwd()
    img = cv.imread("1.jpg", cv.IMREAD_GRAYSCALE)

    plt.figure(figsize=(14,6))
    plt.subplot(1, 2, 1)
    plt.imshow(img, cmap='gray')

    hist = cv.calcHist([img], [0], None, [256], [0, 256])
    plt.subplot(1, 2, 2)
    plt.plot(hist)
    plt.xlabel("Intensitas")
    plt.ylabel("Jumlah Pixel")

    plt.show()

def colorHistogram():
    root = os.getcwd()
    img = cv.imread("1.jpg")

    plt.figure(figsize=(14,6))
    plt.subplot(1, 2, 1)
    plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))

    colors = ('b','g','r')
    plt.subplot(1, 2, 2)
    for i, col in enumerate(colors):
        hist = cv.calcHist([img],[i],None,[256],[0,256])
        plt.plot(hist, color=col)
        plt.xlim([0,256])
    plt.xlabel("Intensitas")
    plt.ylabel("Jumlah Pixel")

    plt.show()

def binaryHistogram():
    root = os.getcwd()
    img = cv.imread("1.jpg", cv.IMREAD_GRAYSCALE)
    _, binary = cv.threshold(img, 127, 255, cv.THRESH_BINARY)

    plt.figure(figsize=(14,6))
    plt.subplot(1, 2, 1)
    plt.imshow(binary, cmap='gray')

    plt.subplot(1, 2, 2)
    plt.hist(binary.ravel(), bins=[0,128,256], color='gray', rwidth=0.8)
    plt.xticks([0,255], ["Hitam (0)","Putih (255)"])
    plt.xlabel("Intensitas")
    plt.ylabel("Jumlah Pixel")

    plt.show()


if __name__ == '__main__':
    pilihan = input("Pilih jenis histogram (1: Grayscale, 2: Warna, 3: Binary): ")
    if pilihan == '1':
        grayscaleHistogram()
    elif pilihan == '2':
        colorHistogram()
    elif pilihan == '3':
        binaryHistogram()
    else:
        print("Pilihan tidak valid. Menampilkan kedua histogram.")
