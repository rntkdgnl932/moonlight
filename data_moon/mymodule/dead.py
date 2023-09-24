import sys
import os
import time
import requests

sys.path.append('C:/my_games/moonlight/data_moon/mymodule')

import variable as v_

def dead_die(cla, sche):
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

        dead = False

        print("dead_die")
        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\dead\\boohwal_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(570, 870, 700, 950, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("boohwal_1...", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
            dead = True
            for i in range(10):
                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\maul\\chango.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(800, 970, 920, 1040, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    break
                else:
                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\action\\loding_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(250, 920, 650, 1040, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        loading(cla)
                time.sleep(0.5)

        if dead == True:
            if sche == "튜토육성":
                get_items(cla)
                repair_start(cla)
                maul_potion_small_only(cla)

                v_.tuto_dead += 1
                if v_.tuto_dead > 1:
                    myQuest_play_add(cla, sche)
            else:
                get_items(cla)
                repair_start(cla)
                maul_potion_small_only(cla)

        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\dead\\exp_recovery.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(200, 30, 350, 100, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("exp recovery...", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)

            for i in range(10):
                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\dead\\exp_recovery_title.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(400, 320, 540, 380, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("exp recovery title", imgs_)
                    click_pos_2(470, 710, cla)
                else:
                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\dead\\anymore_exp_recovery.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(390, 470, 570, 530, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("anymore exp recovery", imgs_)
                        clean_screen(cla)
                        break



    except Exception as e:
        print(e)

