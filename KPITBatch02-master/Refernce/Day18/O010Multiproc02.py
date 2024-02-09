
import os
import time
from PIL import Image, ImageFilter
import concurrent.futures

path = "C:\\Training\\PycharmProjects\\CDAC_NOV2023\\Day18\\"
files = os.listdir(path)
imgFiles = []
for fl in files:
    if fl.endswith(".jpg"):
        imgFiles.append(fl)

st = time.perf_counter()
pxlSize = (1200, 1200)

def imagePrc(imgFl):
    img = Image.open(path+imgFl)
    img = img.filter(ImageFilter.GaussianBlur(50))
    img.thumbnail(pxlSize)
    img.save(f"{path}/{imgFl}")
    print(f"{imgFl} was processed.....")

if __name__ == '__main__':
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(imagePrc, imgFiles)

        et = time.perf_counter()
        print(f"Completed processing of all images in {et - st} seconds.....")