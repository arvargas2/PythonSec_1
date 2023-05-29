import os
import numpy as np # se importa y 
                    # usaremos un alias!!

# Una forma de crear un arreglo es partir
# de una lista
lista_1= [2,5,8]
arreglo_1 = np.array(lista_1)

print(f'''
     {lista_1}   ---> lista
     {arreglo_1} ---> arreglo
      ''')                    


print("\n-- arreglo de largo 5 que contiene solo UNOS ---")
b = np.ones(5)
print(b)

print("\n-- arreglo de largo 5 que contiene solo CEROS ---")
c = np.zeros(5)
print(c)

print("\n-- arreglo con valores entre dos cotas ---")
d= np.arange(1,8)
print(d)






                    
                    
                    
                    