import pygame
from pygame.locals import *
import sys

class Termometro():
    def __init__(self):
        #coloco imagen del termometro
        self.custome = pygame.image.load("images/termo1.png")

class NumberInput():
    __value =  0
    __strValue = "0"
    __position = [0,0]
    __size = [0,0]

    def __init__(self, value = 0):
        #Ponemos una fuete y un tamaño
        self.__font = pygame.font.SysFont('Arial',24)
        #llamo al metodo que me asignara el texto y que comprueba es numero
        self.value(value) 

    def on_event(self, event):
        if event.type == KEYDOWN:
            if event.unicode.isdigit() and len(self.__strValue) <= 5:
                self.__strValue += event.unicode
            elif event.key == K_BACKSPACE:
                #Para borrar la ultima cifra escrita
                self.__strValue = self.__strValue[0:-1]



    def render(self):
        #Renderizamos texto
        textBlock = self.__font.render(self.__strValue, True, (74, 74, 74))
        rect = textBlock.get_rect()
        #Posicionamiento del cuadro de texto
        rect.left = self.__position[0]
        rect.top = self.__position[1]
        rect.size = self.__size

        return (rect, textBlock)

        #return {
        #        "fondo": rect,
        #        "texto": textBlock
        #    }

    
    #Getter y Setters de la clase
    def value(self, val = None):
        if val == None:
            return self.__value
        else:
            val = str(val)
            print(val, "cadena")
            try:
                #Compruebo es un numero
                self.__value = float(val)
                #Una vez que es un numero lo paso a cadena
                self.__strValue = val
            except:
                pass

    def width(self, val = None):
        if val == None:
            return self.__size[0]
        else:
            try:
                self.__size[0] = int(val)
            except:
                pass

    def height(self, val = None):
        if val == None:
            return self.__size[1]
        else:
            try:
                self.__size[1] = int(val)
            except:
                pass

    def size(self, val = None):
        if val == None:
            return self.__size
        else:
            try:
                self.__size = [int(val[0]), int(val[1])]
            except:
                pass

    def posX(self, val = None):
        if val == None:
            return self.__position[0]
        else:
            try:
                self.__position[0] = int(val)
            except:
                pass

    def posY(self, val = None):
        if val == None:
            return self.__position[1]
        else:
            try:
                self.__position[1] = int(val)
            except:
                pass

    def pos(self, val = None):
        if val == None:
            return self.__position
        else:
            try:
                self.__position = [int(val[0]), int(val[1])]
            except:
                pass

class MainApp():
    termometro = None
    entrada = None
    selector = None

    def __init__(self, ):
        #Inicializamos el display
        self.__screen = pygame.display.set_mode((290,415))
        #Titulo de la pantalla
        pygame.display.set_caption("Termometro")
        #Cargamos la imagen de fondo del display
        self.__screen.fill((244,236,203))

        self.termometro = Termometro()
        self.entrada = NumberInput()

        #Posicion del rectangulo
        self.entrada.pos((106, 58))
        self.entrada.size((133,28))
    
    def __close(self):
        pygame.quit()
        sys.exit()

    def start(self):
        while True:    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__close()
                
                self.entrada.on_event(event)



            
            #Nos pinta la pantalla con el termometro
            self.__screen.blit(self.termometro.custome, (50,34))

            #renderizado del cuadro de texto
            #Obtenemos rectangulo blanco y foto de texto, asignamos a text
            text = self.entrada.render() 
            #creamos rectangulo blanco con sus datos (Pos y Tamaño) text[0]
            pygame.draw.rect(self.__screen, (255,255,255), text[0]) 
            #Pintamos la foto del texto (text[1])
            self.__screen.blit(text[1], self.entrada.pos()) 

            #refresco de pantalla
            pygame.display.flip()



if __name__ == '__main__':
    pygame.font.init()
    app = MainApp()
    app.start()