import pygame
import datetime
import sys
pygame.init()
size = (1000, 800)
screen = pygame.display.set_mode(size)
clock_center = (500, 400)
background_img = pygame.image.load(r"C:\Users\Admin\Desktop\PP2labs\Lab_7\images\clock.png")
seconds = pygame.image.load(r"C:\Users\Admin\Desktop\PP2labs\Lab_7\images\leftarm.png")
minutes = pygame.image.load(r"C:\Users\Admin\Desktop\PP2labs\Lab_7\images\rightarm.png")
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.blit(background_img, (-200, -150))
    now = datetime.datetime.now()
    minute_angle = -(now.minute * 6) + 90 - 144 
    second_angle = -(now.second * 6) + 90 - 36 
    min_rotated = pygame.transform.rotate(minutes, minute_angle)
    sec_rotated = pygame.transform.rotate(seconds, second_angle)
    min_rect = min_rotated.get_rect(center = clock_center)
    sec_rect = sec_rotated.get_rect(center = clock_center)
    screen.blit(min_rotated, min_rect.topleft)
    screen.blit(sec_rotated, sec_rect.topleft)
    pygame.display.flip() 
pygame.quit()
sys.exit()