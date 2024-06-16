import math

# class hands:
#     def __init__(self, hand_landmarks, img_width, img_height):
#         self.hand_landmarks = hand_landmarks
#         self.img_width = img_width
#         self.img_height = img_height

#         # Lanmark jari jempol
#         thumb_tip = hand_landmarks.landmark[4]
#         thumb_pip = hand_landmarks.landmark[2]
#         # Konversi koordinat landmark jari jempol pixel
#         self.thumb_tip_x, self.thumb_tip_y = int(thumb_tip.x * img_width), int(thumb_tip.y * img_height)
#         self.thumb_pip_x, self.thumb_pip_y = int(thumb_pip.x * img_width), int(thumb_pip.y * img_height)

#         # Lanmark jari telujuk
#         index_finger_tip = hand_landmarks.landmark[8]
#         index_finger_pip = hand_landmarks.landmark[6]
#         # Konversi koordinat landmark jari telunjuk pixel
#         self.index_finger_tip_x, self.index_finger_tip_y = int(index_finger_tip.x * img_width), int(index_finger_tip.y * img_height)
#         self.index_finger_pip_x, self.index_finger_pip_y = int(index_finger_pip.x * img_width), int(index_finger_pip.y * img_height)

#         # Lanmark jari tengah
#         index_finger_tip = hand_landmarks.landmark[8]
#         index_finger_pip = hand_landmarks.landmark[6]
#         # Konversi koordinat landmark jari telunjuk pixel
#         self.index_finger_tip_x, self.index_finger_tip_y = int(index_finger_tip.x * img_width), int(index_finger_tip.y * img_height)
#         self.index_finger_pip_x, self.index_finger_pip_y = int(index_finger_pip.x * img_width), int(index_finger_pip.y * img_height)



def is_ok(hand_landmarks, img_width ,img_height):
    thumb_tip = hand_landmarks.landmark[4]
    index_finger_tip = hand_landmarks.landmark[8]
    middle_finger_tip = hand_landmarks.landmark[12]
    ring_finger_tip = hand_landmarks.landmark[16]
    pinky_finger_tip = hand_landmarks.landmark[20]

    # Konversi koordinat landmark ke pixel
    thumb_tip_x, thumb_tip_y = int(thumb_tip.x * img_width), int(thumb_tip.y * img_height)
    index_finger_tip_x, index_finger_tip_y = int(index_finger_tip.x * img_width), int(index_finger_tip.y * img_height)
    middle_finger_tip_y = int(middle_finger_tip.y * img_height)
    ring_finger_tip_y = int(ring_finger_tip.y * img_height)
    pinky_finger_tip_y = int(pinky_finger_tip.y * img_height)


    # Hitung jarak Euclidean antara thumb tip dan index finger tip
    distance_thumb_and_index = math.sqrt((thumb_tip_x - index_finger_tip_x) ** 2 + (thumb_tip_y - index_finger_tip_y) ** 2)

    isTouching = distance_thumb_and_index < 25
    middle_finger_condition = abs(index_finger_tip_y - middle_finger_tip_y) > 40
    ring_finger_condition = abs(index_finger_tip_y - ring_finger_tip_y) > 100
    pinky_finger_tip_condition = abs(index_finger_tip_y - pinky_finger_tip_y) > 60
    
    # Jika jarak kurang dari ambang batas, anggap bersentuhan
    if isTouching and middle_finger_condition and ring_finger_condition and pinky_finger_tip_condition:  # Ambang batas jarak bisa disesuaikan
        return True
    
    return False

# Fungsi untuk memeriksa apakah tangan dalam pose "thumbs up"
def is_fuck(hand_landmarks, img_height):
    # Landmark jari tengah
    middle_finger_tip = hand_landmarks.landmark[12]
    middle_finger_pip = hand_landmarks.landmark[10]
    # Konversi koordinat landmark jari tengah ke pixel
    middle_finger_tip_y = int(middle_finger_tip.y * img_height)
    middle_finger_pip_y = int(middle_finger_pip.y * img_height)


    # Landmark jari telunjuk
    index_finger_tip = hand_landmarks.landmark[8]
    index_finger_pip = hand_landmarks.landmark[6]
    # Konversi koordinat landmark jari telunjuk ke pixel
    index_finger_tip_y = int(index_finger_tip.y * img_height)
    index_finger_pip_y = int(index_finger_pip.y * img_height)

    # Landmark jari  manis
    ring_finger_tip = hand_landmarks.landmark[16]
    ring_finger_pip = hand_landmarks.landmark[14]
    # Konversi koordinat landmark jari manis ke pixel
    ring_finger_tip_y = int(ring_finger_tip.y * img_height)
    ring_finger_pip_y = int(ring_finger_pip.y * img_height)

    # Landmark jari kelingking
    pinky_tip = hand_landmarks.landmark[20]
    pinky_pip = hand_landmarks.landmark[18]
    # Konversi koordinat landmark jari kelingking ke pixel
    pinky_tip_y = int(pinky_tip.y * img_height)
    pinky_pip_y = int(pinky_pip.y * img_height)
    # Konversi koordinat landmark ke pixel

    # Logika untuk mendeteksi pose "fuck"
    middle_finger_condition = middle_finger_tip_y < middle_finger_pip_y
    index_finger_condition = index_finger_tip_y > index_finger_pip_y
    ring_finger_condition = ring_finger_tip_y > ring_finger_pip_y
    pinky_finger_condition = pinky_tip_y > pinky_pip_y

    # createOutput = f"""
    # Jari Telunjuk: tip = {index_finger_tip_y}, pip = {index_finger_pip_y}
    # Jari Tengah: tip = {middle_finger_tip_y}, pip = {middle_finger_pip_y}
    # Jari Manis: tip = {ring_finger_tip_y}, pip = {ring_finger_pip_y}
    # Jari Kelingking = {pinky_tip_y}, pip = {pinky_pip_y}
    # """

    # print(createOutput.lstrip())


    if(middle_finger_condition and index_finger_condition and ring_finger_condition and pinky_finger_condition):
        return True
    

    return False


def is_thumb (hand_landmarks, img_width ,img_height, hand_orientation):

    # Landmark jari jempol
    thumb_tip = hand_landmarks.landmark[4]
    # Konversi koordinat landmark jari tengah ke pixel
    thumb_tip_y = int(thumb_tip.y * img_height)
    middle_finger_tip = hand_landmarks.landmark[12]
    middle_finger_pip = hand_landmarks.landmark[10]
    # Konversi koordinat landmark jari tengah ke pixel
    middle_finger_tip_x = int(middle_finger_tip.x * img_width)
    middle_finger_pip_x, middle_finger_pip_y = int(middle_finger_pip.x * img_width),int(middle_finger_pip.y * img_height)


    # Landmark jari telunjuk
    index_finger_tip = hand_landmarks.landmark[8]
    index_finger_pip = hand_landmarks.landmark[6]
    # Konversi koordinat landmark jari telunjuk ke pixel
    index_finger_tip_x = int(index_finger_tip.x * img_width)
    index_finger_pip_x = int(index_finger_pip.x * img_width)

    # Landmark jari  manis
    ring_finger_tip = hand_landmarks.landmark[16]
    ring_finger_pip = hand_landmarks.landmark[14]
    # Konversi koordinat landmark jari manis ke pixel
    ring_finger_tip_x = int(ring_finger_tip.x * img_width)
    ring_finger_pip_x = int(ring_finger_pip.x * img_width)

    # Landmark jari kelingking
    pinky_tip = hand_landmarks.landmark[20]
    pinky_pip = hand_landmarks.landmark[18]
    # Konversi koordinat landmark jari kelingking ke pixel
    pinky_tip_x = int(pinky_tip.x * img_width)
    pinky_pip_x = int(pinky_pip.x * img_width)
    # Konversi koordinat landmark ke pixel

    thumb_to_index_distance = (middle_finger_pip_y - thumb_tip_y) < 150
    if hand_orientation == "Right": # memerika apakah kondisi tangan kiri
        index_finger_condition = index_finger_tip_x > index_finger_pip_x
        middle_finger_condition = middle_finger_tip_x > middle_finger_pip_x
        ring_finger_condition = ring_finger_tip_x > ring_finger_pip_x
        pinky_finger_condition =  pinky_tip_x > pinky_pip_x
    else:  # memerika apakah kondisi tangan kanan
        index_finger_condition = index_finger_tip_x < index_finger_pip_x
        middle_finger_condition = middle_finger_tip_x < middle_finger_pip_x
        ring_finger_condition = ring_finger_tip_x < ring_finger_pip_x
        pinky_finger_condition =  pinky_tip_x < pinky_pip_x




    if(thumb_to_index_distance and index_finger_condition and middle_finger_condition and ring_finger_condition and pinky_finger_condition):
        return True
    

    return False


