import sys
import os
import time
import requests

sys.path.append('C:/my_games/moonlight/data_moon/mymodule')

import variable as v_

def go_test():
    import numpy as np
    import cv2
    import pyautogui
    import random

    from function_moon import imgs_set_, click_pos_reg, click_pos_2, drag_pos_reg

    from action_moon import menu_open, clean_screen, out_check

    from get_item import get_event

    from tuto_moon import tuto_start

    print("tst")
    cla = "one"

    plus = 0

    if cla == "two":
        plus = 960
    if cla == "three":
        plus = 960 * 2
    if cla == "four":
        plus = 960 * 3

    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\tuto\\tuto_click4.PNG"
    img_array = np.fromfile(full_path, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    imgs_ = imgs_set_(850, 100, 900, 450, cla, img, 0.8)
    if imgs_ is not None and imgs_ != False:
        print("tuto_click4", imgs_)
        drag_pos_reg(imgs_.x, imgs_.y, imgs_.x, imgs_.y + 150, cla)

