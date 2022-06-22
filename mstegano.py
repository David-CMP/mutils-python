import cv2
import numpy as np
from numpy.typing import NDArray
import mconv


def str2img(str_: str, impath: str) -> NDArray[np.uint8]:
    image = cv2.imread(impath, cv2.IMREAD_UNCHANGED)
    bin_map = iter(mconv.str2bin(str_) + mconv.int2bin(0xffd9))
    
    for i, line in enumerate(image):
        for j, px in enumerate(line):
            for k, s in enumerate(px):
                v = next(bin_map, None)
                if v is None:
                    continue    
                elif (s%2) != int(v):
                    image[i, j, k] = s + [-1, 1][int(s == 0)]
                else:
                    image[i, j, k] = s
    
    cv2.imwrite("out.png", image)
    return image


def img2str(impath: str) -> str:
    im = cv2.imread(impath)
    str_ = ""
    for line in im:
        for px in line:
            for s in px:
                str_ += str(s%2)
    str_ = str_.split(mconv.int2bin(0xffd9))[0]
    return str_
