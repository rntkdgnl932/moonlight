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
    from schedule import myQuest_play_add

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

def clean_screen(cla):
    import numpy as np
    import cv2
    from function_moon import imgs_set_, click_pos_reg, click_pos_2
    from schedule import myQuest_play_check
    from dead import dead_die
    from massenger import line_to_me

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
                print("블랙스크린 100회 될 경우 알림감", v_.black_screen_count)
                if v_.black_screen_count > 100:
                    data = "달조 블랙스크린이다!!!"
                    v_.black_screen_count = 0
                    line_to_me(cla, data)


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
            imgs_ = imgs_set_(570, 870, 700, 950, cla, img, 0.8)
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
