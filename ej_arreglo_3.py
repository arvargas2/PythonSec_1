import os
import numpy as np
os.system("cls")

tamaño=3
arr_profes = np.empty(tamaño, dtype=object)

for k in range(tamaño):
    arr_profes[k]=str(input("Ingrese nombre: "))
    
print(arr_profes)    

print(f"2do--->{arr_profes[1]}")