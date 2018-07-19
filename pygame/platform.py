import pygame
import sys, os, random
import numpy as np
import cv2
##
sys.path.append('/usr/local/lib/python2.7/dist-packages/')
import freenect
import imutils
from collections import deque
 
# Global constants
 
# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
 
# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
####################################################################33          
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
        self.up            = False
        self.left          = False
        self.right         = False        
        self.down          = False
        self.on_move       = False
        self.buffer        = 15
        self.pts           = deque(maxlen=self.buffer)
        self.counter       = 0
        self.direction     = ""
        self.epsilon       = 40
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
    def movement(self):
        
        if (len(self.pts) == self.buffer):
            # compute the difference between the x and y
            # coordinates and re-initialize the direction
            # text variables
            dX = self.pts[-self.buffer][0] - self.pts[-1][0]
            dY = self.pts[-self.buffer][1] - self.pts[-1][1]
            
            (dirX, dirY) = ("", "")
                
            # ensure there is significant movement in the
            # x-direction
            if np.abs(dX) > self.epsilon:
                self.left  = np.sign(dX)==-1
                self.right = np.sign(dX)==1
                dirX = "Izquierda" if self.left else "Derecha"
            else:
                self.left  = False
                self.right = False
                
            # ensure there is significant movement in the
            # y-direction
            if np.abs(dY) > self.epsilon:
                self.up   = np.sign(dY)==-1
                self.down = np.sign(dY)==1
                dirY = "Arriba" if np.sign(dY) == -1 else "Abajo"
            else: 
                self.up   = False
                self.down = False
 
            # handle when both directions are non-empty
            if dirX != "" and dirY != "":
                self.direction = "{}-{}".format(dirY, dirX)
 
            # otherwise, only one direction is non-empty
            else:
                self.direction = dirX if dirX != "" else dirY
                
        self.counter+=1
        self.on_move = self.up or self.down or self.left or self.right
        return
           
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
        self.x0=self.x
        self.y0=self.y
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
             self.pts.appendleft((cX,cY))
             if not(self.window == None):
                # draw the contour and center of the shape on the image             
                cv2.drawContours(self.img_g, [c], -1, (0, 255, 0), 2)
                cv2.circle(self.img_g, (cX, cY), 7, (255, 255, 255), -1)
                cv2.putText(self.img_g, "center", (cX - 20, cY - 20),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (100, 100, 100), 2)
                self.window.on_draw(self.img_g)
            except:
             pass
        self.movement()
        return 
####################################################################33         
class Player(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the player
        controls. """
 
    # -- Methods
    def __init__(self):
        """ Constructor function """
 
        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self) 
 
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        width = 40
        height = 60
        self.image = pygame.Surface([width, height])
        self.image.fill(RED)
 
        # Set a referance to the image rect.
        self.rect = self.image.get_rect()
 
        # Set speed vector of player
        self.change_x = 0
        self.change_y = 0
 
        # List of sprites we can bump against
        self.level = None
 
    def update(self):
        """ Move the player. """
        # Gravity
        self.calc_grav()
 
        # Move left/right
        self.rect.x += self.change_x
 
        # See if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right
 
        # Move up/down
        self.rect.y += self.change_y
 
        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
 
            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom
 
            # Stop our vertical movement
            self.change_y = 0
 
    def calc_grav(self):
        """ Calculate effect of gravity. """
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .35
 
        # See if we are on the ground.
        if self.rect.y >= SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = SCREEN_HEIGHT - self.rect.height
 
    def jump(self):
        """ Called when user hits 'jump' button. """
 
        # move down a bit and see if there is a platform below us.
        # Move down 2 pixels because it doesn't work well if we only move down
        # 1 when working with a platform moving down.
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2
 
        # If it is ok to jump, set our speed upwards
        if len(platform_hit_list) > 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.change_y = -10
 
    # Player-controlled movement:
    def go_left(self):
        """ Called when the user hits the left arrow. """
        self.change_x = -6
 
    def go_right(self):
        """ Called when the user hits the right arrow. """
        self.change_x = 6
 
    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.change_x = 0
 
 
class Platform(pygame.sprite.Sprite):
    """ Platform the user can jump on """
 
    def __init__(self, width, height):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this
            code. """
        pygame.sprite.Sprite.__init__(self) 
 
        self.image = pygame.Surface([width, height])
        self.image.fill(GREEN)
 
        self.rect = self.image.get_rect()
 
 
class Level(object):
    """ This is a generic super-class used to define a level.
        Create a child class for each level with level-specific
        info. """
 
    def __init__(self, player):
        """ Constructor. Pass in a handle to player. Needed for when moving platforms
            collide with the player. """
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.player = player
         
        # Background image
        self.background = None
 
    # Update everythign on this level
    def update(self):
        """ Update everything in this level."""
        self.platform_list.update()
        self.enemy_list.update()
 
    def draw(self, screen):
        """ Draw everything on this level. """
 
        # Draw the background
        screen.fill(BLUE)
 
        # Draw all the sprite lists that we have
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)
 
 
# Create platforms for the level
class Level_01(Level):
    """ Definition for level 1. """
 
    def __init__(self, player):
        """ Create level 1. """
 
        # Call the parent constructor
        Level.__init__(self, player)
 
        # Array with width, height, x, and y of platform
        level = [[210, 70, 500, 500],
                 [210, 70, 200, 400],
                 [210, 70, 600, 300],
                 ]
 
        # Go through the array above and add platforms
        for platform in level:
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)
 



def main():
    """ Main Program """
    pygame.init()
 
    # Set the height and width of the screen
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
 
    pygame.display.set_caption("Saltar entre plataformas")
 
    # Create the player
    player = Player()
 
    # Create all the levels
    level_list = []
    level_list.append( Level_01(player) )
 
    # Set the current level
    current_level_no = 0
    current_level = level_list[current_level_no]
 
    active_sprite_list = pygame.sprite.Group()
    player.level = current_level
 
    player.rect.x = 340
    player.rect.y = SCREEN_HEIGHT - player.rect.height
    active_sprite_list.add(player)
 
    # Loop until the user clicks the close button.
    done = False
 
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    cam=kinect_cam()
    # -------- Main Program Loop -----------
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            
        cam.get_depth()
        if cam.on_move and not(cam.down):
                if cam.left:
                   player.go_left()
                if cam.right:
                   player.go_right()
                if cam.up:
                   player.jump()                
        if not(cam.on_move) or cam.down:
                player.stop()
        
        # Update the player.
        active_sprite_list.update()
 
        # Update items in the level
        current_level.update()
 
        # If the player gets near the right side, shift the world left (-x)
        if player.rect.right > SCREEN_WIDTH:
            player.rect.right = SCREEN_WIDTH
 
        # If the player gets near the left side, shift the world right (+x)
        if player.rect.left < 0:
            player.rect.left = 0
 
        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        current_level.draw(screen)
        active_sprite_list.draw(screen)
 
        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
 
        # Limit to 60 frames per second
        clock.tick(60)
 
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
 
    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()
 
if __name__ == "__main__":
    main()
