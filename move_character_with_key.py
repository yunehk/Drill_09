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


def handle_events():
    global running
    for event in get_events():
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
            elif event.key in (SDLK_LEFT, SDLK_RIGHT, SDLK_UP, SDLK_DOWN):
                pressed_keys.add(event.key)
        elif event.type == SDL_KEYUP:
            pressed_keys.discard(event.key)


