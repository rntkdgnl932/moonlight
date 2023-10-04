import sys
import os
import time
import requests

sys.path.append('C:/my_games/moonlight/data_moon/mymodule')

import variable as v_

def jadong_start(cla, sche):
    import numpy as np
    import cv2

    from function_moon import imgs_set_, click_pos_reg
    from action_moon import attack_check_and_attack
    from potion_moon import potion_check


    try:

        print("jadong_start")

        # 던전 입장 표시 끄기
        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\clean_screen\\cancle.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(220, 470, 700, 900, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            click_pos_reg(imgs_.x, imgs_.y, cla)

        # 스케쥴 분석석
        result_spot = sche.split("/")

        # 사냥터
        dir_path = "C:\\my_games\\moonlight\\data_moon"
        file_path = dir_path + "\\jadong\\moon_" + result_spot[1] + ".txt"

        with open(file_path, "r", encoding='utf-8-sig') as file:
            read_spot = file.read().splitlines()
            print("read_spot", read_spot)

        # 해당 지역 검색
        for i in range(len(read_spot)):
            result_spot_ready = read_spot[i].split("_")
            if result_spot_ready[0] == result_spot[2]:
                result_data_ready = read_spot[i]
                time.sleep(0.1)
                break
        result_data = result_data_ready.split("_")
        print("result_data", result_data)

        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\jadong\\map_list\\" + result_data[3] + ".PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(50, 110, 160, 160, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:

            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\maul\\chango.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(800, 970, 960, 1040, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("마을이다. 사냥터로 이동하자")
                jadong_spot_in(cla, sche)
            else:
                print("자동사냥중")
                attack_check_and_attack(cla)
                potion_check(cla)
        # 전투중(해당맵에 있는지 파악후 공격중인지 파악하기, 물약 파악하기)
        else:
            # 전투중 아닐때
            print("사냥터로 이동하자")
            jadong_spot_in(cla, sche)

    except Exception as e:
        print(e)


def jadong_spot_in(cla, sche):

    try:
        print("jadong_spot_in")



        # 지도 펼치기
        map_open_check(cla)
        map_spot_in(cla, sche)


    except Exception as e:
        print(e)

def map_open_check(cla):
    import numpy as np
    import cv2

    from function_moon import imgs_set_, click_pos_reg
    from action_moon import clean_screen


    try:
        print("map_open_check")
        # 지도 펼치기
        for i in range(5):
            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\check\\map_open.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(40, 110, 80, 150, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                break
            else:
                clean_screen(cla)
                time.sleep(0.1)
                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\check\\map_close.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(40, 110, 80, 150, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
            time.sleep(0.5)


    except Exception as e:
        print(e)

def map_spot_in(cla, sche):
    import numpy as np
    import cv2

    from function_moon import imgs_set_, click_pos_reg, click_pos_2


    try:
        print("map_spot_in", sche)

        # 스케쥴 분석석
        result_spot = sche.split("/")

        # 지도 펼치기
        map_in = False
        map_in_count = 0
        while map_in is False:
            map_in_count += 1
            if map_in_count > 7:
                map_in = True

            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\jadong\\map\\now_reg.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(860, 950, 950, 1000, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:

                map_in = True

                # 지역정보 활성화
                for i in range(10):
                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\jadong\\map\\region_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(5, 30, 110, 80, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        break
                    else:
                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\jadong\\map\\region_information.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(560, 950, 620, 1000, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                        else:
                            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\jadong\\map\\region_information2.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(560, 950, 620, 1000, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                            else:
                                if i > 7:
                                    click_pos_2(620, 980, cla)

                    time.sleep(0.5)


                # 월드맵 전환
                for i in range(5):
                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\jadong\\map\\world_map.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(710, 30, 800, 80, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        break
                    else:
                        click_pos_2(705, 980, cla)
                    time.sleep(0.2)

                # 상세위치로 맵이동
                for i in range(5):
                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\jadong\\map\\world_map.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(710, 30, 800, 80, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\jadong\\map\\map_" + str(
                            result_spot[1]) + ".PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(550, 310, 960, 730, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.1)
                    else:
                        break
                    time.sleep(0.5)

                # 지역 맵 클릭하기
                map_spot_in_region(cla, sche)

            else:
                click_pos_2(130, 210, cla)
                for i in range(10):
                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\jadong\\map\\now_reg.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(860, 950, 950, 1000, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        break
                    time.sleep(0.3)



    except Exception as e:
        print(e)


def map_spot_in_region(cla, sche):
    import numpy as np
    import cv2
    import pyautogui
    import random

    from function_moon import imgs_set_, click_pos_reg, click_pos_2, mouse_move_cpp
    from action_moon import out_check, attack_check_and_attack, loading, moving, clean_screen


    try:
        print("map_spot_in_region", sche)

        # 스케쥴 분석석
        result_spot = sche.split("/")

        # 사냥터
        dir_path = "C:\\my_games\\moonlight\\data_moon"
        file_path = dir_path + "\\jadong\\moon_" + result_spot[1] + ".txt"

        with open(file_path, "r", encoding='utf-8-sig') as file:
            read_spot = file.read().splitlines()
            print("read_spot", read_spot)

        # 해당 지역 클릭
        for i in range(len(read_spot)):
            result_spot_ready = read_spot[i].split("_")
            if result_spot_ready[0] == result_spot[2]:
                result_data = read_spot[i]
                click_pos_2(int(result_spot_ready[1]), int(result_spot_ready[2]), cla)
                time.sleep(0.1)

                for r in range(10):
                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\jadong\\map\\region_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(5, 30, 110, 80, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        break
                    time.sleep(0.3)
                break


        # 랜덤으로 포털 타기
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

        y_plus = 0

        if result_spot[2] == "바란" or result_spot[2] == "세라보그외곽":
            y_plus = 100

        result_random_num = 0
        contect_random_num = 0

        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\jadong\\map\\teleport_click.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        for i in pyautogui.locateAllOnScreen(img, region=(10 + plus, 100 + y_plus, 530, 400),
                                             confidence=0.8):
            result_random_num += 1
            last_x = i.left
            last_y = i.top
            # print(result_random_num, "=> last_x : ", last_x, ", last_y :", last_y)

        # print(result_random_num)

        result = random.randint(1, result_random_num)

        print("result", result)

        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\jadong\\map\\teleport_click.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        for i in pyautogui.locateAllOnScreen(img, region=(10 + plus, 100 + y_plus, 530, 400),
                                             confidence=0.8):
            contect_random_num += 1
            last_x = i.left
            last_y = i.top
            if result == contect_random_num:
                break

        print("last_x : ", last_x, ", last_y :", last_y)



        for m in range(10):
            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\jadong\\map\\move_confirm.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(450, 560, 630, 630, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                click_pos_reg(imgs_.x, imgs_.y, cla)
                break
            else:
                click_pos_reg(last_x, last_y, cla)
            time.sleep(0.3)

        # 다시 세분화해서 정보 얻기
        result_datas = result_data.split("_")

        if result_datas[4] == "end":

            out_ = False
            out_count = 0
            while out_ is False:
                out_count += 1
                if out_count > 7:
                    out_ = True
                result_out = out_check(cla)
                if result_out == True:
                    #공격 버튼 클릭
                    out_ = True
                    attack_check_and_attack(cla)
                    time.sleep(0.1)
                    mouse_move_cpp(500, 500, cla)
                    time.sleep(0.1)

                else:
                    print("자동 사냥터 이동중...", result_spot[2])
                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\action\\loding_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(250, 920, 650, 1040, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        loading(cla)
                time.sleep(1)
        else:
            print("한번 더 이동하자")

            out_ = False
            out_count = 0
            while out_ is False:
                out_count += 1
                if out_count > 7:
                    out_ = True
                result_out = out_check(cla)
                if result_out == True:

                    out_ = True

                    # 지도 클릭
                    click_pos_2(125, 205, cla)
                    for i in range(10):
                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\jadong\\map\\now_reg.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(860, 950, 950, 1000, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            break
                        time.sleep(0.3)



                    if result_datas[0] == "벌레굴":
                        print("최종도착지", result_datas[0])
                        arrived_x = 937
                        arrived_y = 667
                        click_pos_2(937, 667, cla)
                    elif result_datas[0] == "폭군의신전":
                        print("최종도착지", result_datas[0])
                    elif result_datas[0] == "아슬란둥지":
                        print("최종도착지", result_datas[0])
                    elif result_datas[0] == "해방된공중사원":
                        print("최종도착지", result_datas[0])

                    for i in range(10):
                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\jadong\\map_region_title\\" + \
                                    result_datas[
                                        3] + ".PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(690, 40, 850, 100, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            break
                        else:
                            click_pos_2(arrived_x, arrived_y, cla)
                        time.sleep(0.5)

                    # 랜덤 목적지 찍기
                    x_reg = random.randint(590, 930)
                    y_reg = random.randint(350, 680)
                    click_pos_2(x_reg, y_reg, cla)
                    time.sleep(0.1)
                    clean_screen(cla)

                    arrived = False
                    arrived_count = 0
                    arrived_count_msg = 0
                    while arrived is False:
                        arrived_count += 1
                        arrived_count_msg += 1
                        if arrived_count > 7:
                            arrived = True
                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\jadong\\and\\" + result_datas[3] + ".PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(410, 900, 540, 955, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            arrived_count = 0
                            if arrived_count_msg < 4:
                                print("열심히 가는 중...")

                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\action\\loding_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(250, 920, 650, 1040, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            loading(cla)
                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\action\\move_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(250, 820, 650, 1040, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            arrived = True
                            moving(cla)
                        time.sleep(0.5)

                    # 공격 버튼 클릭
                    attack_check_and_attack(cla)
                    time.sleep(0.1)
                    mouse_move_cpp(500, 500, cla)
                    time.sleep(0.1)



                else:
                    print("자동 사냥터 이동중...", result_spot[2])
                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\action\\loding_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(250, 920, 650, 1040, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        loading(cla)
                time.sleep(1)
        #########
        # 아래부터는 자동 사냥 특수한 경우
        #########

        # 모레평원은 무기부터 획득하도록 해보자
        if result_datas[0] == "모래평원":

            # 지도 펼치기
            map_in = False
            map_in_count = 0
            while map_in is False:
                map_in_count += 1
                if map_in_count > 7:
                    map_in = True

                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\jadong\\map\\now_reg.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(860, 950, 950, 1000, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:

                    map_in = True

                    # 모래평원 특수 위치
                    click_pos_2(890, 525, cla)

                    # 지도 비활성화 하기
                    for i in range(3):
                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\jadong\\map\\now_reg.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(860, 950, 950, 1000, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_2(935, 55, cla)
                        else:
                            break
                        time.sleep(0.5)

                    # 이동중
                    moving(cla)




                else:
                    click_pos_2(130, 210, cla)
                    for i in range(10):
                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\jadong\\map\\now_reg.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(860, 950, 950, 1000, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            break
                        time.sleep(0.3)


    except Exception as e:
        print(e)


