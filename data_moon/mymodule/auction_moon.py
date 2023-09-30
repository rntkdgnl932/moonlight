import sys
import os
import time
import requests

sys.path.append('C:/my_games/moonlight/data_moon/mymodule')

import variable as v_


def auction_start(cla):
    import numpy as np
    import cv2

    from function_moon import imgs_set_, click_pos_reg, click_pos_2

    from action_moon import out_check, menu_open


    try:
        print("auction start")

        auction_ready = False
        auction_ready_count = 0
        while auction_ready is False:
            auction_ready_count += 1
            if auction_ready_count > 7:
                auction_ready = True
            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\title\\auction_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(5, 30, 150, 80, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("auction_title", imgs_)

                auction_ready = True

                auction_end = False

                # 거래 직전까지 진입
                for i in range(10):
                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\auction\\auction_in.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(820, 125, 890, 180, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        break
                    else:
                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\auction\\sell_click.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(60, 80, 500, 130, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.4)
                # 판매대금 받기
                for i in range(10):
                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\auction\\sell_complete_click.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(440, 160, 620, 970, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                    else:
                        break
                    time.sleep(0.4)
                # 물품 올리기
                file_path = "C:\\my_games\\moonlight\\data_moon\\imgs\\auction\\list\\list.txt"

                with open(file_path, "r", encoding='utf-8-sig') as file:
                    read_list = file.read().splitlines()
                    # print("read_num", read_num)
                    for i in range(len(read_list)):
                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\auction\\list\\" + read_list[i] + ".PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(610, 160, 960, 1000, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print(i, read_list[i], imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            for k in range(10):
                                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\auction\\registration_auction_title.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(440, 315, 555, 365, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print("registration_auction_title", imgs_)
                                    break
                                else:
                                    # 더이상...end
                                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\auction\\anymore_auction.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(440, 130, 570, 170, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        print("물품 다 올렸다...")
                                        auction_end = True
                                        break
                                time.sleep(0.4)

                            if auction_end == False:
                                # 판매수량 보이면 판매수량 파악하기
                                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\auction\\sell_quantity.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(200, 525, 280, 570, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print("sell_quantity", imgs_)
                                    click_pos_2(470, 550, cla)
                                    time.sleep(0.1)
                                    click_pos_2(470, 550, cla)
                                    time.sleep(0.2)
                                    # max 누르기
                                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\auction\\num_click\\max.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(650, 550, 750, 650, cla, img, 0.95)
                                    if imgs_ is not None and imgs_ != False:
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                        time.sleep(0.1)
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                        time.sleep(0.2)

                                    # 수량 파악 하기
                                    result_many = how_many(cla)
                                else:
                                    result_many = "1"

                                # 등록현황 누르고 개별 가격 파악하기
                                for n in range(10):
                                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\auction\\market_list_title.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(430, 300, 525, 365, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        print("market_list_title", imgs_)
                                        result_price = price_check(cla)
                                        break
                                    else:
                                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\auction\\market_list_click.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(650, 380, 720, 420, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            click_pos_reg(imgs_.x, imgs_.y, cla)
                                    time.sleep(0.5)
                                # 최종가격  result_many * result_price
                                this_price_ready = float(result_many) * float(result_price)
                                print("this_price_ready", this_price_ready)
                                this_price = int(this_price_ready)
                                print("this_price", this_price)

                                # 가격이 10원 이하면 취소 누르기
                                if this_price > 10:

                                    click_pos_2(370, 610, cla)
                                    time.sleep(0.1)
                                    click_pos_2(370, 610, cla)
                                    time.sleep(0.1)

                                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\auction\\num_click\\ac.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(500, 480, 750, 630, cla, img, 0.95)
                                    if imgs_ is not None and imgs_ != False:
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                        time.sleep(0.1)
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                        time.sleep(0.1)

                                    str_price = str(this_price)
                                    for n in range(len(str_price)):
                                        print(n, str_price[n])
                                        if str_price[n] == "0":
                                            click_pos_2(620, 610, cla)
                                        elif str_price[n] == "1":
                                            click_pos_2(545, 510, cla)
                                        elif str_price[n] == "2":
                                            click_pos_2(620, 510, cla)
                                        elif str_price[n] == "3":
                                            click_pos_2(700, 510, cla)
                                        elif str_price[n] == "4":
                                            click_pos_2(545, 545, cla)
                                        elif str_price[n] == "5":
                                            click_pos_2(620, 545, cla)
                                        elif str_price[n] == "6":
                                            click_pos_2(700, 545, cla)
                                        elif str_price[n] == "7":
                                            click_pos_2(545, 575, cla)
                                        elif str_price[n] == "8":
                                            click_pos_2(620, 575, cla)
                                        elif str_price[n] == "9":
                                            click_pos_2(700, 575, cla)
                                        time.sleep(0.3)


                                    # 최종 누른것과 계산한 결과 같은지 파악하기
                                    result_equal = last_price_equal(cla)
                                    if str_price == result_equal:
                                        for j in range(10):
                                            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\auction\\auction_confirm_4.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(500, 630, 590, 680, cla, img, 0.8)
                                            if imgs_ is not None and imgs_ != False:
                                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                                time.sleep(0.1)
                                                break
                                            else:
                                                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\auction\\auction_confirm_2.PNG"
                                                img_array = np.fromfile(full_path, np.uint8)
                                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                imgs_ = imgs_set_(525, 710, 620, 750, cla, img, 0.8)
                                                if imgs_ is not None and imgs_ != False:
                                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                            time.sleep(0.5)



                                    else:
                                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\auction\\auction_cancle.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(370, 710, 440, 750, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            click_pos_reg(imgs_.x, imgs_.y, cla)
                                    time.sleep(0.1)

                                    for k in range(10):
                                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\auction\\registration_auction_title.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(440, 315, 555, 365, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\auction\\auction_cancle.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(370, 710, 440, 750, cla, img, 0.8)
                                            if imgs_ is not None and imgs_ != False:
                                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\auction\\auction_confirm_4.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(500, 630, 590, 680, cla, img, 0.8)
                                            if imgs_ is not None and imgs_ != False:
                                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                            time.sleep(0.1)
                                        else:
                                            break
                                        time.sleep(0.4)
                                else:
                                    print("10원 이하다 취소 누르자")
                                    for k in range(10):
                                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\auction\\registration_auction_title.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(440, 315, 555, 365, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\auction\\auction_cancle.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(370, 710, 440, 750, cla, img, 0.8)
                                            if imgs_ is not None and imgs_ != False:
                                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                        else:
                                            break
                                        time.sleep(0.4)
                            else:
                                print("끝!")
                                break


                # 더이상 물품 올릴수 없습니다. 또는 판매 리스트 끝나면 거래소 종료하기
            else:
                menu_open(cla)
                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\auction\\menu_auction.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(670, 160, 960, 330, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("menu_auction", imgs_)

                    for i in range(10):
                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\title\\auction_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(5, 30, 150, 80, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            break
                        else:
                            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\auction\\menu_auction.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(670, 160, 960, 330, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.5)


        for i in range(10):

            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\auction\\auction_confirm_4.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(500, 630, 590, 680, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                click_pos_reg(imgs_.x, imgs_.y, cla)
                time.sleep(0.1)

            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\auction\\auction_confirm_3.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(490, 580, 590, 630, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:

                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\auction\\exit_cancle.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(360, 580, 460, 620, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.1)
                    for k in range(7):
                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\auction\\sell_complete_click.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(440, 160, 620, 970, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                        else:
                            break
                        time.sleep(0.4)

            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\auction\\auction_confirm_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(445, 705, 525, 750, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                click_pos_reg(imgs_.x, imgs_.y, cla)
                time.sleep(0.1)
            else:
                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\auction\\auction_cancle.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(370, 710, 440, 750, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.1)
                else:
                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\title\\auction_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(5, 30, 150, 80, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_2(935, 55, cla)
                        for k in range(10):
                            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\auction\\auction_confirm_3.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(490, 580, 590, 630, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                break
                            else:
                                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\title\\auction_title.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(5, 30, 150, 80, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print("아직 못 나감...")
                                else:
                                    break
                            time.sleep(0.1)
                    else:
                        break
            time.sleep(0.1)





    except Exception as e:
        print(e)


def price_check(cla):
    import numpy as np
    import cv2

    from function_moon import imgs_set_, click_pos_reg, mouse_move_cpp

    from action_moon import out_check

    try:
        print("auction price check")

        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\auction\\market_list_title.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(430, 300, 525, 365, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("good", imgs_)


            for i in range(3):
                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\auction\\price\\up_click.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(705, 365, 750, 410, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    break
                else:
                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\auction\\price\\down_click.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(705, 365, 750, 410, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.1)
                        mouse_move_cpp(630, 730, cla)
                        time.sleep(0.1)
                time.sleep(0.5)

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
                imgs_ = imgs_set_(340, 485, 400, 500, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("1000", imgs_)
                    num_1000 = True
                    num_1000_x = imgs_.x
                    #356, 492
                else:
                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\auction\\price\\one_price\\1000_2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(340, 485, 400, 500, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("1000_2", imgs_)
                        num_1000 = True
                        num_1000_x = imgs_.x
                        # 356, 492

                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\auction\\price\\one_price\\point.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(340, 485, 400, 500, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("point", imgs_)
                    num_point = True
                    num_point_x = imgs_.x
                else:
                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\auction\\price\\one_price\\point2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(340, 485, 400, 500, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("point2", imgs_)
                        num_point = True
                        num_point_x = imgs_.x
                    else:
                        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\auction\\price\\one_price\\point3.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(340, 485, 400, 500, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            print("point3", imgs_)
                            num_point = True
                            num_point_x = imgs_.x
                        else:
                            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\auction\\price\\one_price\\point4.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(340, 485, 400, 500, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                print("point4", imgs_)
                                num_point = True
                                num_point_x = imgs_.x

                result_price = ""

                for n in range(6):
                    jari = n + 1
                    x1 = 344 + (n * 6)
                    x2 = 356 + (n * 6)
                    if num_1000 == True and num_point == True and x2 > num_point_x:
                        break


                    for i in range(17):
                        result_num = "none"
                        if num_1000 == False and num_point == False:
                            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\auction\\price\\one_price\\" + str(i) + ".PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(x1, 475, x2, 500, cla, img, 0.85)
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
                                        print(jari, "번쩨 숫자 : ", x1, x2,  result_num, imgs_)
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
                                # 362, 두자리 정수
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


                            elif 364 < num_point_x < 371:
                                # 367, 세자리 정수
                                if jari < 4:
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



                        if result_num != "none":

                            file_path = "C:\\my_games\\moonlight\\data_moon\\imgs\\auction\\price\\one_price\\number.txt"

                            with open(file_path, "r", encoding='utf-8-sig') as file:
                                read_num = file.read().splitlines()
                                # print("read_num", read_num)
                                for r in range(len(read_num)):
                                    read_num_ready = read_num[r].split(":")
                                    if read_num_ready[0] == result_num:
                                        result_num = read_num_ready[1]
                                        break
                            print("result_num", result_num)

                            result_price += result_num

                            if num_point == True and num_1000 == False:
                                if num_point_x < 359:
                                    if jari == 1:
                                        print("point write 1")
                                        result_price += "."
                                elif 359 < num_point_x < 365:
                                    if jari == 2:
                                        print("point write 2")
                                        result_price += "."

                                elif 364 < num_point_x < 371:
                                    if jari == 3:
                                        print("point write 3")
                                        result_price += "."

                            print("result_price...", result_price)
                            break
            else:
                # 개당가격 x

                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\auction\\price\\only_price\\gijoon.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(580, 450, 700, 500, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("gijoon", imgs_)
                    x_reg = imgs_.x + 9
                else:
                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\auction\\price\\only_price\\gijoon2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(580, 450, 700, 500, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("gijoon2", imgs_)
                        x_reg = imgs_.x + 9

                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\auction\\price\\one_price\\1000.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(620, 460, 700, 490, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("1000", imgs_)
                    num_1000 = True
                    num_1000_x = imgs_.x
                    # 646, 649
                else:
                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\auction\\price\\one_price\\1000_2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(620, 460, 700, 490, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("1000_2", imgs_)
                        num_1000 = True
                        num_1000_x = imgs_.x



                result_price = ""

                for n in range(6):
                    jari = n + 1
                    x1 = x_reg + (n * 7)
                    x2 = x_reg + 10 + (n * 7)

                    for i in range(11):
                        result_num = "none"
                        if num_1000 == False:
                            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\auction\\price\\only_price\\" + str(
                                i) + ".PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(x1, 460, x2, 490, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                result_num = str(i)
                                print(jari, "번쩨 숫자 : ", result_num, imgs_)

                        else:
                            if 644 < num_1000_x < 648:
                                if jari == 1:
                                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\auction\\price\\only_price\\" + str(
                                        i) + ".PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(x1, 460, x2, 490, cla, img, 0.85)
                                    if imgs_ is not None and imgs_ != False:
                                        result_num = str(i)
                                        print(jari, "번쩨 숫자 : ", result_num, imgs_)
                                else:
                                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\auction\\price\\only_price\\" + str(
                                        i) + ".PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(x1 + 4, 460, x2 + 4, 490, cla, img, 0.85)
                                    if imgs_ is not None and imgs_ != False:
                                        result_num = str(i)
                                        print(jari, "번쩨 숫자 : ", result_num, imgs_)
                            elif 647 < num_1000_x < 651:
                                if jari < 3:
                                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\auction\\price\\only_price\\" + str(
                                        i) + ".PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(x1, 460, x2, 490, cla, img, 0.85)
                                    if imgs_ is not None and imgs_ != False:
                                        result_num = str(i)
                                        print(jari, "번쩨 숫자 : ", result_num, imgs_)
                                else:
                                    full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\auction\\price\\only_price\\" + str(
                                        i) + ".PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(x1 + 4, 460, x2 + 4, 490, cla, img, 0.85)
                                    if imgs_ is not None and imgs_ != False:
                                        result_num = str(i)
                                        print(jari, "번쩨 숫자 : ", result_num, imgs_)

                        if result_num != "none":

                            file_path = "C:\\my_games\\moonlight\\data_moon\\imgs\\auction\\price\\only_price\\number.txt"

                            with open(file_path, "r", encoding='utf-8-sig') as file:
                                read_num = file.read().splitlines()
                                # print("read_num", read_num)
                                for r in range(len(read_num)):
                                    read_num_ready = read_num[r].split(":")
                                    if read_num_ready[0] == result_num:
                                        result_num = read_num_ready[1]
                                        break
                            print("result_num", result_num)

                            result_price += result_num

                            print("result_price............", result_price)
                            break

            print("last price =>", result_price)
        else:
            print("notnornotnotnot")

        if result_price == "":
            result_price = "9999"

        for n in range(6):
            full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\auction\\market_list_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(430, 300, 525, 365, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\auction\\auction_confirm_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(445, 705, 525, 750, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
            else:
                break
            time.sleep(0.5)

        return result_price
    except Exception as e:
        print(e)


def how_many(cla):
    import numpy as np
    import cv2

    from function_moon import imgs_set_
    try:
        print("how_many")

        last_num = ""
        # 467, 475, 481


        for n in range(3):
            result_num = "none"
            x1 = 463 + (n * 7)
            x2 = 471 + (n * 7)
            for i in range(10):
                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\auction\\howmany\\" + str(
                    i) + ".PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(x1, 535, x2, 565, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    result_num = str(i)
                    print("숫자 : ", result_num, imgs_)
            if result_num != "none":
                last_num += result_num
        print("last_num", last_num)
        if last_num == "" or last_num == "0":
            last_num = 999
        return last_num
    except Exception as e:
        print(e)

def last_price_equal(cla):
    import numpy as np
    import cv2

    from function_moon import imgs_set_
    try:
        print("last_price_equal")

        last_num = ""
        # 467, 475, 481


        for n in range(3):
            result_num = "none"
            x1 = 463 + (n * 7)
            x2 = 471 + (n * 7)
            for i in range(10):
                full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\auction\\howmany\\" + str(
                    i) + ".PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(x1, 585, x2, 625, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    result_num = str(i)
                    print("숫자 : ", result_num, imgs_)
            if result_num != "none":
                last_num += result_num
        print("last_num", last_num)
        if last_num == "" or last_num == "0":
            last_num = 999
        return last_num
    except Exception as e:
        print(e)