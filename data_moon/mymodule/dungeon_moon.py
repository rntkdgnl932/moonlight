import sys
import os
import time
import requests

sys.path.append('C:/my_games/moonlight/data_moon/mymodule')

import variable as v_

def dungeon_start(cla, sche):
    import numpy as np
    import cv2

    from function_moon import imgs_set_

    from action_moon import attack_check_and_attack
    from schedule import myQuest_play_add
    from potion_moon import potion_check


    try:
        print("dungeon_start")

        complete = False

        d_in_ = dungeon_ing_check(cla)



        if d_in_ == True:
            print("던전 돌고 있는 중")
            attack_check_and_attack(cla)
            potion_check(cla)
        else:
            complete = dungeon_in(cla, sche)

        if complete == True:
            myQuest_play_add(cla, sche)


    except Exception as e:
        print(e)

def dungeon_ing_check(cla):
    import numpy as np
    import cv2

    from function_moon import imgs_set_

    from action_moon import attack_check_and_attack


    try:
        print("dungeon_ing_check")

        d_in_ = False

        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\dungeon\\stair_ing1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(40, 100, 130, 160, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            attack_check_and_attack(cla)
            d_in_ = True
        else:
            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\dungeon\\stair_ing2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(40, 100, 130, 160, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                attack_check_and_attack(cla)
                d_in_ = True
            else:
                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\dungeon\\stair_ing2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(40, 100, 130, 160, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    attack_check_and_attack(cla)
                    d_in_ = True

        return d_in_
    except Exception as e:
        print(e)

def dungeon_in(cla, sche):
    import numpy as np
    import cv2
    import pyautogui
    import random

    from function_moon import imgs_set_, click_pos_reg, click_pos_2

    from action_moon import loading, menu_open, attack_check_and_attack
    from get_item import get_items
    from potion_moon import maul_potion_small_only
    from schedule import myQuest_play_add
    from repair_moon import repair_start


    try:
        print("dungeon_in")

        complete = False

        # 스케쥴에서 던전 정보 뽑기
        result_dun = sche.split("/")
        # result_dun[0] => 던전
        # result_dun[1] => 균열, 심연, 월드
        # result_dun[2] => 던전종류_층수
        result_dun_detail = result_dun[2].split("_")
        # result_dun_detail[0] => 균열(홈염의신전, 얼음유적지, 마리아스의동굴), 심연(뒤틀린심연), 월드(스피렌의안뜰)
        # result_dun_detail[1] => 층수


        d_in_ = False
        d_in_count = 0
        while d_in_ is False:
            d_in_count += 1
            if d_in_count > 7:
                d_in_ = True

            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\title\\dungeon_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 30, 120, 100, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("hi")

                # 던전종류 클릭
                if result_dun[1] == "균열":
                    click_pos_2(100, 100, cla)
                    time.sleep(0.1)
                    click_pos_2(100, 100, cla)
                    time.sleep(0.5)

                    if result_dun_detail[0] == "홍염의신전":
                        click_pos_2(150, 400, cla)

                        if int(result_dun_detail[1]) > 5:

                            dun_stair = 5
                        else:
                            dun_stair = int(result_dun_detail[1])

                        y_reg = 95 + (dun_stair * 55)
                        time.sleep(0.1)

                        for i in range(10):
                            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\dungeon\\hongyum_in_check.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(10, 300, 200, 500, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_2(100, y_reg, cla)
                                time.sleep(0.2)
                                click_pos_2(875, 1005, cla)
                                break
                            time.sleep(0.3)


                    if result_dun_detail[0] == "얼음유적지":
                        click_pos_2(450, 400, cla)

                        if int(result_dun_detail[1]) > 5:

                            dun_stair = 5
                        else:
                            dun_stair = int(result_dun_detail[1])

                        y_reg = 95 + (dun_stair * 55)
                        time.sleep(0.1)

                        for i in range(10):
                            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\dungeon\\ice_in_check.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(10, 300, 200, 500, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_2(100, y_reg, cla)
                                time.sleep(0.2)
                                click_pos_2(875, 1005, cla)
                                break
                            time.sleep(0.3)


                    if result_dun_detail[0] == "마리아스의동굴":
                        click_pos_2(750, 400, cla)

                        dun_stair = int(result_dun_detail[1])

                        y_reg = 95 + (dun_stair * 55)
                        time.sleep(0.1)

                        for i in range(10):
                            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\dungeon\\cave_in_check.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(10, 300, 200, 500, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_2(100, y_reg, cla)
                                time.sleep(0.2)
                                click_pos_2(875, 1005, cla)
                                break
                            time.sleep(0.3)
                    # 공통 진입 부분
                    for i in range(15):
                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\dungeon\\stair_ing1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(40, 100, 130, 160, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            attack_check_and_attack(cla)
                            d_in_ = True
                            break
                        else:
                            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\dungeon\\stair_ing2.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(40, 100, 130, 160, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                attack_check_and_attack(cla)
                                d_in_ = True
                                break
                            else:
                                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\dungeon\\stair_ing2.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(40, 100, 130, 160, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    attack_check_and_attack(cla)
                                    d_in_ = True
                                    break
                                else:
                                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\action\\loding_1.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(250, 920, 650, 1040, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        loading(cla)
                                    else:
                                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\dungeon\\dun_complete.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(370, 130, 550, 170, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            d_in_ = True
                                            complete = True
                                            break
                                        else:
                                            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\dungeon\\dun_low_level.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(370, 130, 550, 170, cla, img, 0.8)
                                            if imgs_ is not None and imgs_ != False:
                                                d_in_ = True
                                                complete = True
                                                break
                        time.sleep(0.3)


                elif result_dun[1] == "심연":
                    click_pos_2(250, 100, cla)
                    time.sleep(0.1)
                    click_pos_2(250, 100, cla)
                    time.sleep(0.5)

                    if result_dun_detail[0] == "뒤틀린린":

                        click_pos_2(150, 400, cla)

                        dun_stair = int(result_dun_detail[1])

                        y_reg = 95 + (dun_stair * 55)
                        time.sleep(0.1)

                        for i in range(10):
                            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\dungeon\\hongyum_in_check.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(10, 300, 200, 500, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_2(100, y_reg, cla)
                                time.sleep(0.2)
                                click_pos_2(875, 1005, cla)
                                break
                            time.sleep(0.3)

                    # 공통 진입 부분
                    for i in range(15):
                        # 추후 뒤틀린으로 수정하기
                        #
                        #
                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\dungeon\\stair_ing1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(40, 100, 130, 160, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            attack_check_and_attack(cla)
                            d_in_ = True
                            break
                        else:
                            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\action\\loding_1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(250, 920, 650, 1040, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                loading(cla)
                            else:
                                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\dungeon\\dun_complete.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(370, 130, 550, 170, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    d_in_ = True
                                    complete = True
                                    break
                                else:
                                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\dungeon\\dun_low_level.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(370, 130, 550, 170, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        d_in_ = True
                                        complete = True
                                        break
                        time.sleep(0.3)


                elif result_dun[1] == "월드":
                    click_pos_2(400, 100, cla)
                    time.sleep(0.1)
                    click_pos_2(400, 100, cla)
                    time.sleep(0.5)

            else:
                menu_open(cla)
                time.sleep(0.1)

                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\dungeon\\menu_dungeon.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(680, 240, 960, 400, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)

                    for i in range(10):
                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\title\\dungeon_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(10, 30, 120, 100, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            break
                        time.sleep(0.5)


        return complete
    except Exception as e:
        print(e)

