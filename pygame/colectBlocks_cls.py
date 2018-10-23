import pygame
import sys, os, random
import numpy as np
import cv2
sys.path.append('/usr/local/lib/python2.7/dist-packages/')
import freenect
import imutils
import threading
from PyQt4.QtCore import *
from PyQt4.QtGui import *
# Define some colors


BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
 
class Block(pygame.sprite.Sprite):
    """
    This class represents the player
    """
 
    def __init__(self, color, width, height):
        """ Constructor. Pass in the color of the block,
        and its x and y position. """
        pygame.sprite.Sprite.__init__(self) 
        # Call the parent class (Sprite) constructor
        #super().__init__()
 
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
 
        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()
##############################        
class Frog(pygame.sprite.Sprite):
     def __init__(self, filename):
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
        # image.
        # Update the position of this object by setting the values 
        # of rect.x and rect.y
        self.rect = self.image.get_rect()
################################################################
class mainGame(threading.Thread):
    def __init__(self,screen_width =  640, screen_height = 480,N=10, image='frog2.png'):
        #Initialize Pygame
        threading.Thread.__init__(self)
        # Set the height and width of the screen
        self.N=N
        self.screen_width   = screen_width
        self.screen_height  = screen_height
        self.image          = image
        self.stop           = True
        self.doneSesion     = False

        self.MainWindow     = None
    def initGame(self):
        pygame.init()
        self.screen = pygame.display.set_mode([self.screen_width, self.screen_height])
        # This is a list of 'sprites.' Each block in the program
        self.block_list = pygame.sprite.Group()
        # All blocks and the player block as well.
        self.all_sprites_list = pygame.sprite.Group()
        pos = []
        for i in range(self.N):
            # This represents a block, you need to define an image
            block = Frog(self.image)
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

                block.rect.x = x
                block.rect.y = y
                pos.append(p)
            # Add the block to the list of objects
            self.block_list.add(block)
            self.all_sprites_list.add(block)
 
        # Create a RED player block
        self.player = Block(RED, 20, 15)
        self.all_sprites_list.add(self.player)
 
        # Loop until the user clicks the close button.
        self.doneSesion = False
        # Used to manage how fast the screen updates
        self.clock = pygame.time.Clock() 
        self.score = 0
        
    def quit(self):
        self.MainWindow.show()
        pygame.quit()
        
    def startGame(self):
        # -------- Main Program Loop -----------
        text = "Score: 0 puntos"
        #cam = kinect_cam()
        font = pygame.font.Font('slkscr.ttf', 30)
        while not self.doneSesion:
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT: 
                    self.doneSesion = True
                    
            # Clear the screen
            self.screen.fill(WHITE)
 
            # Get the current hand position
            #cam.get_depth()
            #pos=[cam.x,cam.y]
            pos = pygame.mouse.get_pos()
            
            self.player.rect.x = pos[0]
            self.player.rect.y = pos[1]

            # See if the player block has collided with anything.
            blocks_hit_list = pygame.sprite.spritecollide(self.player, self.block_list, True)
    
            # Check the list of collisions.
    
            for block in blocks_hit_list:
                self.score += 1
            text = "Score: " + str(self.score) + " puntos"

            #print(score)
            self.screen.blit(font.render(text, 1, (0, 255, 0)), (30, 30))
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
            
        
def main():    
    
    game=mainGame(screen_width =  840, screen_height = 680,N=10, image='frog2.png')
    app = QApplication(sys.argv)
    form = AppForm(game)
    game.MainWindow=form
    
    sys.exit(app.exec_())



if __name__ == '__main__':
    main()        
