import sys
import os
import time
import requests

sys.path.append('C:/my_games/moonlight/data_moon/mymodule')

import variable as v_

def get_items(cla):
    try:
        print("get_items")
        get_post(cla)
        get_event(cla)
        get_upjuk(cla)
        get_moster_dalsung(cla)

    except Exception as e:
        print(e)

def get_post(cla):
    import numpy as np
    import cv2

    from function_moon import imgs_set_, click_pos_reg, click_pos_2

    from action_moon import clean_screen
    try:
        print("get_items")
        get = False
        get_count = 0
        while get is False:
            get_count += 1
            if get_count > 7:
                get = True
            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\title\\post_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(5, 30, 100, 100, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("post")


                for i in range(4):
                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\get_items\\bosang_get_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(400, 300, 530, 500, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("bosang_get_1")
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        break
                    else:
                        click_pos_2(110, 100, cla)
                        time.sleep(0.1)
                        click_pos_2(870, 1015, cla)
                        time.sleep(0.1)

                for i in range(4):
                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\get_items\\bosang_get_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(400, 300, 530, 500, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("bosang_get_1")
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        break
                    else:
                        click_pos_2(240, 100, cla)
                        time.sleep(0.1)
                        click_pos_2(870, 1015, cla)
                        time.sleep(0.1)

                for i in range(10):
                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\title\\post_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(5, 30, 100, 100, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:

                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\get_items\\bosang_get_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(400, 300, 530, 500, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("bosang_get_1")
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                        else:
                            clean_screen(cla)
                    else:
                        get = True
                        break


            else:
                clean_screen(cla)
                time.sleep(0.1)
                click_pos_2(705, 65, cla)
                for i in range(10):
                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\title\\post_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(5, 30, 100, 100, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        break
                    time.sleep(0.5)

    except Exception as e:
        print(e)

def get_event(cla):
    import numpy as np
    import cv2

    from function_moon import imgs_set_, click_pos_reg, click_pos_2

    from action_moon import clean_screen
    try:
        print("get_event")
        get = False
        get_count = 0

        not_point_count = 0

        while get is False:
            get_count += 1
            if get_count > 20:
                get = True
            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\get_items\\event_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(400, 300, 545, 345, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("event_title")

                # 먼저 x 처리하기
                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\clean_screen\\x_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(560, 260, 630, 340, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("x_1")
                    click_pos_reg(imgs_.x, imgs_.y, cla)

                y_reg = 330

                for i in range(2):
                    # y 값 기준 정하기
                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\get_items\\event_y.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(150, 330, 220, 770, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("event_y")
                        y_reg = imgs_.y + 15

                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\get_items\\get_point_3.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(50, y_reg, 80, 770, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("get_point_3", imgs_)
                        click_pos_reg(imgs_.x + 20, imgs_.y + 20, cla)
                    time.sleep(0.2)



                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\get_items\\get_point_3.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(50, y_reg, 80, 770, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("get_point_3", imgs_)

                    not_point_count = 0

                    click_pos_reg(imgs_.x + 20, imgs_.y + 20, cla)
                    time.sleep(0.7)

                    for i in range(10):
                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\get_items\\bosang_get_2.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(650, 450, 900, 770, cla, img, 0.83)
                        if imgs_ is not None and imgs_ != False:
                            print("bosang_get_2", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            break
                        else:
                            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\get_items\\bosang_get_3.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(650, 450, 900, 770, cla, img, 0.83)
                            if imgs_ is not None and imgs_ != False:
                                print("bosang_get_3", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                break
                            else:
                                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\get_items\\get_point_2.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(220, 450, 835, 755, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print("get_point_2...", imgs_)
                                    break
                                else:
                                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\get_items\\chulsuk_checked.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(310, 440, 790, 720, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        print("chulsuk_checked...", imgs_)
                                        break


                        time.sleep(0.1)


                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\get_items\\get_point_2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(220, 450, 835, 755, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("get_point_2", imgs_)

                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\get_items\\seven_four.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(220, 450, 900, 520, cla, img, 0.97)
                        if imgs_ is not None and imgs_ != False:
                            print("seven_four", imgs_)
                            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\get_items\\get_point_2.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(220, 450, 835, 755, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("get_point_2", imgs_)
                                click_pos_reg(imgs_.x + 20, imgs_.y + 5, cla)

                                # 1
                                click_pos_2(520, 550, cla)
                                for i in range(10):
                                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\get_items\\get_item_1.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(390, 440, 480, 490, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        print("get_item_1")
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                        break
                                    else:
                                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\clean_screen\\x_1.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(560, 260, 630, 340, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            print("x_1")
                                            click_pos_reg(imgs_.x, imgs_.y, cla)
                                            break
                                    time.sleep(0.2)
                                # 2
                                click_pos_2(840, 550, cla)
                                for i in range(10):
                                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\get_items\\get_item_1.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(390, 440, 480, 490, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        print("get_item_1")
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                        break
                                    else:
                                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\clean_screen\\x_1.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(560, 260, 630, 340, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            print("x_1")
                                            click_pos_reg(imgs_.x, imgs_.y, cla)
                                            break
                                    time.sleep(0.2)
                                # 3
                                click_pos_2(520, 630, cla)
                                for i in range(10):
                                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\get_items\\get_item_1.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(390, 440, 480, 490, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        print("get_item_1")
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                        break
                                    else:
                                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\clean_screen\\x_1.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(560, 260, 630, 340, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            print("x_1")
                                            click_pos_reg(imgs_.x, imgs_.y, cla)
                                            break
                                    time.sleep(0.2)

                                # 4
                                click_pos_2(840, 630, cla)
                                for i in range(10):
                                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\get_items\\get_item_1.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(390, 440, 480, 490, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        print("get_item_1")
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                        break
                                    else:
                                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\clean_screen\\x_1.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(560, 260, 630, 340, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            print("x_1")
                                            click_pos_reg(imgs_.x, imgs_.y, cla)
                                            break
                                    time.sleep(0.2)



                        else:
                            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\get_items\\get_point_2.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(220, 450, 835, 755, cla, img, 0.9)
                            if imgs_ is not None and imgs_ != False:
                                print("get_point_2", imgs_)
                                click_pos_reg(imgs_.x + 20, imgs_.y + 50, cla)
                    else:
                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\get_items\\chulsuk_checked.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(310, 440, 790, 720, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("chulsuk_checked", imgs_)
                            click_pos_reg(imgs_.x + 67, imgs_.y, cla)

                    for i in range(10):
                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\get_items\\get_item_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(390, 440, 480, 490, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("get_item_1")
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            break
                        time.sleep(0.2)

                    # 아이템 먹고 마무리 안되었을 경우...
                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\get_items\\get_item_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(390, 440, 480, 490, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("get_item_1")
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                else:
                    not_point_count += 1

                    if not_point_count > 3:
                        get = True






            else:
                clean_screen(cla)
                time.sleep(0.1)
                click_pos_2(760, 65, cla)
                for i in range(10):
                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\get_items\\event_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(400, 300, 545, 345, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        break
                    time.sleep(0.5)

    except Exception as e:
        print(e)

def get_upjuk(cla):
    import numpy as np
    import cv2

    from function_moon import imgs_set_, click_pos_reg, click_pos_2

    from action_moon import clean_screen, menu_open
    try:
        print("get_upjuk")
        get = False
        get_count = 0
        while get is False:
            get_count += 1
            if get_count > 7:
                get = True
            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\title\\upjuk_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(5, 30, 100, 100, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("upjuk_title")

                click_pos_2(875, 1015, cla)

                for i in range(10):
                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\get_items\\upjuk_complete.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(400, 170, 550, 250, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        break
                    time.sleep(0.3)

                click_pos_2(875, 1015, cla)

                for i in range(10):
                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\title\\upjuk_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(5, 30, 100, 100, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\get_items\\upjuk_complete.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(400, 170, 550, 250, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                        else:
                            click_pos_2(935, 55, cla)
                    else:
                        break
                    time.sleep(0.4)


            else:
                clean_screen(cla)
                time.sleep(0.1)
                menu_open(cla)
                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\get_items\\menu_upjuk.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(670, 180, 960, 400, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    for i in range(10):
                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\title\\upjuk_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(5, 30, 100, 100, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            break
                        time.sleep(0.5)

    except Exception as e:
        print(e)

def get_moster_dalsung(cla):
    import numpy as np
    import cv2

    from function_moon import imgs_set_, click_pos_reg, click_pos_2

    from action_moon import clean_screen, menu_open
    try:
        print("get_moster_dalsung")
        click_pos_2(270, 70, cla)


    except Exception as e:
        print(e)