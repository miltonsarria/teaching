import sys, os, random
sys.path.append('/usr/local/lib/python2.7/dist-packages/')
import freenect
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from gameTools import *

        
def main():    
    mouse=True
    screen_width =  1000 
    screen_height = 700
    N=8
    image1='Globo2.png' 
    image2='frog1.png'
    
    game=mainGame(screen_width =  screen_width, screen_height = screen_height,N=N, image1=image1, image2=image2,mouse=mouse)
    
    app = QApplication(sys.argv)
    form = AppForm(game)
    game.MainWindow=form
    
    sys.exit(app.exec_())



if __name__ == '__main__':
    main()        
