import time
# import os
import sys


sys.path.append('C:/my_games/moonlight/data_moon/mymodule')

import variable as v_



def _stop_please(cla):
    import numpy as np
    import cv2
    from function_moon import imgs_set_, click_pos_reg, click_pos_2

    try:
        print("_stop_please")
        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\18\\18_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(70, 670, 300, 770, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            print("18_1")
            click_pos_reg(imgs_.x, imgs_.y, cla)
            time.sleep(1)
        full_path = "c:\\my_games\\moonlight\\data_moon\\imgs\\18\\18_2.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(70, 670, 300, 770, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            print("18_1")
            click_pos_reg(imgs_.x, imgs_.y, cla)



    except Exception as e:
        print(e)
        return 0



