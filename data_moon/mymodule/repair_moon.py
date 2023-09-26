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
        budy_sohwan(cla)
        hyungsang_sohwan(cla)


    except Exception as e:
        print(e)

def realtime(cla):
    import numpy as np
    import cv2
    from function_moon import imgs_set_, click_pos_reg

    try:


        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\repair\\jangchak\\jangchack.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(820, 760, 930, 840, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("realtime : jangchak", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)





    except Exception as e:
        print(e)
        return 0

def my_stat_up(cla):
    import numpy as np
    import cv2

    from action_moon import clean_screen
    from function_moon import imgs_set_, click_pos_2

    try:
        print("my_stat_up", cla)

        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\repair\\stat_point_check.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 30, 45, 60, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("stat_point_check", imgs_)


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
                            get = True
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
                            imgs_ = imgs_set_(460, 730, 620, 800, cla, img, 0.8)
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
                        get = True
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


def budy_sohwan(cla):
    import numpy as np
    import cv2

    from action_moon import clean_screen, menu_open
    from function_moon import imgs_set_, click_pos_2, click_pos_reg

    try:
        print("budy_sohwan", cla)

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

                    budy_open = False

                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\repair\\budy_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(620, 120, 960, 900, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        budy_open = True
                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\repair\\budy_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(620, 120, 960, 900, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        budy_open = True

                    if budy_open == True:
                        for i in range(10):
                            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\repair\\open.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(460, 730, 620, 800, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                break
                            time.sleep(0.3)

                        for i in range(10):

                            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\repair\\full.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(520, 630, 620, 680, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(0.1)
                                click_pos_2(550, 700, cla)
                                time.sleep(0.1)

                            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\repair\\chooga.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(300, 980, 800, 1040, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(0.1)

                            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\repair\\sohwan_skip.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(0, 950, 80, 1040, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(0.1)

                            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\repair\\sohwan_confirm.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(250, 980, 800, 1040, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                break
                            else:
                                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\repair\\budy_open_1.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(390, 980, 620, 1040, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)

                                else:
                                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\repair\\budy_open_2.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(390, 980, 620, 1040, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        click_pos_reg(imgs_.x, imgs_.y, cla)

                                    else:
                                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\clean_screen\\skip_2.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(0, 30, 950, 800, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            print("skip_1...", imgs_)
                                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.5)

                    # 초급단계에서는 스킬장착 필요없음



                    else:
                        not_have_skillbook += 1
                        if not_have_skillbook > 2:
                            break
                    time.sleep(0.3)

                for s in range(10):
                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\repair\\boonhae_click.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(750, 920, 840, 970, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        clean_screen(cla)
                    else:
                        get = True
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

        # 버디 장착착
        get = False
        get_count = 0
        while get is False:
            get_count += 1
            if get_count > 7:
                get = True
            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\title\\budy_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 30, 100, 100, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                click_pos_2(670, 220, cla)
                time.sleep(0.1)
                click_pos_2(160, 1010, cla)
                time.sleep(0.1)
                clean_screen(cla)
                get = True

            else:
                menu_open(cla)
                time.sleep(0.1)
                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\repair\\menu_budy.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(670, 100, 960, 270, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    for i in range(10):
                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\title\\budy_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(10, 30, 100, 100, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            break
                        time.sleep(0.5)


    except Exception as e:
        print(e)
        return 0

def hyungsang_sohwan(cla):
    import numpy as np
    import cv2

    from action_moon import clean_screen, menu_open
    from function_moon import imgs_set_, click_pos_2, click_pos_reg

    try:
        print("hyungsang_sohwan", cla)

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

                    open_ready = False

                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\repair\\hyungsang_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(620, 120, 960, 900, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        open_ready = True

                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\repair\\hyungsang_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(620, 120, 960, 900, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        open_ready = True

                    if open_ready == True:
                        for i in range(10):
                            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\repair\\open.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(460, 730, 620, 800, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                break
                            time.sleep(0.3)

                        for i in range(10):

                            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\repair\\full.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(520, 630, 620, 680, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(0.1)
                                click_pos_2(550, 700, cla)
                                time.sleep(0.1)

                            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\repair\\chooga.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(300, 980, 800, 1040, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(0.1)

                            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\repair\\sohwan_skip.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(0, 950, 80, 1040, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(0.1)

                            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\repair\\sohwan_confirm.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(250, 980, 800, 1040, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                break
                            else:
                                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\repair\\hyungsang_open_1.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(390, 980, 620, 1040, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)

                                else:
                                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\repair\\budy_open_2.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(390, 980, 620, 1040, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        click_pos_reg(imgs_.x, imgs_.y, cla)

                                    else:
                                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\clean_screen\\skip_2.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(0, 30, 950, 800, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            print("skip_1...", imgs_)
                                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.5)

                    # 초급단계에서는 스킬장착 필요없음



                    else:
                        not_have_skillbook += 1
                        if not_have_skillbook > 2:
                            break
                    time.sleep(0.3)

                for s in range(10):
                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\repair\\boonhae_click.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(750, 920, 840, 970, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        clean_screen(cla)
                    else:
                        get = True
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

        # 버디 장착착
        get = False
        get_count = 0
        while get is False:
            get_count += 1
            if get_count > 7:
                get = True
            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\title\\hyungsang_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 30, 110, 100, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                click_pos_2(670, 220, cla)
                time.sleep(0.1)
                click_pos_2(160, 1010, cla)
                time.sleep(0.1)
                clean_screen(cla)
                get = True

            else:
                menu_open(cla)
                time.sleep(0.1)
                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\repair\\menu_hyungsang.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(670, 100, 960, 270, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    for i in range(10):
                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\title\\hyungsang_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(10, 30, 110, 100, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            break
                        time.sleep(0.5)


    except Exception as e:
        print(e)
        return 0