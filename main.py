#juego de rompecabezas
#julian forero bernal
#29/04/2024

import pygame
import sys # libreria que por ahora solo se que funciona para que el juego cierre sin errores
import constantes
import random
pygame.init()
ventana = pygame.display.set_mode((constantes.ancho,constantes.alto))
pygame.display.set_caption("Juego Rompecabezas")

#matriz que representa el tablero

tablero = [[1, 2, 3], 
            [4, 5, 6], 
            [7, 8, 0]] #crea la matriz 3x3 del 1 al 8 con 0 al final
random.shuffle(tablero) #va a desordenar la matriz tablero

#estado de juego
juego_ganado = False   #variable para controlar cuando acaba el juego

#funciones necesariasa para el juego

def dibujar_en_pantalla() :
    ventana.fill(constantes.negro) #metodo que llena la pantalla de un color (en este caso el negro/importado de constantes)
    fuente_numero = pygame.font.Font(None, 40) # metodo para asignar un tipo de funte a una variable creo
    fuente_mensaje = pygame.font.Font(None, 30)
    for i in range(3): #va a iterar entre los datos de la matriz "tablero"
        for j in range (3):
            valor = tablero[i][j] # le asigana a la variable valor el dato que haya en la pocision i,j de la matriz tablero
            color = constantes.colores.get(valor, constantes.colores[0]) 
            """le asigna a la variable color un color que encuentra en el diccionario colores del arichivo constantes 
            segun el numero que haya en valor en este caso ordenados del 1 al 8
            """
            pygame.draw.rect(ventana,color,(j*constantes.tamaño_celda,  
                                            i*constantes.tamaño_celda, 
                                            constantes.tamaño_celda, 
                                            constantes.tamaño_celda), 0)
            """
            esta funcion dibuja cada rectangulo en (ventana) con el color que haya en la variale color (la cual itera de
            1 a 9) y el tamaño esta dado por j(nuero de la columna)*el tamaño de la celda (en la primera repticion 0 
            despues 100-200-300) des pues va a la siguiente fila(i) y repite el proceso en j(columna)
            """
            if valor != 0:
                texto = fuente_numero.render(str(valor),True,constantes.negro)
                texto_rect = texto.get_rect(center=(j* constantes.tamaño_celda + constantes.tamaño_celda / 2,
                                                    i*constantes.tamaño_celda + constantes.tamaño_celda /2))
                """
                esto de aca dice algo asi como: si el valor en la variable "valor" es diferente de cero (en este caso
                va se asi para todos los valores menos el ultimo) entonces...  
                texto (el numero que ira en el cuadrardo)= funte_numero (la funte que se declaro mas arriba).render(el metodo
                que va a poner ese numerito ahi)str(valor)[convierte la nariable de timpo int "valor" en string], true (hace
                refenrencia a que nesecita antialiasing(suavizado) para que se vea mas nitido), de constantes.negro obtiene
                el color del que sera el numero
                
                texto.get_rect()va a crear un rectangulo al rededor del numero
                center= {dificil de explicar pero si entendi con un dibujito jajajaj}
                """

                ventana.blit(texto,texto_rect) #funcion blit dibuja una imagen dentro de otra (que se dibuja?, sobre que se dibuja?)
    if juego_ganado :
        texto_gana_el_juego = fuente_mensaje.render("Ganaste!! presiona R para reiniciar ;)", True, constantes.rojo)
        #igual que arriba asigna a una veriable un mensaje con una funte, suavizado, y un color
        ventana.blit(ventana,50,constantes.alto/2) #escribe el mensaje en : 50px de ancho , el alto de 
        # la ventana entre 2 - 20 para que se vea mas centrado
def encontrar_negro_fila():
    for i in range (3):
                for j in range (3):
                    if tablero[i][j] == 0:
                        a = i
    return a
def encontrar_negro_columna():
    for i in range (3):
                for j in range (3):
                    if tablero[i][j] == 0:
                        b=j
    return b
def posicion_no_existe():
    fuente_mensaje = pygame.font.Font(None, 30)
    texto_posicion_no_existente = fuente_mensaje.render("ese valor no existe por favor intenta otra direccion", True, constantes.rojo)
    return texto_posicion_no_existente    


running = True
while running :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        a = encontrar_negro_fila()  
        b = encontrar_negro_columna() 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if tablero[a-1][b]:
                    aux = tablero[a-1][b]
                    tablero[a-1][b] = tablero [a][b]
                    tablero[a][b] = aux 
                else :
                    posicion_no_existe()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if tablero[a-1][b]:
                    aux = tablero[a-1][b]
                    tablero[a-1][b] = tablero [a][b]
                    tablero[a][b] = aux 
                else :
                    posicion_no_existe()
                    
            if event.key == pygame.K_DOWN:
                if tablero[a+1][b]:
                    aux = tablero[a+1][b]
                    tablero[a+1][b] = tablero [a][b]
                    tablero[a][b] = aux 
                else :
                    posicion_no_existe()
                    
            if event.key == pygame.K_RIGHT:
                if tablero[a][b+1]:
                    aux = tablero[a][b+1]
                    tablero[a][b+1] = tablero [a][b]
                    tablero[a][b] = aux 
                else :
                    posicion_no_existe()
                    
            if event.key == pygame.K_LEFT:
                if tablero[a][b-1]:
                    aux = tablero[a][b-1]
                    tablero[a][b-1] = tablero [a][b]
                    tablero[a][b] = aux 
                else :
                    posicion_no_existe()            
    if tablero == [[1,2,3],[4,5,6],[7,8,0]]:
        fuente_mensaje = pygame.font.Font(None, 30)
        texto_gano = fuente_mensaje.render("¡HAZ GANADO!", True, constantes.rojo)
        ventana.blit(texto_gano, (50, constantes.alto // 2))        
    dibujar_en_pantalla()
    pygame.display.update()