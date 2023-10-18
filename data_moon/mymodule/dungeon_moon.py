import sys
import os
import time
import requests

sys.path.append('C:/my_games/moonlight/data_moon/mymodule')

import variable as v_

def dungeon_start(cla, sche):
    import numpy as np
    import cv2

    from function_moon import imgs_set_, click_pos_reg

    from action_moon import attack_check_and_attack
    from schedule import myQuest_play_add
    from potion_moon import potion_check, maul_potion_small_only


    try:
        print("dungeon_start")

        # 던전 입장 표시 끄기
        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\clean_screen\\cancle.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(220, 470, 700, 900, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            click_pos_reg(imgs_.x, imgs_.y, cla)


        complete = False

        d_in_ = dungeon_ing_check(cla, sche)


        if d_in_ == True:
            print("던전 돌고 있는 중")
            attack_check_and_attack(cla)
            potion_check(cla)
        else:
            result_potion_bool = potion_check(cla)
            if result_potion_bool == True:
                maul_potion_small_only(cla)

            complete = dungeon_in(cla, sche)

        if complete == True:
            myQuest_play_add(cla, sche)


    except Exception as e:
        print(e)

def dungeon_ing_check(cla, sche):
    import numpy as np
    import cv2

    from function_moon import imgs_set_

    from action_moon import attack_check_and_attack


    try:
        print("dungeon_ing_check")

        d_in_ = False

        if '던전' in sche:

            # 스케쥴에서 던전 정보 뽑기
            result_dun = sche.split("/")
            # result_dun[0] => 던전
            # result_dun[1] => 균열, 심연, 월드
            # result_dun[2] => 던전종류_층수
            result_dun_detail = result_dun[2].split("_")
            # result_dun_detail[0] => 균열(홈염의신전, 얼음유적지, 마리아스의동굴), 심연(뒤틀린심연), 월드(스피렌의안뜰)
            # result_dun_detail[1] => 층수


            d_in_ = False

            if result_dun[1] == "균열":

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
                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\dungeon\\stair_ing3.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(40, 100, 130, 160, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            attack_check_and_attack(cla)
                            d_in_ = True

            elif result_dun[1] == "월드":
                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\dungeon\\world_in_title_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(40, 100, 160, 160, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    attack_check_and_attack(cla)
                    d_in_ = True
                else:
                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\dungeon\\world_in_title_2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(40, 100, 160, 160, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        attack_check_and_attack(cla)
                        d_in_ = True

                if d_in_ == True:

                    in_maul = False

                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\jabhwa_click1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(700, 970, 950, 1040, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("jabhwa_click1", imgs_)
                        in_maul = True
                    else:
                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\jabhwa_click2.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(700, 970, 950, 1040, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("jabhwa_click2", imgs_)
                            in_maul = True

                    if in_maul == True:
                        print("본 사냥터로 이동하자")
                        world_step(cla, int(result_dun_detail[1]))

        else:
            # 스케쥴이 던전이 아닐 경우...
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
                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\dungeon\\stair_ing3.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(40, 100, 130, 160, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        attack_check_and_attack(cla)
                        d_in_ = True
                    else:
                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\dungeon\\world_in_title_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(40, 100, 160, 160, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            attack_check_and_attack(cla)
                            d_in_ = True
                        else:
                            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\dungeon\\world_in_title_2.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(40, 100, 160, 160, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                attack_check_and_attack(cla)
                                d_in_ = True

        return d_in_
    except Exception as e:
        print(e)

def dungeon_in(cla, sche):
    import numpy as np
    import cv2

    from function_moon import imgs_set_, click_pos_reg, click_pos_2

    from action_moon import loading, menu_open, attack_check_and_attack, clean_screen, hunting_check, channel_move

    try:
        print("dungeon_in : 던전 진입")

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
                print("dungeon hi", result_dun[1])

                # 던전종류 클릭
                if result_dun[1] == "균열":
                    click_pos_2(100, 100, cla)
                    time.sleep(0.1)
                    click_pos_2(100, 100, cla)
                    time.sleep(0.5)

                    if result_dun_detail[0] == "홍염의신전":
                        click_pos_2(160, 580, cla)

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
                        click_pos_2(450, 580, cla)

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

                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\dungeon\\dun_lock.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(600, 400, 880, 700, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("던전 미오픈...완료로 간주함")
                            complete = True
                            for i in range(10):
                                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\title\\dungeon_title.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(10, 30, 120, 100, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_2(935, 55, cla)
                                else:
                                    break
                                time.sleep(0.5)
                        else:
                            click_pos_2(750, 580, cla)

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
                    if complete != True:
                        # 공통 진입 부분

                        hunt = False

                        for i in range(15):
                            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\dungeon\\stair_ing1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(40, 100, 130, 160, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                time.sleep(1)
                                # random_move(cla)
                                # attack_check_and_attack(cla)

                                hunt = True
                                d_in_ = True
                                break
                            else:
                                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\dungeon\\stair_ing2.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(40, 100, 130, 160, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    time.sleep(1)
                                    # random_move(cla)
                                    # attack_check_and_attack(cla)

                                    hunt = True
                                    d_in_ = True
                                    break
                                else:
                                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\dungeon\\stair_ing3.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(40, 100, 130, 160, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        time.sleep(1)
                                        # random_move(cla)
                                        # attack_check_and_attack(cla)

                                        hunt = True
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
                                                else:
                                                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\title\\dungeon_title.PNG"
                                                    img_array = np.fromfile(full_path, np.uint8)
                                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                    imgs_ = imgs_set_(10, 30, 120, 100, cla, img, 0.8)
                                                    if imgs_ is not None and imgs_ != False:
                                                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\dungeon\\already_dun1.PNG"
                                                        img_array = np.fromfile(full_path, np.uint8)
                                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                        imgs_ = imgs_set_(370, 120, 500, 170, cla, img, 0.8)
                                                        if imgs_ is not None and imgs_ != False:
                                                            d_in_ = True
                                                            click_pos_2(935, 55, cla)
                                                            break
                                                        else:
                                                            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\dungeon\\already_dun2.PNG"
                                                            img_array = np.fromfile(full_path, np.uint8)
                                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                            imgs_ = imgs_set_(370, 120, 500, 170, cla, img, 0.8)
                                                            if imgs_ is not None and imgs_ != False:
                                                                d_in_ = True
                                                                click_pos_2(935, 55, cla)
                                                                break

                            time.sleep(0.3)
                        if hunt == True:

                            channel_move(cla)

                            attack_check_and_attack(cla)

                            result_hunted = hunting_check(cla)
                            if result_hunted == False:
                                for i in range(15):
                                    print("zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz", i)
                                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\game_start\\character_select_title.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(20, 30, 150, 100, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        print("던전 다시 시작하기", i)
                                        break
                                    else:
                                        menu_open(cla)
                                        time.sleep(0.1)
                                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\action\\menu_character_select.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(670, 470, 960, 670, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            click_pos_reg(imgs_.x, imgs_.y, cla)
                                            for z in range(10):
                                                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\game_start\\character_select_title.PNG"
                                                img_array = np.fromfile(full_path, np.uint8)
                                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                imgs_ = imgs_set_(20, 30, 150, 100, cla, img, 0.8)
                                                if imgs_ is not None and imgs_ != False:
                                                    print("던전 다시 시작하기", z)
                                                    break
                                                time.sleep(1)

                                    time.sleep(1)


                            else:
                                random_move(cla)
                                print("사냥 시작했음")


                elif result_dun[1] == "심연":
                    click_pos_2(250, 100, cla)
                    time.sleep(0.1)
                    click_pos_2(250, 100, cla)
                    time.sleep(0.5)

                    if result_dun_detail[0] == "뒤틀린심연":

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

                    if result_dun_detail[0] == "스피렌의안뜰":

                        dun_stair = int(result_dun_detail[1])

                        y_reg = 95 + (dun_stair * 55)
                        time.sleep(0.1)

                        for i in range(10):
                            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\dungeon\\world_in_check_1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(10, 120, 200, 500, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_2(100, y_reg, cla)
                                time.sleep(0.2)
                                click_pos_2(875, 1005, cla)
                                break
                            time.sleep(0.3)

                    # 공통 진입 부분
                    for i in range(15):
                        #
                        #
                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\dungeon\\world_in_title_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(40, 100, 160, 160, cla, img, 0.8)
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
                            # else:
                            #     full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\dungeon\\dun_complete.PNG"
                            #     img_array = np.fromfile(full_path, np.uint8)
                            #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            #     imgs_ = imgs_set_(370, 130, 550, 170, cla, img, 0.8)
                            #     if imgs_ is not None and imgs_ != False:
                            #         d_in_ = True
                            #         complete = True
                            #         break
                            #     else:
                            #         full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\dungeon\\dun_low_level.PNG"
                            #         img_array = np.fromfile(full_path, np.uint8)
                            #         img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            #         imgs_ = imgs_set_(370, 130, 550, 170, cla, img, 0.8)
                            #         if imgs_ is not None and imgs_ != False:
                            #             d_in_ = True
                            #             complete = True
                            #             break
                        time.sleep(0.3)
                    # 뒤에 1~5 등등 몬스터 레벨에 따라 나누자
                    world_step(cla, int(result_dun_detail[1]))
            else:

                result_dun_in = dungeon_ing_check(cla, "any")

                if result_dun_in == True:
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

def random_move(cla):
    import cv2
    import numpy as np
    from function_moon import imgs_set_, click_pos_reg
    try:
        print("random_move")
        for i in range(10):
            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\dungeon\\quick_random.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(640, 960, 710, 1040, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                click_pos_reg(imgs_.x, imgs_.y, cla)
                time.sleep(0.1)
                break
            time.sleep(0.2)


    except Exception as e:
        print(e)


def world_step(cla, step):
    import cv2
    import numpy as np
    from function_moon import imgs_set_, click_pos_reg, click_pos_2
    from action_moon import moving, channel_move
    try:
        print("world_step", step)

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

                for i in range(5):
                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\dungeon\\world_move_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(500, 570, 570, 620, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        break
                    else:
                        if step == 1:
                            click_pos_2(230, 365, cla)
                        elif step == 2:
                            click_pos_2(475, 320, cla)
                        elif step == 3:
                            click_pos_2(230, 270, cla)
                        elif step == 4:
                            click_pos_2(475, 270, cla)
                        elif step == 5:
                            click_pos_2(230, 320, cla)
                        elif step == 6:
                            click_pos_2(475, 220, cla)
                    time.sleep(0.5)

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

                # 한적한 채널로 변경하기
                channel_move(cla)



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

