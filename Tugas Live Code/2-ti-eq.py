import cv2
import numpy as np
import matplotlib.pyplot as plt

# 1. Baca gambar
img = cv2.imread("Tugas Live Code/image.png", cv2.IMREAD_GRAYSCALE)
print(f"Shape: {img.shape}, Dtype: {img.dtype}")

# 2. Transformasi Intensitas (manual, ga pake cv2.LUT)
r = np.arange(256, dtype=np.float64)  # semua kemungkinan nilai piksel 0-255

# fungsi buat rapikan LUT: bulatin setengah ke atas, clip 0-255, jadiin uint8
def rapikan(lut):
    return np.clip(np.floor(lut + 0.5), 0, 255).astype(np.uint8)

# ---Negatif---
lut_negatif = 255 - r
hasil_negatif = rapikan(lut_negatif)[img]

# ---Logaritmik---
c = 255.0 / np.log(256.0)
lut_log = c * np.log(1.0 + r)
hasil_log = rapikan(lut_log)[img]

# ---Gamma---
def lut_gamma(gamma):
    return 255.0 * (r / 255.0) ** gamma

hasil_gamma_04 = rapikan(lut_gamma(0.4))[img]  # gamma < 1 = lebih terang
hasil_gamma_25 = rapikan(lut_gamma(2.5))[img]  # gamma > 1 = lebih gelap

# ---Contrast Stretching (3 ruas)---
def lut_stretch(r1=80, s1=20, r2=175, s2=240):
    out = np.empty(256, dtype=np.float64)
    bagian1 = r < r1
    bagian2 = (r >= r1) & (r < r2)
    bagian3 = r >= r2
    
    out[bagian1] = (s1 / r1) * r[bagian1]
    out[bagian2] = (s2 - s1) / (r2 - r1) * (r[bagian2] - r1) + s1
    out[bagian3] = (255 - s2) / (255 - r2) * (r[bagian3] - r2) + s2
    return out

hasil_stretch = rapikan(lut_stretch())[img]

# ---Thresholding (binerisasi manual)---
hasil_biner = np.where(img >= 128, 255, 0).astype(np.uint8)

# 3. Ekualisasi Histogram (manual, ga pake cv2.equalizeHist)
def ekualisasi_manual(img, L=256):
    MN = img.size
    
    # hitung histogram pake loop biasa
    hist = np.zeros(L, dtype=np.int64)
    for nilai in img.ravel():
        hist[nilai] += 1
    
    # hitung PDF (probabilitas)
    p = hist / MN
    
    # hitung CDF (distribusi kumulatif)
    cdf = np.cumsum(p)
    
    # buat LUT pemetaan: sk = round((L-1) * CDF)
    s = np.floor((L - 1) * cdf + 0.5)
    lut_eq = np.clip(s, 0, L - 1).astype(np.uint8)
    
    # terapkan ke citra
    return lut_eq[img], hist

hasil_eq, hist_asli = ekualisasi_manual(img)

# 4. Tampilkan Hasil
plt.figure(figsize=(18, 12))

plt.subplot(3, 3, 1), plt.imshow(img, cmap='gray'), plt.title('Asli'), plt.axis('off')
plt.subplot(3, 3, 2), plt.imshow(hasil_negatif, cmap='gray'), plt.title('Negatif'), plt.axis('off')
plt.subplot(3, 3, 3), plt.imshow(hasil_log, cmap='gray'), plt.title('Log'), plt.axis('off')

plt.subplot(3, 3, 4), plt.imshow(hasil_gamma_04, cmap='gray'), plt.title('Gamma 0.4'), plt.axis('off')
plt.subplot(3, 3, 5), plt.imshow(hasil_gamma_25, cmap='gray'), plt.title('Gamma 2.5'), plt.axis('off')
plt.subplot(3, 3, 6), plt.imshow(hasil_stretch, cmap='gray'), plt.title('Contrast Stretch'), plt.axis('off')

plt.subplot(3, 3, 7), plt.imshow(hasil_biner, cmap='gray'), plt.title('Threshold'), plt.axis('off')
plt.subplot(3, 3, 8), plt.imshow(hasil_eq, cmap='gray'), plt.title('Ekualisasi'), plt.axis('off')

# plot histogram sebelum & sesudah ekualisasi
hist_eq = np.zeros(256, dtype=np.int64)
for nilai in hasil_eq.ravel():
    hist_eq[nilai] += 1

plt.subplot(3, 3, 9)
plt.plot(hist_asli, 'gray', label='Asli')
plt.plot(hist_eq, 'black', label='Ekualisasi')
plt.title('Histogram'), plt.xlabel('Intensitas'), plt.ylabel('Jumlah Piksel')
plt.legend()

plt.tight_layout()
plt.show()