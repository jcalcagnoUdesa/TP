from termcolor import cprint, colored
import random
import time
import copy

def crear_dict(dimension):
    dict_valores = {}
    primera_columna = []
    ultima_columna = []
    acumposiciones = 0
    

    for i in range(dimension):
        primera_columna += [dimension * i] 
        ultima_columna += [(dimension *(i + 1)) - 1]

        for j in range(dimension):

            dict_valores[acumposiciones]= "green"
            acumposiciones +=1

    return dimension, dict_valores, primera_columna, ultima_columna
    
def grilla_base(dict_valor, cantComida, cantObstaculos, cantHormigas):
    lista_hormigas = []
    totalComida = cantComida
    dict_valores = copy.deepcopy(dict_valor)
    total = cantComida + cantObstaculos + cantHormigas    
    while(total >0):
        
        randomNum = random.randint(0, len(dict_valores) - 1)
    
        if(cantComida > 0):
            dict_valores[randomNum] = "white"
            cantComida -=1
        elif(cantObstaculos > 0):
            dict_valores[randomNum] = "grey"
            cantObstaculos -=1
        elif(cantHormigas > 0):
            dict_valores[randomNum] = "red"
            lista_hormigas += [randomNum]
            cantHormigas -=1

             
        total-=1

    return dict_valores, lista_hormigas, totalComida
    
    
def recorrerGrilla(dimension, dict_valor, lista_hormigas, primera_columna, ultima_columna, totalComida):
            acumComida = 0
            cant_pasos = 0
            dict_valores = copy.deepcopy(dict_valor)
            while(totalComida / 2 > acumComida):
                for p in range(len(lista_hormigas)):
                    posicion = lista_hormigas[p]
                    if(posicion <= dimension):
                        if(posicion == 0): #posicionrimer casillero de la grilla
                            mov_posibles= [posicion + 1, posicion + dimension]
                           
                          
                        elif(posicion == dimension - 1): #ultima columna posicionrimera fila
                            mov_posibles= [posicion -1, posicion + dimension]
               
                           
                    elif(posicion in ultima_columna): #ultimas columnas 
                        if(posicion == (len(dict_valores) - 1)): #ultimo casillero de la grilla
                            mov_posibles= [posicion -1, posicion - dimension]
            
                           
                        else:
                            mov_posibles= [posicion -1, posicion - dimension, posicion + dimension]
             
                          
                    elif(posicion in primera_columna): #posicionrimeras columnas
 
                            if(posicion == (len(dict_valores) - dimension)): #primera columna ultima fila
                                mov_posibles= [posicion + 1, posicion - dimension]
                       
                         

                                
                                
                            else:
                                mov_posibles= [posicion + 1, posicion - dimension, posicion + dimension]
                  
                               
                    elif(posicion > (len(dict_valores) - dimension)):
                            mov_posibles= [posicion + 1, posicion - 1, posicion - dimension] # ultima fila
                     
                    
                    else:
                        mov_posibles = [posicion +1, posicion -1, posicion + dimension, posicion - dimension]
                       
                    posicionNueva = random.choice(mov_posibles)

                    while(dict_valores[posicionNueva] == "grey" or dict_valores[posicionNueva] == "red"):
                        posicionNueva = random.choice(mov_posibles)
                         
                
                    if(dict_valores[posicionNueva]=="white"):
                        acumComida +=1
            
                    dict_valores[posicionNueva] = "red"
                    lista_hormigas[p] = posicionNueva
                    dict_valores[posicion] = "yellow"
                
    
             
    
         
                
                cant_pasos+=1

              
                
                        
                    
            return cant_pasos
                        
                
            




dim, valores, primera_col, ultima_col = crear_dict(250)
valores_actualizado, hormigas, total = grilla_base(valores, 200, 100, 20)
pasos = recorrerGrilla(dim, valores_actualizado, hormigas, primera_col, ultima_col, total)
contenedorTempMayor = pasos
contenedorTempMenor = pasos
acumulador = pasos
print("iteracion 100", pasos)
for i in range(10):
     
     
     if (contenedorTempMayor < pasos):
          contenedorTempMayor = pasos
     if(contenedorTempMenor > pasos):
          contenedorTempMenor = pasos
              
     pasos = recorrerGrilla(dim, valores_actualizado, hormigas, primera_col, ultima_col, total)
     acumulador+=pasos
     print(f"iteracion {i} con ", pasos, "pasos")
 

print("PROMEDIO", pasos / 100)
print("MAX", contenedorTempMayor)
print("MIN", contenedorTempMenor)
            

    #sabemos que la grilla es cuadrada, o sea que su tamanio es nxn, o n**2 = len(dict_valores) + 1
    #cuentas auxiliares posicionara que la hormiga no se caiga de la grilla
    #si la dimension de la grilla es nxn, tiene i filas y j columnas, entonces cada fila tiene
    # sus lugares indexados desde ((0, 1, 2, ... n) * n) - 1. 
    #ejemposicionlo: si n = 5, fila 0 = lugares 0-4, fila 1= lugares 5-9.
    #el posicionrimer casillero en cada fila es  n * i
    #el ultimo casilero en cada fila es (n*i) - 1, exceposicioncion: posicionrimera fila, donde i = 0
    #posicionara avanzar verticalmente, debe avanzar la dimension de la grilla (n) casilleros 
    # CASOS EXCEposicionCIONALES: posicionrimera y ultima fila, posicionrimer y ultima columna, posicionrimer y ultimo casillero
    #  fila 0 no posicionuede subir, fila (n-1) no posicionuede bajar, 
    # columna 0 no posicionuede izquierda, columna (n-1) no posicionuede derecha
    # casillero 0 no posicionuede subir ni izquierda , casillero (n-1) no posicionuede derecha ni abajo  




    
