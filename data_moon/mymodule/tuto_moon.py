import sys
import os
import time
import requests

sys.path.append('C:/my_games/moonlight/data_moon/mymodule')

import variable as v_

def tuto_start(cla):
    import numpy as np
    import cv2

    from action_moon import moving
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
            tuto_tutorial(cla)
            tuto_click(cla)



    except Exception as e:
        print(e)
        return 0


def tuto_click(cla):
    import numpy as np
    import cv2

    from repair_moon import my_stat_up

    from function_moon import click_pos_reg, click_pos_2, imgs_set_, mouse_move_cpp, drag_pos_reg, drag_pos
    try:
        print("tuto_click", cla)

        tuto_skip(cla)

        # 최초 드래그해서 위로 끌어 올리기

        # 일시적인 오류로 클릭하기
        click_pos_2(480, 555, cla)
        time.sleep(0.1)

        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\tuto\\tuto_check1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(888, 110, 905, 130, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("good tuto")
        else:
            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\tuto\\tuto_check2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(800, 100, 900, 140, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("tuto_check2 tuto")
                click_pos_2(925, 120, cla)
                time.sleep(0.5)
            else:
                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\tuto\\tuto_check3.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(800, 100, 900, 140, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("tuto_check3 tuto")
                    click_pos_2(925, 120, cla)
                    time.sleep(0.5)
                else:
                    print("tuto click...ready")
                    click_pos_2(925, 120, cla)
                    time.sleep(0.5)

        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\tuto\\tuto_click1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(850, 100, 900, 450, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("tuto_click1", imgs_)

            drag_pos_reg(imgs_.x, imgs_.y, imgs_.x, imgs_.y + 350, cla)
        else:
            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\tuto\\tuto_click2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(850, 100, 900, 450, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("tuto_click2", imgs_)
                drag_pos_reg(imgs_.x, imgs_.y, imgs_.x, imgs_.y + 350, cla)
            else:
                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\tuto\\tuto_click3.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(850, 100, 900, 450, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("tuto_click3", imgs_)
                    drag_pos_reg(imgs_.x, imgs_.y, imgs_.x, imgs_.y + 350, cla)
                else:
                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\tuto\\tuto_click4.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(850, 100, 900, 450, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("tuto_click4", imgs_)
                        drag_pos_reg(imgs_.x, imgs_.y, imgs_.x, imgs_.y + 350, cla)
                    else:
                        drag_pos(800, 120, 800, 120 + 350, cla)

        time.sleep(0.5)


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
            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\tuto\\tuto_click1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(850, 100, 900, 150, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("tuto_click1", imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)
                q_click = True
            else:
                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\tuto\\tuto_click2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(850, 100, 900, 150, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("tuto_click2", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    q_click = True
                else:
                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\tuto\\tuto_click3.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(850, 100, 900, 150, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("tuto_click3", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        q_click = True
                    else:
                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\tuto\\tuto_click4.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(850, 100, 900, 150, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("tuto_click4", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            q_click = True

        mouse_move_cpp(500, 500, cla)
        if q_click == True:
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
                time.sleep(0.1)



        return q_click
    except Exception as e:
        print(e)
        return 0



def tuto_tutorial(cla):
    import numpy as np
    import cv2
    import pyautogui

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

