import pygame
import sys
import random


class Runner():
    
    __customes = ("fish", "moray","octopus","prawn","turtle")
    
    def __init__(self,x=0,y=0):
        
        ixCustome = random.randint(0,4)
        
        self.custome = pygame.image.load("imagenes/profe/{}.png".format(self.__customes[ixCustome]))
        self.position = [x,y]
        self.name = ""
        
    def avanzar (self):
        self.position[0] += random.randint(1,6)

class Game():
    
    runners = []
    
    __posY = (160,200,240,280)
    __names = ("Stitch","Yoda", "Penguin", "Groot","Tortuga")
    __startLine = -5
    __finishLine = 620
    
    def __init__(self):
        self.__screen = pygame.display.set_mode((1280,800))
        self.background = pygame.image.load("imagenes/profe/background.png")
        pygame.display.set_caption("Carrera de bichos")
        
        for i in range(4):
            theRunner = Runner(self.__startLine, self.__posY[i])
            theRunner.name = self.__names[i]
            self.runners.append(theRunner)
            
    
          
    def competir (self):
        gameOver = False
        
        while not gameOver:
            #comprobacion de los eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = True
                    
            for activeRunner in self.runners:
                activeRunner.avanzar()
                if activeRunner.position[0] >= self.__finishLine:
                    print("{} ha ganado".format(activeRunner.name))
                    gameOver = True
    
         
            #refrescar / renderizar la pantalla
            self.__screen.blit(self.background,(0,0)) #pinta la pantalla
            
            self.__screen.blit(self.runners[0].custome,self.runners[0].position)
            self.__screen.blit(self.runners[1].custome,self.runners[1].position)
            self.__screen.blit(self.runners[2].custome,self.runners[2].position)
            self.__screen.blit(self.runners[3].custome,self.runners[3].position)
            '''
            for runner in self.__runners:
                self.__screen.blit(runner.custome,runner.position)

            pygame.display.flip()#refresca la pantalla
            '''
            
            
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
        
if __name__ == "__main__":
    game = Game()
    pygame.font.init()
    game.competir()
        