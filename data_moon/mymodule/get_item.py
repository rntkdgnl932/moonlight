import sys
import os
import time
import requests

sys.path.append('C:/my_games/moonlight/data_moon/mymodule')

import variable as v_

def get_items(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random

    from function_moon import imgs_set_, click_pos_reg, click_pos_2

    from action_moon import loading


    from tuto_moon import tuto_start
    try:

        dead = False

        print("get_items")

    except Exception as e:
        print(e)

