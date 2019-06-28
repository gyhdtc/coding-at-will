# -*- coding: UTF-8 -*-
# animation.py
 
# 导入需要的模块
import pygame, sys
import random
from pygame.locals import *
 
# 初始化pygame
pygame.init()
 
# 设置帧率（屏幕每秒刷新的次数）
FPS = 30
 
# 获得pygame的时钟
fpsClock = pygame.time.Clock()
 
# 设置窗口大小
screen = pygame.display.set_mode((500, 400), 0, 32)
 
# 设置标题
pygame.display.set_caption('Animation')
 
# 定义颜色
WHITE = (255, 255, 255)
 
# 加载一张图片（所用到的的图片请参考1.5代码获取）
img = pygame.image.load('lzr.jpg')
 
# 初始化图片的位置
imgx = 10
imgy = 10
num = 0
# 程序主循环
while True:
 
  # 每次都要重新绘制背景白色
  screen.fill(WHITE)
  
  # 随机坐标
  imgx = random.randint(0,300)
  imgy = random.randint(0,300)
 
  # 该方法将用于图片绘制到相应的坐标中
  screen.blit(img, (imgx, imgy))
  # 刷新图片
  pygame.display.update()

  for event in pygame.event.get():
    if event.key == K_ESCAPE:
      pygame.quit()
      sys.exit()
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
    while True:
      if event.type == MOUSEBUTTONUP:
        flag = 0
        x, y = event.pos
        while (x <= imgx + 50 and x >= imgx and y >= imgy and y <= imgy + 50):
          num += 1
          flag = 1
      if flag == 1:
          break

  # 设置pygame时钟的间隔时间
  fpsClock.tick()