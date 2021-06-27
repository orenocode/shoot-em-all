import pygame, math, random, os
from pygame.locals import *
#initiate the game
pygame.init()
width, height = 720, 480
#create screen of the game
screen = pygame.display.set_mode((width, height))
#variable decleared
command_key = [False,False,False,False]
acc = [0, 0]
arrows = []
player_position = [120,100]
badtimer=1000
badtimer1=0
badguys=[[664000, 0]]
healthvalue=194
#create first object
parent_folder = os.getcwd() + '/Python/First_game'
player = pygame.image.load(parent_folder + '/resources/images/dude.png')
grass = pygame.image.load(parent_folder + '/resources/images/grass.png')
castle = pygame.image.load(parent_folder + '/resources/images/castle.png')
arrow = pygame.image.load(parent_folder + '/resources/images/bullet.png')
badguyimg1 = pygame.image.load(parent_folder + '/resources/images/badguy.png')
badguyimg = badguyimg1
#loop over the game
while 1:
    badtimer -= 1
    screen.fill(0)
    for x in range(int(width/grass.get_width())+ 1):
        for y in range(int(height/grass.get_height())+ 1):
            screen.blit(grass, (x*100, y*100))
#Castles needed to defend's positions
    screen.blit(castle, (10 , 10))
    screen.blit(castle, (10 , 120))
    screen.blit(castle, (10 , 240))
    screen.blit(castle, (10 , 360))
#rotate and modify player
    mouse_position = pygame.mouse.get_pos()
    angle = math.atan2(mouse_position[1] - (player_position[1]), mouse_position[0] - (player_position[0]))
    player_rotation = pygame.transform.rotate(player, 360 - angle * 57.29)
    player_rotating_position = (player_position[0] - player_rotation.get_rect().width/2, player_position[1] - player_rotation.get_rect().height/2)
    screen.blit(player_rotation, player_rotating_position)
#Draw arrows
    for bullet in arrows:
        index=0
        velx=math.cos(bullet[0])*10
        vely=math.sin(bullet[0])*10
        bullet[1]+=velx
        bullet[2]+=vely
        if bullet[1]<-64 or bullet[1]>640 or bullet[2]<-64 or bullet[2]>480:
            arrows.pop(index)
        index+=1
        for projectile in arrows:
            arrow1 = pygame.transform.rotate(arrow, 360-projectile[0]*57.29)
            screen.blit(arrow1, (projectile[1], projectile[2]))
    # Draw badgers
    if badtimer==0:
        badguys.append([640, random.randint(50,430)])
        badtimer = 100 - (badtimer1*2)
        if badtimer1 >= 35:
            badtimer1 = 35
        else: 
            badtimer1+=5
    index=0
    for badguy in badguys:
        if badguy[0]<-64:
            badguys.pop(index)
        badguy[0] -= 7
        index+=1
    for badguy in badguys:
        screen.blit(badguyimg, badguy)   
            # Attack castle
        badrect=pygame.Rect(badguyimg.get_rect())
        badrect.top=badguy[1]
        badrect.left=badguy[0]
        if badrect.left < 64:
            healthvalue -= random.randint(5,20)
            badguys.pop(index)
        # Next bad guy
#update the screen
    pygame.display.flip()
    for event in pygame.event.get():
        #quit game
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        # if players are pressing a key
        if event.type == pygame.KEYDOWN:
            if event.key == K_w:
                command_key[0] = True
            elif event.key == K_a:
                command_key[1] = True
            elif event.key == K_s:
                command_key[2] = True
            elif event.key == K_d:
                command_key[3] = True
        # if they aren't pressing any keys
        if event.type == pygame.KEYUP:
            if event.key == K_w:
                command_key[0] = False
            elif event.key == K_a:
                command_key[1] = False
            elif event.key == K_s:
                command_key[2] = False
            elif event.key == K_d:
                command_key[3] = False
#Move the player
    #press W
    if command_key[0]:
        player_position[1] -= 5
    #press A
    elif command_key[1]:
        player_position[0] -= 5
    #press S
    elif command_key[2]:
        player_position[1] += 5
    #press D
    elif command_key[3]:
        player_position[0] += 5
    #load arrows
    if event.type==pygame.MOUSEBUTTONDOWN:
        position=pygame.mouse.get_pos()
        acc[1]+=1
        arrows.append([math.atan2(position[1]-(player_rotating_position[1]+32),position[0]-(player_rotating_position[0]+26)),player_rotating_position[0]+32,player_rotating_position[1]+32])  
