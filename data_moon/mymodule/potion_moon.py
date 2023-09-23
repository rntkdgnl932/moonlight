import sys
import os
import time
import requests

sys.path.append('C:/my_games/moonlight/data_moon/mymodule')

import variable as v_

def maul_potion_small_only(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random

    from function_moon import imgs_set_, click_pos_reg, click_pos_2

    from action_moon import loading, clean_screen
    from get_item import get_items
    from tuto_moon import tuto_stat_up


    try:
        print("maul_potion")

        in_maul = False
        in_maul_count = 0
        while in_maul is False:
            in_maul_count += 1
            if in_maul_count > 7:
                in_maul = True

            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\maul\\chango.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(800, 970, 920, 1040, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                in_maul = True
            else:
                clean_screen(cla)
                click_pos_2(25, 180, cla)
                for i in range(10):
                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\maul\\maul_move_confirm.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(500, 560, 600, 620, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        break
                    time.sleep(0.2)
                for i in range(10):
                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\maul\\chango.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(800, 970, 920, 1040, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        break
                    time.sleep(0.5)

        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\maul\\chango.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(800, 970, 920, 1040, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:

            for i in range(20):
                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\jabhwa_title.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(50, 30, 110, 80, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    break
                else:
                    click_pos_2(745, 1000, cla)
                time.sleep(1)

            buy = False
            buy_count = 0
            while buy is False:
                buy_count += 1
                if buy_count > 7:
                    buy = True

                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\buy_title.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(470, 300, 530, 350, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    buy = True
                    click_pos_2(350, 670, cla)
                    time.sleep(0.1)
                    click_pos_2(350, 670, cla)
                    time.sleep(0.1)
                    click_pos_2(545, 735, cla)
                    time.sleep(0.1)

                    # 밖에 눌러서 나가기
                    click_pos_2(545, 735, cla)
                    time.sleep(0.1)

                else:

                    for i in range(10):
                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\buy_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(470, 300, 530, 350, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            break
                        else:
                            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\small_potion_click.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(50, 120, 100, 170, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.2)
        # 나가기
        for i in range(10):
            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\buy_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(470, 300, 530, 350, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                clean_screen(cla)
            else:
                break
            time.sleep(0.3)


    except Exception as e:
        print(e)

