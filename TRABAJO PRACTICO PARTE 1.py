def palabra_a_adivinar( palabra_adivinar ): 
    """
    Devuelve una cadena de la palabra que el usuario tiene que adivinar en forma de
    incognita, es decir, cada caracter de la palabra a adivnar es una incognita

    Autor: Andy Bruno Ames Berrospi
    """
    
    palabra_incognita = ""
    
    for i in range(len(palabra_adivinar)):  
        palabra_incognita += "?"

    return( palabra_incognita )

def mensaje_ingreso_letra(): 
    
     letra = input("Ingrese letra: ").lower()
     
     return letra



def deteccion_validez(letra, CANT_LETRAS): 
    """
    Analiza si las letras que va ingresando el usuario son validas teniendo en cuenta las
    condiciones del juego, si no cumple las condiciones se le va avisar al usuario que
    ingreso una letra no valida

    Autor: Andy Bruno Ames Berrospi
    """
    
    es_valida = False
    
    if (letra.isalpha() and len(letra) == CANT_LETRAS):
        es_valida = True
    else:
        print("\nIngreso Inválido")
        
    return es_valida



def es_letra_repetida(letra, lista_letras_ingresadas): 
    """
    Analiza si la letra ingresada por el usuario es una letra repetida, si la letra es repetida
    se le va avisar al usuario, si no lo es, se va agregar a una lista de letras ingresadas por
    el usuario

    Autor: Andy Bruno Ames Berrospi
    """
    
    es_repetida = False

    if (letra not in lista_letras_ingresadas):
        lista_letras_ingresadas.append(letra)
    else:
        print("\nLetra ya ingresada")
        es_repetida = True
    
    return es_repetida



def acerto_letra( aciertos ): 
    """
    Si el usuario adivino una letra de la palabra a adivinar se le va sumar un acierto y se le
    avisar felicitandole que acerto una letra

    Autor: Andy Bruno Ames Berrospi
    """
    
    aciertos +=1

    print("\nMuy bien!!!")
    
    return (aciertos )



def letras_encontradas( lista_palabra_incognita, letra, palabra_adivinar): 
    """
    Si el usuario ingreso una letra de la palabra a adivinar, entonces esta funcion de la lista
    que recibe, de la palabra en forma de incognita que se armo con la funcion lambda,
    reemplaza las incognitas de dicha lista por la letra encontrada

    Autor: Andy Bruno Ames Berrospi
    """
    
    for indice in range ( len( palabra_adivinar ) ):
        
        if( letra == palabra_adivinar[indice] ):
            lista_palabra_incognita [indice] = letra
            
    return lista_palabra_incognita



def construyendo_palabra( lista_palabra_incognita ): 
    """
    De la lista que recibe, de la palabra en forma de incognita que se armo con la funcion lambda,
    arma una cadena de los elementos de dicha lista a medida que el usuario va ingresando letras
    para que siempre tenga presente la palabra que tiene que adivinar

    Autor: Andy Bruno Ames Berrospi
    """
    
    armando_palabra = ""
    for letra in lista_palabra_incognita:
        armando_palabra += letra

    return armando_palabra



def desacerto_letra(desaciertos): 
    """
    A medida que el usuario ingrese letras incorrectas se le va a sumar un desacierto

    Autor: Andy Bruno Ames Berrospi  
    """
    
    desaciertos += 1
    
    print("\nLo siento!!!")
    
    return (desaciertos)



def el_usuario_gano( palabra_adivinar , palabra_incognita): 
    """
    Verifica si el usuario adivinó la palabra a adivinar

    Autor: Andy Bruno Ames Berrospi
    """
    
    return ( palabra_adivinar == palabra_incognita )



def el_usuario_perdio ( desaciertos,  MAX_DESACIERTOS ): 
    """
    Verifica si el usuario alcanzo la maxima cantidad de desaciertos

    Autor: Andy Bruno Ames Berrospi
    """
    
    return ( desaciertos ==  MAX_DESACIERTOS )
    


def main():
    """
    Funcion principal que llama a las demas funciones 

    Autor: Andy Bruno Ames Berrospi
    """
    
    MAX_DESACIERTOS = 8
    CANT_LETRAS = 1 # Maxima letras que puede ingrear el usuario

    aciertos=0
    desaciertos=0

    lista_letras_ingresadas = []
    lista_letras_incorrectas = []
    cadena_letras_incorrectas = ""
    palabra_adivinar = "naranja"

    palabra_incognita = palabra_a_adivinar( palabra_adivinar )
    lista_palabra_incognita = list( palabra_incognita)  

    adivino=False
    
    print("Palabra a adivinar: ", palabra_incognita,"  Aciertos: ", aciertos,"  Deasciertos: ", desaciertos)
    letra = mensaje_ingreso_letra()
    salir = letra == "0" or letra == "fin" 
    
    while( not(adivino) and not(salir) ):

        if(deteccion_validez(letra, CANT_LETRAS) and not ( es_letra_repetida(letra, lista_letras_ingresadas) ) ):

            if(letra in palabra_adivinar):
            
                aciertos = acerto_letra(aciertos)
                lista_palabra_incognita = letras_encontradas(lista_palabra_incognita, letra, palabra_adivinar)
                armando_palabra = construyendo_palabra(lista_palabra_incognita)
                palabra_incognita = armando_palabra  #Es necesario hacer este "cambio" de variable

            else:
                desaciertos = desacerto_letra(desaciertos)
                cadena_letras_incorrectas += " - " + letra

        print("Palabra a adivinar: ", palabra_incognita,"  Aciertos: ", aciertos,"  Deasciertos: ", str(desaciertos) + cadena_letras_incorrectas )

        if( not (el_usuario_gano( palabra_adivinar , palabra_incognita) ) and not (el_usuario_perdio( desaciertos,  MAX_DESACIERTOS ))):
            letra = input("Ingrese letra: ")
        else:
            adivino=True
            

    if(el_usuario_gano(palabra_adivinar , palabra_incognita)):
        print("\nGANASTE!!!!!!\n")
        
    else:
        print("\nPERDISTE!!!!!!")
        print("La palabra era: ", palabra_adivinar)

   
                
main()
