import sys, os, random
#sys.path.append('/usr/local/lib/python2.7/dist-packages/')
#import freenect
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from gameTools import *

        
def main():    
    
    game=mainGame(screen_width =  1200, screen_height = 800,N=8, image1='Globo2.png', image2='frog1.png')
    app = QApplication(sys.argv)
    form = AppForm(game)
    game.MainWindow=form
    
    sys.exit(app.exec_())



if __name__ == '__main__':
    main()        
