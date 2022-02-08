import cv2


# 用于存放颜色的 B，G，R值对应的颜色
import numpy as np

'''
各个颜色的B、G、R像素
color = {
    (147, 42, 112):"基佬紫",
    (121, 93, 233):"猛男粉",
    (125, 215, 98):"绿",
    (195, 45, 58):"紫蓝",
    (19, 150, 121):"暗绿",
    (230, 163, 82):"天蓝",
    (65, 139, 232):"橙",
    (102, 99, 98):"灰",
    (34, 42, 197):"红"
    }
'''


'''

glass_img->np.ndarray:提取图像的感兴趣区域，该区域内全为试管；
！！因图像为直接裁剪，此版本只适用zad的手机游戏界面的完整截图！！

glasses_coordinates:返回一个列表，里面装有每个试管的最低点的坐标[列数, 行数]。

water_color_lst:返回与main方法里结构相同的嵌套列表，试管按从左到右，从上到下排列，数字代表的颜色按从上到下排列。
'''

def glass_img_processing(img_path:str) -> np.ndarray:
    img = cv2.imread(img_path)
    glass_img = img[500:1530, :, :]
    return glass_img


def glasses_coordinates(glass_img:np.ndarray) -> list:
    gray = cv2.cvtColor(glass_img, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 190, 255, cv2.THRESH_BINARY_INV)
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    down_point = []
    for contour in contours:
        down_point.append(max(list(contour.reshape(-1, 2)), key=lambda item: item[1]))
    for point in down_point:
        point[1]+=500
    return down_point



def water_color_lst(down_point:list, glass_img:np.ndarray) -> list:
    lst = []

    for coordinate in down_point:
        one_glass = []
        l, h = tuple(coordinate)
        h -= 500
        for i in range(4):
            if judge_color(tuple(glass_img[h - 50 - 88 * i, l])) is not None:
                one_glass.append(judge_color(tuple(glass_img[h - 50 - 88*i, l])))
            else:
                continue
        lst.append(one_glass)
    return lst[::-1]


'''
颜色对应的数字号码：
暗绿 1
绿色 2
灰色 3
蓝色 4
天蓝 5
紫色 6
红色 7
橙色 8
粉色 9

'''
def judge_color(color:tuple) -> int:
    arr = cv2.cvtColor(np.uint8(color).reshape(1,1,3), cv2.COLOR_BGR2HSV)
    h, s, v = tuple(arr.reshape(3,))
    if h > 180:
        h = h - 180
    if 37<=h<=50 and 43<=s<=255 and 46<=v<=255:
        return 1
    elif 51<=h<=77 and 43<=s<=255 and 46<=v<=255:
        return 2
    elif 0<=h<=180 and 0<=s<=43 and 46<=v<=220:
        return 3
    elif 113<=h<=124 and 43<=s<=255 and 46<=v<=255:
        return 4
    elif 100<=h<=112 and 43<=s<=255 and 46<=v<=255:
        return 5
    elif 125<=h<=155 and 43<=s<=255 and 46<=v<=255:
        return 6
    elif 0<=h<=10 and 43<=s<=255 and 46<=v<=255:
        return 7
    elif 11<=h<=25 and 43<=s<=255 and 46<=v<=255:
        return 8
    elif 156<=h<=180 and 43<=s<=255 and 46<=v<=255:
        return 9
    else:
        pass


def parse():
    img_path = "./img/cache.png"
    # 调用上述函数
    glass_img = glass_img_processing(img_path)
    down_point = glasses_coordinates(glass_img)
    print(water_color_lst(down_point, glass_img))
    down_point.reverse()
    return water_color_lst(down_point, glass_img),down_point


if __name__ == "__main__":
    #传一个图片路径，图片大小和zad的手机截图一样的：1080*2340否则可能出现bug
    img_path = "../img/cache.png"

    #调用上述函数
    glass_img = glass_img_processing(img_path)
    down_point = glasses_coordinates(glass_img)
    print(down_point)
    down_point.reverse()
    print(down_point)
    print(water_color_lst(down_point, glass_img))

