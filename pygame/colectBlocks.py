import pygame
import sys, os, random
import numpy as np
import cv2
##
sys.path.append('/usr/local/lib/python2.7/dist-packages/')
import freenect
import imutils

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

class kinect_cam(): 
    def __init__(self):
        self.isopen        = True
        self.rgb           = np.array([])
        self.depth         = np.array([])
        self.convert_rgb   = True
        self.convert_depth = True
        self.window        = None
        self.trh           = 100 
        self.filterSize    = 10
        self.ap_mask       = True
        self.filter        = True
        self.m             = 1.0
        self.b             = 0.0
        self.mask          = 255
        self.kernel        = np.ones((5, 5), np.uint8)
        self.x             = 0
        self.y             = 0

    #function to get RGB image from kinect    
    def get_video(self):
        self.rgb,_ = freenect.sync_get_video()
        if self.rgb is None:
           self.rgb = np.array([])
        if self.convert_rgb:
            self.rgb = cv2.cvtColor(self.rgb,cv2.COLOR_RGB2BGR)
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
        self.process()
        return    
#pre-process image
    def process(self):
        if self.ap_mask:
              self.depth = self.mask - self.depth
        
        #self.depth_p = self.depth*self.m+self.b
        self.img_g = cv2.flip( self.depth, 1 ) #cv2.cvtColor(self.depth, cv2.COLOR_BGR2GRAY);
        
        if self.filter:
          self.img_g = cv2.blur(self.img_g,(self.filterSize,self.filterSize))                

        self.img_wb = cv2.threshold(self.img_g, self.trh, 255, cv2.THRESH_BINARY)[1]
        #self.img_wb = cv2.cvtColor(self.img_wb, cv2.COLOR_BGR2GRAY);
        self.img_wb = cv2.morphologyEx(self.img_wb, cv2.MORPH_CLOSE, self.kernel)
        cnts = cv2.findContours(self.img_wb.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if imutils.is_cv2() else cnts[1]
        # ensure that at least one contour was found
        if len(cnts) > 0:
            # sort the contours according to their size in
            # descending order
            cnts = sorted(cnts, key=cv2.contourArea, reverse=True)
        
#        for c in cnts:
            c = cnts[0]  
            # compute the center of the contour
            M = cv2.moments(c)
            try:
             cX = int(M["m10"] / M["m00"])
             cY = int(M["m01"] / M["m00"])
             self.x=cX
             self.y=cY
             if not(self.window == None):
                # draw the contour and center of the shape on the image             
                cv2.drawContours(self.img_g, [c], -1, (0, 255, 0), 2)
                cv2.circle(self.img_g, (cX, cY), 7, (255, 255, 255), -1)
                cv2.putText(self.img_g, "center", (cX - 20, cY - 20),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (100, 100, 100), 2)
                IMG=np.hstack((self.img_wb,self.img_g))            
                self.window.on_draw(IMG)
            except:
             pass
                       
        return 
        
         
# Initialize Pygame
pygame.init()
 
# Set the height and width of the screen
screen_width =  2*640
screen_height = 2*480
screen = pygame.display.set_mode([screen_width, screen_height])
 
# This is a list of 'sprites.' Each block in the program is
# added to this list. The list is managed by a class called 'Group.'
block_list = pygame.sprite.Group()
 
# This is a list of every sprite. 
# All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()
N=50
pos = []

for i in range(N):
    # This represents a block
    # block = Block(BLACK, 20, 15)
    block = Frog('frog1.png')
 
    # Set a random location for the block
    touch=True
    
    if i==0:
        block.rect.x = random.randrange(screen_width-block.d)
        block.rect.y = random.randrange(screen_height-block.d)
        pos.append(np.array([block.rect.x,block.rect.y]))
    else:
        while touch:
              x = random.randrange(screen_width-block.d)
              y = random.randrange(screen_height-block.d)
              p = np.array([x,y])
              d=np.sqrt(np.sum((p-np.array(pos))**2,1))
              touch = np.any(d<block.d)

        block.rect.x = x
        block.rect.y = y
        pos.append(p)
    # Add the block to the list of objects
    block_list.add(block)
    all_sprites_list.add(block)
 
# Create a RED player block
player = Block(RED, 20, 15)
all_sprites_list.add(player)
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
score = 0
 
# -------- Main Program Loop -----------
text = "Score: 0 puntos"
cam = kinect_cam()
font = pygame.font.Font('slkscr.ttf', 42)
while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True
 
    # Clear the screen
    screen.fill(WHITE)
 
    # Get the current hand position
    cam.get_depth()
    player.rect.x = 2*cam.x
    player.rect.y = 2*cam.y

    # See if the player block has collided with anything.
    blocks_hit_list = pygame.sprite.spritecollide(player, block_list, True)
 
    # Check the list of collisions.
    
    for block in blocks_hit_list:
        score += 1
        text = "Score: " + str(score) + " puntos"

        #print(score)
    screen.blit(font.render(text, 1, (0, 255, 0)), (30, 30))
    # Draw all the spites
    all_sprites_list.draw(screen)
 
    # update the screen 
    pygame.display.flip()
 
    # Limit to 60 frames per second
    clock.tick(60)
 
pygame.quit()
