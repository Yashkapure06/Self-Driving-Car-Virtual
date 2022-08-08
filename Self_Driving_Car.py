#no1 feature it can drive itself
#no2 feature it can stop itself whenever there is any obstracle
#no3 it can trun on its own i.e takes left and right move forward  or backward, etc...
#no4  it can reach the destination by it's own
import pygame

pygame.init()#initialize pygame

window = pygame.display.set_mode((1200,400))

track =  pygame.image.load('Projects\\Self Driving Car\\images\\track6.png')

car = pygame.image.load('Projects\\Self Driving Car\\images\\tesla.png')

car = pygame.transform.scale(car, (30, 60))
#this is to decrease the size of the car image to fit on the road


car_x = 150
car_y = 300
focal_distance = 25
cam_x_offset = 0
cam_y_offset = 0
direction = 'up'
drive = True
clock = pygame.time.Clock()

while drive:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drive = False

    clock.tick(60)
    #blit = block image transfer
    cam_x = car_x+ cam_x_offset + 15
    cam_y = car_y+ cam_y_offset + 15
    up_pix = window.get_at((cam_x, cam_y - focal_distance))[0]
    down_pix = window.get_at((cam_x, cam_y + focal_distance))[0]
    right_pix = window.get_at((cam_x + focal_distance, cam_y))[0]
    print(up_pix, down_pix, right_pix)
    
    #take turn
    if direction=='up' and up_pix!= 255 and right_pix == 255:
        direction = 'right'
        cam_x_offset = 30
        car = pygame.transform.rotate(car, -90)
    
    elif direction=='right' and right_pix!= 255 and down_pix == 255:
        direction = 'down'
        car_x = car_x + 30
        cam_x_offset = 0
        cam_y_offset = 30
        car = pygame.transform.rotate(car, -90)

    elif direction=='down' and down_pix!= 255 and right_pix==255:
        direction = 'right'
        car_y = car_y + 30
        cam_y_offset = 0
        cam_x_offset = 30
        car = pygame.transform.rotate(car, 90)

    elif direction == 'right' and right_pix!= 255 and up_pix==255:
        direction = 'up'
        car_x = car_x + 30
        cam_x_offset = 0
        car = pygame.transform.rotate(car, 90)


    #drive
    if direction=='up' and up_pix == 255:
        car_y = car_y - 2
    elif  direction == 'right'  and right_pix == 255:
        car_x = car_x + 2
    elif  direction == 'down'  and down_pix == 255:
        car_y =car_y + 2


    window.blit(track, (0, 0))
    window.blit(car, (car_x, car_y))#to fit car on road
    pygame.draw.circle(window, (0, 255, 0), (cam_x, cam_y), 5, 5)
    pygame.display.update()
