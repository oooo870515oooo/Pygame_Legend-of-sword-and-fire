import pygame
import random
import time
import math
pygame.init()

def randColour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

#player1 move
def move(image1, image2):
    global locount
    if locount < 5:
        image = image1
    elif locount >= 5:
        image = image2
    if locount >= 10:
        locount = 0
    else:
        locount += 1
    return image

#player2 move
def move1(p2image1, p2image2):
    global p2locount
    if p2locount < 5:
        p2image = p2image1
    elif p2locount >= 5:
        p2image = p2image2
    if p2locount >= 10:
        p2locount = 0
    else:
        p2locount += 1
    return p2image


    
# Window setup
size = [957, 574]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

black = pygame.color.Color("#000000")
count = 0
font = pygame.font.SysFont("arial", 30)
# Load images
background = pygame.image.load("BG.JPG")

#----------------sound---------------------
walk=pygame.mixer.Sound("se_maoudamashii_instruments_bass13.mp3")
winmusic=pygame.mixer.Sound("win.mp3")
hit=pygame.mixer.Sound("battle.wav")
#--------------------------------------
#player1 picture
standing = pygame.image.load('AS2.png')
down1 = pygame.image.load('AS1.png')
down2 = pygame.image.load('AS3.png')
upstanding = pygame.image.load('AW2.png')
up1 = pygame.image.load('AW1.png')
up2 = pygame.image.load('AW3.png')
leftstanding = pygame.image.load('AL2.png')
left1 = pygame.image.load('AL1.png')
left2 = pygame.image.load('AL3.png')
rightstanding = pygame.image.load('AR2.png')
right1 = pygame.transform.flip(left1, True, False)
right2 = pygame.transform.flip(left2, True, False)

#player2 picture
p2standing = pygame.image.load('BS2.png')
p2down1 = pygame.image.load('BS1.png')
p2down2 = pygame.image.load('BS3.png')
p2upstanding = pygame.image.load('BW2.png')
p2up1 = pygame.image.load('BW1.png')
p2up2 = pygame.image.load('BW3.png')
p2leftstanding = pygame.image.load('BL2.png')
p2left1 = pygame.image.load('BL1.png')
p2left2 = pygame.image.load('BL3.png')
p2rightstanding = pygame.image.load('BR2.png')
p2right1 = pygame.transform.flip(p2left1, True, False)
p2right2 = pygame.transform.flip(p2left2, True, False)

#fire picture
fireup = pygame.image.load('Ufire.png')
fireleft = pygame.image.load('Lfire.png')
fireright = pygame.image.load('Rfire.png')
firedown = pygame.image.load('Dfire.png')

#sword picture
swordup = pygame.image.load('USword.png')
swordleft = pygame.image.load('LSword.png')
swordright = pygame.image.load('RSword.png')
sworddown = pygame.image.load('DSword.png')

#win
Win1 = pygame.image.load('Win1.jpg')
Win2 = pygame.image.load('Win2.jpg')
# colours
red = pygame.color.Color('#FF8080')
blue = pygame.color.Color('#8080FF')
white = pygame.color.Color('#FFFFFF')
black = pygame.color.Color('#000000')
yellow=pygame.color.Color('#FFFF33')

def checkOffscreen(x, y):
    #---------------------------------------外牆-------------------
    if x < 39:
        x = 39
    elif x > 890:
        x = 890
    if y < 39:
        y = 39
    elif y > 505:
        y = 505
    #---------------------------------------內部障礙物--------------
    #---------------------------------------------------------------   1
    if x >= 149 and x<=225 and y >= 100 and y <= 467:
        if y<=105 and y>=100:
            y=100
        elif y>=462 and y<=467:
            y=467
        elif x>=149 and x<=154 :
            x=149
        elif x>=220 and x<=225:
            x=225
    if y>=100 and y<=180 and x>=149 and x<=345:
        if y<=105 and y>=100:
            y=100
        elif x>=340 and x<=345:
            x=345
        elif x<=154 and x>=149:
            x=149
        elif y<=180 and y>=175:
            y=180
    #---------------------------------------------------------------   2    
    if x >= 365 and x<=421 and y >= 170 and y <= 253:
        if y<=175 and y>=170:
            y=170
        elif y>=248 and y<=253:
            y=253
        elif x>=365 and x<=370 :
            x=365
        elif x>=416 and x<=421:
            x=421
    if y>=170 and y<=230 and x>=365 and x<=445:
        if y<=175 and y>=170:
            y=170
        elif x>=440 and x<=445:
            x=445
        elif x<=370 and x>=365:
            x=365
        elif y<=230 and y>=225:
            y=230
    #---------------------------------------------------------------   3
    if x >= 365 and x<=421 and y >= 290 and y <= 398:
        if y<=295 and y>=290:
            y=290
        elif y>=395 and y<=398:
            y=398
        elif x>=365 and x<=370 :
            x=365
        elif x>=416 and x<=421:
            x=421
    if y>=337 and y<=397 and x>=316 and x<=470:
        if y<=342 and y>=337:
            y=337
        elif x>=465 and x<=470:
            x=470
        elif x<=321 and x>=316:
            x=316
        elif y<=397 and y>=392:
            y=397
    #---------------------------------------------------------------   4    
    if x >= 507 and x<=566 and y >= 170 and y <= 253:
        if y<=175 and y>=170:
            y=170
        elif y>=248 and y<=253:
            y=253
        elif x>=507 and x<=512 :
            x=506
        elif x>=561 and x<=566:
            x=567
    if y>=170 and y<=230 and x>=483 and x<=566:
        if y<=175 and y>=170:
            y=170
        elif x>=561 and x<=566:
            x=566
        elif x<=488 and x>=482:
            x=482
        elif y<=230 and y>=225:
            y=231
    #---------------------------------------------------------------   5  
    if x >= 461 and x<=513 and y >= 11 and y <= 107:
        if y<=16 and y>=11:
            y=11
        elif y>=102 and y<=107:
            y=107
        elif x>=461 and x<=466 :
            x=460
        elif x>=508 and x<=513:
            x=514
    #---------------------------------------------------------------   6   
    if x >= 677 and x<=753 and y >= 52 and y <= 396:
        if y<=57 and y>=52:
            y=52
        elif y>=391 and y<=396:
            y=396
        elif x>=677 and x<=682 :
            x=676
        elif x>=748 and x<=753:
            x=754
    if y>=316 and y<=396 and x>=558 and x<=753:
        if y<=321 and y>=316:
            y=316
        elif x>=758 and x<=753:
            x=753
        elif x<=563 and x>=558:
            x=557
        elif y<=396 and y>=391:
            y=397
    #---------------------------------------------------------------   7  
    if x >= 798 and x<=917 and y >= 268 and y <= 370:
        if y<=273 and y>=268:
            y=268
        elif y>=365 and y<=370:
            y=370
        elif x>=798 and x<=803 :
            x=797
        elif x>=912 and x<=917:
            x=917
    return x, y
    #------------------------------------------------------------------------------------------
def attackcheckOffscreen(x, y):
    if x < 39:
        x = 1000
    elif x > 890:
        x = 1000
    if y < 39:
        y = 1000
    elif y > 505:
        y = 1000

    #---------------------------------------------------------------   1
    if x >= 149 and x<=225 and y >= 100 and y <= 467:
        if y<=106 and y>=100:
            y=1000
        elif y>=461 and y<=467:
            y=1000
        elif x>=149 and x<=155 :
            x=1000
        elif x>=219 and x<=225:
            x=1000
    if y>=100 and y<=180 and x>=149 and x<=345:
        if y<=106 and y>=100:
            y=1000
        elif x>=339 and x<=345:
            x=1000
        elif x<=155 and x>=149:
            x=1000
        elif y<=180 and y>=174:
            y=1000
    #---------------------------------------------------------------   2    
    if x >= 365 and x<=421 and y >= 170 and y <= 253:
        if y<=176 and y>=170:
            y=1000
        elif y>=247 and y<=253:
            y=1000
        elif x>=365 and x<=371 :
            x=1000
        elif x>=415 and x<=421:
            x=1000
    if y>=170 and y<=230 and x>=365 and x<=445:
        if y<=176 and y>=170:
            y=1000
        elif x>=439 and x<=445:
            x=1000
        elif x<=371 and x>=365:
            x=1000
        elif y<=230 and y>=224:
            y=1000
    #---------------------------------------------------------------   3
    if x >= 365 and x<=421 and y >= 290 and y <= 398:
        if y<=296 and y>=290:
            y=1000
        elif y>=392 and y<=398:
            y=1000
        elif x>=365 and x<=371 :
            x=1000
        elif x>=415 and x<=421:
            x=1000
    if y>=337 and y<=397 and x>=316 and x<=470:
        if y<=343 and y>=337:
            y=1000
        elif x>=464 and x<=470:
            x=1000
        elif x<=322 and x>=316:
            x=1000
        elif y<=397 and y>=391:
            y=1000
    #---------------------------------------------------------------   4    
    if x >= 507 and x<=566 and y >= 170 and y <= 253:
        if y<=176 and y>=170:
            y=1000
        elif y>=247 and y<=253:
            y=1000
        elif x>=507 and x<=513 :
            x=1000
        elif x>=560 and x<=566:
            x=1000
    if y>=170 and y<=230 and x>=483 and x<=566:
        if y<=176 and y>=170:
            y=1000
        elif x>=560 and x<=566:
            x=1000
        elif x<=488 and x>=482:
            x=1000
        elif y<=230 and y>=226:
            y=1000
    #---------------------------------------------------------------   5  
    if x >= 461 and x<=513 and y >= 11 and y <= 107:
        if y<=17 and y>=11:
            y=1000
        elif y>=101 and y<=107:
            y=1000
        elif x>=461 and x<=467 :
            x=1000
        elif x>=507 and x<=513:
            x=1000
    #---------------------------------------------------------------   6   
    if x >= 677 and x<=753 and y >= 52 and y <= 396:
        if y<=58 and y>=52:
            y=1000
        elif y>=390 and y<=396:
            y=1000
        elif x>=677 and x<=683 :
            x=1000
        elif x>=747 and x<=753:
            x=1000
    if y>=326 and y<=396 and x>=558 and x<=753:
        if y<=332 and y>=326:
            y=1000
        elif x>=759 and x<=753:
            x=1000
        elif x<=564 and x>=558:
            x=1000
        elif y<=396 and y>=390:
            y=1000
    #---------------------------------------------------------------   7  
    if x >= 798 and x<=917 and y >= 268 and y <= 370:
        if y<=274 and y>=268:
            y=1000
        elif y>=364 and y<=370:
            y=1000
        elif x>=798 and x<=804 :
            x=1000
        elif x>=911 and x<=917:
            x=1000
    return x, y

pygame.mixer.music.load("game_maoudamashii_2_lastboss03.ogg")
pygame.mixer.music.play()
        
# Game loop
done = False

# attack
fire1upx=1000#1號向上火球座標
fire1upy=1000
fire2upx=1000#2號向上火球座標
fire2upy=1000
fire3upx=1000#3號向上火球座標
fire3upy=1000
fire1downx=1000#1號向下火球座標
fire1downy=1000
fire2downx=1000#2號向下火球座標
fire2downy=1000
fire3downx=1000#3號向下火球座標
fire3downy=1000
fire1rightx=1000#1號向右火球座標
fire1righty=1000
fire2rightx=1000#2號向右火球座標
fire2righty=1000
fire3rightx=1000#3號向右火球座標
fire3righty=1000
fire1leftx=1000#1號向左火球座標
fire1lefty=1000
fire2leftx=1000#2號向左火球座標
fire2lefty=1000
fire3leftx=1000#3號向左火球座標
fire3lefty=1000

sword1upx=1000#1號向上寶劍座標
sword1upy=1000
sword2upx=1000#2號向上寶劍座標
sword2upy=1000
sword3upx=1000#3號向上寶劍座標
sword3upy=1000
sword1downx=1000#1號向下寶劍座標
sword1downy=1000
sword2downx=1000#2號向下寶劍座標
sword2downy=1000
sword3downx=1000#3號向下寶劍座標
sword3downy=1000
sword1rightx=1000#1號向右寶劍座標
sword1righty=1000
sword2rightx=1000#2號向右寶劍座標
sword2righty=1000
sword3rightx=1000#3號向右寶劍座標
sword3righty=1000
sword1leftx=1000#1號向左寶劍座標
sword1lefty=1000
sword2leftx=1000#2號向左寶劍座標
sword2lefty=1000
sword3leftx=1000#3號向左寶劍座標
sword3lefty=1000


# get current time
timeStart = pygame.time.get_ticks()
locount=0
p2locount=0
# Variables for walls
leftWall = 39
topWall = 39
rightWall = 916
bottomWall = 533
# Variables for position etc.
lox = 300
loy = 275
x1 = 620
y1 = 275
Win1x=278
Win1y=67
Win2x=278
Win2y=67
winop=0
direction=0
p2direction=0
pOneCount = 0
pTwoCount = 0
pOneMoving = False
pTwoMoving = False
fire1number=0#火球數在1的方向下
fire2number=0#火球數在2的方向下
fire3number=0#火球數在3的方向下
fire4number=0#火球數在4的方向下
sword1number=0#寶劍數在1的方向下
sword2number=0#寶劍數在2的方向下
sword3number=0#寶劍數在3的方向下
sword4number=0#寶劍數在4的方向下

#PlayersHP
HPI=5
HPII=5

def P1hurt(x,y):
    if x<=lox+37 and x>=lox-37 and y<=loy+37 and y>=loy-37:
        global HPI
        hit.play()
        HPI=HPI-1
        x=1000
        y=1000
    return x,y
    
def P2hurt(x,y):
    if x<=x1+37 and x>=x1-37 and y<=y1+37 and y>=y1-37:
        global HPII
        hit.play()
        HPII=HPII-1
        x=1000
        y=1000
    return x,y
        
while not done:
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        done = True
    # Draw Player1HP
    for I in range(HPI):
        P1HP= 39 + I*9
        pygame.draw.rect(screen,red, (P1HP,39, 8, 14))
    # Draw Player2HP
    for II in range(HPII):
        P2HP= 910 - II*9
        pygame.draw.rect(screen,red, (P2HP,39, 8, 14))
    #musicplay
    if keys[pygame.K_t]:
        pygame.mixer.music.play()
      
    #player1 movement
    if keys[pygame.K_LSHIFT]:
  
        if keys[pygame.K_w]:
            walk.play()
            image = move(up1,up2)
            loy -= 5
            direction=1

            
        elif keys[pygame.K_s]:
            walk.play()
            image = move(down1,down2)
            loy += 5
            direction=0

           
        elif keys[pygame.K_a]:
            walk.play()
            image = move(left1,left2)
            lox -= 5
            direction=2

          
        elif keys[pygame.K_d]:
            walk.play()
            image = move(right1,right2)
            lox += 5
            direction=3

        else:
            if direction==1:
                image=upstanding
                locount=0
            elif direction==2:
                image=leftstanding
                locount=0
            elif direction==3:
                image=rightstanding
                locount=0
            else:
                image =standing
                locount=0
        if keys[pygame.K_SPACE]:
            
            if direction==1:
                fire1number+=2
                if(fire1number==20):
                    fire1number=0
                elif(fire1number==2):
                    fire1upx=lox+8
                    fire1upy=loy+14
                elif(fire1number==8):
                    fire2upx=lox+7
                    fire2upy=loy+14
                elif(fire1number==14):
                    fire3upx=lox+7
                    fire3upy=loy+14

                    
            elif direction==2:
                fire2number+=2
                if(fire2number==20):
                    fire2number=0
                if(fire2number==2):
                    fire1leftx=lox+13
                    fire1lefty=loy+14
                elif(fire2number==8):
                    fire2leftx=lox+13
                    fire2lefty=loy+14
                elif(fire2number==14):
                    fire3leftx=lox+13
                    fire3lefty=loy+14


            elif direction==3:
                fire3number+=2
                if(fire3number==20):
                    fire3number=0
                if(fire3number==2):
                    fire1rightx=lox+13
                    fire1righty=loy+14
                elif(fire3number==8):
                    fire2rightx=lox+13
                    fire2righty=loy+14
                elif(fire3number==14):
                    fire3rightx=lox+13
                    fire3righty=loy+14

                    
            else: 
                fire4number+=2
                if(fire4number==20):
                    fire4number=0
                if(fire4number==2):
                    fire1downx=lox+8
                    fire1downy=loy+14
                elif(fire4number==8):
                    fire2downx=lox+8
                    fire2downy=loy+14
                elif(fire4number==14):
                    fire3downx=lox+8
                    fire3downy=loy+14
                
            
            
    else:
        if keys[pygame.K_w]:
            walk.play()
            image = move(up1,up2)
            loy -= 3
            direction=1
            
        
        elif keys[pygame.K_s]:
            walk.play()
            image = move(down1,down2)
            loy += 3
            direction=0
           
           
        elif keys[pygame.K_a]:
            walk.play()
            image = move(left1,left2)
            lox -= 3
            direction=2
           
            
        elif keys[pygame.K_d]:
            walk.play()
            image = move(right1,right2)
            lox += 3
            direction=3

        else:
            if direction==1:
                image=upstanding
                locount=0
            elif direction==2:
                image=leftstanding
                locount=0
            elif direction==3:
                image=rightstanding
                locount=0
            else:
                image =standing
                locount=0
                
        if keys[pygame.K_SPACE]:
            
            if direction==1:
                fire1number+=2
                if(fire1number==20):
                    fire1number=0
                if(fire1number==2):
                    fire1upx=lox+8
                    fire1upy=loy+14
                elif(fire1number==8):
                    fire2upx=lox+8
                    fire2upy=loy+14
                elif(fire1number==14):
                    fire3upx=lox+8
                    fire3upy=loy+14
                    
            elif direction==2:
                
                fire2number+=2
                if(fire2number==20):
                    fire2number=0
                if(fire2number==2):
                    fire1leftx=lox+13
                    fire1lefty=loy+14
                elif(fire2number==8):
                    fire2leftx=lox+13
                    fire2lefty=loy+14
                elif(fire2number==14):
                    fire3leftx=lox+13
                    fire3lefty=loy+14

            elif direction==3:
                
                fire3number+=2
                if(fire3number==20):
                    fire3number=0
                if(fire3number==2):
                    fire1rightx=lox+13
                    fire1righty=loy+14
                elif(fire3number==8):
                    fire2rightx=lox+13
                    fire2righty=loy+14
                elif(fire3number==14):
                    fire3rightx=lox+13
                    fire3righty=loy+14

            else:
                fire4number+=2
                if(fire4number==20):
                    fire4number=0
                if(fire4number==2):
                    fire1downx=lox+8
                    fire1downy=loy+14
                elif(fire4number==8):
                    fire2downx=lox+8
                    fire2downy=loy+14
                elif(fire4number==14):
                    fire3downx=lox+8
                    fire3downy=loy+14


#火球移動
    fire1upy-=6
    fire1leftx-=6
    fire1rightx+=6
    fire1downy+=6
    fire2upy-=6
    fire2leftx-=6
    fire2rightx+=6
    fire2downy+=6
    fire3upy-=6
    fire3leftx-=6
    fire3rightx+=6
    fire3downy+=6

#Player2扣血
    fire1upx,fire1upy =P2hurt(fire1upx,fire1upy)
    fire2upx,fire2upy =P2hurt(fire2upx,fire1upy)
    fire3upx,fire3upy =P2hurt(fire3upx,fire1upy)
    fire1leftx,fire1lefty =P2hurt(fire1leftx,fire1lefty)
    fire2leftx,fire2lefty =P2hurt(fire2leftx,fire2lefty)
    fire3leftx,fire3lefty =P2hurt(fire3leftx,fire3lefty)
    fire1rightx,fire1righty =P2hurt(fire1rightx,fire1righty)
    fire2rightx,fire2righty =P2hurt(fire2rightx,fire2righty)
    fire3rightx,fire3righty =P2hurt(fire3rightx,fire3righty)
    fire1downx,fire1downy =P2hurt(fire1downx,fire1downy)
    fire2downx,fire2downy =P2hurt(fire2downx,fire2downy)
    fire3downx,fire3downy =P2hurt(fire3downx,fire3downy)
    
#player2 movement
   
    if keys[pygame.K_b]:
      
        if keys[pygame.K_i]:
            walk.play()
            p2image = move1(p2up1,p2up2)
            y1 -= 5
            p2direction=1
          
            
        elif keys[pygame.K_k]:
            walk.play()
            p2image = move1(p2down1,p2down2)
            y1 +=5
            p2direction=0
       
            
        elif keys[pygame.K_j]:
            walk.play()
            p2image = move1(p2left1,p2left2)
            x1 -=5
            p2direction=2
   
            
        elif keys[pygame.K_l]:
            walk.play()
            p2image = move1(p2right1,p2right2)
            x1 +=5
            p2direction=3
   
        else:
            if p2direction==1:
                p2image=p2upstanding
                p2locount=0
            elif p2direction==2:
                p2image=p2leftstanding
                p2locount=0
            elif p2direction==3:
                p2image=p2rightstanding
                p2locount=0
            else:
                p2image =p2standing
                p2locount=0
                
        if keys[pygame.K_p]:
            
            if p2direction==1:
                sword1number+=2
                if(sword1number==20):
                    sword1number=0
                elif(sword1number==2):
                    sword1upx=x1+8
                    sword1upy=y1+14
                elif(sword1number==8):
                    sword2upx=x1+8
                    sword2upy=y1+14
                elif(sword1number==14):
                    sword3upx=x1+8
                    sword3upy=y1+14

                    
            elif p2direction==2:
                sword2number+=2
                if(sword2number==20):
                    sword2number=0
                if(sword2number==2):
                    sword1leftx=x1+13
                    sword1lefty=y1+14
                elif(sword2number==8):
                    sword2leftx=x1+13
                    sword2lefty=y1+14
                elif(sword2number==14):
                    sword3leftx=x1+13
                    sword3lefty=y1+14


            elif p2direction==3:
                sword3number+=2
                if(sword3number==20):
                    sword3number=0
                if(sword3number==2):
                    sword1rightx=x1+13
                    sword1righty=y1+14
                elif(sword3number==8):
                    sword2rightx=x1+13
                    sword2righty=y1+14
                elif(sword3number==14):
                    sword3rightx=x1+13
                    sword3righty=y1+14

                    
            else: 
                sword4number+=2
                if(sword4number==20):
                    sword4number=0
                if(sword4number==2):
                    sword1downx=x1+8
                    sword1downy=y1+14
                elif(sword4number==8):
                    sword2downx=x1+8
                    sword2downy=y1+14
                elif(sword4number==14):
                    sword3downx=x1+8
                    sword3downy=y1+14

    else:
        if keys[pygame.K_i]:
            walk.play()
            p2image = move1(p2up1,p2up2)
            y1 -= 3
            p2direction=1
         
            
        elif keys[pygame.K_k]:
            walk.play()
            p2image = move1(p2down1,p2down2)
            y1 +=3
            p2direction=0
       
            
        elif keys[pygame.K_j]:
            walk.play()
            p2image = move1(p2left1,p2left2)
            x1 -=3
            p2direction=2
     
            
        elif keys[pygame.K_l]:
            walk.play()
            p2image = move1(p2right1,p2right2)
            x1 +=3
            p2direction=3
            
        else:
            if p2direction==1:
                p2image=p2upstanding
                p2locount=0
            elif p2direction==2:
                p2image=p2leftstanding
                p2locount=0
            elif p2direction==3:
                p2image=p2rightstanding
                p2locount=0
            else:
                p2image =p2standing
                p2locount=0
                
        if keys[pygame.K_p]:
            if p2direction==1:
                sword1number+=2
                if(sword1number==20):
                    sword1number=0
                elif(sword1number==2):
                    sword1upx=x1+8
                    sword1upy=y1+14
                elif(sword1number==8):
                    sword2upx=x1+8
                    sword2upy=y1+14
                elif(sword1number==14):
                    sword3upx=x1+8
                    sword3upy=y1+14

                    
            elif p2direction==2:
                sword2number+=2
                if(sword2number==20):
                    sword2number=0
                if(sword2number==2):
                    sword1leftx=x1+13
                    sword1lefty=y1+14
                elif(sword2number==8):
                    sword2leftx=x1+13
                    sword2lefty=y1+14
                elif(sword2number==14):
                    sword3leftx=x1+13
                    sword3lefty=y1+14


            elif p2direction==3:
                sword3number+=2
                if(sword3number==20):
                    sword3number=0
                if(sword3number==2):
                    sword1rightx=x1+13
                    sword1righty=y1+14
                elif(sword3number==8):
                    sword2rightx=x1+13
                    sword2righty=y1+14
                elif(sword3number==14):
                    sword3rightx=x1+13
                    sword3righty=y1+14

                    
            else: 
                sword4number+=2
                if(sword4number==20):
                    sword4number=0
                if(sword4number==2):
                    sword1downx=x1+8
                    sword1downy=y1+14
                elif(sword4number==8):
                    sword2downx=x1+8
                    sword2downy=y1+14
                elif(sword4number==14):
                    sword3downx=x1+8
                    sword3downy=y1+14      

#寶劍移動
    sword1upy-=6
    sword1leftx-=6
    sword1rightx+=6
    sword1downy+=6
    sword2upy-=6
    sword2leftx-=6
    sword2rightx+=6
    sword2downy+=6
    sword3upy-=6
    sword3leftx-=6
    sword3rightx+=6
    sword3downy+=6
    
#Player1扣血
    
    sword1upx,sword1upy= P1hurt(sword1upx,sword1upy)
    sword2upx,sword2upy= P1hurt(sword2upx,sword2upy)
    sword3upx,sword3upy= P1hurt(sword3upx,sword3upy)
    sword1leftx,sword1lefty= P1hurt(sword1leftx,sword1lefty)
    sword2leftx,sword2lefty= P1hurt(sword2leftx,sword2lefty)
    sword3leftx,sword3lefty= P1hurt(sword3leftx,sword3lefty)
    sword1rightx,sword1righty= P1hurt(sword1rightx,sword1righty)
    sword2rightx,sword2righty= P1hurt(sword2rightx,sword2righty)
    sword3rightx,sword3righty= P1hurt(sword3rightx,sword3righty)
    sword1downx,sword1downy= P1hurt(sword1downx,sword1downy)
    sword2downx,sword2downy= P1hurt(sword2downx,sword2downy)
    sword3downx,sword3downy= P1hurt(sword3downx,sword3downy)
    
# Check off screen
    x1,y1 = checkOffscreen(x1,y1)
   
    lox,loy=checkOffscreen(lox,loy)

#火球判定---------------------------------------------------------------    
    fire1upx,fire1upy =attackcheckOffscreen(fire1upx,fire1upy)
    fire2upx,fire2upy =attackcheckOffscreen(fire2upx,fire2upy)
    fire3upx,fire3upy =attackcheckOffscreen(fire3upx,fire3upy)
    fire1leftx,fire1lefty =attackcheckOffscreen(fire1leftx,fire1lefty)
    fire2leftx,fire2lefty =attackcheckOffscreen(fire2leftx,fire2lefty)
    fire3leftx,fire3lefty =attackcheckOffscreen(fire3leftx,fire3lefty)
    fire1rightx,fire1righty =attackcheckOffscreen(fire1rightx,fire1righty)
    fire2rightx,fire2righty =attackcheckOffscreen(fire2rightx,fire2righty)
    fire3rightx,fire3righty =attackcheckOffscreen(fire3rightx,fire3righty)
    fire1downx,fire1downy =attackcheckOffscreen(fire1downx,fire1downy)
    fire2downx,fire2downy =attackcheckOffscreen(fire2downx,fire2downy)
    fire3downx,fire3downy =attackcheckOffscreen(fire3downx,fire3downy)
#寶劍判定---------------------------------------------------------------    
    sword1upx,sword1upy =attackcheckOffscreen(sword1upx,sword1upy)
    sword2upx,sword2upy =attackcheckOffscreen(sword2upx,sword2upy)
    sword3upx,sword3upy =attackcheckOffscreen(sword3upx,sword3upy)
    sword1leftx,sword1lefty =attackcheckOffscreen(sword1leftx,sword1lefty)
    sword2leftx,sword2lefty =attackcheckOffscreen(sword2leftx,sword2lefty)
    sword3leftx,sword3lefty =attackcheckOffscreen(sword3leftx,sword3lefty)
    sword1rightx,sword1righty =attackcheckOffscreen(sword1rightx,sword1righty)
    sword2rightx,sword2righty =attackcheckOffscreen(sword2rightx,sword2righty)
    sword3rightx,sword3righty =attackcheckOffscreen(sword3rightx,sword3righty)
    sword1downx,sword1downy =attackcheckOffscreen(sword1downx,sword1downy)
    sword2downx,sword2downy =attackcheckOffscreen(sword2downx,sword2downy)
    sword3downx,sword3downy =attackcheckOffscreen(sword3downx,sword3downy)

#------------------------------

    # draw player
    screen.blit(image,(lox,loy))

    # draw player2
    screen.blit(p2image,(x1,y1))

    # draw fire
    screen.blit(fireup,(fire1upx,fire1upy))#向上1號火球
    screen.blit(fireup,(fire2upx,fire2upy))#向上2號火球
    screen.blit(fireup,(fire3upx,fire3upy))#向上3號火球
    screen.blit(fireleft,(fire1leftx,fire1lefty))#向左1號火球
    screen.blit(fireleft,(fire2leftx,fire2lefty))#向左2號火球
    screen.blit(fireleft,(fire3leftx,fire3lefty))#向左3號火球
    screen.blit(fireright,(fire1rightx,fire1righty))#向右1號火球
    screen.blit(fireright,(fire2rightx,fire2righty))#向右2號火球
    screen.blit(fireright,(fire3rightx,fire3righty))#向右3號火球
    screen.blit(firedown,(fire1downx,fire1downy))#向下1號火球
    screen.blit(firedown,(fire2downx,fire2downy))#向下2號火球
    screen.blit(firedown,(fire3downx,fire3downy))#向下2號火球

    screen.blit(swordup,(sword1upx,sword1upy))#向上1號寶劍
    screen.blit(swordup,(sword2upx,sword2upy))#向上2號寶劍
    screen.blit(swordup,(sword3upx,sword3upy))#向上3號寶劍
    screen.blit(swordleft,(sword1leftx,sword1lefty))#向左1號寶劍
    screen.blit(swordleft,(sword2leftx,sword2lefty))#向左2號寶劍
    screen.blit(swordleft,(sword3leftx,sword3lefty))#向左3號寶劍
    screen.blit(swordright,(sword1rightx,sword1righty))#向右1號寶劍
    screen.blit(swordright,(sword2rightx,sword2righty))#向右2號寶劍
    screen.blit(swordright,(sword3rightx,sword3righty))#向右3號寶劍
    screen.blit(sworddown,(sword1downx,sword1downy))#向下1號寶劍
    screen.blit(sworddown,(sword2downx,sword2downy))#向下2號寶劍
    screen.blit(sworddown,(sword3downx,sword3downy))#向下2號寶劍
    if(HPI<1):
        winop+=1
        if winop==1:
            pygame.mixer.music.load("win.mp3")
            pygame.mixer.music.play()
            screen.fill(black)
            screen.blit(Win2,(Win1x,Win1y))
        screen.fill(black)
        screen.blit(Win2,(Win1x,Win1y))
        text_surface = font.render("press esc to exit", True, (255, 255, 255))
        screen.blit(text_surface, (387, 467))
        
    if(HPII<1):
        winop+=1
        if winop==1:
            pygame.mixer.music.load("win.mp3")
            pygame.mixer.music.play()
            screen.fill(black)
            screen.blit(Win1,(Win1x,Win1y))
        screen.fill(black)
        screen.blit(Win1,(Win1x,Win1y))
        text_surface = font.render("press esc to exit", True, (255, 255, 255))
        screen.blit(text_surface, (387, 467))
            
        
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        
    clock.tick(32)
pygame.quit()

