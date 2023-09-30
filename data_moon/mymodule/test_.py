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

    from get_item import get_event
    from repair_moon import budy_sohwan, hyungsang_sohwan, my_stat_up
    from potion_moon import maul_potion_small_only, maul_potion_full, quick_slot_check
    from jadong_moon import map_open_check
    from character_select_and_game_start import game_start_screen, character_change
    from soojib_boonhae_moon import soojib_boonhae_start, soojib_setting
    from auction_moon import price_check


    print("tst")
    cla = "one"

    plus = 0

    if cla == "two":
        plus = 960
    if cla == "three":
        plus = 960 * 2
    if cla == "four":
        plus = 960 * 3

    # quick_slot_check(cla)

    price_check(cla)
    # for i in range(10):
    #     full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\auction\\price\\one_price\\" + str(
    #         i) + ".PNG"
    #     img_array = np.fromfile(full_path, np.uint8)
    #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    #     imgs_ = imgs_set_(362, 475, 370, 500, cla, img, 0.8)
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