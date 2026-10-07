from pathlib import Path
from pico2d import *

WIDTH, HEIGHT = 1280, 1024
FRAME_SIZE = 100
ANIMATION_FPS = 8
MOVE_SPEED = 250  # 초당 이동 거리

x, y = WIDTH / 2, HEIGHT / 2
frame = 0
facing = 1  # 1: 오른쪽, -1: 왼쪽
running = True
pressed_keys = set()
moving = False


