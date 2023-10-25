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

    from function_moon import imgs_set_, click_pos_reg, click_pos_2, drag_pos_reg, drag_pos, drag_pos_Press, mouse_move_cpp, mouse_move_adu_drag, text_check_get

    from action_moon import menu_open, clean_screen, out_check, attack_check_and_attack, hunting_check, mine_check

    from get_item import get_event, get_event_sub, get_sangjum_sohwan
    from repair_moon import budy_sohwan, hyungsang_sohwan, my_stat_up
    from potion_moon import maul_potion_small_only, maul_potion_full, quick_slot_check,maul_potion_dead_only, exist_buf
    from jadong_moon import map_open_check, boss_check
    from character_select_and_game_start import game_start_screen, character_change
    from soojib_boonhae_moon import soojib_boonhae_start, soojib_setting, soojib_start
    from auction_moon import price_check, auction_start, how_many
    from request_moon import get_my_request
    from chango_moon import dajoong_click, chango_jangbi_in_start, chango_auction_out_start, take_off, chango_jaelyo_in_start, chango_restart, chango_auction_in_start, chango_jangbi_out_start
    from property_moon import my_property_upload
    from guild_moon import guild_choolsuk
    from tuto_moon import quest_click

    print("tst")
    cla = "two"

    plus = 0


    if cla == "one":
        plus = 0
    elif cla == "two":
        plus = 960
    elif cla == "three":
        plus = 960 * 2
    elif cla == "four":
        plus = 960 * 3

    time.sleep(0.8)
    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\chango\\dajoong_select_left.PNG"
    img_array = np.fromfile(full_path, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    imgs_ = imgs_set_(0, 970, 120, 1030, cla, img, 0.8)
    if imgs_ is not None and imgs_ != False:
        click_pos_reg(imgs_.x, imgs_.y, cla)
        time.sleep(0.1)

    # full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\chango\\jaelyo_in\\jungsoo_jogagsa_skill.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(630, 120, 960, 900, cla, img, 0.8)
    # if imgs_ is not None and imgs_ != False:
    #     print("jungsoo_gongyong_skill", imgs_)

    # full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\chango\\jaelyo_in\\jungsoo_jogagsa_skill.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(0, 120, 330, 900, cla, img, 0.8)
    # if imgs_ is not None and imgs_ != False:
    #     print("jungsoo_jogagsa_skill", imgs_)
    #
    # full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\chango\\jaelyo_in\\jungsoo_gongyong_skill.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(0, 120, 330, 900, cla, img, 0.8)
    # if imgs_ is not None and imgs_ != False:
    #     print("jungsoo_gongyong_skill", imgs_)
    #
    # full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\chango\\jaelyo_in\\jungsoo_junsa_skill.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(0, 120, 330, 900, cla, img, 0.8)
    # if imgs_ is not None and imgs_ != False:
    #     print("jungsoo_junsa_skill", imgs_)
    #
    # full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\chango\\jaelyo_in\\jungsoo_mabubsa_skill.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(0, 120, 330, 900, cla, img, 0.8)
    # if imgs_ is not None and imgs_ != False:
    #     print("jungsoo_mabubsa_skill", imgs_)

    # full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\chango\\jaelyo_in\\jungsoo_goongsoo_skill.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(0, 120, 330, 900, cla, img, 0.7)
    # if imgs_ is not None and imgs_ != False:
    #     print("jungsoo_goongsoo_skill", imgs_)

    # full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\get_items\\chulsuk_checked.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # for i in pyautogui.locateAllOnScreen(img, region=(310 + plus, 440, 480, 280),
    #                                      confidence=0.75):
    #     last_x = i.left
    #     last_y = i.top
    #     print("last_x", last_x)
    #     print("last_y", last_y)
    # mine_check(cla)
    # get_my_request(cla, "의뢰_바란")

    # chango_action(cla, "jangbi_out")

    # chango_action(cla, "jaelyo_in")

    # read_dia = text_check_get(783, 48, 835, 63, cla)
    # print("read_dia 783", read_dia)
    #
    # read_dia = text_check_get(784, 48, 835, 63, cla)
    # print("read_dia 784", read_dia)
    #
    # read_dia = text_check_get(785, 48, 835, 63, cla)
    # print("read_dia 785", read_dia)


    # ran_item = []
    #
    # file_path = "C:\\my_games\\moonlight\\data_moon\\imgs\\auction\\list\\list.txt"
    #
    # with open(file_path, "r", encoding='utf-8-sig') as file:
    #     read_list = file.read().splitlines()
    #     print("read_list len", len(read_list))
    #
    #     for i in range(len(read_list)):
    #         full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\auction\\list\\" + read_list[i] + ".PNG"
    #         img_array = np.fromfile(full_path, np.uint8)
    #         img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    #         imgs_ = imgs_set_(610, 160, 960, 1000, cla, img, 0.8)
    #         if imgs_ is not None and imgs_ != False:
    #             print(i, read_list[i], imgs_)
    #             ran_item.append(i)
    #
    # print("result", ran_item)
    # print("len ran_item", len(ran_item))
    #
    # if len(ran_item) < 5:
    #     sell_many = len(ran_item)
    # else:
    #     sell_many = 5
    #
    # sell_list = random.sample(ran_item, sell_many)
    #
    # print("sell_list", sell_list)
    #
    # print("sell_list[0]", sell_list[0])
    #
    # for ran_list in range(sell_many):
    #
    #     for i in range(len(read_list)):
    #         full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\auction\\list\\" + read_list[i] + ".PNG"
    #         img_array = np.fromfile(full_path, np.uint8)
    #         img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    #         imgs_ = imgs_set_(610, 160, 960, 1000, cla, img, 0.8)
    #         if imgs_ is not None and imgs_ != False:
    #             if sell_list[ran_list] == i:
    #                 print(i, read_list[i], imgs_)



    # full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\chango\\item_lock_on.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(x_reg - 75, y_reg - 30, x_reg, y_reg + 30, cla, img, 0.8)
    # if imgs_ is not None and imgs_ != False:
    #     print("item_lock_on", imgs_)
    #     lock_exist = True
    #     time.sleep(0.1)
    # else:
    #     full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\chango\\item_lock_on2.PNG"
    #     img_array = np.fromfile(full_path, np.uint8)
    #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    #     imgs_ = imgs_set_(x_reg - 75, y_reg - 30, x_reg, y_reg + 30, cla, img, 0.8)
    #     if imgs_ is not None and imgs_ != False:
    #         print("item_lock_on2", imgs_)
    #         lock_exist = True
    #         time.sleep(0.1)
    #     else:
    #         full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\chango\\item_lock_on3.PNG"
    #         img_array = np.fromfile(full_path, np.uint8)
    #         img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    #         imgs_ = imgs_set_(x_reg - 75, y_reg - 30, x_reg, y_reg + 30, cla, img, 0.8)
    #         if imgs_ is not None and imgs_ != False:
    #             print("item_lock_on3", imgs_)
    #             lock_exist = True
    #             time.sleep(0.1)
    #
    # full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\chango\\e2.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(625, 115, 960, 900, cla, img, 0.8)
    # if imgs_ is not None and imgs_ != False:
    #     print("e2", imgs_)
    #     x_reg = imgs_.x - plus
    #     y_reg = imgs_.y
    #     e_exist = True
    #     time.sleep(0.1)
    # full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\chango\\e.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(625, 115, 960, 900, cla, img, 0.8)
    # if imgs_ is not None and imgs_ != False:
    #     print("e", imgs_)
    #     x_reg = imgs_.x - plus
    #     y_reg = imgs_.y
    #     e_exist = True
    #     time.sleep(0.1)
    # full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\chango\\e3.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(625, 115, 960, 900, cla, img, 0.8)
    # if imgs_ is not None and imgs_ != False:
    #     print("e3", imgs_)
    #     x_reg = imgs_.x - plus
    #     y_reg = imgs_.y
    #     e_exist = True
    #     time.sleep(0.1)
    # full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\chango\\e4.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(625, 115, 960, 900, cla, img, 0.8)
    # if imgs_ is not None and imgs_ != False:
    #     print("e4", imgs_)
    #     x_reg = imgs_.x - plus
    #     y_reg = imgs_.y
    #     e_exist = True
    #     time.sleep(0.1)

    # last_x = 0
    # last_y = 0
    #
    # full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\chango\\in\\segongsuk.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # for i in pyautogui.locateAllOnScreen(img, region=(625 + plus, 115, 960 - 625, 900 - 115), confidence=0.8):
    #     last_x = i.left
    #     last_y = i.top
    #     click_pos_reg(last_x, last_y, cla)
    #     time.sleep(0.1)
    #     print("last_x", last_x)
    #     print("last_y", last_y)
    # if last_x != 0:
    #     print("얏호")
    #
    # full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\chango\\in\\segongsuk.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(625, 115, 960, 900, cla, img, 0.8)
    # if imgs_ is not None and imgs_ != False:
    #     print("segongsuk", imgs_)
    # else:
    #     print("segongsuk 없??????")

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