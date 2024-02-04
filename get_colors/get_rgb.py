import numpy as np
import pyscreenshot
import serial
import scipy
import time

ser = serial.Serial('/dev/ttyACM1')

x_res = 1920
y_res = 1080
num_pixels = 150
NUM_CLUSTERS = 5
slice_width = x_res / num_pixels

def get_dominant_color(image):
    data = image.getdata()
    data = np.asarray(data)
    exit()
    print(scipy.cluster.vq.kmeans(image, k_or_guess=8))
    exit()
    return None


while True:
    print('loop')
    image = pyscreenshot.grab()
    rgb_colors = bytearray()
    start = time.time()
    for i in range(num_pixels):
        x_start = i * slice_width
        x_stop = x_start + slice_width
        sliced = image.crop((x_start, 0, x_stop, y_res))

        dominant_color = get_dominant_color(sliced)

        for i in range(3):
            color = dominant_color[i]
            rgb_colors.append(color)
    end = (time.time() - start) * 1000
    if (end > 100):
        print(end, "ms")

    print(len(rgb_colors))
    ser.write(rgb_colors)
