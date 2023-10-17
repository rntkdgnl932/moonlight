import time
import sys


sys.path.append('C:/my_games/moonlight/data_moon/mymodule')

import variable as v_

def action_moon(cla):
    import numpy as np
    import cv2
    from function_moon import imgs_set_, click_pos_reg, click_pos_2
    from schedule import myQuest_play_add

    try:
        print("action_moon")


    except Exception as e:
        print(e)
        return 0

def loading(cla):
    import numpy as np
    import cv2
    from function_moon import imgs_set_, click_pos_reg, click_pos_2
    from schedule import myQuest_play_add

    try:
        print("loading")

        loaded = False
        loaded_count = 0

        loaded_counting = 0

        while loaded is False:
            loaded_count += 1
            if loaded_count > 7:
                loaded = True

            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\action\\loding_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(250, 920, 650, 1040, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("loding_1", imgs_)
                loaded_count = 0
                loaded_counting = 0
            else:
                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\action\\loding_2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(250, 920, 650, 1040, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("loding_2", imgs_)
                    loaded_count = 0
                    loaded_counting = 0
                else:
                    loaded_counting += 1
                    if loaded_counting > 3:
                        loaded = True
            time.sleep(0.5)



    except Exception as e:
        print(e)
        return 0


def moving(cla):
    import numpy as np
    import cv2
    from function_moon import imgs_set_, click_pos_reg, click_pos_2
    from schedule import myQuest_play_add, myQuest_play_check

    try:
        print("moving")

        moved = False
        moved_count = 0
        moved_count_msg = 0

        moved_counting = 0

        while moved is False:
            moved_count += 1
            moved_count_msg += 1
            if moved_count > 7:
                moved = True

            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\action\\move_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(250, 820, 650, 1040, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                if moved_count_msg < 4:
                    print("move_1", imgs_)
                elif moved_count_msg > 201:

                    # 스케쥴부터 불러오기
                    result_schedule = myQuest_play_check(v_.now_cla, "check")
                    print("result_schedule", result_schedule)
                    character_id = result_schedule[0][1]
                    result_schedule_ = result_schedule[0][2]

                    if result_schedule_ == "튜토육성":
                        click_pos_2(480, 555, cla)
                        time.sleep(0.1)

                    moved = True
                moved_count = 0
                moved_counting = 0

                # 이동하기
                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\confirm\\move.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(450, 500, 700, 700, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("move : move", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                else:
                    # 던전 입장
                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\confirm\\dun_in.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(500, 720, 580, 780, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("move : dun_in", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
            else:
                moved_counting += 1
                if moved_counting > 3:
                    moved = True

            time.sleep(0.5)



    except Exception as e:
        print(e)
        return 0

def let_is_maul_in(cla):
    import numpy as np
    import cv2
    from function_moon import imgs_set_, click_pos_reg, click_pos_2
    from dungeon_moon import dungeon_ing_check

    try:
        print("let_is_maul_in")

        in_maul = False
        in_maul_count = 0
        while in_maul is False:
            in_maul_count += 1
            if in_maul_count > 7:
                in_maul = True

            result_dun = dungeon_ing_check(cla, "go")

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

                for i in range(10):
                    result_out = out_check(cla)
                    if result_out == True:
                        break
                    time.sleep(1)

            else:
                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\maul\\chango.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(800, 970, 960, 1040, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    in_maul = True
                    time.sleep(0.1)

                else:
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



    except Exception as e:
        print(e)
        return 0


def clean_screen(cla):
    import numpy as np
    import cv2
    from function_moon import imgs_set_, click_pos_reg, click_pos_2
    from schedule import myQuest_play_check
    from dead import dead_die
    from massenger import line_to_me

    import random

    try:
        print("clean_screen")

        cleaned = False
        cleaned_count = 0
        while cleaned is False:
            cleaned_count += 1
            if cleaned_count > 7:
                cleaned = True


            # 절전모드 끄기

            # 비정상 블랙 스크린
            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\clean_screen\\moon_black_screen.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 0, 100, 100, cla, img, 0.9)
            if imgs_ is not None and imgs_ != False:
                v_.black_screen_count = 0
            else:
                v_.black_screen_count += 1
                if v_.black_screen_count == 5 or v_.black_screen_count == 50 or v_.black_screen_count > 150:
                    print("블랙스크린 200회 될 경우 알림감", v_.black_screen_count)
                if v_.black_screen_count > 500:
                    data = "달조 블랙스크린이다!!!"
                    v_.black_screen_count = 0
                    line_to_me(cla, data)

            # 각종 대답 오케이
            confirm_all(cla)
            time.sleep(0.1)

            # 의뢰퀘 완료 있을 경우 보상 받기
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

            # 타이틀 화면으로...클릭하고 재접하기
            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\clean_screen\\in_title_screen.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(370, 570, 580, 680, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                click_pos_reg(imgs_.x, imgs_.y, cla)
                line_to_me(cla, "재접속 화면 뜸")

            # 던전 입장 표시 끄기
            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\clean_screen\\cancle.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(220, 470, 700, 900, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                click_pos_reg(imgs_.x, imgs_.y, cla)

            # 죽었는지...
            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\dead\\boohwal_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(400, 870, 700, 950, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                result_schedule = myQuest_play_check(v_.now_cla, "check")
                print("confirm_all : result_schedule", result_schedule)
                character_id = result_schedule[0][1]
                sche = result_schedule[0][2]

                dead_die(cla, sche)

            # 각종 창 닫기
            have_x = False

            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\clean_screen\\x_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(30, 30, 960, 1030, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                have_x = True
            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\clean_screen\\x_2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(30, 30, 960, 1030, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                have_x = True

            if have_x == True:
                for i in range(10):
                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\clean_screen\\x_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(30, 30, 960, 1030, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                    else:
                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\clean_screen\\x_2.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(30, 30, 960, 1030, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                        else:
                            break
                    time.sleep(0.3)

            else:

                result_out = out_check(cla)
                if result_out == True:
                    #메뉴까지 닫기
                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\action\\menu_character_select.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(670, 470, 960, 670, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_2(935, 55, cla)
                        time.sleep(0.1)
                    cleaned = True
                else:
                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\clean_screen\\x_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(100, 100, 960, 1030, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.1)




    except Exception as e:
        print(e)
        return 0


def out_check(cla):
    import numpy as np
    import cv2
    from function_moon import imgs_set_, click_pos_reg, click_pos_2
    from schedule import myQuest_play_add

    try:
        print("out_check")

        out = False

        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\clean_screen\\out_talk.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(5, 970, 50, 1030, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("out_talk", imgs_)
            out = True
        else:
            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\clean_screen\\moon_black_screen.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 0, 110, 100, cla, img, 0.9)
            if imgs_ is not None and imgs_ != False:
                print("out_check : not moon_black_screen", imgs_)
                out = True
            else:
                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\clean_screen\\moon_black_screen2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 0, 110, 100, cla, img, 0.9)
                if imgs_ is not None and imgs_ != False:
                    print("out_check : not moon_black_screen2", imgs_)
                    out = True
                else:
                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\maul\\chango.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(800, 970, 960, 1040, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("out_check : chango", imgs_)
                        out = True

        return out
    except Exception as e:
        print(e)
        return 0


def menu_open(cla):
    import numpy as np
    import cv2
    from function_moon import imgs_set_, click_pos_reg, click_pos_2
    from schedule import myQuest_play_add

    try:
        print("menu_open")

        # 경험치 회복창 끄기
        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\dead\\exp_recovery_title.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(400, 320, 540, 380, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("menu_open : exp recovery title", imgs_)
            for i in range(5):
                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\clean_screen\\x_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(30, 300, 960, 1030, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("x_1", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                else:
                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\clean_screen\\x_2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(30, 300, 960, 1030, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("x_2", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                    else:
                        break
                time.sleep(0.3)


        opened = False
        opened_count = 0
        while opened is False:
            opened_count += 1
            if opened_count > 7:
                opened = True

            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\action\\menu_character_select.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(670, 470, 960, 670, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                opened = True
            else:
                clean_screen(cla)
                time.sleep(0.1)
                click_pos_2(920, 60, cla)
                for i in range(10):
                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\action\\menu_character_select.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(670, 470, 960, 670, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        break
                    time.sleep(0.5)


    except Exception as e:
        print(e)
        return 0

def bag_open(cla):
    import numpy as np
    import cv2
    from function_moon import imgs_set_, click_pos_reg, click_pos_2
    from schedule import myQuest_play_add

    try:

        print("bag_open")

        bag_opened = False
        bag_opened_count = 0
        while bag_opened is False:
            bag_opened_count += 1
            if bag_opened_count > 4:
                bag_opened = True
            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\repair\\boonhae_click.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(750, 920, 840, 970, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("bag")
                bag_opened = True
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


def attack_check_and_attack(cla):
    import numpy as np
    import cv2
    from function_moon import imgs_set_, click_pos_reg, click_pos_2
    from schedule import myQuest_play_add

    try:
        print("attack_check_and_attack")

        attack = False
        attack_count = 0
        while attack is False:
            attack_count += 1
            if attack_count > 7:
                attack = True

            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\check\\auto_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(890, 860, 960, 920, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                attack = True
            else:
                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\check\\auto_2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(890, 860, 960, 920, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    attack = True
                else:
                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\check\\auto_3.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(890, 860, 960, 920, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        attack = True

            if attack == False:

                clean_screen(cla)
                time.sleep(0.1)
                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\check\\ready_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(890, 860, 960, 920, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    attack = True
                else:
                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\check\\ready_2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(890, 860, 960, 920, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        attack = True
                    else:
                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\check\\ready_3.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(890, 860, 960, 920, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            attack = True
                        else:
                            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\check\\ready_4.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(890, 860, 960, 920, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                attack = True



    except Exception as e:
        print(e)
        return 0

def hunting_check(cla):
    import numpy as np
    import cv2
    from function_moon import imgs_set_, click_pos_reg, click_pos_2, text_check_get, in_number_check, int_put_
    from schedule import myQuest_play_add

    try:
        print("hunting_check")

        hunted = False

        # 우선 몬스터카드로 가자

        monster_in = False
        monster_in_count = 0
        while monster_in is False:
            monster_in_count += 1
            if monster_in_count > 7:
                monster_in = True
            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\title\\budy_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(5, 30, 150, 80, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                monster_in = True



                result_mine = mine_check(cla)

                print("result_mine", result_mine[0], result_mine[1])

                before_gold = result_mine[0]

                for i in range(20):

                    result_mine = mine_check(cla)

                    if before_gold != result_mine[0]:
                        print("before_gold vs now_gold", before_gold, result_mine[0])
                        hunted = True
                        break

                    time.sleep(1)


            else:
                menu_open(cla)
                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\repair\\menu_budy.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(670, 100, 960, 270, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("menu_monster", imgs_)

                    for i in range(10):
                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\title\\budy_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(5, 30, 150, 80, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            break
                        else:
                            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\repair\\menu_budy.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(670, 100, 960, 270, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                if i > 7:
                                    monster_in = True
                        time.sleep(0.5)

        for i in range(10):
            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\title\\budy_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(5, 30, 150, 80, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                click_pos_2(935, 55, cla)
            else:
                result_out = out_check(cla)
                if result_out == True:
                    break
                else:
                    clean_screen(cla)
            time.sleep(0.5)

        return hunted

    except Exception as e:
        print(e)
        return 0

def mine_check(cla):
    import numpy as np
    import cv2
    from function_moon import imgs_set_, click_pos_reg, click_pos_2, text_check_get, in_number_check, int_put_
    from schedule import myQuest_play_add

    try:
        print("mine_check")

        gold_ = 0
        dia_ = 0

        monster_in = False
        monster_in_count = 0
        while monster_in is False:
            monster_in_count += 1
            if monster_in_count > 7:
                monster_in = True
            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\title\\budy_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(5, 30, 150, 80, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                monster_in = True

                read_gold = text_check_get(635, 48, 700, 63, cla)
                print("read_gold", read_gold)

                digit_ready = in_number_check(read_gold)
                print("digit_ready", digit_ready)
                if digit_ready == True:
                    read_data_int = int(int_put_(read_gold))
                    print("read_data_int", read_data_int)
                    gold_ = read_data_int

                read_dia = text_check_get(784, 48, 835, 63, cla)
                print("read_dia", read_dia)

                digit_ready = in_number_check(read_dia)
                print("digit_ready", digit_ready)
                if digit_ready == True:
                    read_data_int = int(int_put_(read_dia))
                    print("read_data_int", read_data_int)
                    dia_ = read_data_int


            else:
                menu_open(cla)
                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\repair\\menu_budy.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(670, 100, 960, 270, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("menu_monster", imgs_)

                    for i in range(10):
                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\title\\budy_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(5, 30, 150, 80, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            break
                        else:
                            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\repair\\menu_budy.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(670, 100, 960, 270, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                if i > 7:
                                    monster_in = True
                        time.sleep(0.5)






        return gold_, dia_

    except Exception as e:
        print(e)
        return 0

def confirm_all(cla):
    import numpy as np
    import cv2
    from function_moon import imgs_set_, click_pos_reg, click_pos_2
    from schedule import myQuest_play_add, myQuest_play_check
    from get_item import get_items
    from repair_moon import repair_start
    from potion_moon import maul_potion_small_only

    try:
        print("confirm_all")

        # 버디알 오픈
        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\confirm\\budy_open.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(400, 980, 540, 1040, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("budy_open...", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)

        # 소환 오픈
        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\confirm\\sohwan_open.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(400, 980, 540, 1040, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("sohwan_open...", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)

        # 소환 후 확인
        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\confirm\\confirm_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(430, 980, 540, 1040, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("confirm_1", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
        else:
            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\repair\\sohwan_confirm.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(250, 980, 800, 1040, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                click_pos_reg(imgs_.x, imgs_.y, cla)

        # 이동하기
        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\confirm\\move.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(450, 500, 700, 700, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("move", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)

        # 던전 입장
        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\confirm\\dun_in.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(500, 720, 580, 780, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("dun_in", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
        # 던전 나가기
        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\confirm\\exit_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(300, 500, 700, 800, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("exit_1", imgs_)
            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\dead\\failed.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(300, 300, 700, 800, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\confirm\\exit_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(300, 500, 700, 800, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)

                    result_schedule = myQuest_play_check(v_.now_cla, "check")
                    print("confirm_all : result_schedule", result_schedule)
                    character_id = result_schedule[0][1]
                    sche = result_schedule[0][2]

                    if sche == "튜토육성":
                        get_items(cla)
                        repair_start(cla)
                        maul_potion_small_only(cla)

                        v_.tuto_dead += 1
                        if v_.tuto_dead > 1:
                            myQuest_play_add(cla, sche)
            else:
                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\confirm\\exit_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(300, 500, 700, 800, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)

        # 자동사냥 이동
        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\jadong\\map\\move_confirm.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(450, 560, 630, 630, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            click_pos_reg(imgs_.x, imgs_.y, cla)


    except Exception as e:
        print(e)
        return 0


def channel_move(cla):
    import numpy as np
    import cv2
    from function_moon import imgs_set_, click_pos_reg, click_pos_2, drag_pos
    from schedule import myQuest_play_add

    try:
        print("channel_move")

        channel_in = False
        channel_in_count = 0
        while channel_in is False:
            channel_in_count += 1
            if channel_in_count > 5:
                channel_in = True

            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\action\\channel_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(420, 350, 520, 400, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("channel in")

                exist = False

                # 원활
                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\action\\channel_wonhwal.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(380, 420, 430, 660, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("원활", imgs_)
                    click_pos_reg(imgs_.x + 200, imgs_.y, cla)
                    exist = True
                else:
                    # 보통
                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\action\\channel_botong.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(380, 420, 430, 660, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("보통", imgs_)
                        click_pos_reg(imgs_.x + 200, imgs_.y, cla)
                        exist = True
                time.sleep(0.1)

                if exist == True:
                    channel_in = True
                    for i in range(10):
                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\action\\channel_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(420, 350, 520, 400, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_2(630, 375, cla)
                        else:
                            break
                        time.sleep(0.5)
                else:
                    drag_pos(450, 650, 450, 450, cla)
                    time.sleep(0.5)


            else:
                result_out = out_check(cla)
                if result_out == False:
                    clean_screen(cla)
                    time.sleep(0.5)
                click_pos_2(25, 140, cla)
                for i in range(10):
                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\action\\channel_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(420, 350, 520, 400, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        break
                    time.sleep(0.3)


    except Exception as e:
        print(e)
        return 0