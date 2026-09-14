import cv2
import numpy as np

# 1. Read n Show Img
image = cv2.imread("image.png")
print(f"Shape: {image.shape}, Dtype: {image.dtype}")
cv2.imshow("Foto Aseli", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 2. Filter Warna Citra
img = cv2.imread("image.png")

#filter merah
img_merah = img.copy()
img_merah[:, :, 0] = 0  # Blue = 0
img_merah[:, :, 1] = 0  # Green = 0
cv2.imshow("Merah", img_merah)
cv2.waitKey(0)
cv2.destroyAllWindows()

#filter hijau
img_hijau = img.copy()
img_hijau[:, :, 0] = 0  # Blue = 0
img_hijau[:, :, 2] = 0  # Red = 0
cv2.imshow("Hijau", img_hijau)
cv2.waitKey(0)
cv2.destroyAllWindows()

#filter biru
img_biru = img.copy()
img_biru[:, :, 1] = 0  # Green = 0
img_biru[:, :, 2] = 0  # Red = 0
cv2.imshow("Biru", img_biru)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 3. Filter Warna Video
cap = cv2.VideoCapture(0)
mode = 'm'  # m=merah, h=hijau, b=biru

while True:
    ok, frame = cap.read()
    if not ok:
        break
    
    if mode == 'm':
        result = frame.copy()
        result[:, :, 0] = 0
        result[:, :, 1] = 0
    elif mode == 'h':
        result = frame.copy()
        result[:, :, 0] = 0
        result[:, :, 2] = 0
    elif mode == 'b':
        result = frame.copy()
        result[:, :, 1] = 0
        result[:, :, 2] = 0
    else:
        result = frame
    
    # teks petunjuk di kiri atas sedang mode apa
    cv2.putText(result, f"Mode: {mode.upper()}", (10, 30), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    
    # menggabungkan frame asli dan hasil filter menjadi satu jendela
    combined = np.hstack([frame, result])
    cv2.imshow("Asli | Filter", combined)
    
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key in [ord('m'), ord('h'), ord('b')]:
        mode = chr(key)

cap.release()
cv2.destroyAllWindows()