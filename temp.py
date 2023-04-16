import pygame
import csv_bs


print(csv_bs.add_score("kharghuvel",100,3,"scores.csv"))
# pygame.init()
# screen=pygame.display.set_mode((400,400))
# clock=pygame.time.Clock()
# box=pygame.Rect(100,100,200,120)
# while True:
#     for i in pygame.event.get():
#         if i.type==256:
#             pygame.quit()
#         if i.type==pygame.KEYDOWN:
#             print(i.unicode)
#     pygame.draw.rect(screen,"blue",box)
#     pygame.display.update()
#     clock.tick(60)