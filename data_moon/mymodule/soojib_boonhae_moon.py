import sys
import os
import time
import requests

sys.path.append('C:/my_games/moonlight/data_moon/mymodule')

import variable as v_

def soojib_boonhae_start(cla):
    from action_moon import clean_screen
    try:
        print("soojib_boonhe")
        soojib_start(cla)
        clean_screen(cla)
        boonhae_start(cla)


    except Exception as e:
        print(e)

def soojib_start(cla):
    import numpy as np
    import cv2

    from function_moon import imgs_set_, click_pos_reg, click_pos_2
    from action_moon import menu_open
    try:
        print("soojib_boonhe")

        soojib = False
        soojib_count = 0
        while soojib is False:
            soojib_count += 1
            if soojib_count > 7:
                soojib = True
            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\title\\soojib_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 10, 120, 80, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:

                soojib = True

                print("soojib_title", imgs_)
                # 공격
                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\soojib_boonhae\\soojib_title_point.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(80, 60, 140, 110, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    click_pos_2(110, 100, cla)
                    soojib_setting(cla)
                    soojib_join(cla, "attack")
                    time.sleep(0.1)

                # 방어
                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\soojib_boonhae\\soojib_title_point.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(210, 60, 280, 110, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    click_pos_2(250, 100, cla)
                    soojib_setting(cla)
                    soojib_join(cla, "amor")
                    time.sleep(0.1)

                # 기타
                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\soojib_boonhae\\soojib_title_point.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(360, 60, 410, 110, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    click_pos_2(390, 100, cla)
                    soojib_setting(cla)
                    soojib_join(cla, "etc")
                    time.sleep(0.1)

                # 이벤트
                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\soojib_boonhae\\soojib_title_point.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(500, 60, 560, 110, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    click_pos_2(530, 100, cla)
                    soojib_join(cla, "event")
                    time.sleep(0.1)

            else:
                menu_open(cla)
                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\soojib_boonhae\\menu_soojib.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(670, 170, 960, 350, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("menu soojb", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)

                    for i in range(10):
                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\title\\soojib_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(10, 10, 120, 80, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            break
                        time.sleep(0.5)
            time.sleep(0.3)





    except Exception as e:
        print(e)


def soojib_setting(cla):
    import numpy as np
    import cv2

    from function_moon import imgs_set_, click_pos_reg, click_pos_2

    try:
        print("soojib setting")

        soojib = False
        soojib_count = 0
        while soojib is False:
            soojib_count += 1
            if soojib_count > 7:
                soojib = True
            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\soojib_boonhae\\filter_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(420, 300, 490, 360, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("filter title", imgs_)

                # filter
                for i in range(2):
                    boonhae_cheking(cla)
                    time.sleep(0.1)

                for i in range(5):
                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\soojib_boonhae\\filter_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(420, 300, 490, 360, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_2(480, 730, cla)
                    else:
                        soojib = True
                        break
                    time.sleep(0.5)

            else:
                click_pos_2(70, 1015, cla)

                for i in range(10):
                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\soojib_boonhae\\filter_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(420, 300, 490, 360, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        break
                    time.sleep(0.5)
            time.sleep(0.3)





    except Exception as e:
        print(e)

def soojib_join(cla, data):
    import numpy as np
    import cv2

    from function_moon import imgs_set_, click_pos_reg, click_pos_2

    try:
        print("soojib join", data)

        soojib = False
        soojib_count = 0
        while soojib is False:
            soojib_count += 1
            if soojib_count > 10:
                soojib = True

            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\soojib_boonhae\\soojib_click_point.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(170, 120, 660, 990, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("soojib point click", imgs_)
                click_pos_reg(imgs_.x + 10, imgs_.y + 5, cla)
                time.sleep(0.3)


                for i in range(10):

                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\soojib_boonhae\\join_click.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(300, 900, 960, 1000, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("join click", imgs_)
                        click_pos_reg(imgs_.x + 5, imgs_.y + 5, cla)
                        time.sleep(0.3)
                        if data == "event":
                            for i in range(10):
                                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\soojib_boonhae\\soojib_confirm.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(490, 610, 600, 700, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    break
                                time.sleep(0.3)
                            for i in range(10):
                                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\soojib_boonhae\\soojib_confirm.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(490, 610, 600, 700, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print("join soojib_confirm", imgs_)
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    time.sleep(0.3)
                                else:
                                    break
                                time.sleep(0.3)



                    complete = False

                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\soojib_boonhae\\soojib_complete1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(140, 240, 700, 700, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("soojib_complete1 click", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.3)
                        complete = True
                    else:
                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\soojib_boonhae\\soojib_complete2.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(140, 240, 700, 700, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("soojib_complete2 click", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.3)
                            complete = True
                    if complete == True:
                        for k in range(10):
                            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\soojib_boonhae\\soojib_click_point.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(170, 120, 660, 990, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                break
                            time.sleep(0.1)

                    time.sleep(0.2)
            else:
                soojib = True



    except Exception as e:
        print(e)



def boonhae_cheking(cla):
    import numpy as np
    import cv2

    from function_moon import imgs_set_, click_pos_reg
    try:
        # 상태
        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\soojib_boonhae\\filter_checked_off.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(140, 370, 200, 420, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            click_pos_reg(imgs_.x, imgs_.y, cla)
            time.sleep(0.1)

        # 등급
        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\soojib_boonhae\\filter_checked_off.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(270, 420, 330, 480, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            click_pos_reg(imgs_.x, imgs_.y, cla)
            time.sleep(0.1)

        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\soojib_boonhae\\filter_checked_off.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(390, 420, 460, 480, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            click_pos_reg(imgs_.x, imgs_.y, cla)
            time.sleep(0.1)

        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\soojib_boonhae\\filter_checked_off.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(510, 420, 570, 480, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            click_pos_reg(imgs_.x, imgs_.y, cla)
            time.sleep(0.1)

        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\soojib_boonhae\\filter_checked_on.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(630, 420, 690, 480, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            click_pos_reg(imgs_.x, imgs_.y, cla)
            time.sleep(0.1)

        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\soojib_boonhae\\filter_checked_on.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(750, 420, 810, 480, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            click_pos_reg(imgs_.x, imgs_.y, cla)
            time.sleep(0.1)

        # 강화
        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\soojib_boonhae\\filter_checked_off.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(150, 475, 210, 525, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            click_pos_reg(imgs_.x, imgs_.y, cla)
            time.sleep(0.1)

        # 옵션
        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\soojib_boonhae\\filter_checked_off.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(150, 610, 210, 670, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            click_pos_reg(imgs_.x, imgs_.y, cla)
            time.sleep(0.1)
    except Exception as e:
        print(e)

def boonhae_start(cla):
    import numpy as np
    import cv2

    from function_moon import imgs_set_, click_pos_reg, click_pos_2
    from action_moon import menu_open, clean_screen
    try:
        print("boonhae_start")

        boonhae = False
        boonhae_count = 0
        while boonhae is False:
            boonhae_count += 1
            if boonhae_count > 7:
                boonhae = True
            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\repair\\boonhae_click.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(750, 920, 840, 970, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                x_reg = imgs_.x
                y_reg = imgs_.y
                for i in range(10):
                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\title\\jangbi_gaejo_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(10, 10, 150, 80, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        break
                    else:
                        click_pos_reg(x_reg, y_reg, cla)
                    time.sleep(0.5)
                for i in range(2):
                    # 수집록 장비
                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\soojib_boonhae\\boonhae_checked_off_soojib.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(815, 940, 890, 985, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.1)

                    # 일반
                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\soojib_boonhae\\boonhae_checked_off_common.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(645, 970, 690, 1040, cla, img, 0.95)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.1)

                    # # 고급
                    # full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\soojib_boonhae\\boonhae_checked_off_gogb.PNG"
                    # img_array = np.fromfile(full_path, np.uint8)
                    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    # imgs_ = imgs_set_(700, 970, 760, 1040, cla, img, 0.95)
                    # if imgs_ is not None and imgs_ != False:
                    #     click_pos_reg(imgs_.x, imgs_.y, cla)
                    #     time.sleep(0.1)

                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\soojib_boonhae\\boonhae_click.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(260, 960, 360, 1030, cla, img, 0.95)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.1)

                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\soojib_boonhae\\boonhae_result.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(410, 50, 550, 120, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.1)

                for i in range(2):
                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\soojib_boonhae\\boonhae_result.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(410, 50, 550, 120, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.2)

                for i in range(5):
                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\title\\jangbi_gaejo_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(10, 10, 150, 80, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        clean_screen(cla)
                    else:
                        boonhae = True
                        break
                    time.sleep(0.5)

            else:
                menu_open(cla)
                click_pos_2(870, 65, cla)

                for i in range(10):
                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\repair\\boonhae_click.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(750, 920, 840, 970, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        break
                    time.sleep(0.5)

            time.sleep(0.3)





    except Exception as e:
        print(e)