# https://www.codewars.com/kata/surface-area-and-volume-of-a-box/train/python


def get_size(w, h, d):
    area = 2*(w*h + w*d + d*h)
    volume = w*h*d
    return [area, volume]


print(get_size(3, 2, 5))