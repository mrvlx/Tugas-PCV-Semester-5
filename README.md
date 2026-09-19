# PCV TUGAS SEMESTER 5
| | |
|---|---|
| **Nama** | Reidita Eirene Anastasia Katampuge |
| **NRP** | 5024241001 |

## PCV - Pengolahan Citra dan Video
Menggunakan bahasa pemrograman Python dengan library OpenCV dan NumPy. Disarankan menggunakan VSCode atau Spyder.

### Fungsi Dasar OpenCV
- `cv2.imread` = membaca citra dari file
- `cv2.imshow` = menampilkan citra ke layar
- `cv2.waitKey` = menunggu tombol ditekan
- `cv2.destroyAllWindows` = menutup semua jendela
- `cv2.VideoCapture` = mengakses webcam

---

## TUGAS

### 1-Intro
Program dasar pengolahan citra dan video yang berisi:

1. **Read & Show Image**  
   Membaca dan menampilkan citra menggunakan `cv2.imread` dan `cv2.imshow`

2. **Filter Warna Citra (BGR)**  
   - Filter Merah: kanal Blue=0, Green=0, Red dipertahankan
   - Filter Hijau: kanal Blue=0, Red=0, Green dipertahankan  
   - Filter Biru: kanal Green=0, Red=0, Blue dipertahankan
   - **Implementasi**: NumPy slicing manual `img[:, :, kanal] = 0`

3. **Filter Warna Video (Webcam)**  
   - Real-time filtering pada webcam
   - Interaksi keyboard: `m`=merah, `h`=hijau, `b`=biru, `q`=quit
   - Tampilan side-by-side: asli vs filter
   - **Implementasi**: Pipeline dengan `cv2.VideoCapture` dan NumPy

#### Output

**Foto Asli**

<img src="Output/1-intro/foto aseli.png" width="400">

**Filter Warna Citra (BGR)**

| Merah | Hijau | Biru |
|---|---|---|
| <img src="Output/1-intro/output filter warna merah.png" width="250"> | <img src="Output/1-intro/output filter warna hijau.png" width="250"> | <img src="Output/1-intro/output filter warna biru.png" width="250"> |

**Filter Warna Video (Webcam)**

| Mode Merah | Mode Hijau | Mode Biru |
|---|---|---|
| <img src="Output/1-intro/Filter video merah.png" width="250"> | <img src="Output/1-intro/Filter video hijau.png" width="250"> | <img src="Output/1-intro/Filter video biru.png" width="250"> |

---
 
### 2-TI-EQ (Transformasi Intensitas & Ekualisasi Histogram)
Program pengolahan citra grayscale yang berisi:
 
1. **Transformasi Intensitas (manual, tanpa `cv2.LUT`)**
   - **Negatif**: `s = 255 - r`
   - **Logaritmik**: `s = c * log(1 + r)`
   - **Gamma Correction**: `s = 255 * (r/255)^gamma` (gamma 0.4 = lebih terang, gamma 2.5 = lebih gelap)
   - **Contrast Stretching**: pemetaan 3 ruas linear dengan titik kontrol `(r1, s1)` dan `(r2, s2)`
   - **Thresholding**: binerisasi manual dengan `np.where(img >= 128, 255, 0)`
2. **Ekualisasi Histogram (manual, tanpa `cv2.equalizeHist`)**
   - Hitung histogram dengan loop manual
   - Hitung PDF (probabilitas) dan CDF (distribusi kumulatif)
   - Bentuk LUT pemetaan `sk = round((L-1) * CDF)`
   - Terapkan LUT ke citra asli
   - Bandingkan histogram sebelum vs sesudah ekualisasi
3. **Visualisasi**
   - Grid 3x3 menampilkan semua hasil transformasi + histogram menggunakan `matplotlib`
#### Output
 
<img src="Output/2-ti-eq.py/ini pcv2.png" width="700">
---