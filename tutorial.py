# -*- coding: utf-8 -*-
import sys
import pygame
from pygame.locals import *

def main():
    (width, height) = (400, 400)   # 画面サイズ
    pygame.init()       # pygame初期化
    pygame.display.set_mode((width, height), 0, 32)  # 画面設定
    screen = pygame.display.get_surface()
    font = pygame.font.Font(None, 55)
    screen.fill((0, 0, 0, 0))  # 画面の背景色
    text = font.render("Try Shoryuken", True, (255, 255, 255))
    screen.blit(text, (50, 100))

    states = ["none", "right", "down", "right-down", "punches"]
    state_index = 0
    prev_key = K_SPACE

    while 1:
        pygame.display.update()     # 画面更新
        pygame.time.wait(30)        # 更新時間間隔
        print(states[state_index])
        # イベント処理
        for event in pygame.event.get():
            # 画面の閉じるボタンを押したとき
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            # キーを押したとき
            if event.type == KEYDOWN:
                print(event.key)
                # ESCキーなら終了
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                if state_index == 0:
                    state_index = check_right(event.key)
                elif state_index == 1:
                    state_index = check_down(event.key)
                elif state_index == 2:
                    state_index = check_rightdown(event.key, prev_key)
                elif state_index == 3:
                    state_index = check_punches(event.key)

                prev_key = event.key
            # else:
                #state_index = 0

            if state_index == 4:
                text = font.render("!!!Shoryuken!!!", True, (255, 0, 0))
                screen.blit(text, (50, 250))


def check_right(key):
    if key == K_RIGHT:
        state_index = 1
    else:
        state_index = 0
    return state_index


def check_down(key):
    if key == K_DOWN:
        state_index = 2
    else:
        state_index = 0
    return state_index


def check_rightdown(key, prev_key):
    if key == K_DOWN and prev_key == K_RIGHT:
        state_index = 3
    elif key == K_RIGHT and prev_key == K_DOWN:
        state_index = 3
    else:
        state_index = 0
    return state_index


def check_punches(key):
    if key == K_p:
        state_index = 4
    else:
        state_index = 0
    return state_index


if __name__ == "__main__":
    main()
