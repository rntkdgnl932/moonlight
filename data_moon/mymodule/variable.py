# 현재실행중인 클라우드
now_cla = 'none'

# 아두이노 관련
now_arduino = "none"

# 달빛조각사 관련
# 튜토리얼 죽은 횟수
tuto_dead = 0
# 물약 카운터
need_potion = 0
# 어택 체크 카운터
attack_check_count = 0
# 블랙스크린 카운터
black_screen_count = 0
# 부활금지
not_boohwal = False

# 튜토리얼 moving error
moving_error = 0

# 의뢰 클릭 카운터
re_click_count = 0


# 버젼

dir_path = "C:\\my_games\\moonlight\\data_moon"
file_path = dir_path + "\\mymodule\\version.txt"
file_path2 = "C:\\my_games\\mouse\\port.txt"

with open(file_path, "r", encoding='utf-8-sig') as file:
    version_ = file.read()
    print("version???", version_)

with open(file_path2, "r", encoding='utf-8-sig') as file:
    read_port = file.read().splitlines()
    COM_ = read_port[0]
    speed_ = int(read_port[1])
    print("COM???", COM_)
    print("speed_???", speed_)

this_game = "달빛조각사"


# 강제로 돈벌기
forcee_not_sub = False
force_sub_quest = False
onForceGold = 5000000
onForceGoldSpot = "none"
# 수집(아레스에서는 다크디멘션으로 대체)
onCollection = False


# 마우스 관련
mouse_speed = 20
mouse_pm = 3