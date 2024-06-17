import cv2
import mediapipe as mp
import time
import serial

import Function

# Menginisialisasi webcam untuk menangkap video.
webcam = cv2.VideoCapture(0)


# Memuat solusi MediaPipe untuk deteksi tangan.
mpHands = mp.solutions.hands

# Membuat objek hands untuk mendeteksi tangan.
hands = mpHands.Hands()

# Objek untuk menggambar landmark tangan pada gambar.
mpDraw = mp.solutions.drawing_utils

# Inisialisasi waktu untuk menghitung FPS.
pTime = 0
cTime = 0

try:
    ser = serial.Serial('COM4', 9600, timeout=1)
    if ser.is_open:
        print(f"Koneksi serial ke {ser.name} berhasil dibuka.")
    else:
        print(f"Gagal membuka koneksi serial ke {ser.name}.")
except serial.SerialException as e:
    print(f"SerialException: {e}")



# Loop utama untuk menangkap video frame-by-frame
while webcam.isOpened(): # memerika apakah webcam terbuka
    success, img = webcam.read()  # Menangkap frame dari webcam.
    # memerika apakah menangkap frame dari webcam berhasil jika tidak maka akan program akana berhenti
    if not success:
        break

    img = cv2.flip(img, 1)  # Membalik gambar secara horizontal (mirroring).
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Mengonversi gambar dari format BGR ke RGB karena MediaPipe bekerja dengan gambar RGB.
    results = hands.process(imgRGB)  # Memproses gambar untuk mendeteksi tangan.
    
    if results.multi_hand_landmarks:  # Memeriksa apakah ada tangan yang terdeteksi.
        for handLms, handedness in zip(results.multi_hand_landmarks, results.multi_handedness):  # Loop melalui setiap tangan yang terdeteksi.
            
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS) # Menggambar landmark tangan pada gambar.
            height, width, c = img.shape # Dapatkan dimensi gambar
            hand_orientation = handedness.classification[0].label # menentukan origentai gambar
            hand_pose = Function.hands(handLms, width , height, hand_orientation) #objek dari kelas Mahasiswa
            data = "" # variabel unutk meyimpan data yang akan di kirim ke serial

            # Periksa apakah tangan dalam pose "OK"
            if hand_pose.is_ok():
                cv2.putText(img, 'OK', (10, 130), cv2.FONT_HERSHEY_PLAIN, 2, (3, 252, 23), 3) # Menambahkan teks "FUCK" ke gambar.
                data = "OK\n"
                ser.write(data.encode('utf-8'))

            # Jika tidak periksa apakah tangan dalam pose "FUCK"
            elif hand_pose.is_fuck():
                cv2.putText(img, 'FUCK', (10, 130), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 3)  # Menambahkan teks "FUCK" ke gambar.
                data = "FUCK\n" # isi data sesuai kondisi tangan
                ser.write(data.encode('utf-8')) # kirim data ke serial

            # Jika tidak periksa apakah tangan dalam pose "THUMB UP"
            elif hand_pose.is_thumb_up():
                cv2.putText(img, 'THUMB UP', (10, 130), cv2.FONT_HERSHEY_PLAIN, 2, (3, 252, 23), 3)  # Menambahkan teks "FUCK" ke gambar.
                data = "THUMB UP\n" # isi data sesuai kondisi tangan
                ser.write(data.encode('utf-8')) # kirim data ke seria

            # Jika tidak periksa apakah tangan dalam pose "THUMB UP"
            elif hand_pose.is_thumb_down():
                cv2.putText(img, 'THUMB DOWN', (10, 130), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 3)  # Menambahkan teks "FUCK" ke gambar.
                data = "THUMB DOWN\n" # isi data sesuai kondisi tangan
                ser.write(data.encode('utf-8')) # kirim data ke seria
            elif hand_pose.is_call_me():
                cv2.putText(img, 'CALL ME', (10, 130), cv2.FONT_HERSHEY_PLAIN, 2, (3, 252, 23), 3)  # Menambahkan teks "FUCK" ke gambar.
                data = "CALL ME\n" # isi data sesuai kondisi tangan
                ser.write(data.encode('utf-8')) # kirim data ke seria
            # Jika tidak dalam kondisi apapun atau unknown
            else:
                data = "UNKNOWN\n"
                ser.write(data.encode('utf-8'))


            # Baca data dari serial dan print
            if ser.in_waiting > 0:
                dataS = ser.readline().decode('utf-8').strip()
                print(f'Data diterima: {dataS}')


    # Menghitung FPS
    cTime = time.time()  # Mengambil waktu saat ini.
    if cTime != pTime:  # Jika cTime tidak sama dengan pTime
        fps = 1 / (cTime - pTime)  # Menghitung FPS dengan rumus 1 / (cTime - pTime).
        pTime = cTime  # Memperbarui pTime dengan cTime.
        cv2.putText(img, f'FPS: {int(fps)}', (10, 70), cv2.FONT_HERSHEY_PLAIN, 2, (3, 252, 19), 3)  # Menambahkan teks FPS ke gambar.

    #  Keluar jika tombol q di tekan
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    cv2.imshow("Image", img)  # Menampilkan gambar dengan jendela yang berjudul "Image".
    cv2.waitKey(1)  # Menunggu selama 1 milidetik untuk input kunci. Ini diperlukan untuk memperbarui jendela dengan gambar baru secara terus-menerus.



# Release the webcam and close all OpenCV windows
# ser.close()
webcam.release()
cv2.destroyAllWindows()