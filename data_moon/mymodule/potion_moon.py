import sys
import os
import time
import requests

sys.path.append('C:/my_games/moonlight/data_moon/mymodule')

import variable as v_


def potion_check(cla):
    import numpy as np
    import cv2

    from function_moon import imgs_set_

    from action_moon import out_check


    try:
        print("potion check")
        not_potion = False


        result_out = out_check(cla)
        if result_out == True:

            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\no_potion_small.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(410, 970, 480, 1040, cla, img, 0.93)
            if imgs_ is not None and imgs_ != False:
                print("small potion", imgs_)
                not_potion = True
            else:
                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\no_potion_middle.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(410, 970, 480, 1040, cla, img, 0.93)
                if imgs_ is not None and imgs_ != False:
                    print("middle potion", imgs_)
                    not_potion = True
                else:
                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\no_potion_all.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(410, 970, 480, 1040, cla, img, 0.93)
                    if imgs_ is not None and imgs_ != False:
                        print("no_potion_all potion", imgs_)
                        not_potion = True
                    else:
                        print("포션 있다.", v_.need_potion)
                        v_.need_potion = 0

        if not_potion == True:
            v_.need_potion += 1
            print("3회 이상 물약 없을 시 물약 사러 ㄱㄱ", v_.need_potion)
            if v_.need_potion > 2:

                # 의뢰 체크 갱신
                v_.re_click_count = 0

                maul_potion_small_only(cla)
                v_.need_potion = 0
        return not_potion
    except Exception as e:
        print(e)


def maul_potion_small_only(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random

    from function_moon import imgs_set_, click_pos_reg, click_pos_2

    from action_moon import loading, clean_screen
    from dungeon_moon import dungeon_ing_check
    from soojib_boonhae_moon import soojib_boonhae_start
    from schedule import myQuest_play_check


    try:
        print("maul_potion_small_only")

        # 마을  이동 후 수집분해부터 하기


        in_maul = False
        in_maul_count = 0
        while in_maul is False:
            in_maul_count += 1
            if in_maul_count > 7:
                in_maul = True

            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\maul\\chango.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(800, 970, 960, 1040, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                in_maul = True

                soojib_boonhae_start(cla)
                time.sleep(0.1)

            else:

                # 스케쥴부터 불러오기
                result_schedule = myQuest_play_check(cla, "check")
                print("maul_potion_small_only : result_schedule", result_schedule)
                character_id = result_schedule[0][1]
                result_schedule_ = result_schedule[0][2]

                result_dun = dungeon_ing_check(cla, result_schedule_)

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
                click_pos_2(25, 180, cla)
                for i in range(10):
                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\maul\\maul_move_confirm.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(500, 560, 600, 620, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        break
                    time.sleep(0.2)
                for i in range(10):
                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\maul\\chango.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(800, 970, 960, 1040, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        # click_pos_reg(imgs_.x, imgs_.y, cla)

                        break
                    time.sleep(0.5)

        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\maul\\chango.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(800, 970, 960, 1040, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:

            for i in range(20):
                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\jabhwa_title.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(50, 30, 110, 80, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    break
                else:
                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\jabhwa_click1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(700, 970, 950, 1040, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("jabhwa_click1", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                    else:
                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\jabhwa_click2.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(700, 970, 950, 1040, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("jabhwa_click2", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                        else:
                            print("없다...")
                            click_pos_2(745, 1000, cla)
                time.sleep(1)

            print("hi")
            print("광폭의비약")
            result = exist_buf(cla, "gwangpok")
            if result == True:
                # 광폭의 비약
                buy = False
                buy_count = 0
                while buy is False:
                    buy_count += 1
                    if buy_count > 7:
                        buy = True

                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\buy_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(470, 300, 530, 350, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        buy = True

                        for i in range(10):
                            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\buy_title.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(470, 300, 530, 350, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_2(575, 635, cla)
                                time.sleep(0.1)


                        for i in range(3):
                            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\buy_title.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(470, 300, 530, 350, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_2(545, 735, cla)
                            else:
                                break
                            time.sleep(0.5)

                    else:

                        for i in range(10):
                            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\buy_title.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(470, 300, 530, 350, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                break
                            else:
                                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\gwangpok.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(50, 250, 200, 800, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.2)

            print("구운 고기")
            result = exist_buf(cla, "goowoon_gogi")
            if result == True:
                buy_ready = True

                for i in range(3):
                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\sangjum_my_bag\\goowoon_gogi.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(620, 110, 960, 910, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        buy_ready = False
                        break
                    else:
                        click_pos_2(765, 100, cla)
                    time.sleep(0.5)

                if buy_ready == True:

                    # 구운 고기
                    buy = False
                    buy_count = 0
                    while buy is False:
                        buy_count += 1
                        if buy_count > 7:
                            buy = True

                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\buy_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(470, 300, 530, 350, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            buy = True

                            for i in range(10):
                                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\buy_title.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(470, 300, 530, 350, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_2(575, 635, cla)
                                    time.sleep(0.1)
                            for i in range(3):
                                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\buy_title.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(470, 300, 530, 350, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_2(545, 735, cla)
                                else:
                                    break
                                time.sleep(0.5)

                        else:

                            for i in range(10):
                                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\buy_title.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(470, 300, 530, 350, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    break
                                else:
                                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\goowoon_gogi.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(50, 250, 200, 800, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(0.2)

            print("교관의 도시락")
            result = exist_buf(cla, "dosirak")
            if result == True:

                buy_ready = True

                for i in range(3):
                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\sangjum_my_bag\\dosirak.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(620, 110, 960, 910, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        buy_ready = False
                        break
                    else:
                        click_pos_2(765, 100, cla)
                    time.sleep(0.5)

                if buy_ready == True:

                    # 교관의 도시락
                    buy = False
                    buy_count = 0
                    while buy is False:
                        buy_count += 1
                        if buy_count > 7:
                            buy = True

                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\buy_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(470, 300, 530, 350, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            buy = True
                            for i in range(10):
                                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\buy_title.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(470, 300, 530, 350, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_2(575, 635, cla)
                                    time.sleep(0.1)
                            for i in range(3):
                                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\buy_title.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(470, 300, 530, 350, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_2(545, 735, cla)
                                else:
                                    break
                                time.sleep(0.5)

                        else:

                            for i in range(10):
                                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\buy_title.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(470, 300, 530, 350, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    break
                                else:
                                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\dosirak.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(50, 250, 200, 800, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(0.2)

            print("과일 꼬치")
            result = exist_buf(cla, "ggochi")
            if result == True:

                buy_ready = True

                for i in range(3):
                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\sangjum_my_bag\\ggochi.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(620, 110, 960, 910, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        buy_ready = False
                        break
                    else:
                        click_pos_2(765, 100, cla)
                    time.sleep(0.5)

                if buy_ready == True:

                    # 과일 꼬치
                    buy = False
                    buy_count = 0
                    while buy is False:
                        buy_count += 1
                        if buy_count > 7:
                            buy = True

                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\buy_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(470, 300, 530, 350, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            buy = True
                            for i in range(10):
                                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\buy_title.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(470, 300, 530, 350, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_2(575, 635, cla)
                                    time.sleep(0.1)
                            for i in range(3):
                                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\buy_title.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(470, 300, 530, 350, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_2(545, 735, cla)
                                else:
                                    break
                                time.sleep(0.5)

                        else:

                            for i in range(10):
                                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\buy_title.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(470, 300, 530, 350, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    break
                                else:
                                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\ggochi.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(50, 250, 200, 800, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(0.2)

            # 물약사기
            buy = False
            buy_count = 0
            while buy is False:
                buy_count += 1
                if buy_count > 7:
                    buy = True

                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\buy_title.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(470, 300, 530, 350, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    buy = True
                    click_pos_2(530, 670, cla)
                    time.sleep(0.1)
                    click_pos_2(530, 670, cla)
                    time.sleep(0.1)
                    click_pos_2(545, 735, cla)
                    time.sleep(0.1)

                    # 밖에 눌러서 나가기
                    click_pos_2(545, 735, cla)
                    time.sleep(0.1)

                else:

                    for i in range(10):
                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\buy_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(470, 300, 530, 350, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            break
                        else:
                            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\middle_buy.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(50, 200, 120, 260, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                            else:
                                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\small_potion_click.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(50, 120, 100, 170, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.2)
        # 나가기
        for i in range(10):
            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\buy_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(470, 300, 530, 350, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                clean_screen(cla)
            else:
                break
            time.sleep(0.3)


    except Exception as e:
        print(e)


def maul_potion_dead_only(cla):
    import numpy as np
    import cv2

    from function_moon import imgs_set_, click_pos_reg, click_pos_2

    from action_moon import loading, clean_screen
    from dungeon_moon import dungeon_ing_check
    from soojib_boonhae_moon import soojib_boonhae_start
    from schedule import myQuest_play_check
    from get_item import get_items
    from repair_moon import repair_start


    try:
        print("maul_potion_dead_only")

        # 마을  이동 후 수집분해부터 하기


        in_maul = False
        in_maul_count = 0
        while in_maul is False:
            in_maul_count += 1
            if in_maul_count > 7:
                in_maul = True

            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\maul\\chango.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(800, 970, 960, 1040, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                in_maul = True


                get_items(cla)
                repair_start(cla)

                soojib_boonhae_start(cla)

                time.sleep(0.1)

            else:

                # 스케쥴부터 불러오기
                result_schedule = myQuest_play_check(cla, "check")
                print("maul_potion_small_only : result_schedule", result_schedule)
                character_id = result_schedule[0][1]
                result_schedule_ = result_schedule[0][2]

                result_dun = dungeon_ing_check(cla, result_schedule_)

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
                click_pos_2(25, 180, cla)
                for i in range(10):
                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\maul\\maul_move_confirm.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(500, 560, 600, 620, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        break
                    time.sleep(0.2)
                for i in range(10):
                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\maul\\chango.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(800, 970, 960, 1040, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        # click_pos_reg(imgs_.x, imgs_.y, cla)

                        break
                    time.sleep(0.5)

        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\maul\\chango.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(800, 970, 960, 1040, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:

            for i in range(20):
                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\jabhwa_title.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(50, 30, 110, 80, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    click_pos_2(765, 100, cla)
                    time.sleep(0.1)
                    click_pos_2(765, 100, cla)
                    time.sleep(0.1)
                    break
                else:
                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\jabhwa_click1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(700, 970, 950, 1040, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("jabhwa_click1", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                    else:
                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\jabhwa_click2.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(700, 970, 950, 1040, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("jabhwa_click2", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                        else:
                            print("없다...")
                            click_pos_2(745, 1000, cla)
                time.sleep(1)



            print("광폭의비약")
            result = exist_buf(cla, "gwangpok")
            if result == True:
                # 광폭의 비약
                buy = False
                buy_count = 0
                while buy is False:
                    buy_count += 1
                    if buy_count > 7:
                        buy = True

                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\buy_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(470, 300, 530, 350, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        buy = True

                        for i in range(40):
                            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\buy_title.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(470, 300, 530, 350, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print(i)
                                if i > 29:
                                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\many\\" + str(i) + ".PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(430, 560, 520, 620, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        break
                                    else:
                                        click_pos_2(575, 635, cla)
                                        time.sleep(0.1)
                                else:
                                    click_pos_2(575, 635, cla)
                                    time.sleep(0.1)

                        for i in range(3):
                            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\buy_title.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(470, 300, 530, 350, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_2(545, 735, cla)
                            else:
                                break
                            time.sleep(0.5)

                    else:

                        for i in range(10):
                            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\buy_title.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(470, 300, 530, 350, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                break
                            else:
                                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\gwangpok.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(50, 250, 200, 800, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.2)

            print("구운 고기")
            result = exist_buf(cla, "goowoon_gogi")
            if result == True:
                buy_ready = True

                for i in range(3):
                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\sangjum_my_bag\\goowoon_gogi.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(620, 110, 960, 910, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        buy_ready = False
                        break
                    else:
                        click_pos_2(765, 100, cla)
                    time.sleep(0.5)

                if buy_ready == True:

                    # 구운 고기
                    buy = False
                    buy_count = 0
                    while buy is False:
                        buy_count += 1
                        if buy_count > 7:
                            buy = True

                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\buy_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(470, 300, 530, 350, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            buy = True

                            for i in range(40):
                                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\buy_title.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(470, 300, 530, 350, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print(i)
                                    if i > 29:
                                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\many\\" + str(
                                            i) + ".PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(430, 560, 520, 620, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            break
                                        else:
                                            click_pos_2(575, 635, cla)
                                            time.sleep(0.1)
                                    else:
                                        click_pos_2(575, 635, cla)
                                        time.sleep(0.1)
                            for i in range(3):
                                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\buy_title.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(470, 300, 530, 350, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_2(545, 735, cla)
                                else:
                                    break
                                time.sleep(0.5)

                        else:

                            for i in range(10):
                                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\buy_title.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(470, 300, 530, 350, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    break
                                else:
                                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\goowoon_gogi.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(50, 250, 200, 800, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(0.2)

            print("교관의 도시락")
            result = exist_buf(cla, "dosirak")
            if result == True:

                buy_ready = True

                for i in range(3):
                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\sangjum_my_bag\\dosirak.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(620, 110, 960, 910, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        buy_ready = False
                        break
                    else:
                        click_pos_2(765, 100, cla)
                    time.sleep(0.5)

                if buy_ready == True:

                    # 교관의 도시락
                    buy = False
                    buy_count = 0
                    while buy is False:
                        buy_count += 1
                        if buy_count > 7:
                            buy = True

                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\buy_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(470, 300, 530, 350, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            buy = True
                            for i in range(40):
                                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\buy_title.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(470, 300, 530, 350, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print(i)
                                    if i > 29:
                                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\many\\" + str(
                                            i) + ".PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(430, 560, 520, 620, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            break
                                        else:
                                            click_pos_2(575, 635, cla)
                                            time.sleep(0.1)
                                    else:
                                        click_pos_2(575, 635, cla)
                                        time.sleep(0.1)
                            for i in range(3):
                                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\buy_title.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(470, 300, 530, 350, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_2(545, 735, cla)
                                else:
                                    break
                                time.sleep(0.5)

                        else:

                            for i in range(10):
                                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\buy_title.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(470, 300, 530, 350, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    break
                                else:
                                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\dosirak.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(50, 250, 200, 800, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(0.2)

            print("과일 꼬치")
            result = exist_buf(cla, "ggochi")
            if result == True:

                buy_ready = True

                for i in range(3):
                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\sangjum_my_bag\\ggochi.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(620, 110, 960, 910, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        buy_ready = False
                        break
                    else:
                        click_pos_2(765, 100, cla)
                    time.sleep(0.5)

                if buy_ready == True:

                    # 과일 꼬치
                    buy = False
                    buy_count = 0
                    while buy is False:
                        buy_count += 1
                        if buy_count > 7:
                            buy = True

                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\buy_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(470, 300, 530, 350, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            buy = True
                            for i in range(40):
                                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\buy_title.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(470, 300, 530, 350, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print(i)
                                    if i > 29:
                                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\many\\" + str(
                                            i) + ".PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(430, 560, 520, 620, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            break
                                        else:
                                            click_pos_2(575, 635, cla)
                                            time.sleep(0.1)
                                    else:
                                        click_pos_2(575, 635, cla)
                                        time.sleep(0.1)
                            for i in range(3):
                                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\buy_title.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(470, 300, 530, 350, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_2(545, 735, cla)
                                else:
                                    break
                                time.sleep(0.5)

                        else:

                            for i in range(10):
                                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\buy_title.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(470, 300, 530, 350, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    break
                                else:
                                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\ggochi.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(50, 250, 200, 800, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(0.2)


            # 물약 사기
            buy = False
            buy_count = 0
            while buy is False:
                buy_count += 1
                if buy_count > 7:
                    buy = True

                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\buy_title.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(470, 300, 530, 350, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    buy = True
                    click_pos_2(530, 670, cla)
                    time.sleep(0.1)
                    click_pos_2(530, 670, cla)
                    time.sleep(0.1)
                    click_pos_2(545, 735, cla)
                    time.sleep(0.1)

                    # 밖에 눌러서 나가기
                    click_pos_2(545, 735, cla)
                    time.sleep(0.1)

                else:

                    for i in range(10):
                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\buy_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(470, 300, 530, 350, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            break
                        else:
                            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\middle_buy.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(50, 200, 120, 260, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                            else:
                                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\small_potion_click.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(50, 120, 100, 170, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.2)
        # 나가기
        for i in range(10):
            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\buy_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(470, 300, 530, 350, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                clean_screen(cla)
            else:
                break
            time.sleep(0.3)


    except Exception as e:
        print(e)


def maul_potion_full(cla):
    import numpy as np
    import cv2

    from function_moon import imgs_set_, click_pos_reg, click_pos_2

    from action_moon import clean_screen
    from dungeon_moon import dungeon_ing_check
    from soojib_boonhae_moon import soojib_boonhae_start
    from schedule import myQuest_play_check


    try:
        print("maul_potion_full")



        in_maul = False
        in_maul_count = 0
        while in_maul is False:
            in_maul_count += 1
            if in_maul_count > 7:
                in_maul = True

            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\maul\\chango.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(800, 970, 960, 1040, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                in_maul = True

                # 수집분해부터 하기
                soojib_boonhae_start(cla)
                time.sleep(0.1)

            else:
                # 스케쥴부터 불러오기
                result_schedule = myQuest_play_check(cla, "check")
                print("maul_potion_small_only : result_schedule", result_schedule)
                character_id = result_schedule[0][1]
                result_schedule_ = result_schedule[0][2]

                result_dun = dungeon_ing_check(cla, result_schedule_)

                if result_dun == True:
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

                clean_screen(cla)
                click_pos_2(25, 180, cla)
                for i in range(10):
                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\maul\\maul_move_confirm.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(500, 560, 600, 620, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        break
                    time.sleep(0.2)
                for i in range(10):
                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\maul\\chango.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(800, 970, 960, 1040, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        break
                    time.sleep(0.5)

        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\maul\\chango.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(800, 970, 960, 1040, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:

            for i in range(20):
                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\jabhwa_title.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(50, 30, 110, 80, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    break
                else:
                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\jabhwa_click1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(700, 970, 950, 1040, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("jabhwa_click1", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                    else:
                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\jabhwa_click2.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(700, 970, 950, 1040, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("jabhwa_click2", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                        else:
                            print("없다...")
                            click_pos_2(745, 1000, cla)
                time.sleep(1)

            print("광폭의비약")
            # 광폭의 비약
            buy = False
            buy_count = 0
            while buy is False:
                buy_count += 1
                if buy_count > 7:
                    buy = True

                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\buy_title.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(470, 300, 530, 350, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    buy = True

                    for i in range(40):
                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\buy_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(470, 300, 530, 350, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print(i)
                            if i > 29:
                                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\many\\" + str(i) + ".PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(430, 560, 520, 620, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    break
                                else:
                                    click_pos_2(575, 635, cla)
                                    time.sleep(0.1)
                            else:
                                click_pos_2(575, 635, cla)
                                time.sleep(0.1)

                    for i in range(3):
                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\buy_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(470, 300, 530, 350, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_2(545, 735, cla)
                        else:
                            break
                        time.sleep(0.5)

                else:

                    for i in range(10):
                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\buy_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(470, 300, 530, 350, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            break
                        else:
                            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\gwangpok.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(50, 250, 200, 800, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.2)

            print("구운 고기")

            buy_ready = True

            for i in range(3):
                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\sangjum_my_bag\\goowoon_gogi.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(620, 110, 960, 910, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    buy_ready = False
                    break
                else:
                    click_pos_2(765, 100, cla)
                time.sleep(0.5)

            if buy_ready == True:

                # 구운 고기
                buy = False
                buy_count = 0
                while buy is False:
                    buy_count += 1
                    if buy_count > 7:
                        buy = True

                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\buy_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(470, 300, 530, 350, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        buy = True



                        for i in range(40):
                            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\buy_title.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(470, 300, 530, 350, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print(i)
                                if i > 29:
                                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\many\\" + str(i) + ".PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(430, 560, 520, 620, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        break
                                    else:
                                        click_pos_2(575, 635, cla)
                                        time.sleep(0.1)
                                else:
                                    click_pos_2(575, 635, cla)
                                    time.sleep(0.1)
                        for i in range(3):
                            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\buy_title.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(470, 300, 530, 350, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_2(545, 735, cla)
                            else:
                                break
                            time.sleep(0.5)

                    else:

                        for i in range(10):
                            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\buy_title.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(470, 300, 530, 350, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                break
                            else:
                                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\goowoon_gogi.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(50, 250, 200, 800, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.2)



            print("교관의 도시락")

            buy_ready = True

            for i in range(3):
                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\sangjum_my_bag\\dosirak.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(620, 110, 960, 910, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    buy_ready = False
                    break
                else:
                    click_pos_2(765, 100, cla)
                time.sleep(0.5)

            if buy_ready == True:

                # 교관의 도시락
                buy = False
                buy_count = 0
                while buy is False:
                    buy_count += 1
                    if buy_count > 7:
                        buy = True

                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\buy_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(470, 300, 530, 350, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        buy = True
                        for i in range(40):
                            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\buy_title.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(470, 300, 530, 350, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print(i)
                                if i > 29:
                                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\many\\" + str(i) + ".PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(430, 560, 520, 620, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        break
                                    else:
                                        click_pos_2(575, 635, cla)
                                        time.sleep(0.1)
                                else:
                                    click_pos_2(575, 635, cla)
                                    time.sleep(0.1)
                        for i in range(3):
                            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\buy_title.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(470, 300, 530, 350, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_2(545, 735, cla)
                            else:
                                break
                            time.sleep(0.5)

                    else:

                        for i in range(10):
                            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\buy_title.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(470, 300, 530, 350, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                break
                            else:
                                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\dosirak.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(50, 250, 200, 800, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.2)

            print("과일 꼬치")

            buy_ready = True

            for i in range(3):
                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\sangjum_my_bag\\ggochi.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(620, 110, 960, 910, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    buy_ready = False
                    break
                else:
                    click_pos_2(765, 100, cla)
                time.sleep(0.5)

            if buy_ready == True:

                # 과일 꼬치
                buy = False
                buy_count = 0
                while buy is False:
                    buy_count += 1
                    if buy_count > 7:
                        buy = True

                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\buy_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(470, 300, 530, 350, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        buy = True
                        for i in range(40):
                            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\buy_title.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(470, 300, 530, 350, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print(i)
                                if i > 29:
                                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\many\\" + str(i) + ".PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(430, 560, 520, 620, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        break
                                    else:
                                        click_pos_2(575, 635, cla)
                                        time.sleep(0.1)
                                else:
                                    click_pos_2(575, 635, cla)
                                    time.sleep(0.1)
                        for i in range(3):
                            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\buy_title.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(470, 300, 530, 350, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_2(545, 735, cla)
                            else:
                                break
                            time.sleep(0.5)

                    else:

                        for i in range(10):
                            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\buy_title.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(470, 300, 530, 350, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                break
                            else:
                                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\ggochi.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(50, 250, 200, 800, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.2)

            print("순간 이동 주문서")
            # 순간 이동 주문서
            buy = False
            buy_count = 0
            while buy is False:
                buy_count += 1
                if buy_count > 7:
                    buy = True

                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\buy_title.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(470, 300, 530, 350, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    buy = True
                    for i in range(5):
                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\buy_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(470, 300, 530, 350, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_2(575, 635, cla)
                            time.sleep(0.1)
                    for i in range(3):
                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\buy_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(470, 300, 530, 350, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_2(545, 735, cla)
                        else:
                            break
                        time.sleep(0.5)

                else:

                    for i in range(10):
                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\buy_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(470, 300, 530, 350, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            break
                        else:
                            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\random_move.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(50, 250, 200, 800, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.2)

            # 물약사기
            buy = False
            buy_count = 0
            while buy is False:
                buy_count += 1
                if buy_count > 7:
                    buy = True

                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\buy_title.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(470, 300, 530, 350, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    buy = True
                    click_pos_2(530, 670, cla)
                    time.sleep(0.1)
                    click_pos_2(530, 670, cla)
                    time.sleep(0.1)
                    click_pos_2(545, 735, cla)
                    time.sleep(0.1)

                    # 밖에 눌러서 나가기
                    click_pos_2(545, 735, cla)
                    time.sleep(0.1)
                    for i in range(3):
                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\buy_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(470, 300, 530, 350, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_2(545, 735, cla)
                        else:
                            break
                        time.sleep(0.5)

                else:

                    for i in range(10):
                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\buy_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(470, 300, 530, 350, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            break
                        else:
                            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\middle_buy.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(50, 200, 120, 260, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                            else:
                                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\small_potion_click.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(50, 120, 100, 170, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.2)
            quick_slot_check(cla)
        # 나가기
        for i in range(10):
            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\buy_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(470, 300, 530, 350, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                clean_screen(cla)
            else:
                break
            time.sleep(0.3)


    except Exception as e:
        print(e)

def quick_slot_check(cla):
    import numpy as np
    import cv2

    from function_moon import imgs_set_, click_pos_reg, click_pos_2

    from action_moon import menu_open, clean_screen
    try:


        bag_open = False
        bag_open_count = 0
        while bag_open is False:
            bag_open_count += 1
            if bag_open_count > 10:
                bag_open = True
            print("bag", bag_open_count)

            gogi = False
            dosirak = False
            ggochi = False
            gwangpok = False
            ran_move = False

            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\repair\\boonhae_click.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(750, 920, 840, 970, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:

                # not able
                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\quick_slot\\not_able_click.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(630, 950, 960, 1040, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    click_pos_2(710, 95, cla)
                    time.sleep(0.5)
                    click_pos_2(670, 160, cla)
                    time.sleep(0.5)



                # gogi
                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\quick_slot\\goowoon_gogi.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(630, 950, 710, 1040, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    gogi = True
                else:
                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\quick_slot\\goowoon_gogi_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(630, 950, 710, 1040, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        gogi = True
                    else:
                        # goowoon_gogi
                        for i in range(5):
                            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\quick_slot\\goowoon_gogi.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(630, 950, 710, 1040, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                break
                            else:
                                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\quick_slot\\goowoon_gogi_1.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(630, 950, 710, 1040, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    break

                                else:
                                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\quick_slot\\goowoon_gogi2.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(615, 115, 960, 890, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                        time.sleep(0.1)
                                        click_pos_2(670, 990, cla)
                                    else:
                                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\quick_slot\\goowoon_gogi2_2.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(615, 115, 960, 890, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            click_pos_reg(imgs_.x, imgs_.y, cla)
                                            time.sleep(0.1)
                                            click_pos_2(670, 990, cla)
                                        else:
                                            click_pos_2(760, 100, cla)
                            time.sleep(0.5)
                # dosirak
                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\quick_slot\\dosirak.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(690, 950, 770, 1040, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    dosirak = True
                else:
                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\quick_slot\\dosirak_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(690, 950, 770, 1040, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        dosirak = True
                    else:
                        for i in range(5):
                            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\quick_slot\\dosirak.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(690, 950, 770, 1040, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                break
                            else:
                                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\quick_slot\\dosirak_1.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(690, 950, 770, 1040, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    break
                                else:
                                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\quick_slot\\dosirak2.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(615, 115, 960, 890, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                        time.sleep(0.1)
                                        click_pos_2(730, 990, cla)
                                    else:
                                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\quick_slot\\dosirak2_2.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(615, 115, 960, 890, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            click_pos_reg(imgs_.x, imgs_.y, cla)
                                            time.sleep(0.1)
                                            click_pos_2(730, 990, cla)
                                        else:
                                            click_pos_2(760, 100, cla)
                            time.sleep(0.5)
                # ggpchi
                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\quick_slot\\ggochi.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(750, 950, 840, 1040, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    ggochi = True
                else:
                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\quick_slot\\ggochi_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(750, 950, 840, 1040, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        ggochi = True
                    else:
                        for i in range(5):
                            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\quick_slot\\ggochi.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(750, 950, 840, 1040, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                break
                            else:
                                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\quick_slot\\ggochi_1.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(750, 950, 840, 1040, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    break
                                else:
                                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\quick_slot\\ggochi2.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(615, 115, 960, 890, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                        time.sleep(0.1)
                                        click_pos_2(795, 990, cla)
                                    else:
                                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\quick_slot\\ggochi2_2.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(615, 115, 960, 890, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            click_pos_reg(imgs_.x, imgs_.y, cla)
                                            time.sleep(0.1)
                                            click_pos_2(795, 990, cla)
                                        else:
                                            click_pos_2(760, 100, cla)
                            time.sleep(0.5)
                # gwangpok
                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\quick_slot\\gwangpok.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(820, 950, 890, 1040, cla, img, 0.95)
                if imgs_ is not None and imgs_ != False:
                    gwangpok = True
                else:
                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\quick_slot\\gwangpok_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(820, 950, 890, 1040, cla, img, 0.95)
                    if imgs_ is not None and imgs_ != False:
                        gwangpok = True
                    else:
                        for i in range(5):
                            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\quick_slot\\gwangpok.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(820, 950, 890, 1040, cla, img, 0.95)
                            if imgs_ is not None and imgs_ != False:
                                break
                            else:
                                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\quick_slot\\gwangpok_1.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(820, 950, 890, 1040, cla, img, 0.95)
                                if imgs_ is not None and imgs_ != False:
                                    break
                                else:
                                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\quick_slot\\gwangpok2.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(615, 115, 960, 890, cla, img, 0.95)
                                    if imgs_ is not None and imgs_ != False:
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                        time.sleep(0.1)
                                        click_pos_2(855, 990, cla)
                                    else:
                                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\quick_slot\\gwangpok2_2_2.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(615, 115, 960, 890, cla, img, 0.95)
                                        if imgs_ is not None and imgs_ != False:
                                            click_pos_reg(imgs_.x, imgs_.y, cla)
                                            time.sleep(0.1)
                                            click_pos_2(855, 990, cla)
                                        else:
                                            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\quick_slot\\gwangpok2_2.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(615, 115, 960, 890, cla, img, 0.95)
                                            if imgs_ is not None and imgs_ != False:
                                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                                time.sleep(0.1)
                                                click_pos_2(855, 990, cla)
                                            else:
                                                click_pos_2(760, 100, cla)
                            time.sleep(0.5)
                # random
                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\quick_slot\\random_move.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(880, 950, 960, 1040, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    ran_move = True
                else:
                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\quick_slot\\random_move_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(880, 950, 960, 1040, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        ran_move = True
                    else:
                        for i in range(5):
                            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\quick_slot\\random_move.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(880, 950, 960, 1040, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                break
                            else:
                                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\quick_slot\\random_move_1.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(880, 950, 960, 1040, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    break
                                else:
                                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\quick_slot\\random_move2.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(615, 115, 960, 890, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                        time.sleep(0.1)
                                        click_pos_2(920, 990, cla)
                                    else:
                                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\quick_slot\\random_move2_2.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(615, 115, 960, 890, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            click_pos_reg(imgs_.x, imgs_.y, cla)
                                            time.sleep(0.1)
                                            click_pos_2(920, 990, cla)
                                        else:
                                            click_pos_2(760, 100, cla)
                            time.sleep(0.5)
                if gogi == True and dosirak == True and ggochi == True and gwangpok == True and ran_move == True:
                    clean_screen(cla)
                    bag_open = True
            else:
                menu_open(cla)
                time.sleep(0.1)
                click_pos_2(865, 65, cla)
                for i in range(10):
                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\repair\\boonhae_click.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(750, 920, 840, 970, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        break
                    time.sleep(0.2)
    except Exception as e:
        print(e)

def exist_buf(cla, data):
    import numpy as np
    import cv2

    from function_moon import imgs_set_
    try:
        buying = True
        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\buf\\" + str(data) + ".PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(630, 120, 960, 900, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            buying = False

        return buying
    except Exception as e:
        print(e)