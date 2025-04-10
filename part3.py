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
            area = 0
            dict_valores = copy.deepcopy(dict_valor)
            iterador = 0
            while(iterador < 200):
                for p in range(len(lista_hormigas)):
                    posicion = lista_hormigas[p]
                    if(posicion <= dimension):
                        if(posicion == 0): #posicionrimer casillero de la grilla
                            mov_posibles= [posicion + 1, posicion + dimension]
                            
                           
                          
                        elif(posicion == dimension - 1): #ultima columna primera fila
                            mov_posibles= [posicion -1, posicion + dimension]
                            
                        else:
                            mov_posibles= [posicion -1, posicion + dimension, posicion+1]
               
                           
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
                         
                
                    if(dict_valores[posicionNueva]!="yellow"):
                        area+=1
                        if(dict_valores[posicionNueva]!="white"):
                             
                            acumComida +=1
                    
            
                    dict_valores[posicionNueva] = "red"
                    lista_hormigas[p] = posicionNueva
                    dict_valores[posicion] = "yellow"
                iterador+=1
           
            return area




dim, valores, primera_col, ultima_col = crear_dict(30)
valores_actualizado, hormigas, total = grilla_base(valores, 0, 10, 5)
area = recorrerGrilla(dim, valores_actualizado, hormigas, primera_col, ultima_col, total)
print(area)
i = 10000
while(i > 0):
    valores_actualizado, hormigas, total = grilla_base(valores, 0, 10, 5)
    area += recorrerGrilla(dim, valores_actualizado, hormigas, primera_col, ultima_col, total)
    print(area)
    i-=1

print("PROMEDIO", area / 10000)
     