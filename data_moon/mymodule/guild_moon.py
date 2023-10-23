import sys
import os
import time
import requests

sys.path.append('C:/my_games/moonlight/data_moon/mymodule')

import variable as v_

def guild_start(cla):
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

        print("guild_start")

        # chapter 1
        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\dead\\boohwal_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(400, 870, 700, 950, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("boohwal_1...", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)

    except Exception as e:
        print(e)

def guild_choolsuk(cla):
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

        print("guild_choolsuk")

        guild_in = False
        guild_in_count = 0
        while guild_in is False:
            guild_in_count += 1
            if guild_in_count > 5:
                guild_in = True
            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\title\\guild_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(5, 30, 100, 100, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("guild_title...", imgs_)
                guild_in = True
                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\guild\\max.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(260, 890, 320, 950, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("max...", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.5)
                    click_pos_2(250, 1000, cla)
                    time.sleep(0.5)
                    click_pos_2(520, 100, cla)
                    time.sleep(0.1)
                    click_pos_2(520, 100, cla)
                    time.sleep(0.5)
                    for i in range(10):
                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\guild\\bosang_get.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(800, 940, 900, 1000, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            # click_pos_reg(imgs_.x, imgs_.y, cla)
                            click_pos_2(900, 965, cla)
                        else:
                            break
                        time.sleep(0.5)

                click_pos_2(935, 55, cla)



            else:
                menu_open(cla)
                for i in range(10):
                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\guild\\menu_guild.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(670, 320, 960, 500, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("menu_guild...", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        for z in range(10):
                            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\title\\guild_title.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(5, 30, 100, 100, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("guild_title...", imgs_)
                                break
                            time.sleep(0.5)
                        break
                    time.sleep(0.5)




    except Exception as e:
        print(e)