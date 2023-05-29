import os
import random
import numpy as np

os.system("cls")

# crearemos un arreglo de cinco celdas int
#           np.empty(TAMAÑO, dtype=TIPO_DE_DATO)
arr_notas = np.empty(5, dtype=int)

# vamos a cargar los datos randomicos
# Recordemos: range(5)=0,1,2,3,4
for k in range(5):
    arr_notas[k]= random.randint(1,7)
    
print(arr_notas)

promedio = sum(arr_notas)/len(arr_notas)

print(f'''
      NOTAS: {arr_notas}
      Promedio:{promedio} ''')

