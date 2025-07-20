import numbers
def fib(numero):
    #Precondicion: El valor de valor de entrada debe de ser un numero entero

    #Definicion de las variables a emplear
    a = 0
    b = 1

    #Se comprueba que el valor de entrada es un numero entero
    #Si el valor no es un numero, entonces se le dice al usuario que el valor es incorrecto y que vuelva a probarlo.
    #En caso de que no, pues se ejecuta el algoritmo.

    if isinstance(numero, numbers.Number):
        print('Es un numero')
    
        #Algoritmo
        while a < numero:
            print(a, end='')
            a = b
            b = a + b

            #Valores de salida
            print()
        print('Fin del programa')
    else:
        print('No es un numero')
        print('Fin del programa, debido a falta de valor numerico')

fib(10000)
#Precondiciones
#El parametro que va a recibir la funcion, debe ser numerico.


#Algoritmo
#Precondiciones
#Postcondiciones