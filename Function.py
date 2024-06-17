import math

class hands:
    def __init__(self, hand_landmarks, img_width, img_height,hand_orientation):
        self.hand_landmarks = hand_landmarks
        self.img_width = img_width
        self.img_height = img_height
        self.hand_orientation = hand_orientation

        # Lanmark jari jempol
        thumb_tip = hand_landmarks.landmark[4]
        thumb_ip = hand_landmarks.landmark[3]
        thumb_mcp = hand_landmarks.landmark[2]
        # Konversi koordinat landmark jari jempol pixel
        self.thumb_tip_x, self.thumb_tip_y = int(thumb_tip.x * img_width), int(thumb_tip.y * img_height)
        self.thumb_ip_x, self.thumb_ip_y = int(thumb_ip.x * img_width), int(thumb_ip.y * img_height)
        self.thumb_mcp_x, self.thumb_mcp_y = int(thumb_mcp.x * img_width), int(thumb_mcp.y * img_height)

        # Lanmark jari telujuk
        index_finger_tip = hand_landmarks.landmark[8]
        index_finger_dip = hand_landmarks.landmark[7]
        index_finger_pip = hand_landmarks.landmark[6]
        # Konversi koordinat landmark jari telunjuk pixel
        self.index_finger_tip_x, self.index_finger_tip_y = int(index_finger_tip.x * img_width), int(index_finger_tip.y * img_height)
        self.index_finger_dip_x, self.index_finger_dip_y = int(index_finger_dip.x * img_width), int(index_finger_dip.y * img_height)
        self.index_finger_pip_x, self.index_finger_pip_y = int(index_finger_pip.x * img_width), int(index_finger_pip.y * img_height)

        # Lanmark jari tengah
        middle_finger_tip = hand_landmarks.landmark[12]
        middle_finger_pip = hand_landmarks.landmark[10]
        # Konversi koordinat landmark jari tengah pixel
        self.middle_finger_tip_x, self.middle_finger_tip_y = int(middle_finger_tip.x * img_width), int(middle_finger_tip.y * img_height)
        self.middle_finger_pip_x, self.middle_finger_pip_y = int(middle_finger_pip.x * img_width), int(middle_finger_pip.y * img_height)

        # Lanmark jari manis
        ring_finger_tip = hand_landmarks.landmark[16]
        ring_finger_pip = hand_landmarks.landmark[14]
        # Konversi koordinat landmark jari manis pixel
        self.ring_finger_tip_x, self.ring_finger_tip_y = int(ring_finger_tip.x * img_width), int(ring_finger_tip.y * img_height)
        self.ring_finger_pip_x, self.ring_finger_pip_y = int(ring_finger_pip.x * img_width), int(ring_finger_pip.y * img_height)

         # Lanmark jari kelingking
        pinky_finger_tip = hand_landmarks.landmark[20]
        pinky_finger_pip = hand_landmarks.landmark[18]
        # Konversi koordinat landmark jari kelingking pixel
        self.pinky_finger_tip_x, self.pinky_finger_tip_y = int(pinky_finger_tip.x * img_width), int(pinky_finger_tip.y * img_height)
        self.pinky_finger_pip_x, self.pinky_finger_pip_y = int(pinky_finger_pip.x * img_width), int(pinky_finger_pip.y * img_height)


    
    # function unutk menentukan memperhitungkan kodisi tangan berpose ok
    def is_ok(self):
        # Hitung jarak Euclidean antara thumb tip dan index finger tip
        thumb_to_index_distance = math.sqrt((self.thumb_tip_x - self.index_finger_tip_x) ** 2 + (self.thumb_tip_y - self.index_finger_tip_y) ** 2)
        # Menentukan kondisi jari dengan jari lainya
        thumb_and_index_is_touching = thumb_to_index_distance < 25
        middle_finger_condition = abs(self.index_finger_tip_y - self.middle_finger_tip_y) > 40
        ring_finger_condition = abs(self.index_finger_tip_y - self.ring_finger_tip_y) > 100
        pinky_finger_tip_condition = abs(self.index_finger_tip_y - self.pinky_finger_tip_y) > 60

        # Memerika apakah semua kondisi terpenuhi agar terbentuk pose "OK"
        if thumb_and_index_is_touching and middle_finger_condition and ring_finger_condition and pinky_finger_tip_condition : 
            return True 

        return False # return false jika tidak memenuhi kondisi
    

    # function unutk menentukan memperhitungkan kodisi tangan berpose fuck
    def is_fuck(self):
        # Menentukan kondisi jari dengan jari lainya
        diff_x = abs(self.middle_finger_tip_x - self.middle_finger_pip_x)
        diff_y = abs(self.middle_finger_tip_y - self.middle_finger_pip_y)

        if diff_x > diff_y:
            if self.middle_finger_tip_x > self.middle_finger_pip_x:
                # print("right")
                middle_finger_condition = self.middle_finger_tip_x > self.middle_finger_pip_x
                index_finger_condition = self.index_finger_tip_x < self.index_finger_pip_x
                ring_finger_condition = self.ring_finger_tip_x < self.ring_finger_pip_x
                pinky_finger_condition = self.pinky_finger_tip_x < self.pinky_finger_pip_x
            else:
                # print("left") 
                middle_finger_condition = self.middle_finger_tip_x < self.middle_finger_pip_x
                index_finger_condition = self.index_finger_tip_x > self.index_finger_pip_x
                ring_finger_condition = self.ring_finger_tip_x > self.ring_finger_pip_x
                pinky_finger_condition = self.pinky_finger_tip_x > self.pinky_finger_pip_x
        else:
            if self.middle_finger_tip_y > self.middle_finger_pip_y:
                # print("down")
                middle_finger_condition = self.middle_finger_tip_y > self.middle_finger_pip_y
                index_finger_condition = self.index_finger_tip_y < self.index_finger_pip_y
                ring_finger_condition = self.ring_finger_tip_y < self.ring_finger_pip_y
                pinky_finger_condition = self.pinky_finger_tip_y < self.pinky_finger_pip_y
            else:
                # print("up") 
                middle_finger_condition = self.middle_finger_tip_y < self.middle_finger_pip_y
                index_finger_condition = self.index_finger_tip_y > self.index_finger_pip_y
                ring_finger_condition = self.ring_finger_tip_y > self.ring_finger_pip_y
                pinky_finger_condition = self.pinky_finger_tip_y > self.pinky_finger_pip_y



            


        #Memerika apakah semua kondisi terpenuhi agar terbentuk pose "FUCK"
        if middle_finger_condition and index_finger_condition and ring_finger_condition and pinky_finger_condition :
            return True

        return False # return false jika tidak memenuhi kondisi
    

    # function unutk menentukan memperhitungkan kodisi tangan berpose thumb up
    def is_thumb_up(self):

        # Menentukan kondisi jari dengan jari lainya
        thumb_to_index_distance = abs(self.middle_finger_pip_y - self.thumb_tip_y) > 100
        thumb_orientation = self.thumb_tip_y < self.pinky_finger_pip_y
        if self.hand_orientation == "Right": # memerika apakah kondisi tangan kiri
            index_finger_condition = self.index_finger_tip_x > self.index_finger_pip_x
            middle_finger_condition = self.middle_finger_tip_x > self.middle_finger_pip_x
            ring_finger_condition = self.ring_finger_tip_x > self.ring_finger_pip_x
            pinky_finger_condition = self. pinky_finger_tip_x > self.pinky_finger_pip_x
        else:  # memerika apakah kondisi tangan kanan
            index_finger_condition = self.index_finger_tip_x < self.index_finger_pip_x
            middle_finger_condition = self.middle_finger_tip_x < self.middle_finger_pip_x
            ring_finger_condition = self.ring_finger_tip_x < self.ring_finger_pip_x
            pinky_finger_condition = self. pinky_finger_tip_x < self.pinky_finger_pip_x

        #Memerika apakah semua kondisi terpenuhi agar terbentuk pose "THUMB"
        if(thumb_to_index_distance and thumb_orientation and index_finger_condition and middle_finger_condition and ring_finger_condition and pinky_finger_condition):
            return True
        
        return False # return false jika tidak memenuhi kondisi
    

    # function unutk menentukan memperhitungkan kodisi tangan berpose thumb down
    def is_thumb_down(self):

        # Menentukan kondisi jari dengan jari lainya
        thumb_to_index_distance = abs(self.middle_finger_tip_y - self.thumb_mcp_y) > 55
        thumb_orientation = self.thumb_tip_y > self.pinky_finger_pip_y

        if self.hand_orientation == "Right": # memerika apakah kondisi tangan kiri
            index_finger_condition = self.index_finger_tip_x > self.index_finger_pip_x
            middle_finger_condition = self.middle_finger_tip_x > self.middle_finger_pip_x
            ring_finger_condition = self.ring_finger_tip_x > self.ring_finger_pip_x
            pinky_finger_condition = self. pinky_finger_tip_x > self.pinky_finger_pip_x
        else:  # memerika apakah kondisi tangan kanan
            index_finger_condition = self.index_finger_tip_x < self.index_finger_pip_x
            middle_finger_condition = self.middle_finger_tip_x < self.middle_finger_pip_x
            ring_finger_condition = self.ring_finger_tip_x < self.ring_finger_pip_x
            pinky_finger_condition = self. pinky_finger_tip_x < self.pinky_finger_pip_x

        #Memerika apakah semua kondisi terpenuhi agar terbentuk pose "THUMB"
        if(thumb_to_index_distance and thumb_orientation and index_finger_condition and middle_finger_condition and ring_finger_condition and pinky_finger_condition):
            return True
        
        return False # return false jika tidak memenuhi kondisi
    
    def is_call_me(self):
        # Hitung jarak Euclidean antara thumb tip dan pinky finger tip
        thumb_to_pinky_distance = math.sqrt((self.thumb_tip_x - self.pinky_finger_tip_x) ** 2 + (self.thumb_tip_y - self.pinky_finger_tip_y) ** 2)

        index_finger_condition = self.index_finger_tip_x > self.index_finger_pip_x
        middle_finger_condition = self.middle_finger_tip_x > self.middle_finger_pip_x
        ring_finger_condition = self.ring_finger_tip_x > self.ring_finger_pip_x
        pinky_finger_condition = self.pinky_finger_tip_x < self.pinky_finger_pip_x

        #Memerika apakah semua kondisi terpenuhi agar terbentuk pose "CALL ME"
        if (thumb_to_pinky_distance > 150) and index_finger_condition and middle_finger_condition and ring_finger_condition and pinky_finger_condition:
            return True
        
        return False
    



         
    




