# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import sys

def main():
    (w,h) = (400,400)   # 画面サイズ
    pygame.init()       # pygame初期化
    pygame.display.set_mode((w, h), 0, 32)  # 画面設定
    screen = pygame.display.get_surface()
    font = pygame.font.Font(None, 55)
    screen.fill((0, 0, 0, 0))  # 画面の背景色
    text = font.render("Try Shoryuken", True, (255,255,255))
    screen.blit(text, (50, 100))

    states = ["none", "right", "down", "right-down", "punches"]
    stateIndex = 0
    previousKey = K_SPACE

    while (1):
        pygame.display.update()     # 画面更新
        pygame.time.wait(30)        # 更新時間間隔
        print(stateIndex)
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

                if stateIndex == 0:
                    stateIndex = checkRight(event.key)
                elif stateIndex == 1:
                    stateIndex = checkDown(event.key)
                elif stateIndex == 2:
                    stateIndex = checkRightDown(event.key, previousKey)
                elif stateIndex == 3:
                    stateIndex = checkPunches(event.key)
                
                previousKey = event.key
            #else:
                #stateIndex = 0

            if stateIndex == 4:
                 text = font.render("!!!Shoryuken!!!", True, (255,0,0))
                 screen.blit(text, (50, 250))

def checkRight(key):
    if key == K_RIGHT:
        stateIndex = 1
    else:
        stateIndex = 0
    return stateIndex

def checkDown(key):
    if key == K_DOWN:
        stateIndex = 2
    else:
        stateIndex = 0
    return stateIndex

def checkRightDown(key, previousKey):
    if key == K_DOWN and previousKey == K_RIGHT:
        stateIndex = 3
    elif key == K_RIGHT and previousKey == K_DOWN:
        stateIndex = 3
    else:
        stateIndex = 0
    return stateIndex

def checkPunches(key):
    if key == K_p:
        stateIndex = 4
    else:
        stateIndex = 0
    return stateIndex

if __name__ == "__main__":
    main()