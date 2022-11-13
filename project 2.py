

import pygame
import random
import time



pygame.init()
screen = pygame.display.set_mode((1200, 700))
 
image_string={"1🔸":r"./images/AD.png",
              "2🔸":r"./images/2D.png",
              "3🔸":r"./images/3D.png",
              '4🔸':r"./images/4D.png",
              '5🔸':r"./images/5D.png",
              '6🔸':r"./images/6D.png",
              '7🔸':r"./images/7D.png",
              '8🔸':r"./images/8D.png",
              '9🔸':r"./images/9D.png",
              '10🔸':r"./images/10D.png",
              '11🔸':r"./images/JD.png",
              '12🔸' :r"./images/QD.png",
              '13🔸':r"./images/KD.png",
              
              "1❤":r"./images/AH.png",
              "2❤":r"./images/2H.png",
              "3❤":r"./images/3H.png",
              '4❤':r"./images/4H.png",
              '5❤':r"./images/5H.png",
              '6❤':r"./images/6H.png",
              '7❤':r"./images/7H.png",
              '8❤':r"./images/8H.png",
              '9❤':r"./images/9H.png",
              '10❤':r"./images/10H.png",
              '11❤':r"./images/JH.png",
              '12❤':r"./images/QH.png",
              '13❤':r"./images/KH.png",
              
              "1☘":r"./images/AC.png",
              "2☘":r"./images/2C.png",
              "3☘":r"./images/3C.png",
              '4☘':r"./images/4C.png",
              '5☘':r"./images/5C.png",
              '6☘':r"./images/6C.png",
              '7☘':r"./images/7C.png",
              '8☘':r"./images/8C.png",
              '9☘':r"./images/9C.png",
              '10☘':r"./images/10C.png",
              '11☘':r"./images/JC.png",
              '12☘':r"./images/QC.png",
              '13☘':r"./images/KC.png",
              
              "1 ":r"./images/AS.png",
              "2 ":r"./images/2S.png",
              "3 ":r"./images/3S.png",
              '4 ':r"./images/4S.png",
              '5 ':r"./images/5S.png",
              '6 ':r"./images/6S.png",
              '7 ':r"./images/7S.png",
              '8 ':r"./images/8S.png",
              '9 ':r"./images/9S.png",
              '10 ':r"./images/10S.png",
              '11 ':r"./images/JS.png",
              '12 ':r"./images/QS.png",
              '13 ':r"./images/KS.png",
              
              }
        

def welcome_screen():
       
    screen.fill('red')
    welcome_image=pygame.image.load(r"./images/welcome_image.png")
    screen.blit(welcome_image,(0,20))
    pygame.display.set_caption('welcome')
    pygame.display.update()
    

    
    pygame.display.flip()
    
    
    ru=True
    
    while ru:
        
        pygame.display.flip()
        mouse_pos=pygame.mouse.get_pos()
                
        for e in pygame.event.get():
            
            if e.type==pygame.QUIT:
                pygame.quit()
                ru=False
                
            if mouse_pos[0] in range(490,720) and mouse_pos[1] in range(360,425):
                
                if pygame.mouse.get_pressed()[0]==1 :
                    ru=False                                    
                    return 'play'
                
            if mouse_pos[0] in range(490,720) and mouse_pos[1] in range(440,505):
    
                if pygame.mouse.get_pressed()[0]==1 :
                    return 'how_to_play'
                
                
            if mouse_pos[0] in range(490,720) and mouse_pos[1] in range(530,595):
                
                if pygame.mouse.get_pressed()[0]==1 :
                    ru=False
                    return 'quit'
 
# card shuffle method

def shufflePack(l):
    newPack=[]
    total=len(l)
    
    for i in range(0,total):
        n=random.randint(0,len(l)-1)
        newPack.append(l[n])
        l.pop(n)
    
    return newPack



# set images on GUI

def bind_images_User1(l1,screen,image_string):
    card1=pygame.image.load(image_string.get(l1[0]))
    card2=pygame.image.load(image_string.get(l1[1]))
    card3=pygame.image.load(image_string.get(l1[2]))
    card4=pygame.image.load(image_string.get(l1[3]))
    screen.blit(card1,(70,470))
    screen.blit(card2,(190,470))
    screen.blit(card3,(310,470))
    screen.blit(card4,(430,470))
    
    
    
def bind_images_User2(l1,screen,image_string):
        card5=pygame.image.load(image_string.get(l1[0]))
        card6=pygame.image.load(image_string.get(l1[1]))
        card7=pygame.image.load(image_string.get(l1[2]))
        card8=pygame.image.load(image_string.get(l1[3]))
        screen.blit(card5,(670,470))
        screen.blit(card6,(790,470))
        screen.blit(card7,(910,470))
        screen.blit(card8,(1030,470))
     
# random card for selection
     
def random_card(pack,pre):
    n=random.randint(0,len(pack)-1)

    
    if (n==pre):
        return random_card(pack,pre)
     
    else:
        main_card=pygame.image.load(image_string.get(pack[n]))
        screen.blit(main_card,(550,100))
        return n        
       
        
def change_card(num,pack,user,n):
    num=num-1
    pack.append(user.pop(num))
    user.insert(num,pack[n])
    pack.pop(n)
   

def display_winner(w):
    
    player1_name='Player 1'
    player2_name='Player 2'
        
    
    
    try:        
        screen.fill('Blue')
        winner_bg=pygame.image.load(r"./images/winner_bg.png")
        screen.blit(winner_bg,(0,0))
    

        pygame.draw.rect(screen,'green',pygame.rect.Rect(200,250,150,30))
        text_1=pygame.font.SysFont('carbel',50)
        t=text_1.render("Winner :- ",False,'Black')
        screen.blit(t,(200,250))
    
    
    
        if (w==1):
            text_winner_name=pygame.font.SysFont('carbel',50)
            text=text_winner_name.render(player1_name,False,'Black')
            screen.blit(text,(250,300))
        elif (w==2):
            text_winner_name=pygame.font.SysFont('carbel',50)
            text=text_winner_name.render(player2_name,False,'Black')
            screen.blit(text,(250,300))
        
    except Exception:
        pass
    
    
    
    pygame.display.flip()
    r=True
    while r:
        
        for event in pygame.event.get():
            
            if event.type==pygame.QUIT:
                r=False
                 
#how to play button game loop 
def how_to_play():
    
    screen.fill('orange')
    
    how_to_play_image=pygame.image.load(r"./images/how_to_play.png")
    screen.blit(how_to_play_image,(0,0))
    

    
    
    pygame.display.update()
    
    run=True
    while run:
        pygame.display.flip()
        mouse_pos=pygame.mouse.get_pos()
        
        for e in pygame.event.get():
            
            if e.type==pygame.QUIT :
                run=False
                
            if mouse_pos[0] in range(464,652) and mouse_pos[1] in range(612,667):
                
                if pygame.mouse.get_pressed()[0]==1:
                    run=False
    
def main_game():
    
    background_colour ='green'
    screen.fill(background_colour)
    pygame.display.set_caption('Card game')
    pygame.display.flip()
    
    
# card pack GUI
    pygame.draw.rect(screen,'red',pygame.Rect(550,100,104,160))
    card_pack_image=pygame.image.load(r"./images/cardPack.png")
    screen.blit(card_pack_image,(545,98))


# Red color GUI
    pygame.draw.rect(screen,'red',pygame.Rect(50,450,500,200))
    pygame.draw.rect(screen,'red',pygame.Rect(650,450,500,200))



# button for skip
    pygame.draw.rect(screen,'Blue',pygame.Rect(550,400,90,40))
    text_skip=pygame.font.SysFont('carbel',50)
    text=text_skip.render('SKIP',False,'Black')
    screen.blit(text,(555,400))


#   indicate rects
    indicate_image=pygame.image.load(r"./images/indicate_user.png")
    screen.blit(indicate_image,(500,420))
    
    hide_indicate_image=pygame.image.load(r"./images/hide_indicate.png")
    screen.blit(hide_indicate_image,(700,420))
    
    
# string and image relation
    
    pack=["1🔸","2🔸","3🔸",'4🔸','5🔸','6🔸','7🔸','8🔸','9🔸','10🔸','11🔸','12🔸'
          ,'13🔸',"1❤","2❤","3❤",'4❤','5❤','6❤','7❤','8❤','9❤','10❤','11❤','12❤','13❤',
          "1☘","2☘","3☘",'4☘','5☘','6☘','7☘','8☘','9☘','10☘','11☘','12☘','13☘',
          "1 ","2 ","3 ",'4 ','5 ','6 ','7 ','8 ' ,'9 ','10 ','11 ','12 ','13 ']


    user1=[]
    user2=[]



    for i in range(4):
        n=random.randint(0,len(pack)-1)
        user1.append(pack[n])
        pack.pop(n)
    
    
    
        n=random.randint(0,len(pack)-1)
        user2.append(pack[n])
        pack.pop(n)
    
   
    bind_images_User1(user1,screen,image_string)
    bind_images_User2(user2,screen,image_string)


    n=random_card(pack,-1)
    ready_user1=True
    ready_user2=False
    w=0
    run=True
    while run:
        main_mouse_pos=pygame.mouse.get_pos()
        
        pygame.display.flip()
        
        
        for event in pygame.event.get():
            
            if event.type==pygame.QUIT:
                
                run=False
                
                
            if main_mouse_pos[0] in range(50,550) and main_mouse_pos[1] in range(450,650):
               
                
                if main_mouse_pos[0] in range(70,174) and main_mouse_pos[1] in range(470,630):
                    if pygame.mouse.get_pressed()[0]==1  and ready_user1==True:
                       
                        change_card(1,pack,user1,n)
                        bind_images_User1(user1,screen,image_string)
                        n=random_card(pack,n)
                        ready_user1=False
                        ready_user2=True
                    
                                      
                    
                
                if main_mouse_pos[0] in range(190,294) and main_mouse_pos[1] in range(470,630):
                    if pygame.mouse.get_pressed()[0]==1 and ready_user1==True:
                       
                        change_card(2,pack,user1,n)
                        bind_images_User1(user1,screen,image_string)
                        n=random_card(pack,n)
                        ready_user1=False
                        ready_user2=True
            
                if main_mouse_pos[0] in range(310,414) and main_mouse_pos[1] in range(470,630):
                    if pygame.mouse.get_pressed()[0]==1 and ready_user1==True:
                        change_card(3,pack,user1,n)
                       
                        bind_images_User1(user1,screen,image_string)
                        n=random_card(pack,n)
                        ready_user1=False
                        ready_user2=True
            
                if main_mouse_pos[0] in range(430,534) and main_mouse_pos[1] in range(470,630):
                    if pygame.mouse.get_pressed()[0]==1 and ready_user1==True:
                       
                        change_card(4,pack,user1,n)
                        bind_images_User1(user1,screen,image_string)
                        n=random_card(pack,n)
                        ready_user1=False
                        ready_user2=True
            
            if main_mouse_pos[0] in range(650,1150) and main_mouse_pos[1] in range(450,650) :
               
                
                if main_mouse_pos[0] in range(670,774) and main_mouse_pos[1] in range(470,630):
                    if pygame.mouse.get_pressed()[0]==1 and ready_user2==True:
                       
                        change_card(1,pack,user2,n)
                        bind_images_User2(user2,screen,image_string)
                        n=random_card(pack,n)
                        ready_user1=True
                        ready_user2=False
                
                if main_mouse_pos[0] in range(790,894) and main_mouse_pos[1] in range(470,630):
                    if pygame.mouse.get_pressed()[0]==1 and ready_user2==True:
                       
                        change_card(2,pack,user2,n)
                        bind_images_User2(user2,screen,image_string)
                        n=random_card(pack,n)
                        ready_user1=True
                        ready_user2=False
            
                if main_mouse_pos[0] in range(910,1014) and main_mouse_pos[1] in range(470,630):
                    if pygame.mouse.get_pressed()[0]==1 and ready_user2==True:
                        
                        change_card(3,pack,user2,n)
                        bind_images_User2(user2,screen,image_string)
                        n=random_card(pack,n)
                        ready_user1=True
                        ready_user2=False
            
                if main_mouse_pos[0] in range(1030,1134) and main_mouse_pos[1] in range(470,630):
                    if pygame.mouse.get_pressed()[0]==1 and ready_user2==True:
                        
                        change_card(4,pack,user2,n)
                        bind_images_User2(user2,screen,image_string)
                        n=random_card(pack,n)
                        ready_user1=True
                        ready_user2=False
                        
                        
            if main_mouse_pos[0] in range(550,640) and main_mouse_pos[1] in range(400,440):
                # skip
                
                if pygame.mouse.get_pressed()[0]==1:
                    
                    if ready_user1==True:
                        ready_user1=False
                        ready_user2=True
                    else:
                        ready_user2=False
                        ready_user1=True 
                    
                    pack=shufflePack(pack)
                    n=random_card(pack,n)
                    time.sleep(0.3)
                        
            
            if ready_user1==True:
                screen.blit(indicate_image,(500,420))
                screen.blit(hide_indicate_image,(700,420))
                
                
                
            if ready_user2==True:
                screen.blit(indicate_image,(700,420))
                screen.blit(hide_indicate_image,(500,420))
                
            
           
                    
            if(user1[0][0]==user1[1][0]==user1[2][0]==user1[3][0]):
                
                if(user1[0][1] in ['0','1','2','3'] or user1[1][1] in ['0','1','2','3'] or user1[2][1] in ['0','1','2','3'] or user1[3][1] in ['0','1','2','3']):                    
                    if(user1[0][1]==user1[1][1]==user1[2][1]==user1[3][1]):
                        run=False
                        w=1
                else:
                    run=False
                    w=1
                
                
    
            if(user2[0][0]==user2[1][0]==user2[2][0]==user2[3][0]):
                
                if(user2[0][1] in ['0','1','2','3'] or user2[1][1] in ['0','1','2','3'] or user2[2][1] in ['0','1','2','3'] or  user2[3][1] in ['0','1','2','3']):                    
                    if (user2[0][1]==user2[1][1]==user2[2][1]==user2[3][1]):
                        run=False
                        w=2
                else:
                    run=False
                    w=2
                
                
                
                
                
                
    if w==1:
        return display_winner(1)
    elif w==2:
        return display_winner(2)
        


background_colour ='green'
screen.fill(background_colour)
pygame.display.set_caption('Card game')
pygame.display.flip()

#  for Running game 

s=True
running = True
while running:
    
    try:
        
        for event in pygame.event.get():
            
            if event.type==pygame.QUIT:
                s=False
                running=False   
        
            if s==True:
                y=welcome_screen()  
                s=False          
            
            if(y=='play'):
               
                main_game()
                s=True
                
            if y=='how_to_play':
                how_to_play()
                s=True
            
            if y=='quit':
                running=False
                s=False
         
    
    
    except Exception:
        
        pass
                
                    
              
            
        
        
            
        
      
            
    
	
        
        
   
      
        
        
        
        
        
