import pygame, time, math, random, sys
height = 500
width = 900
pygame.init()
pygame.mixer.init()
pygame.display.set_caption('Geometry Dash')
screen=pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
obstacles_velocity = 10
isjump = False
pausing = False
v = 5
m = 1
running = True
white=(255,255,255)
BLUE=(0,0,255)
GREEN=(0,255,0)
font = pygame.font.SysFont('san',50)
font1 = pygame.font.SysFont('san',22)
# sound=pygame.mixer.Sound('E:/images/music.mp3')
# main
x_main = 100
y_main = 345.5
main_img = pygame.image.load('E:/images/main2.jpg')
main_img = pygame.transform.scale(main_img,(35,35))
#background
Background_img = pygame.image.load('E:/images/background123.jpg')
Background_img = pygame.transform.scale(Background_img,(900,500))

obstacles_op_img = pygame.image.load('E:/images/obstacles_op.png')
obstacles_img = pygame.image.load('E:/images/obstacles.png')
# obstacles_img = pygame.transform.scale(obstacles_img,(40,40))

floor_img = pygame.image.load('E:/images/floor.jpg')
floor_img = pygame.transform.scale(floor_img,(4000,155))

portal_img = pygame.image.load('E:/images/portal.png')
portal_img = pygame.transform.scale(portal_img,(20,80))

x_obstacles1 = 300
x_obstacles2 = 500
x_obstacles3 = 700
x_obstacles4 = 730
x_obstacles5 = 850
x_obstacles6 = 1000
x_obstacles7 = 1125
x_obstacles8 = 1250
x_obstacles9 = 1280
x_obstacles10 = 1400
x_obstacles11 = 1510
x_obstacles12 = 1600
x_obstacles13 = 1750
x_obstacles14 = 1775
x_obstacles15 = 1900
x_obstacles16 = 2000
x_obstacles17 = 2115

x_op_obstacles1 = 400
x_op_obstacles2 = 600
x_op_obstacles3 = 630
x_op_obstacles4 = 800
x_op_obstacles5 = 1080
x_op_obstacles6 = 1500
x_op_obstacles7 = 1800
x_op_obstacles8 = 1300
x_op_obstacles9 = 1330

x_floor = 0

x_portal = 2400

while running:
    clock.tick(120)
    screen.fill(white)
    screen.blit(Background_img,(0,0))

    screen.blit(floor_img, (x_floor, 379))

    screen.blit(portal_img, (x_portal,300))

    obstacles_img = pygame.transform.scale(obstacles_img, (30, 30))
    obstacles1_img = pygame.transform.scale(obstacles_img, (25, 25))
    obstacles2_img = pygame.transform.scale(obstacles_img, (35, 40))

    obstacles1 = screen.blit(obstacles_img, (x_obstacles1, 351))
    obstacles2 = screen.blit(obstacles_img, (x_obstacles2, 351))
    obstacles3 = screen.blit(obstacles_img, (x_obstacles3, 351))
    obstacles4 = screen.blit(obstacles1_img, (x_obstacles4, 355))
    obstacles5 = screen.blit(obstacles_img, (x_obstacles5, 351))
    obstacles6 = screen.blit(obstacles_img, (x_obstacles6, 351))
    obstacles7 = screen.blit(obstacles_img, (x_obstacles7, 351))
    obstacles8 = screen.blit(obstacles_img, (x_obstacles8, 351))
    obstacles9 = screen.blit(obstacles1_img, (x_obstacles9, 355))
    obstacles10 = screen.blit(obstacles2_img, (x_obstacles10, 340))

    obstacles11 = screen.blit(obstacles_img, (x_obstacles11, 351))
    obstacles12 = screen.blit(obstacles_img, (x_obstacles12, 351))
    obstacles13 = screen.blit(obstacles_img, (x_obstacles13, 351))
    obstacles14 = screen.blit(obstacles1_img, (x_obstacles14, 355))
    obstacles15 = screen.blit(obstacles2_img, (x_obstacles15, 340))
    obstacles16 = screen.blit(obstacles_img, (x_obstacles16, 351))
    obstacles17 = screen.blit(obstacles2_img, (x_obstacles17, 340))

    obstacles_op_img = pygame.transform.scale(obstacles_op_img, (30, 30))
    obstacles1_op = screen.blit(obstacles_op_img, (x_op_obstacles1, 230))
    obstacles2_op = screen.blit(obstacles_op_img, (x_op_obstacles2, 230))
    obstacles3_op = screen.blit(obstacles_op_img, (x_op_obstacles3, 230))
    obstacles4_op = screen.blit(obstacles_op_img, (x_op_obstacles4, 230))
    obstacles5_op = screen.blit(obstacles_op_img, (x_op_obstacles5, 230))
    obstacles6_op = screen.blit(obstacles_op_img, (x_op_obstacles6, 230))
    obstacles7_op = screen.blit(obstacles_op_img, (x_op_obstacles7, 230))
    obstacles8_op = screen.blit(obstacles_op_img, (x_op_obstacles8, 230))
    obstacles9_op = screen.blit(obstacles_op_img, (x_op_obstacles9, 230))


    main=screen.blit(main_img, (x_main, y_main))

    x_obstacles1 -= obstacles_velocity
    x_obstacles2 -= obstacles_velocity
    x_obstacles3 -= obstacles_velocity
    x_obstacles4 -= obstacles_velocity
    x_obstacles5 -= obstacles_velocity
    x_obstacles6 -= obstacles_velocity
    x_obstacles7 -= obstacles_velocity
    x_obstacles8 -= obstacles_velocity
    x_obstacles9 -= obstacles_velocity
    x_obstacles10 -= obstacles_velocity
    x_obstacles11 -= obstacles_velocity
    x_obstacles12 -= obstacles_velocity
    x_obstacles13 -= obstacles_velocity
    x_obstacles14 -= obstacles_velocity
    x_obstacles15 -= obstacles_velocity
    x_obstacles16 -= obstacles_velocity
    x_obstacles17 -= obstacles_velocity

    x_op_obstacles1 -= obstacles_velocity
    x_op_obstacles2 -= obstacles_velocity
    x_op_obstacles3 -= obstacles_velocity
    x_op_obstacles4 -= obstacles_velocity
    x_op_obstacles5 -= obstacles_velocity
    x_op_obstacles6 -= obstacles_velocity
    x_op_obstacles7 -= obstacles_velocity
    x_op_obstacles8 -= obstacles_velocity
    x_op_obstacles9 -= obstacles_velocity

    x_floor -= obstacles_velocity
    x_portal -= obstacles_velocity

    # pygame.mixer.Sound.play(sound)
    # obstacles123 = [obstacles1_op, obstacles2_op, obstacles3_op, obstacles4_op, obstacles5_op, obstacles6_op, obstacles7_op, obstacles8_op, obstacles9_op]
    obstacles123 = [obstacles1, obstacles2, obstacles3, obstacles4, obstacles5, obstacles6, obstacles7, obstacles8, obstacles9, obstacles10, obstacles11, obstacles12, obstacles13, obstacles14, obstacles15, obstacles16, obstacles17, obstacles1_op, obstacles2_op, obstacles3_op, obstacles4_op, obstacles5_op, obstacles6_op, obstacles7_op, obstacles8_op,obstacles9_op]

    for obstacles in obstacles123:
        if main.colliderect(obstacles):
            # pygame.mixer.pause()
            obstacles_velocity = 0
            v = 0
            game_over_txt = font.render("--- Game Over ---", True, BLUE)
            screen.blit(game_over_txt, (325, 200))
            space_txt = font1.render("Press Space To Continue!", True, GREEN)
            screen.blit(space_txt, (367, 250))
            pausing = True


    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if isjump == False:
        if keys[pygame.K_SPACE]:
            isjump = True

    if isjump:
        F = (2)*m * (v ** 2)
        y_main -= F
        v = v - 1
        if v < 0:
            m = -1

        if v == -6:
            isjump = False
            v = 5
            m = 1
        if pausing:
            # pygame.mixer.unpause()
            x_main = 100
            y_main = 345
            x_obstacles1 = 300
            x_obstacles2 = 500
            x_obstacles3 = 700
            x_obstacles4 = 730
            x_obstacles5 = 850
            x_obstacles6 = 1000
            x_obstacles7 = 1125
            x_obstacles8 = 1250
            x_obstacles9 = 1280
            x_obstacles10 = 1400
            x_obstacles11 = 1510
            x_obstacles12 = 1600
            x_obstacles13 = 1750
            x_obstacles14 = 1775
            x_obstacles15 = 1900
            x_obstacles16 = 2000
            x_obstacles17 = 2115

            x_op_obstacles1 = 400
            x_op_obstacles2 = 600
            x_op_obstacles3 = 630
            x_op_obstacles4 = 800
            x_op_obstacles5 = 1080
            x_op_obstacles6 = 1500
            x_op_obstacles7 = 1800
            x_op_obstacles8 = 1300
            x_op_obstacles9 = 1330

            obstacles_velocity = 10
            pausing = False
            v = 5
            m = 1
            x_floor = 0
            x_portal = 2400

    # time delay (20ms)
    pygame.time.delay(35)
    # update
    pygame.display.flip()
pygame.quit()