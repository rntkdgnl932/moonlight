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

    from function_moon import imgs_set_, click_pos_reg, click_pos_2, drag_pos_reg

    from action_moon import menu_open, clean_screen, out_check

    from get_item import get_event
    from repair_moon import budy_sohwan, hyungsang_sohwan, my_stat_up

    from tuto_moon import tuto_start

    print("tst")
    cla = "one"

    plus = 0

    if cla == "two":
        plus = 960
    if cla == "three":
        plus = 960 * 2
    if cla == "four":
        plus = 960 * 3

    my_stat_up(cla)

