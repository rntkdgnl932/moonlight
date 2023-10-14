import sys
import os
import time
import requests

sys.path.append('C:/my_games/moonlight/data_moon/mymodule')

import variable as v_

def dead_die(cla, sche):
    import numpy as np
    import cv2
    import pyautogui
    import random

    from function_moon import imgs_set_, click_pos_reg, click_pos_2

    from action_moon import loading, clean_screen, menu_open
    from character_select_and_game_start import game_start_screen
    from potion_moon import maul_potion_dead_only
    from schedule import myQuest_play_add
    from schedule import myQuest_play_check
    from dungeon_moon import dungeon_ing_check


    try:

        dead = False

        boohwal = False

        print("dead_die")

        # chapter 1
        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\dead\\boohwal_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(400, 870, 700, 950, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("boohwal_1...", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
            dead = True

        # chapter 2
        if v_.not_boohwal == False:

            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\dead\\exp_recovery.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(200, 30, 350, 100, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("exp recovery...", imgs_)
                boohwal = True

        if dead == True or boohwal == True:
            for i in range(10):
                result_dun = dungeon_ing_check(cla, "any")

                if result_dun == True:
                    click_pos_2(925, 270, cla)
                    for k in range(10):
                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\dungeon\\dun_out_confirm.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(510, 560, 580, 620, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            break
                        time.sleep(0.3)

                else:
                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\maul\\chango.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(800, 970, 960, 1040, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        break
                    else:
                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\action\\loding_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(250, 920, 650, 1040, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            loading(cla)
                time.sleep(0.5)

            if boohwal == True:
                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\maul\\chango.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(800, 970, 960, 1040, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("good boohwal maul")
                    if sche == "튜토육성":
                        maul_potion_dead_only(cla)

                        v_.tuto_dead += 1
                        if v_.tuto_dead > 0:
                            myQuest_play_add(cla, sche)
                    else:
                        maul_potion_dead_only(cla)
                else:
                    # 메뉴 열기
                    menu_open(cla)
                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\action\\menu_character_select.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(670, 470, 960, 670, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        for i in range(10):
                            # 로딩중 확인
                            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\action\\loding_1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(250, 920, 650, 1040, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                loading(cla)
                            else:
                                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\game_start\\character_select_title.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(20, 30, 150, 100, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    break
                            time.sleep(1)
                    # 스케쥴부터 불러오기
                    result_schedule = myQuest_play_check(v_.now_cla, "check")
                    character_id = result_schedule[0][1]

                    # 게임 시작 화면인지 분석부터 하기
                    game_start_screen(cla, character_id)
            else:
                if sche == "튜토육성":
                    maul_potion_dead_only(cla)

                    v_.tuto_dead += 1
                    if v_.tuto_dead > 0:
                        myQuest_play_add(cla, sche)
                else:
                    maul_potion_dead_only(cla)

        # chapter 2
        if v_.not_boohwal == False:

            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\dead\\exp_recovery.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(200, 30, 350, 100, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("exp recovery...", imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)

                for i in range(10):
                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\dead\\anymore_exp_recovery.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(390, 470, 570, 530, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("anymore exp recovery", imgs_)
                        clean_screen(cla)
                        break
                    else:
                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\dead\\dead_nabi.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(300, 600, 650, 800, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            v_.not_boohwal = True
                            clean_screen(cla)
                            break

                        else:
                            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\dead\\exp_recovery_title.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(400, 320, 540, 380, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("exp recovery title : click_pos_2(470, 710, cla)", imgs_)
                                click_pos_2(470, 710, cla)
                                time.sleep(0.1)
                                if i > 8:
                                    clean_screen(cla)
                                    break
                    time.sleep(0.3)





    except Exception as e:
        print(e)

