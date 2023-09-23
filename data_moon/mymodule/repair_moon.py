import sys
import os
import time
import requests

sys.path.append('C:/my_games/moonlight/data_moon/mymodule')

import variable as v_

def repair_start(cla):
    try:

        my_stat_up(cla)
        skillbook_study(cla)


    except Exception as e:
        print(e)



def my_stat_up(cla):
    import numpy as np
    import cv2

    from action_moon import clean_screen
    from function_moon import imgs_set_, click_pos_2

    try:
        print("my_stat_up", cla)

        get = False
        get_count = 0
        while get is False:
            get_count += 1
            if get_count > 7:
                get = True

            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\tuto\\stat_point.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 130, 90, 170, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                for i in range(10):
                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\tuto\\stat_zero.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(60, 130, 100, 170, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_2(280, 150, cla)
                        break
                    else:
                        click_pos_2(145, 225, cla)
                    time.sleep(0.2)
                for i in range(10):
                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\tuto\\stat_point.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 130, 90, 170, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        clean_screen(cla)
                    else:
                        break
                    time.sleep(0.2)
            else:
                clean_screen(cla)

                for i in range(10):
                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\tuto\\stat_point.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 130, 90, 170, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        break
                    else:
                        click_pos_2(35, 65, cla)
                        time.sleep(0.2)
                        click_pos_2(45, 100, cla)
                    time.sleep(0.2)



    except Exception as e:
        print(e)
        return 0


def skillbook_study(cla):
    import numpy as np
    import cv2

    from action_moon import clean_screen
    from function_moon import imgs_set_, click_pos_2, click_pos_reg

    try:
        print("skillbook_study", cla)

        get = False
        get_count = 0
        while get is False:
            get_count += 1
            if get_count > 7:
                get = True

            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\repair\\boonhae_click.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(750, 920, 840, 970, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                click_pos_2(700, 940, cla)
                time.sleep(0.1)
                click_pos_2(700, 940, cla)
                time.sleep(1)

                not_have_skillbook = 0

                for s in range(10):
                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\repair\\skillbook_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(620, 120, 960, 900, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        for i in range(10):
                            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\repair\\study.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(460, 730, 560, 800, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                break
                            time.sleep(0.3)

                    # 초급단계에서는 스킬장착 필요없음



                    else:
                        not_have_skillbook += 1
                        if not_have_skillbook > 2:
                            break
                    time.sleep(0.2)

                for s in range(10):
                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\repair\\boonhae_click.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(750, 920, 840, 970, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        clean_screen(cla)
                    else:
                        break
                    time.sleep(0.2)

            else:
                clean_screen(cla)

                for i in range(10):
                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\repair\\boonhae_click.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(750, 920, 840, 970, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        break
                    else:
                        click_pos_2(870, 65, cla)
                    time.sleep(0.2)



    except Exception as e:
        print(e)
        return 0