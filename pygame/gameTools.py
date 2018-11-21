import pygame
import random
import numpy as np
import threading
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import cv2
import imutils
import pyttsx

# Define some colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)

lower = np.array([80,100,100])
upper = np.array([110,255,255])
kernel = np.ones((10,10),np.uint8)

#######################################
#class AppForm(QMainWindow):
class AppForm(QWidget):
    def __init__(self, game, parent=None):
        super(AppForm, self).__init__()
        #QMainWindow.__init__(self, parent)
        self.setWindowTitle('Main: ventana principal')
        self.create_main_frame()
        self.game = game
    def closeEvent(self, event):        
        reply = QMessageBox.question(self, 'Message',
            "Exit?", QMessageBox.Yes | 
            QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.game.stop=True
            event.accept() 
        else:
            event.ignore()  
                  
    def create_main_frame(self):
        self.main_frame = QWidget()
        self.l1 = QLabel("Nombre del jugador: ")
        self.e1 = QLineEdit()
        self.e1.setText('')
   
        self.l2 = QLabel("Edad: ")
        self.e2 = QLineEdit()
        self.e2.setText('')
        self.start_button = QPushButton("Iniciar")
        self.connect(self.start_button, SIGNAL('clicked()'), self.iniciar)
        vbox = QVBoxLayout()
        for w in [self.l1,self.e1,  self.l2,  self.e2,  self.start_button]:
            vbox.addWidget(w)
            vbox.setAlignment(w, Qt.AlignVCenter)
        
        #self.main_frame.setLayout(vbox)
        #self.setCentralWidget(self.main_frame)
        self.setLayout(vbox) 
        
        self.setGeometry(300, 300, 400, 450)
        self.show() #mostrar lo construido   
    def iniciar(self):
        #self.close()
        if self.game.stop:
            self.game.start()
            
        else:
            self.game.doneSesion=False
            
##########################################################################################             
class Player(pygame.sprite.Sprite):
    """
    This class represents the player
    """ 
    def __init__(self, color, width, height,image='bate.png'):
        pygame.sprite.Sprite.__init__(self) 
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        #self.image = pygame.Surface([width, height])
        self.image = pygame.image.load(image).convert()
        #self.image.fill(color) 
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()
        #self.cam = kinect_cam()
        return
    def update(self):
        #self.cam.get_depth()
        #pos=[cam.x,cam.y]
        pos = pygame.mouse.get_pos()            
        self.rect.x = pos[0]
        self.rect.y = pos[1]   
        
        return     
##########################################################################################        
class Item(pygame.sprite.Sprite):
    def __init__(self, filename, allowed=1):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)  
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.image.load(filename).convert()
        (h,w)=self.image.get_size()
        self.d=int(np.ceil(np.sqrt(h**2+w**2)))
        # Set background color to be transparent. Adjust to WHITE if your
        # background is WHITE.
        self.image.set_colorkey(BLACK)
 
        # Fetch the rectangle object that has the dimensions of the image       
        self.rect = self.image.get_rect()
        
        #allowed define si se puede o no tocar el bloque: 0 -> NO, 1 -> SI
        self.allowed = 0
    def reset_pos(self):
        self.rect.x =  random.randrange(self.screen_width-self.d) 
        self.rect.y =  self.d
        return
    def update(self):
        # Update the position of this object by setting the values 
        # of rect.x and rect.y
        self.rect.y += 1
        if self.rect.y > self.screen_height:
          self.reset_pos()
        return  
##############################################################################################
class mainGame(threading.Thread):
    def __init__(self,screen_width = 640, screen_height = 480,N=10, image1='frog2.png',  image2='frog2.png'):
        #Initialize Pygame
        threading.Thread.__init__(self)
        # Set the height and width of the screen
        self.N=N
        self.screen_width   = screen_width
        self.screen_height  = screen_height
        self.image1         = image1
        self.image2         = image2
        self.stop           = True
        self.doneSesion     = False
        self.MainWindow     = None
        self.engine         = pyttsx.init()                  #se inicializa un objeto tipo pyttsx
        voices = self.engine.getProperty('voices')           #optenemos la lista de voces
        spanish=voices[20]                                   #seleccionamos la 20 o 19, para espanol
        self.engine.setProperty('voice', spanish.id)         #ponemos espanol como voz a usar
        
    def initGame(self):
        pygame.init()
        self.screen = pygame.display.set_mode([self.screen_width, self.screen_height])
        # This is a list of 'sprites.' Each block in the program
        self.block_list = pygame.sprite.Group()
        # All blocks and the player block as well.
        self.all_sprites_list = pygame.sprite.Group()
        pos = []
        for i in range(self.N + self.N/2):
            # This represents a block, you need to define an image
            if i<self.N:
                    block = Item(self.image1)
                    block.allowed = 1                                        
            else:
                    block = Item(self.image2)            
                    block.allowed = 0
            block.screen_height=self.screen_height
            block.screen_width =self.screen_width
            touch=True
            # Set a random location for the block        
            if i==0:
                block.rect.x = random.randrange(self.screen_width-block.d)
                block.rect.y = random.randrange(self.screen_height-block.d)                
                pos.append(np.array([block.rect.x,block.rect.y]))
            else:
                while touch:
                    x = random.randrange(self.screen_width-block.d)
                    y = random.randrange(self.screen_height-block.d)
                    p = np.array([x,y])
                    d=np.sqrt(np.sum((p-np.array(pos))**2,1))
                    touch = np.any(d<block.d)

                block.rect.x  = x
                block.rect.y  = y

                pos.append(p)
            # Add the block to the list of objects
            self.block_list.add(block)
            self.all_sprites_list.add(block) 
        # Create a player block
        self.player = Player(RED, 20, 15)
        self.all_sprites_list.add(self.player)

        self.doneSesion = False
        # Used to manage how fast the screen updates
        self.clock = pygame.time.Clock() 
        self.score = 0
        self.NotScore = 0
        
    def quit(self):
        self.MainWindow.show()
        pygame.quit()
        
    def startGame(self):
        # -------- Main Program Loop -----------
        font = pygame.font.Font('slkscr.ttf', 20)
        # Loop until the user clicks the close button or session is finished 
        while not self.doneSesion:
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT: 
                    self.doneSesion = True
                    
            # Clear the screen and draw items
            self.screen.fill(WHITE) 
            self.all_sprites_list.update()        
            # See if the player block has collided with anything.
            blocks_hit_list = pygame.sprite.spritecollide(self.player, self.block_list, True)
            # Check the list of collisions.
            for block in blocks_hit_list:
                if block.allowed == 0:
                        #add again the block to the list so it does not disapear
                        self.block_list.add(block)
                        self.all_sprites_list.add(block)
                        self.NotScore += 1
                        self.engine.say("No")
                        self.engine.runAndWait()  
                    
                else:                
                        self.score += 1
            text1 = "Score 1: " + str(self.score) + " puntos"
            text2 = "Score 2: " + str(self.NotScore) + " puntos negativos"

            #print(score)
            self.screen.blit(font.render(text1, 1, (0, 255, 0)), (30, 30))
            self.screen.blit(font.render(text2, 1, (0, 255, 0)), (30, 50))
            # Draw all the spites
            self.all_sprites_list.draw(self.screen)
 
            # update the screen 
            pygame.display.flip()
 
            # Limit to 60 frames per second
            self.clock.tick(60)
 
        self.quit()
    
    def run(self):
        self.stop=False        
        while not self.stop:
            if not self.doneSesion:
                self.initGame()
                self.startGame()
#################################################################################################
#### camera functions
class CAM(): 
    def __init__(self):
        self.isopen        = True
        self.rgb           = np.array([])
        self.depth         = np.array([])
        self.gray          = np.array([])
        self.convert_rgb   = True
        self.convert_depth = True
        self.window        = None
        self.trh           = 50
        self.filterSize    = 10
        self.ap_mask       = True
        self.filter        = True
        self.m             = 1.0
        self.b             = 0.0
        self.mask          = 255
        self.kernel        = np.ones((5, 5), np.uint8)
        self.x             = 0
        self.y             = 0
        #webcam
        self.cap = cv2.VideoCapture(0)
    #function to get RGB image from webcam    
    def get_cam(self):
        _, self.rgb = cap.read()
        if self.rgb is None:
           self.rgb = np.array([])
        elif self.convert_rgb:                   
           hsv          = cv2.cvtColor(self.rgb, cv2.COLOR_BGR2HSV)
           mask         = cv2.inRange(hsv, lower, upper)
           res          = cv2.bitwise_and(self.rgb,self.rgb, mask= mask)
           self.gray    = cv2.cvtColor(res,cv2.COLOR_BGR2GRAY)    
           self.process()
        return 
  
    #function to get depth image from kinect
    def get_depth(self):
        self.depth,_ = freenect.sync_get_depth()
        if self.depth is None:
           self.depth = np.array([])
        if self.convert_depth:   
        #clip max depth to 1023, convert to 8-bit grayscale
            np.clip(self.depth,0,2**10-1, self.depth)
            self.depth >>= 2
            self.depth = self.depth.astype(np.uint8)
        if self.ap_mask:
              self.depth = self.mask - self.depth        
        #self.depth_p = self.depth*self.m+self.b
        self.gray = cv2.flip( self.depth, 1 ) #cv2.cvtColor(self.depth, cv2.COLOR_BGR2GRAY);
        self.process()
        return    
    #pre-process image
    def process(self):
        
        if self.filter:
                self.gray   = cv2.GaussianBlur(self.gray,(self.filterSize,self.filterSize),0)
                
        _,self.img_wb = cv2.threshold(self.gray, self.trh, 255, cv2.THRESH_BINARY)
        self.img_wb = cv2.morphologyEx(self.img_wb, cv2.MORPH_CLOSE, self.kernel)
        cnts = cv2.findContours(self.img_wb.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if imutils.is_cv2() else cnts[1]
        # ensure that at least one contour was found
        if len(cnts) > 0:
            # sort the contours according to their size in
            # descending order
            cnts = sorted(cnts, key=cv2.contourArea, reverse=True)
            c = cnts[0]  
            # compute the center of the contour
            M = cv2.moments(c)
            try:
             cX = int(M["m10"] / M["m00"])
             cY = int(M["m01"] / M["m00"])
             self.x=cX
             self.y=cY
            except:
             pass
                      
        return 
