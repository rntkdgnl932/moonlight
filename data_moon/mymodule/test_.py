import sys
import os
import time
import requests

sys.path.append('C:/my_games/moonlight/data_moon/mymodule')

import variable as v_

def go_test():
    import numpy as np
    import cv2
    import pyautogui
    import random

    from function_moon import imgs_set_, click_pos_reg, click_pos_2, drag_pos_reg, drag_pos, drag_pos_Press, mouse_move_cpp, mouse_move_adu_drag

    from action_moon import menu_open, clean_screen, out_check, attack_check_and_attack

    from get_item import get_event, get_event_sub
    from repair_moon import budy_sohwan, hyungsang_sohwan, my_stat_up
    from potion_moon import maul_potion_small_only, maul_potion_full, quick_slot_check
    from jadong_moon import map_open_check, boss_check
    from character_select_and_game_start import game_start_screen, character_change
    from soojib_boonhae_moon import soojib_boonhae_start, soojib_setting, soojib_start
    from auction_moon import price_check, auction_start, how_many
    from request_moon import get_my_request

    print("tst")
    cla = "one"

    plus = 0

    if cla == "two":
        plus = 960
    if cla == "three":
        plus = 960 * 2
    if cla == "four":
        plus = 960 * 3

    # get_my_request(cla, "의뢰_바란")

    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\request\\re_confirm.PNG"
    img_array = np.fromfile(full_path, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    imgs_ = imgs_set_(800, 950, 950, 1040, cla, img, 0.9)
    if imgs_ is not None and imgs_ != False:
        print("re_confirm tuto", imgs_)
    else:
        print("수락 없")
    # full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\tuto\\tuto_check1_2.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(900, 90, 950, 150, cla, img, 0.9)
    # if imgs_ is not None and imgs_ != False:
    #     print("tuto_check1_2 tuto", imgs_)

    # file_path = "C:\\my_games\\moonlight\\data_moon\\imgs\\auction\\price\\one_price\\number.txt"
    #
    # with open(file_path, "r", encoding='utf-8-sig') as file:
    #     read_num = file.read().splitlines()
    #     print(len(read_num))


    #
    #     full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\get_items\\seven_four.PNG"
    #     img_array = np.fromfile(full_path, np.uint8)
    #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    #     imgs_ = imgs_set_(220, 450, 900, 520, cla, img, 0.97)
    #     if imgs_ is not None and imgs_ != False:
    #         print("seven_four", imgs_)
    #
    #     full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\get_items\\seven_four2.PNG"
    #     img_array = np.fromfile(full_path, np.uint8)
    #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    #     imgs_ = imgs_set_(220, 450, 900, 520, cla, img, 0.97)
    #     if imgs_ is not None and imgs_ != False:
    #         print("seven_four2", imgs_)

    # full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\dead\\exp_recovery_title.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(400, 320, 540, 380, cla, img, 0.8)
    # if imgs_ is not None and imgs_ != False:
    #     print("exp recovery title : click_pos_2(470, 710, cla)", imgs_)
    # else:
    #     print("ntmckkkckkdkdk")

    # how_many(cla)

    # for i in range(10):
    #     full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\auction\\num_click\\" + str(
    #         i) + ".PNG"
    #     img_array = np.fromfile(full_path, np.uint8)
    #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    #     imgs_ = imgs_set_(500, 480, 750, 630, cla, img, 0.95)
    #     if imgs_ is not None and imgs_ != False:
    #         print("숫자 : ", i, imgs_)
    #         click_pos_reg(imgs_.x, imgs_.y, cla)
    #         time.sleep(0.1)

    #
    # file_path = "C:\\my_games\\moonlight\\data_moon\\imgs\\auction\\price\\one_price\\number.txt"
    #
    # with open(file_path, "r", encoding='utf-8-sig') as file:
    #     read_num = file.read().splitlines()
    #     print("read_num", read_num)
    #     for i in range(len(read_num)):
    #         print(read_num[i])
    #         print(read_num[i][0])
    #         print(read_num[i][1])
    #
    # full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\auction\\price\\only_price\\1000.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(580, 460, 700, 490, cla, img, 0.8)
    # if imgs_ is not None and imgs_ != False:
    #     print("1000", imgs_)
    #
    # full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\auction\\price\\only_price\\gijoon.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(580, 460, 700, 490, cla, img, 0.8)
    # if imgs_ is not None and imgs_ != False:
    #     print("gijoon", imgs_)
    #     x_reg = imgs_.x
    #
    # for i in range(10):
    #     full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\auction\\howmany\\" + str(
    #         i) + ".PNG"
    #     img_array = np.fromfile(full_path, np.uint8)
    #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    #     imgs_ = imgs_set_(450, 535, 488, 565, cla, img, 0.8)
    #     if imgs_ is not None and imgs_ != False:
    #         result_num = str(i)
    #         print("숫자 : ", result_num, imgs_)

    # for i in range(10):
    #     full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\auction\\howmany\\" + str(
    #         i) + ".PNG"
    #     img_array = np.fromfile(full_path, np.uint8)
    #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    #     imgs_ = imgs_set_(450, 585, 488, 625, cla, img, 0.8)
    #     if imgs_ is not None and imgs_ != False:
    #         result_num = str(i)
    #         print("숫자 : ", result_num, imgs_)


    # full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\auction\\market_list_title.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(430, 300, 525, 365, cla, img, 0.8)
    # if imgs_ is not None and imgs_ != False:
    #     print("good", imgs_)
    # else:
    #     print("notnornotnotnot")



    # for i in range(4):
    #     pyautogui.moveTo(600, 660 , 0.2)
    #     pyautogui.dragTo(600, 500 , 0.5)
    #     time.sleep(0.3)

    # full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\get_items\\bosang_get_2.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(650, 450, 900, 770, cla, img, 0.87)
    # if imgs_ is not None and imgs_ != False:

    # full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\get_items\\bosang_get_2.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(650, 450, 900, 770, cla, img, 0.87)
    # if imgs_ is not None and imgs_ != False:
    #     print("bosang_get_2", imgs_)
    #
    # full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\get_items\\bosang_get_3.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(650, 450, 900, 770, cla, img, 0.93)
    # if imgs_ is not None and imgs_ != False:
    #     print("bosang_get_3", imgs_)

    # full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\get_items\\chulsuk_checked.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # for i in pyautogui.locateAllOnScreen(img, region=(310 + plus, 440, 480, 280), confidence=0.8):
    #     last_x = i.left
    #     last_y = i.top
    #     print("last_x", last_x)
    #     print("last_y", last_y)
    # if last_x != 0:
    #     print("얏호")