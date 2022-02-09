import math
import array

import cv2
import numpy as np


class Parser:
    def __init__(self, img_path:str):
        self.img_path = img_path
        self.length, self.width, _ = cv2.imread(img_path).shape
        self.proportion = self.img_scale_calculation(img_path)
        self.color_dic = {}

    def __call__(self):
        glass_img = self.glass_img_processing(self.img_path)
        down_point = self.glasses_coordinates(glass_img)
        return self.water_color_lst(down_point, glass_img), self.center_coordinates(down_point)



    def img_scale_calculation(self, img_path: str) -> float:
        img = cv2.imread(img_path)
        length, width, _ = img.shape
        length_original, width_original = 2340, 1080
        return length / length_original



    def center_coordinates(self, down_point: list,) -> list:
        lst = []
        for array_ in down_point:
            item_list = array_.tolist()
            lst.append((item_list[0] + 10, item_list[1] + (int(self.proportion * 550) - int(50 * self.proportion))))
        return lst[::-1]

    def glass_img_processing(self, img_path: str) -> np.ndarray:
        img = cv2.imread(self.img_path)
        glass_img = img[int(550 * self.proportion):int(1530 * self.proportion), :, :]
        # glass_img = img[700:1200, :, :]
        return glass_img

    def glasses_coordinates(self, glass_img: np.ndarray) -> list:
        gray = cv2.cvtColor(glass_img, cv2.COLOR_BGR2GRAY)
        _, binary = cv2.threshold(gray, 190, 255, cv2.THRESH_BINARY_INV)
        contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        down_point = []
        for contour in contours:
            down_point.append(max(list(contour.reshape(-1, 2)), key=lambda item: item[1]))
        return down_point

    def water_color_lst(self, down_point: list, glass_img: np.ndarray) -> list:
        lst = []
        first = int(50 * self.proportion)
        other = int(88 * self.proportion)
        for coordinate in down_point:
            one_glass = []
            l, h = tuple(coordinate)
            for i in range(4):
                if self.judgement_color(tuple(glass_img[h - first - other * i, l])) != 0:
                    one_glass.append(self.judgement_color(tuple(glass_img[h - first - other * i, l])))
            lst.append(one_glass)
        return lst[::-1]

    def HSVDistance(self,hsv_1: tuple, hsv_2: tuple) -> float:
        H_1, S_1, V_1 = hsv_1
        H_2, S_2, V_2 = hsv_2
        R = 100
        angle = 30
        h = R * math.cos(angle / 180 * math.pi)
        r = R * math.sin(angle / 180 * math.pi)
        x1 = r * V_1 * S_1 * math.cos(H_1 / 180 * math.pi)
        y1 = r * V_1 * S_1 * math.sin(H_1 / 180 * math.pi)
        z1 = h * (1 - V_1)
        x2 = r * V_2 * S_2 * math.cos(H_2 / 180 * math.pi)
        y2 = r * V_2 * S_2 * math.sin(H_2 / 180 * math.pi)
        z2 = h * (1 - V_2)
        dx = x1 - x2
        dy = y1 - y2
        dz = z1 - z2
        return math.sqrt(dx * dx + dy * dy + dz * dz)



    def judgement_color(self,color_rgb: tuple):
        arr = cv2.cvtColor(np.uint8(color_rgb).reshape(1, 1, 3), cv2.COLOR_BGR2HSV)
        color_hsv = tuple(arr.reshape(3, ))
        if not self.color_dic:
            self.color_dic[color_hsv] = 0
            return self.color_dic[color_hsv]
        else:
            if all(map(lambda key: self.HSVDistance(color_hsv, key) >= 80000, self.color_dic.keys())):
                self.color_dic[color_hsv] = len(self.color_dic.values())
                return self.color_dic[color_hsv]
            else:
                min_distance = min((self.HSVDistance(color_hsv, i) for i in self.color_dic.keys()))
                for i in self.color_dic.keys():
                    if self.HSVDistance(i, color_hsv) == min_distance:
                        return self.color_dic[i]
                    else:
                        continue



p = Parser(img_path="5.jpg")



water_list, glass_list = p()

print(water_list)
print(glass_list)


