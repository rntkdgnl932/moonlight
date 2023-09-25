import sys
import os
import time
import requests

sys.path.append('C:/my_games/moonlight/data_moon/mymodule')

import variable as v_

def temporary_event_start(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random

    from function_moon import imgs_set_, click_pos_reg, click_pos_2

    from action_moon import loading, clean_screen
    from get_item import get_items
    from potion_moon import maul_potion_small_only
    from schedule import myQuest_play_add
    from repair_moon import repair_start


    try:

        print("temporary_event_start")
        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\temporary_event\\5000.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(240, 60, 300, 100, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            click_pos_reg(imgs_.x, imgs_.y, cla)

            for i in range(10):
                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\temporary_event\\gonghundo_bosang.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(200, 300, 700, 700, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    break
                time.sleep(0.3)



                



    except Exception as e:
        print(e)

