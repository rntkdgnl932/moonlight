import sys
import os
import time
import requests

sys.path.append('C:/my_games/moonlight/data_moon/mymodule')

import variable as v_

def chango_start(cla, data):

    try:
        print("chango_start")

    except Exception as e:
        print(e)

def chango_(cla, data):

    try:
        print("chango_start")

    except Exception as e:
        print(e)


def chango_action(cla, data):
    import numpy as np
    import cv2
    import pyautogui
    import random

    from function_moon import imgs_set_, click_pos_reg, click_pos_2

    from action_moon import let_is_maul_in, bag_open
    from get_item import get_items
    from potion_moon import maul_potion_dead_only
    from schedule import myQuest_play_add
    from repair_moon import repair_start

    try:

        print("chango_in")

        # 던전 등 빠져나와 마을로 오기
        let_is_maul_in(cla)

        # 장비 넣기전 빼기
        if data == "jangbi_in":
            for i in range(3):
                take_off(cla)
                time.sleep(0.1)

        # 마을에 도착하면 창고로 가기

        chango_arrive = False
        chango_arrive_count = 0
        while chango_arrive is False:
            chango_arrive_count += 1
            if chango_arrive_count > 7:
                chango_arrive = True
            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\title\\gongyong_chango_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 30, 100, 100, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                chango_arrive = True
                time.sleep(0.1)
                if data == "jaelyo_in":
                    # 창고에 재료 넣기 시작
                    chango_jaelyo_in_start(cla)
                elif data == "jaelyo_out":
                    # 창고에서 재료 빼기 시작
                    chango_jaelyo_out_start(cla)
                elif data == "jangbi_in":

                    # 창고에 재료 넣기 시작
                    chango_jaelyo_in_start(cla)
                    # 창고에 장비 넣기 시작
                    for i in range(3):
                        chango_jangbi_in_start(cla)
                        time.sleep(0.1)

                elif data == "jangbi_out":
                    # 창고에서 장비 빼기 시작
                    for i in range(3):
                        chango_jangbi_out_start(cla)
                        time.sleep(0.1)


                # 나가기
                for i in range(5):
                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\title\\gongyong_chango_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 30, 100, 100, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_2(935, 55, cla)
                    else:
                        break
                    time.sleep(0.5)

                if data == "jangbi_out":
                    # 장비 착용하기
                    bag_open(cla)

                    click_pos_2(680, 940, cla)

                    for i in range(10):
                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\repair\\boonhae_click.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(750, 920, 840, 970, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_2(935, 55, cla)
                        else:
                            break

                        time.sleep(0.5)
            else:
                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\maul\\chango.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(800, 970, 960, 1040, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    for i in range(10):
                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\title\\gongyong_chango_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(0, 30, 100, 100, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            break
                        time.sleep(1)
                time.sleep(0.1)





    except Exception as e:
        print(e)

def chango_jaelyo_in_start(cla):
    import numpy as np
    import cv2
    import pyautogui

    from function_moon import imgs_set_, click_pos_reg, click_pos_2

    try:

        print("chango_jaelyo_in_start")

        let_chango_in = False
        let_chango_in_count = 0
        while let_chango_in is False:
            let_chango_in_count += 1
            if let_chango_in_count > 7:
                let_chango_in = True

            # 각종 재료 넣기

            # 창고에 오른쪽 재료창 클릭
            click_pos_2(765, 100, cla)
            time.sleep(0.1)
            click_pos_2(765, 100, cla)
            time.sleep(0.5)

            # 먼저 필터창 열어서 정리해주기
            for i in range(10):
                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\chango\\filter_title.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(350, 30, 410, 80, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    dajoong_click(cla, "jaelyo")
                    break
                else:
                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\chango\\dajoong_select_right.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(660, 910, 770, 980, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                time.sleep(0.5)

            # 한번 더 필터 확인해주고 창고에 일괄 넣기
            dajoong_click(cla, "jaelyo")
            time.sleep(0.1)



            # 나머지 찾아서 창고에 넣기

            file_path = "C:\\my_games\\moonlight\\data_moon\\imgs\\chango\\jaelyo_in_list.txt"
            with open(file_path, "r", encoding='utf-8-sig') as file:
                read_list = file.read().splitlines()

            for i in range(len(read_list)):
                # 물품 찾아서 창고에 넣기

                if cla == "one":
                    plus = 0
                elif cla == "two":
                    plus = 960
                elif cla == "three":
                    plus = 960 * 2
                elif cla == "four":
                    plus = 960 * 3

                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\chango\\jaelyo_in\\" + read_list[i] + ".PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                for c in pyautogui.locateAllOnScreen(img, region=(625 + plus, 115, 960 - 625, 900 - 115), confidence=0.95):
                    last_x = c.left
                    last_y = c.top
                    click_pos_reg(last_x, last_y, cla)
                    time.sleep(0.1)
                    print("last_x", last_x)
                    print("last_y", last_y)

            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\chango\\bogwanhagi_right.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(820, 920, 910, 970, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                click_pos_reg(imgs_.x, imgs_.y, cla)
                time.sleep(0.1)
                click_pos_reg(imgs_.x, imgs_.y, cla)
                time.sleep(0.4)
                let_chango_in = True
        # # 나가기
        # for i in range(5):
        #     full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\title\\gongyong_chango_title.PNG"
        #     img_array = np.fromfile(full_path, np.uint8)
        #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #     imgs_ = imgs_set_(0, 30, 100, 100, cla, img, 0.8)
        #     if imgs_ is not None and imgs_ != False:
        #         click_pos_2(935, 55, cla)
        #     else:
        #         break
        #     time.sleep(0.5)



    except Exception as e:
       print(e)


def chango_jangbi_in_start(cla):
    import numpy as np
    import cv2
    import pyautogui

    from function_moon import imgs_set_, click_pos_reg, click_pos_2

    try:

        print("chango_jangbi_in_start")

        let_chango_in = False
        let_chango_in_count = 0
        while let_chango_in is False:
            let_chango_in_count += 1
            if let_chango_in_count > 7:
                let_chango_in = True

            # 각종 재료 넣기

            # 창고에 오른쪽 장비창 클릭
            click_pos_2(710, 100, cla)
            time.sleep(0.1)
            click_pos_2(710, 100, cla)
            time.sleep(0.5)

            # 먼저 다중선택창 열기
            for i in range(10):
                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\chango\\filter_title.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(350, 30, 410, 80, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    dajoong_click(cla, "jangbi")
                    break
                else:
                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\chango\\dajoong_select_right.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(660, 910, 770, 980, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                time.sleep(0.5)

            # 한번 더 필터 확인해주고 창고에 일괄 넣기
            dajoong_click(cla, "jangbi")
            time.sleep(0.1)



            # 나머지 찾아서 창고에 넣기

            file_path = "C:\\my_games\\moonlight\\data_moon\\imgs\\chango\\jangbi_in_list.txt"
            with open(file_path, "r", encoding='utf-8-sig') as file:
                read_list = file.read().splitlines()


            for i in range(len(read_list)):
                # 물품 찾아서 창고에 넣기
                exist = False

                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\chango\\jangbi_in\\" + read_list[i] + ".PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(625, 115, 960, 900, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    exist = True
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.2)
            if exist == True:
                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\chango\\bogwanhagi_right.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(820, 920, 910, 970, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.1)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.4)
            let_chango_in = True
        # # 나가기
        # for i in range(5):
        #     full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\title\\gongyong_chango_title.PNG"
        #     img_array = np.fromfile(full_path, np.uint8)
        #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #     imgs_ = imgs_set_(0, 30, 100, 100, cla, img, 0.8)
        #     if imgs_ is not None and imgs_ != False:
        #         click_pos_2(935, 55, cla)
        #     else:
        #         break
        #     time.sleep(0.5)



    except Exception as e:
       print(e)

def take_off(cla):
    import numpy as np
    import cv2
    import pyautogui

    from function_moon import imgs_set_, click_pos_reg, click_pos_2
    from action_moon import bag_open

    try:
        print("take off")

        if cla == "one":
            plus = 0
        elif cla == "two":
            plus = 960
        elif cla == "three":
            plus = 960 * 2
        elif cla == "four":
            plus = 960 * 3

        bag_open(cla)

        click_pos_2(710, 100, cla)
        time.sleep(0.1)
        click_pos_2(710, 100, cla)
        time.sleep(0.5)

        file_path = "C:\\my_games\\moonlight\\data_moon\\imgs\\chango\\take_off_list.txt"
        with open(file_path, "r", encoding='utf-8-sig') as file:
            read_list = file.read().splitlines()
        exist = False

        for i in range(len(read_list)):
            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\chango\\take_off\\" + read_list[i] + ".PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(625, 115, 960, 900, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("list : ", read_list[i])
                x_reg = imgs_.x - plus
                y_reg = imgs_.y

                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\chango\\e.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(x_reg - 20, y_reg - 75, x_reg + 75, y_reg + 30, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    click_pos_2(x_reg, y_reg, cla)
                    time.sleep(0.1)
                    exist = True

                    for t in range(10):
                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\chango\\jangbi_x.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(570, 270, 630, 330, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            break
                        time.sleep(0.3)
            if exist == True:
                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\chango\\take_off_click.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(540, 740, 600, 800, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                else:
                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\chango\\jangbi_x.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(570, 270, 630, 330, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                time.sleep(0.3)
            else:
                time.sleep(0.1)
        for i in range(10):
            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\chango\\take_off_click.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(540, 740, 600, 800, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                click_pos_reg(imgs_.x, imgs_.y, cla)
            else:
                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\repair\\boonhae_click.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(750, 920, 840, 970, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    click_pos_2(935, 55, cla)
                else:
                    break
            time.sleep(0.5)


    except Exception as e:
        print(e)

def chango_jaelyo_out_start(cla):
    import numpy as np
    import cv2
    import pyautogui

    from function_moon import imgs_set_, click_pos_reg, click_pos_2, mouse_move_cpp

    try:

        print("chango_jaelyo_out_start")

        let_chango_out = False
        let_chango_out_count = 0
        while let_chango_out is False:
            let_chango_out_count += 1
            if let_chango_out_count > 7:
                let_chango_out = True

            # 각종 재료 넣기

            # 창고에 왼쪽 다중 선택 클릭

            # 먼저 왼쪽 다중 선택창 누르기
            for i in range(10):
                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\chango\\select_cancle_left.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 970, 120, 1030, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    break
                else:
                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\chango\\dajoong_select_left.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 970, 120, 1030, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.1)
                        mouse_move_cpp(500, 500, cla)
                        time.sleep(0.1)
                time.sleep(0.5)



            # 나머지 찾아서 창고에 넣기

            file_path = "C:\\my_games\\moonlight\\data_moon\\imgs\\chango\\jaelyo_out_list.txt"
            with open(file_path, "r", encoding='utf-8-sig') as file:
                read_list = file.read().splitlines()

            for i in range(len(read_list)):
                # 물품 창고에서 빼오기

                if cla == "one":
                    plus = 0
                elif cla == "two":
                    plus = 960
                elif cla == "three":
                    plus = 960 * 2
                elif cla == "four":
                    plus = 960 * 3

                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\chango\\jaelyo_out\\" + read_list[i] + ".PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                for c in pyautogui.locateAllOnScreen(img, region=(0 + plus, 115, 330, 900 - 115), confidence=0.95):
                    last_x = c.left
                    last_y = c.top
                    click_pos_reg(last_x, last_y, cla)
                    time.sleep(0.1)
                    print("last_x", last_x)
                    print("last_y", last_y)

            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\chango\\get_in_click.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(110, 970, 220, 1020, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                click_pos_reg(imgs_.x, imgs_.y, cla)
                time.sleep(0.1)
                click_pos_reg(imgs_.x, imgs_.y, cla)
                time.sleep(0.4)
                let_chango_out = True
        # # 나가기
        # for i in range(5):
        #     full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\title\\gongyong_chango_title.PNG"
        #     img_array = np.fromfile(full_path, np.uint8)
        #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #     imgs_ = imgs_set_(0, 30, 100, 100, cla, img, 0.8)
        #     if imgs_ is not None and imgs_ != False:
        #         click_pos_2(935, 55, cla)
        #     else:
        #         break
        #     time.sleep(0.5)



    except Exception as e:
       print(e)


def chango_jangbi_out_start(cla):
    import numpy as np
    import cv2
    import pyautogui

    from function_moon import imgs_set_, click_pos_reg, click_pos_2, mouse_move_cpp
    from action_moon import bag_open

    try:

        print("chango_jangbi_out_start")

        let_chango_out = False
        let_chango_out_count = 0
        while let_chango_out is False:
            let_chango_out_count += 1
            if let_chango_out_count > 7:
                let_chango_out = True

            # 각종 재료 및 장비 넣기

            # 창고에 왼쪽 다중 선택 클릭

            # 먼저 왼쪽 다중 선택창 누르기
            for i in range(10):
                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\chango\\select_cancle_left.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 970, 120, 1030, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    break
                else:
                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\chango\\dajoong_select_left.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 970, 120, 1030, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.1)
                        mouse_move_cpp(500, 500, cla)
                        time.sleep(0.1)
                time.sleep(0.5)



            # 찾아서 창고ㅔ서 빼기

            file_path = "C:\\my_games\\moonlight\\data_moon\\imgs\\chango\\jangbi_out_list.txt"
            with open(file_path, "r", encoding='utf-8-sig') as file:
                read_list = file.read().splitlines()
            exist = False
            for i in range(len(read_list)):
                print('out list', read_list[i])
                # 물품 창고에서 빼오기

                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\chango\\jangbi_out\\" + read_list[i] + ".PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 115, 330, 900, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.2)
                    exist = True
            if exist == True:
                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\chango\\get_in_click.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(110, 970, 220, 1020, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.1)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.4)
            let_chango_out = True
        # # 나가기
        # for i in range(5):
        #     full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\title\\gongyong_chango_title.PNG"
        #     img_array = np.fromfile(full_path, np.uint8)
        #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #     imgs_ = imgs_set_(0, 30, 100, 100, cla, img, 0.8)
        #     if imgs_ is not None and imgs_ != False:
        #         click_pos_2(935, 55, cla)
        #     else:
        #         break
        #     time.sleep(0.5)
        #
        # # 장비 착용하기
        # bag_open(cla)
        #
        # click_pos_2(680, 940, cla)
        #
        # for i in range(10):
        #     full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\repair\\boonhae_click.PNG"
        #     img_array = np.fromfile(full_path, np.uint8)
        #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #     imgs_ = imgs_set_(750, 920, 840, 970, cla, img, 0.8)
        #     if imgs_ is not None and imgs_ != False:
        #         click_pos_2(935, 55, cla)
        #     else:
        #         break
        #
        #     time.sleep(0.5)


    except Exception as e:
       print(e)

def dajoong_click(cla, data):
    import cv2
    import numpy as np
    from function_moon import imgs_set_, click_pos_reg
    try:
        # 1
        if data == "jaelyo":
            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\chango\\checked_on.PNG"
        elif data == "jangbi":
            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\chango\\checked_off.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(350, 100, 405, 165, cla, img, 0.9)
        if imgs_ is not None and imgs_ != False:
            if data == "jaelyo":
                print("checked_on", imgs_)
            elif data == "jangbi":
                print("checked_off", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
            time.sleep(0.2)
        # 2
        if data == "jaelyo":
            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\chango\\checked_on.PNG"
        elif data == "jangbi":
            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\chango\\checked_off.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(480, 100, 530, 165, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            if data == "jaelyo":
                print("checked_on", imgs_)
            elif data == "jangbi":
                print("checked_off", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
            time.sleep(0.2)
        # 3
        if data == "jaelyo":
            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\chango\\checked_on.PNG"
        elif data == "jangbi":
            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\chango\\checked_off.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(360, 160, 405, 210, cla, img, 0.88)
        if imgs_ is not None and imgs_ != False:
            if data == "jaelyo":
                print("checked_on", imgs_)
            elif data == "jangbi":
                print("checked_off", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
            time.sleep(0.2)
        # 4
        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\chango\\checked_on.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(480, 155, 530, 210, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("checked_on", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
            time.sleep(0.2)
        # 5
        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\chango\\checked_off.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(350, 200, 405, 255, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("checked_off", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
            time.sleep(0.2)
        # 6
        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\chango\\checked_on.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(480, 200, 530, 255, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("checked_on", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
            time.sleep(0.2)

        # 7
        if data == "jaelyo":
            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\chango\\checked_off.PNG"
        elif data == "jangbi":
            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\chango\\checked_on.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(350, 290, 405, 350, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            if data == "jaelyo":
                print("checked_off", imgs_)
            elif data == "jangbi":
                print("checked_on", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
            time.sleep(0.2)
        # 8
        if data == "jaelyo":
            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\chango\\checked_off.PNG"
        elif data == "jangbi":
            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\chango\\checked_on.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(480, 290, 530, 350, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            if data == "jaelyo":
                print("checked_on", imgs_)
            elif data == "jangbi":
                print("checked_off", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
            time.sleep(0.2)
        # 9
        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\chango\\checked_off.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(350, 340, 405, 390, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("checked_off", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
            time.sleep(0.2)
        # 10
        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\chango\\checked_off.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(480, 340, 530, 390, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("checked_off", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
            time.sleep(0.2)
        # 11
        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\chango\\checked_on.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(350, 380, 405, 440, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("checked_on", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
            time.sleep(0.2)
        # 12
        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\chango\\checked_on.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(480, 380, 530, 440, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("checked_on", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
            time.sleep(0.2)
    except Exception as e:
        print(e)