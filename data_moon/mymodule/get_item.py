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

def get_items_sub(cla):
    try:
        print("get_items")
        get_post(cla)
        get_event_sub(cla)
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
    import pyautogui

    from function_moon import imgs_set_, click_pos_reg, click_pos_2, drag_pos, mouse_move_cpp

    from action_moon import clean_screen
    try:
        print("get_event")

        if cla == "one":
            plus = 0
        elif cla == "two":
            plus = 960
        elif cla == "three":
            plus = 960 * 2
        elif cla == "four":
            plus = 960 * 3

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
                        # click_pos_reg(imgs_.x + 20, imgs_.y + 20, cla)
                        click_pos_reg(imgs_.x + 20, imgs_.y, cla)
                    time.sleep(0.2)


                # 타이틀에 포인트 클릭하기
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
                        # 일시적인 이벤트?
                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\temporary_event\\rullet_go.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(670, 630, 760, 680, cla, img, 0.83)
                        if imgs_ is not None and imgs_ != False:
                            print("rullet_go", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            break


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
                            imgs_ = imgs_set_(650, 450, 900, 770, cla, img, 0.9)
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
                                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\get_items\\daily_attend\\daily_attend_title.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(490, 355, 700, 430, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        print("daily_attend_title...", imgs_)
                                        break


                                    # full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\get_items\\chulsuk_checked.PNG"
                                    # img_array = np.fromfile(full_path, np.uint8)
                                    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    # imgs_ = imgs_set_(310, 440, 790, 720, cla, img, 0.8)
                                    # if imgs_ is not None and imgs_ != False:
                                    #     print("chulsuk_checked...", imgs_)
                                    #     break


                        time.sleep(0.1)
                    ############
                    # 한가위 수집 이벤트 관련 패스하기
                    ##########
                    gyohwan = False

                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\get_items\\ex\\gyohwan1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(220, 670, 890, 750, cla, img, 0.95)
                    if imgs_ is not None and imgs_ != False:
                        print("gyohwan1", imgs_)
                        gyohwan = True
                    else:
                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\get_items\\ex\\gyohwan2.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(220, 670, 890, 750, cla, img, 0.95)
                        if imgs_ is not None and imgs_ != False:
                            print("gyohwan2", imgs_)
                            gyohwan = True

                    if gyohwan == True:
                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\get_items\\ex\\season_event.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(50, 330, 210, 760, cla, img, 0.95)
                        if imgs_ is not None and imgs_ != False:

                            for i in range(10):
                                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\get_items\\event_y.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(150, 330, 220, 770, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    print("닫는 중")
                                else:
                                    break
                                time.sleep(0.5)

                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\get_items\\ex\\grow_guide.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(50, 330, 210, 760, cla, img, 0.95)
                        if imgs_ is not None and imgs_ != False:
                            for i in range(10):
                                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\get_items\\event_y.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(150, 330, 220, 770, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    break
                                else:
                                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\get_items\\ex\\grow_guide.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(50, 330, 210, 760, cla, img, 0.95)
                                    if imgs_ is not None and imgs_ != False:
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(0.5)
                    else:
                        #######
                        # 드래그 필요한 경우
                        #######

                        drag = False

                        # 시즌 이벤트에 한가위 이벤트
                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\get_items\\drag\\hangawe_drag.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(210, 350, 550, 420, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            drag = True

                        # 시즌 이벤트에 대륙 정화 미션 이벤트
                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\get_items\\drag\\junghwa_mission.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(210, 350, 550, 420, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            drag = True

                        # 시즌패스에 패스미션
                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\get_items\\drag\\pass_mission_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(400, 350, 580, 420, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            drag = True

                        if drag is True:

                            drag_count = 0
                            while drag is True:
                                drag_count += 1
                                if drag_count > 18:
                                    drag = False
                                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\get_items\\bosang_get_3.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(650, 450, 900, 770, cla, img, 0.9)
                                if imgs_ is not None and imgs_ != False:
                                    print("bosang_get_3", imgs_)
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                else:
                                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\get_items\\get_point_3.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(50, y_reg, 80, 770, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        print("get_point_3", imgs_)
                                        click_pos_reg(imgs_.x, imgs_.y, cla)

                                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\get_items\\drag\\pass_mission_title.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(400, 350, 580, 420, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:

                                            if drag_count < 11:
                                                mouse_move_cpp(600, 660, cla)
                                                pyautogui.dragTo(600 + plus, 500, 0.5)
                                                time.sleep(0.2)
                                            else:
                                                mouse_move_cpp(600, 500, cla)
                                                pyautogui.dragTo(600 + plus, 660, 0.5)
                                                time.sleep(0.2)
                                        else:
                                            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\get_items\\drag\\junghwa_mission.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(210, 350, 550, 420, cla, img, 0.8)
                                            if imgs_ is not None and imgs_ != False:

                                                if drag_count < 11:
                                                    mouse_move_cpp(600, 660, cla)
                                                    pyautogui.dragTo(600 + plus, 500, 0.5)
                                                    time.sleep(0.2)
                                                else:
                                                    mouse_move_cpp(600, 500, cla)
                                                    pyautogui.dragTo(600 + plus, 660, 0.5)
                                                    time.sleep(0.2)
                                            else:
                                                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\get_items\\drag\\hangawe_drag.PNG"
                                                img_array = np.fromfile(full_path, np.uint8)
                                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                imgs_ = imgs_set_(210, 350, 550, 420, cla, img, 0.8)
                                                if imgs_ is not None and imgs_ != False:

                                                    if drag_count < 11:
                                                        mouse_move_cpp(600, 660, cla)
                                                        pyautogui.dragTo(600 + plus, 500, 0.5)
                                                        time.sleep(0.2)
                                                    else:
                                                        mouse_move_cpp(600, 500, cla)
                                                        pyautogui.dragTo(600 + plus, 660, 0.5)
                                                        time.sleep(0.2)
                                                else:
                                                    drag = False
                                    else:
                                        drag = False
                                time.sleep(0.5)
                        else:
                            # 첫번째 seven_four

                            seven_four = False

                            # 시즌이벤트에 데일리 7일 미션
                            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\get_items\\seven_four\\daily_seven_mission.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(220, 350, 630, 420, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("daily_seven_mission", imgs_)
                                seven_four = True

                            if seven_four == True:
                                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\get_items\\get_point_2.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(220, 450, 880, 510, cla, img, 0.8)
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
                                # 접속보상에 매일출석 이벤트(28일짜리)
                                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\get_items\\daily_attend\\daily_attend_title.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(490, 355, 700, 430, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print("daily_attend_title...", imgs_)

                                    last_x = 0
                                    last_y = 0

                                    if cla == "one":
                                        plus = 0
                                    if cla == "two":
                                        plus = 960
                                    if cla == "three":
                                        plus = 960 * 2
                                    if cla == "four":
                                        plus = 960 * 3

                                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\get_items\\chulsuk_checked.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    for i in pyautogui.locateAllOnScreen(img, region=(310 + plus, 440, 480, 280),
                                                                         confidence=0.8):
                                        last_x = i.left
                                        last_y = i.top
                                        print("last_x", last_x)
                                        print("last_y", last_y)

                                    if last_x == 0:
                                        click_pos_2(355, 480, cla)
                                    elif last_x > 720 + plus:
                                        if last_y < 515:
                                            click_pos_2(355, 550, cla)
                                        elif last_y < 580:
                                            click_pos_2(355, 550, cla)
                                        elif last_y < 650:
                                            click_pos_2(355, 550, cla)
                                        else:
                                            print("다 받았다.")
                                    else:
                                        click_pos_reg(last_x + 67, last_y, cla)
                                    time.sleep(0.2)

                                else:
                                    # seven

                                    seven = False

                                    # 접속보상에 이브의 특별 출석
                                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\get_items\\seven\\eve_special_chulsuk.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(210, 350, 660, 420, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        print("eve_special_chulsuk", imgs_)
                                        seven = True
                                    # 접속보상에 한가위 특별 출석
                                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\get_items\\seven\\hangawe_special_chulsuk.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(210, 350, 660, 420, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        print("hangawe_special_chulsuk", imgs_)
                                        seven = True

                                    if seven == True:
                                        last_x = 0
                                        last_y = 0

                                        if cla == "one":
                                            plus = 0
                                        if cla == "two":
                                            plus = 960
                                        if cla == "three":
                                            plus = 960 * 2
                                        if cla == "four":
                                            plus = 960 * 3

                                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\get_items\\chulsuk_checked.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        for i in pyautogui.locateAllOnScreen(img,
                                                                             region=(
                                                                                     245 + plus, 690, 780 - 245,
                                                                                     735 - 690),
                                                                             confidence=0.8):
                                            last_x = i.left
                                            last_y = i.top
                                            print("last_x", last_x)
                                            print("last_y", last_y)

                                        if last_x == 0:
                                            click_pos_2(270, 710, cla)
                                        elif last_x > 800 + plus:
                                            print("다 받음")
                                        else:
                                            click_pos_reg(last_x + 100, last_y, cla)
                                        time.sleep(0.2)

                                    else:
                                        # ten

                                        ten = False

                                        # 접속보상에 뉴월드 특별 출석
                                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\get_items\\ten\\newworld_special_chulsuk.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(210, 350, 620, 420, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            print("newworld_special_chulsuk...1", imgs_)
                                            ten = True

                                        # 접속보상에 뉴월드 특별 출석2
                                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\get_items\\ten\\newworld_special_chulsuk2.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(210, 350, 620, 420, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            print("newworld_special_chulsuk...2", imgs_)
                                            ten = True

                                        if ten == True:

                                            last_x = 0
                                            last_y = 0

                                            if cla == "one":
                                                plus = 0
                                            if cla == "two":
                                                plus = 960
                                            if cla == "three":
                                                plus = 960 * 2
                                            if cla == "four":
                                                plus = 960 * 3

                                            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\get_items\\chulsuk_checked.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            for i in pyautogui.locateAllOnScreen(img,
                                                                                 region=(235 + plus, 570, 680 - 235,
                                                                                         740 - 570),
                                                                                 confidence=0.8):
                                                last_x = i.left
                                                last_y = i.top
                                                print("last_x", last_x)
                                                print("last_y", last_y)

                                            if last_x == 0:
                                                click_pos_2(270, 710, cla)
                                            elif last_y > 640 and last_x > 600 + plus:
                                                    print("다 받음")

                                            elif last_y < 640 and last_x > 600 + plus:
                                                    click_pos_2(270, 710, cla)
                                            else:
                                                click_pos_reg(last_x + 100, last_y, cla)
                                            time.sleep(0.2)

                    # 마무리
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

        clean_screen(cla)

    except Exception as e:
        print(e)

def get_event_sub(cla):
    import numpy as np
    import cv2
    import pyautogui

    from function_moon import imgs_set_, click_pos_reg, click_pos_2, drag_pos, mouse_move_cpp

    from action_moon import clean_screen
    try:
        print("get_event_sub")

        if cla == "one":
            plus = 0
        elif cla == "two":
            plus = 960
        elif cla == "three":
            plus = 960 * 2
        elif cla == "four":
            plus = 960 * 3

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

                # 성장 가이드에 듀발의 성장계획 첫번째

                guide = False

                for i in range(10):
                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\get_items\\grow_plan_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(50, 340, 210, 770, cla, img, 0.83)
                    if imgs_ is not None and imgs_ != False:
                        print("grow_plan_1", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        guide = True
                        break
                    else:

                        drag_pos(130, 700, 130, 400, cla)

                        time.sleep(0.1)

                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\get_items\\grow_guide_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(50, 340, 210, 770, cla, img, 0.83)
                        if imgs_ is not None and imgs_ != False:
                            print("grow_guide_title", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.5)

                if guide == True:
                    for i in range(10):
                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\get_items\\bosang_get_2.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(650, 450, 900, 770, cla, img, 0.83)
                        if imgs_ is not None and imgs_ != False:
                            print("bosang_get_2", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)



                            # 마무리
                            for k in range(10):
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
                            get = True
                            break
                        time.sleep(0.5)

                    # 아이템 먹고 마무리 안되었을 경우...
                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\get_items\\get_item_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(390, 440, 480, 490, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("get_item_1")
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                else:
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

        clean_screen(cla)

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
                    time.sleep(0.2)

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
                        get = True
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