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
            time.sleep(0.7)



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
