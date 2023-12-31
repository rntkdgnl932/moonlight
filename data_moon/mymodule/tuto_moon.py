import sys
import os
import time
import requests

sys.path.append('C:/my_games/moonlight/data_moon/mymodule')

import variable as v_

def tuto_start(cla):
    import numpy as np
    import cv2

    from action_moon import moving, out_check
    from function_moon import imgs_set_

    try:
        print("tuto_start", cla)

        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\action\\move_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(250, 820, 650, 1040, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            moving(cla)
        else:
            tuto_click(cla)
            for i in range(10):
                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\jabhwa_title.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(50, 30, 110, 80, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    scd = (i + 1) * 0.1
                    print("잡화상점 보인다", scd)
                    tuto_gwangpok(cla)
                    break
                time.sleep(0.1)
            tuto_tutorial(cla)



    except Exception as e:
        print(e)
        return 0

def quest_check(cla):
    import numpy as np
    import cv2

    from repair_moon import my_stat_up
    from dungeon_moon import dungeon_ing_check

    from function_moon import click_pos_reg, click_pos_2, imgs_set_, mouse_move_cpp, drag_pos_reg, drag_pos
    try:
        print("quest_check", cla)

        tuto_look = False

        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\tuto\\tuto_check1_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(900, 90, 950, 150, cla, img, 0.9)
        if imgs_ is not None and imgs_ != False:
            print("quest_check : tuto_check1_1", imgs_)
            tuto_look = True

        if tuto_look == False:
            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\tuto\\tuto_check2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(800, 100, 900, 140, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("quest_check : tuto_check2", imgs_)
                click_pos_2(925, 120, cla)
                time.sleep(0.5)
            else:
                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\tuto\\tuto_check3.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(800, 100, 900, 140, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("quest_check : tuto_check3", imgs_)
                    click_pos_2(925, 120, cla)
                    time.sleep(0.5)
                else:
                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\tuto\\tuto_check1_2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(900, 90, 950, 150, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        print("quest_check : tuto_check1_2", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.5)

    except Exception as e:
        print(e)
        return 0

def quest_click(cla):
    import numpy as np
    import cv2
    from function_moon import click_pos_reg, imgs_set_, click_pos_2, drag_pos
    from repair_moon import my_stat_up
    from action_moon import confirm_all
    from schedule import myQuest_play_add
    try:
        print("quest_click", cla)

        q_click = False

        # 완료 또는 진행하기
        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\tuto\\q_clear_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(840, 80, 910, 350, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("q_clear_1", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
            my_stat_up(cla)
        else:
            # 드래그 해주기
            drag_pos(800, 220, 800, 220 + 350, cla)

            time.sleep(1)


            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\request\\clear_re.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(840, 80, 910, 350, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("clear_re", imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)
                my_stat_up(cla)

            else:
                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\tuto\\tuto_click1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(850, 100, 900, 150, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("q_click1", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    q_click = True
                else:
                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\tuto\\tuto_click2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(850, 100, 900, 150, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("q_click2", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        q_click = True
                    else:
                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\tuto\\tuto_click3.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(850, 100, 900, 150, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("q_click3", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            q_click = True
                        else:
                            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\tuto\\tuto_click4.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(850, 100, 900, 150, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("q_click4", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                q_click = True
        time.sleep(0.1)

        if q_click == True:
            for i in range(10):

                stop_tuto = False

                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\tuto\\stop_tuto\\arklasya.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(300, 350, 500, 480, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    stop_tuto = True

                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\tuto\\stop_tuto\\kamosya.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(300, 350, 500, 480, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    stop_tuto = True

                if stop_tuto == True:
                    click_pos_2(410, 755, cla)
                    time.sleep(0.5)
                    click_pos_2(410, 755, cla)
                    time.sleep(0.5)
                    click_pos_2(25, 180, cla)
                    time.sleep(0.1)
                    click_pos_2(25, 180, cla)
                    for c in range(10):
                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\tuto\\stop_tuto\\confirm.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(510, 560, 580, 620, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            break
                        time.sleep(0.2)
                    myQuest_play_add(cla, "튜토육성")
                    break
                time.sleep(0.3)


        return q_click
    except Exception as e:
        print(e)
        return 0


def tuto_click(cla):
    import numpy as np
    import cv2


    from dungeon_moon import dungeon_ing_check

    from function_moon import click_pos_reg, click_pos_2, imgs_set_, mouse_move_cpp, drag_pos_reg, drag_pos

    from action_moon import out_check, clean_screen
    try:
        print("tuto_click", cla)

        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\action\\menu_character_select.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(670, 470, 960, 670, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            click_pos_2(935, 55, cla)
            time.sleep(0.1)

        result_out = out_check(cla)
        if result_out == False:
            clean_screen(cla)
            time.sleep(0.1)


        tuto_skip(cla)

        # 최초 던전 중인지 파악하기...
        result_dun = dungeon_ing_check(cla, "튜토육성")

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

        # 일시적인 오류로 클릭하기
        click_pos_2(480, 555, cla)
        time.sleep(0.1)



        # 화면에 퀘스트 활성화 되어있는지 확인
        quest_check(cla)
        # 화면에 활성화 되어 있는 퀘스트를 클릭하기
        result_click = quest_click(cla)
        time.sleep(0.1)
        if result_click == False:
            # 안 보여서 드래그하기
            drag_pos(800, 260, 800, 260 + 350, cla)
            time.sleep(0.5)

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



        return result_click
    except Exception as e:
        print(e)
        return 0



def tuto_tutorial(cla):
    import numpy as np
    import cv2
    import pyautogui

    from potion_moon import maul_potion_full

    from function_moon import click_pos_reg, click_pos_2, imgs_set_
    try:
        print("tuto_tutorial", cla)

        # 최초 무기 장착
        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\tuto\\tutorial\\jangchak_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(840, 780, 920, 840, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("jangchak_1", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)

        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\tuto\\tutorial\\gabang_touch_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(770, 100, 855, 155, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("gabang_touch_1", imgs_)
            click_pos_2(870, 65, cla)

        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\clean_screen\\jangbi_title.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(440, 80, 510, 135, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("jangbi_title", imgs_)
            click_pos_2(930, 55, cla)

        # 스킬북 선택
        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\tuto\\tutorial\\skillbook_select1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(550, 200, 960, 450, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("skillbook_select1", imgs_)
            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\tuto\\tutorial\\skillbook_select2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(610, 110, 960, 450, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("skillbook_select2", imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)
        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\tuto\\tutorial\\study.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(460, 700, 560, 820, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("study", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\tuto\\tutorial\\menu_open.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(800, 100, 960, 200, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("menu_open", imgs_)
            click_pos_2(920, 60, cla)
        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\tuto\\tutorial\\skill_hwagin.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(650, 170, 760, 240, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("menu_open", imgs_)
            click_pos_2(760, 140, cla)
        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\title\\skill_title.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(5, 30, 80, 80, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("skill_title", imgs_)
            for i in range(5):
                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\clean_screen\\x_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(900, 30, 960, 90, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                else:
                    break
                time.sleep(0.2)

        # 버디알 선택

        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\tuto\\tutorial\\tuto_budy_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(30, 800, 400, 1040, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("tuto budy", imgs_)
            click_pos_2(215, 1010, cla)

        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\tuto\\tutorial\\budyegg_select1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(550, 200, 960, 350, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("budyegg_select1", imgs_)
            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\tuto\\tutorial\\budyegg_select2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(620, 110, 960, 400, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("budyegg_select2", imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)
        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\tuto\\tutorial\\open.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(480, 730, 600, 800, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("open", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)

        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\tuto\\tutorial\\budy_touch.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(700, 180, 830, 230, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("budy_touch", imgs_)
            click_pos_2(815, 140, cla)

        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\tuto\\tutorial\\budy_sohwan.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(100, 980, 200, 1040, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("budy_sohwan", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
        else:
            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\tuto\\tutorial\\budy_sohwan2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(100, 980, 200, 1040, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("budy_sohwan2", imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)
        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\clean_screen\\x_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(900, 30, 960, 90, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            click_pos_reg(imgs_.x, imgs_.y, cla)

        # 형상 소환권
        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\tuto\\tutorial\\hyungsang_sohwan_click1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(620, 110, 960, 400, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("hyungsang_sohwan_click1", imgs_)
            click_pos_2(725, 160, cla)

        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\tuto\\tutorial\\hyungsang_sohwan_click2.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(620, 110, 960, 400, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("hyungsang_sohwan_click2", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)

        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\tuto\\tutorial\\hyungsang_touch_click1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(580, 250, 700, 300, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("hyungsang_touch_click1", imgs_)
            click_pos_2(710, 215, cla)
        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\tuto\\tutorial\\hyungsang_chagyong_click1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(220, 520, 330, 590, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("hyungsang_chagyong_click1", imgs_)
            click_pos_2(210, 500, cla)
        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\tuto\\tutorial\\hyungsang_chagyong_click2.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(220, 520, 330, 590, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("hyungsang_chagyong_click2", imgs_)
            click_pos_2(160, 1010, cla)

        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\tuto\\tutorial\\jangchak_2.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(120, 980, 200, 1040, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("jangchak_2", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)

        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\tuto\\tutorial\\hyungsang_out_click1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(360, 120, 500, 200, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("hyungsang_out_click1", imgs_)
            click_pos_2(530, 100, cla)
        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\tuto\\tutorial\\hyungsang_out_click2.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(480, 60, 580, 150, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("hyungsang_out_click2", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)

        # 설득하기
        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\tuto\\tutorial\\talking_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(500, 400, 800, 520, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("talking_1", imgs_)
            click_pos_2(470, 530, cla)




    except Exception as e:
        print(e)
        return 0

def tuto_gwangpok(cla):
    import numpy as np
    import cv2

    from action_moon import confirm_all, clean_screen

    from function_moon import click_pos_reg, click_pos_2, imgs_set_
    try:
        print("tuto_gwngpok", cla)

        # 잡화 상점
        print("잡화상점")
        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\jabhwa_title.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(50, 30, 110, 80, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
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

                    click_pos_2(575, 635, cla)
                    time.sleep(0.1)

                    for i in range(3):
                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\potion\\buy_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(470, 300, 530, 350, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            for k in range(3):
                                click_pos_2(545, 735, cla)
                                time.sleep(0.3)
                        else:
                            break
                        time.sleep(0.5)

                    clean_screen(cla)

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

    except Exception as e:
        print(e)
        return 0

def tuto_skip(cla):
    import numpy as np
    import cv2

    from action_moon import confirm_all

    from function_moon import click_pos_reg, click_pos_2, imgs_set_
    try:
        print("tuto_skip", cla)

        # 스킵하기
        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\clean_screen\\skip_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(840, 30, 950, 80, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("skip_1", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\clean_screen\\skip_2.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 30, 950, 800, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("skip_2...", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)

        confirm_all(cla)

    except Exception as e:
        print(e)
        return 0

