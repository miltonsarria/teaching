import pygame
import sys, os, random
import numpy as np
import cv2
sys.path.append('/usr/local/lib/python2.7/dist-packages/')
import freenect
import imutils
  

 
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
  
 
class Bloque(pygame.sprite.Sprite):
   def __init__(self, nombre_de_archivo):
        pygame.sprite.Sprite.__init__(self)        
        self.image = pygame.image.load(nombre_de_archivo).convert()
        self.image.set_colorkey(NEGRO)
        (h,w)=self.image.get_size()
        self.d=int(np.ceil(np.sqrt(h**2+w**2)))
        self.rect = self.image.get_rect()

   def reset_pos(self):
        self.rect.y = random.randrange(-300, -20)
        self.rect.x = random.randrange(700-20) 

   def update(self):
       self.rect.y += 1
       if self.rect.y > 410:
          self.reset_pos()
    
 
class Protagonista(pygame.sprite.Sprite):
   def __init__(self, color, width, height):
        pygame.sprite.Sprite.__init__(self) 
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
   def update(self):
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0]
        self.rect.y = pos[1]        

pygame.init()
  
WIDTH = 2*640
HEIGHT =2*480
pantalla = pygame.display.set_mode([WIDTH, HEIGHT])
bloque_lista = pygame.sprite.Group()
listade_todoslos_sprites= pygame.sprite.Group()

pos = []
N=10
  
for i in range(N):
   
    bloque = Bloque("Globo2.png")
    touch = True
    if i==0:
        bloque.rect.x = random.randrange(WIDTH-bloque.d)
        bloque.rect.y = random.randrange(HEIGHT-bloque.d)
        pos.append(np.array([bloque.rect.x,bloque.rect.y]))
    else:
        while touch:
              x = random.randrange(WIDTH-bloque.d)
              y = random.randrange(HEIGHT-bloque.d)
              p = np.array([x,y])
              d= np.sqrt(np.sum((p-np.array(pos))**2,1))
              touch = np.any(d<bloque.d)
        bloque.rect.x = x
        bloque.rect.y = y
        pos.append(p)
   
    bloque_lista.add(bloque)
    listade_todoslos_sprites.add(bloque)

protagonista = Protagonista(ROJO, 20, 15)
listade_todoslos_sprites.add(protagonista)

hecho = False

reloj = pygame.time.Clock()
  
puntuacion = 0

while not hecho:
    for evento in pygame.event.get(): 
        if evento.type == pygame.QUIT:
            hecho = True
        if puntuacion == 10:
            hecho = True
  
    pantalla.fill(BLANCO)
    listade_todoslos_sprites.update()

    lista_impactos_bloques = pygame.sprite.spritecollide(protagonista, bloque_lista, True)  
      
    
    for bloque in lista_impactos_bloques:
        puntuacion += 1
        print( puntuacion )
         
        
        #bloque.reset_pos() 
          
   
    listade_todoslos_sprites.draw(pantalla)
      
    
    reloj.tick(60)
  
  
    pygame.display.flip()
  
pygame.quit()
