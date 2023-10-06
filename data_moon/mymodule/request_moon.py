import sys
import os
import time
import requests

sys.path.append('C:/my_games/moonlight/data_moon/mymodule')

import variable as v_

def request_start(cla, sche):
    import numpy as np
    import cv2
    import pyautogui
    import random

    from function_moon import imgs_set_, click_pos_reg, click_pos_2, drag_pos
    from tuto_moon import quest_check, quest_click

    from action_moon import loading, clean_screen
    from get_item import get_items
    from potion_moon import maul_potion_dead_only, potion_check
    from schedule import myQuest_play_add
    from repair_moon import repair_start


    try:

        print("request_start")

        quest_check(cla)

        request_ing = False

        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\request\\bosang_re2.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(430, 400, 510, 450, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            request_bosang_and_move(cla, sche)
        else:
            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\request\\execute_re2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(680, 90, 730, 280, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("execute_re2", imgs_)
                request_ing = True
            else:
                drag_pos(800, 260, 800, 130, cla)
                time.sleep(0.5)
                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\request\\execute_re2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(680, 90, 730, 280, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("execute_re22", imgs_)
                    request_ing = True
                else:
                    print("not execute_re2 => get_my_request")
                    get_my_request(cla, sche)

        if request_ing == True:
            request_bosang_and_move(cla, sche)
            potion_check(cla)






    except Exception as e:
        print(e)


def get_my_request(cla, sche):
    import numpy as np
    import cv2
    import pyautogui
    import random

    from function_moon import imgs_set_, click_pos_reg, click_pos_2

    from action_moon import loading, clean_screen, menu_open
    from get_item import get_items
    from potion_moon import maul_potion_dead_only
    from schedule import myQuest_play_add
    from repair_moon import repair_start
    from dungeon_moon import dungeon_ing_check

    try:

        # 던전일 경우 빠져나오기

        result_dun = dungeon_ing_check(cla, sche)

        if result_dun == True:
            clean_screen(cla)
            click_pos_2(925, 270, cla)
            for i in range(10):
                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\dungeon\\dun_out_confirm.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(510, 560, 580, 620, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    break
                time.sleep(0.5)

            loading(cla)
            clean_screen(cla)

        complete = False
        recieve = False

        # 스케쥴에서 던전 정보 뽑기
        result_dun = sche.split("_")
        # result_dun[0] => 외뢰
        # result_dun[1] => 세라보그, 바란, 국경지대, 유로키나산맥

        if result_dun[1] == "세라보그":
            x_reg = 105
        elif result_dun[1] == "바란":
            x_reg = 245
        elif result_dun[1] == "국경지대":
            x_reg = 385
        elif result_dun[1] == "유로키나산맥맥":
            x_reg = 525


        print("request_start")

        get_request = False
        get_request_count = 0
        while get_request is False:
            get_request_count += 1
            if get_request_count > 7:
                get_request = True

            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\title\\request_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 10, 160, 100, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("request_title...", imgs_)

                if recieve == False:

                    # 의뢰 지역 클릭
                    click_pos_2(x_reg, 100, cla)
                    time.sleep(0.1)
                    click_pos_2(x_reg, 100, cla)
                    time.sleep(0.5)

                    break_count = 0
                    fresh_count = 0

                    for r in range(15):
                        # 진행중인 의뢰 밑으로 클릭하도록 하기
                        y_point = 0

                        if cla == "one":
                            plus = 0
                        if cla == "two":
                            plus = 960
                        if cla == "three":
                            plus = 960 * 2
                        if cla == "four":
                            plus = 960 * 3

                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\request\\re_y_point.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        for i in pyautogui.locateAllOnScreen(img, region=(230 + plus, 130, 300 - 230, 800 - 130),
                                                             confidence=0.8):
                            #last_x = i.left
                            last_y = i.top
                            #print("last_x", last_x)
                            print("last_y", last_y)
                            y_point = last_y


                        # 먼저 아래쪽 클릭하기

                        if y_point != 0:
                            click_pos_2(160, y_point + 60, cla)
                            time.sleep(0.1)
                            click_pos_2(160, y_point + 60, cla)
                            time.sleep(0.1)
                        else:
                            click_pos_2(160, 160, cla)
                            time.sleep(0.1)
                        time.sleep(0.5)

                        exist_request = False


                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\request\\get_re_s.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(310, 130, 370, 180, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            exist_request = True
                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\request\\get_re_a.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(310, 130, 370, 180, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            exist_request = True
                        if exist_request == True:
                            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\request\\re_confirm.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(800, 950, 950, 1040, cla, img, 0.9)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                            else:

                                for i in range(20):
                                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\request\\re_y_point.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(230, 130, 300, 800, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        v_.re_click_count = 0
                                        complete = False
                                        break
                                    else:
                                        complete = True
                                    time.sleep(0.1)
                                if complete == True:
                                    # S, A 존재함에도 불구하고 수락이 비활성화 and 받은 의뢰가 없음 => 받기 완료 되었다는 뜻
                                    get_request = True
                                    myQuest_play_add(cla, sche)
                                    time.sleep(0.1)

                                    recieve = True

                                    break
                                else:
                                    # S, A 존재함에도 불구하고 수락이 비활성화 => 받기 완료 되었다는 뜻
                                    get_request = True

                                    recieve = True

                                    break

                            time.sleep(0.5)
                        else:
                            break_count += 1
                            if break_count > 1:

                                print("클릭한 위치에 S급, A급 퀘스트 존재하지 않음")
                                if fresh_count < 3:
                                    # 수락 가능한 상태일 경우 갱신하기
                                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\request\\re_confirm.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(800, 950, 950, 1040, cla, img, 0.9)
                                    if imgs_ is not None and imgs_ != False:
                                        for f in range(10):
                                            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\request\\refresh_confirm.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(500, 550, 600, 620, cla, img, 0.9)
                                            if imgs_ is not None and imgs_ != False:
                                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                                # click_pos_2(410, 590, cla)
                                                fresh_count += 1
                                                break_count = 0
                                                break
                                            else:
                                                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\request\\reftresh_free.PNG"
                                                img_array = np.fromfile(full_path, np.uint8)
                                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                imgs_ = imgs_set_(100, 990, 200, 1030, cla, img, 0.9)
                                                if imgs_ is not None and imgs_ != False:
                                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                                    time.sleep(0.2)
                                                else:
                                                    fresh_count += 1
                                                    break
                                            time.sleep(0.5)
                                    else:
                                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\request\\re_disclaim.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(810, 970, 910, 1020, cla, img, 0.9)
                                        if imgs_ is not None and imgs_ != False:
                                            # 이건 클릭 잘못한 것임
                                            break
                                        else:
                                            # 이건 더이상 수락할 수 없는 상태임
                                            get_request = True
                                            break
                                else:
                                    click_pos_2(160, y_point + 60, cla)
                                    time.sleep(0.1)
                                    click_pos_2(160, y_point + 60, cla)
                                    time.sleep(0.5)
                                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\request\\re_confirm.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(800, 950, 950, 1040, cla, img, 0.9)
                                    if imgs_ is not None and imgs_ != False:
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                    else:
                                        break_count += 1
                                        if break_count > 2:
                                            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\request\\re_disclaim.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(810, 970, 910, 1020, cla, img, 0.9)
                                            if imgs_ is not None and imgs_ != False:
                                                # 이건 클릭 잘못한 것임
                                                break
                                            else:
                                                # 이건 더이상 수락할 수 없는 상태임
                                                get_request = True


                                                for i in range(20):
                                                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\request\\re_y_point.PNG"
                                                    img_array = np.fromfile(full_path, np.uint8)
                                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                    imgs_ = imgs_set_(230, 130, 300, 800, cla, img, 0.8)
                                                    if imgs_ is not None and imgs_ != False:
                                                        v_.re_click_count = 0
                                                        complete = False
                                                        break
                                                    else:
                                                        complete = True
                                                    time.sleep(0.1)
                                                if complete == True:
                                                    get_request = True
                                                    myQuest_play_add(cla, sche)
                                                    time.sleep(0.1)

                            time.sleep(0.5)
                        if recieve == True:
                            get_request = True
                            break
                else:
                    get_request = True

                # 받기 완료 후 나가기
                for o in range(5):
                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\request\\refresh_confirm.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(500, 550, 600, 620, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                    else:
                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\title\\request_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(10, 10, 160, 100, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_2(935, 55, cla)
                            get_request = True
                        else:
                            break
                    time.sleep(0.5)
            else:
                menu_open(cla)
                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\request\\menu_open.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(670, 240, 950, 400, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("request_menu_open...", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    for i in range(10):
                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\title\\request_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(10, 10, 160, 100, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("request_title...opened", imgs_)
                            break
                        time.sleep(0.3)
    except Exception as e:
        print(e)


def request_bosang_and_move(cla, sche):
    import numpy as np
    import cv2
    import pyautogui
    import random

    from function_moon import imgs_set_, click_pos_reg, drag_pos, mouse_move_cpp, click_pos_2
    from repair_moon import my_stat_up

    try:

        print("request_bosang_and_move")
        v_.re_click_count += 1
        print(v_.re_click_count, "번 지남...의뢰퀘스트 중(20번 마다 체크)")



        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\request\\clear_re.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(840, 80, 910, 350, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("clear_re", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
            my_stat_up(cla)

        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\request\\bosang_re2.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(430, 400, 510, 450, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:

            for i in range(10):
                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\request\\bosang_re.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(290, 620, 673, 710, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    result_ran = random.randint(1, 5)

                    ran_x = 270 + (result_ran * 70)

                    click_pos_2(ran_x, 665, cla)
                else:
                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\request\\bosang_re2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(430, 400, 510, 450, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y + 100, cla)
                        break
                time.sleep(0.5)





            # 퀘스트 완료시 보상 선택하기
        else:
            # 보상 선택 없다면 퀘스트 다시 클릭하기

            # 60번마다 의뢰퀘스트 진행중인지 체크해주기


            request_ing = False

            request_click_x = 0
            request_click_y = 0

            for i in range(3):

                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\request\\execute_re2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(680, 90, 730, 280, cla, img, 0.9)
                if imgs_ is not None and imgs_ != False:
                    print("execute_re2", imgs_)
                    request_click_x = imgs_.x + 170
                    request_click_y = imgs_.y
                    request_ing = True
                    break
                else:
                    drag_pos(800, 260, 800, 130, cla)
                    time.sleep(0.5)
                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\request\\execute_re2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(680, 90, 730, 280, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        print("execute_re22", imgs_)
                        request_click_x = imgs_.x + 170
                        request_click_y = imgs_.y
                        request_ing = True
                        break
                    else:
                        print("not execute_re2", i)
                        if i > 1:
                            get_my_request(cla, sche)
                time.sleep(0.5)

            if request_ing == True:
                if v_.re_click_count < 3 or v_.re_click_count % 20 == 0:

                    click_pos_reg(request_click_x, request_click_y, cla)
                    time.sleep(0.1)
                    mouse_move_cpp(500, 500, cla)
                    time.sleep(0.1)
                    for i in range(10):
                        # 이동하기
                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\confirm\\move.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(450, 500, 700, 700, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("move", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.1)
                            break
                        time.sleep(0.2)
                else:
                    time.sleep(0.2)





    except Exception as e:
        print(e)