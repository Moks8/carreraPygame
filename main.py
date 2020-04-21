import pygame
import sys


class runner():
    pass

class Game():
    corredores = []
    __starLine = 20
    __finishLine =620
    
    def __init__(self):
        self.__screen = pygame.display.set_mode((640,480))
        pygame.display.set_caption("Carrera de bichos")
        self.background = pygame.image.load("imagenes/background.png")
        
        self.runner = pygame.image.load("imagenes/stitch3.png")
        
    def competir (self):
        x= 0
        gameOver = False
        
        while not gameOver:
            #comprobacion de los eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
            #refrescar / renderizar la pantalla
            self.__screen.blit(self.background,(0,0)) #pinta la pantalla
            self.__screen.blit(self.runner, (x,20))
            pygame.display.flip()#refresca la pantalla
            
            x += 3
            if x >= 20:
                gameOver = True
                
        pygame.quit()
        sys.exit()
        
        
if __name__ == "__main__":
    pygame.init ()
    game = Game ()
    game.competir()
        