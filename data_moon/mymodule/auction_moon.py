import sys
import os
import time
import requests

sys.path.append('C:/my_games/moonlight/data_moon/mymodule')

import variable as v_


def auction_start(cla):
    import numpy as np
    import cv2

    from function_moon import imgs_set_

    from action_moon import out_check


    try:
        print("auction start")

    except Exception as e:
        print(e)


def price_check(cla):
    import numpy as np
    import cv2

    from function_moon import imgs_set_

    from action_moon import out_check

    try:
        print("auction price check")

        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\auction\\market_list_title.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(430, 300, 525, 365, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("good", imgs_)

            one_price = False

            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\auction\\price\\one_price1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(270, 465, 330, 500, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("one price1", imgs_)
                one_price = True

            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\auction\\price\\one_price2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(270, 465, 330, 500, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("one price2", imgs_)
                one_price = True

            num_1000 = False
            num_point = False


            if one_price == True:
                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\auction\\price\\one_price\\1000.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(340, 485, 400, 500, cla, img, 0.9)
                if imgs_ is not None and imgs_ != False:
                    print("1000", imgs_)
                    num_1000 = True
                    num_1000_x = imgs_.x
                    #356, 492

                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\auction\\price\\one_price\\point.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(340, 485, 400, 500, cla, img, 0.9)
                if imgs_ is not None and imgs_ != False:
                    print("point", imgs_)
                    num_point = True
                    num_point_x = imgs_.x

                result_price = ""

                for n in range(6):
                    jari = n + 1
                    x1 = 344 + (n * 6)
                    x2 = 356 + (n * 6)

                    for i in range(10):
                        result_num = "none"
                        if num_1000 == False and num_point == False:
                            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\auction\\price\\one_price\\" + str(i) + ".PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(x1, 475, x2, 500, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                result_num = str(i)
                                print(jari, "번쩨 숫자 : ", result_num, imgs_)
                                # 1000 (o)
                                # 351 // 360, 366

                                #1000(o)
                                # 351 // 357, 363 // 372
                        elif num_1000 == True:
                            if num_1000_x < 359:
                                if jari == 1:
                                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\auction\\price\\one_price\\" + str(
                                        i) + ".PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(x1, 475, x2, 500, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        result_num = str(i)
                                        print(jari, "번쩨 숫자 : ", result_num, imgs_)
                                else:
                                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\auction\\price\\one_price\\" + str(
                                        i) + ".PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(x1 + 3, 475, x2 + 3, 500, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        result_num = str(i)
                                        print(jari, "번쩨 숫자 : ", result_num, imgs_)
                            elif 359 < num_1000_x < 365:
                                if jari < 3:
                                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\auction\\price\\one_price\\" + str(
                                        i) + ".PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(x1, 475, x2, 500, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        result_num = str(i)
                                        print(jari, "번쩨 숫자 : ", result_num, imgs_)
                                else:
                                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\auction\\price\\one_price\\" + str(
                                        i) + ".PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(x1 + 3, 475, x2 + 3, 500, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        result_num = str(i)
                                        print(jari, "번쩨 숫자 : ", result_num, imgs_)
                        elif num_point == True and num_1000 == False:
                            if num_point_x < 359:
                                if jari == 1:
                                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\auction\\price\\one_price\\" + str(
                                        i) + ".PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(x1, 475, x2, 500, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        result_num = str(i)
                                        print(jari, "번쩨 숫자 : ", result_num, imgs_)
                                else:
                                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\auction\\price\\one_price\\" + str(
                                        i) + ".PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(x1 + 3, 475, x2 + 3, 500, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        result_num = str(i)
                                        print(jari, "번쩨 숫자 : ", result_num, imgs_)
                            elif 359 < num_point_x < 365:
                                if jari < 3:
                                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\auction\\price\\one_price\\" + str(
                                        i) + ".PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(x1, 475, x2, 500, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        result_num = str(i)
                                        print(jari, "번쩨 숫자 : ", result_num, imgs_)

                                else:
                                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\auction\\price\\one_price\\" + str(
                                        i) + ".PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(x1 + 3, 475, x2 + 3, 500, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        result_num = str(i)
                                        print(jari, "번쩨 숫자 : ", result_num, imgs_)

                            if jari == 2:
                                print("point write")
                                result_price += "."
                        if result_num != "none":
                            result_price += result_num
                            print("result_price", result_price)
                            break
            print("last price =>", result_price)
        else:
            print("notnornotnotnot")

    except Exception as e:
        print(e)