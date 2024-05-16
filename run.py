#Leer el contenido de un archivo de texto input.txt y procesarlo por lineas y espacios, dejar el contenido en un archivos .csv

import csv
import pandas as pd

with open('input.txt', 'r') as file:
    a = 0
    lines = 0
    for line in file:
        lines += 1
        # print(line)
        line = line.split()
        nota = line[-1]

        if nota == "I":
            nota = "Insuficiente"
        if nota == "D":
            nota = "Desaprobado"
        if nota == "APROBADO":
            nota = "Aprobado"
        nombre = line[0:-3]

        #Aprobados con nota entre parantesis
        
        if "(" in nota:
            nota = nota[1]
            nombre = line[0:-3]
        else:
            nombre = line[0:-2]


        # print(line[-2])
        # if lines == 45:
        #     print(line)
        # if line[-2] == "Mazullo" or line[-1] == "MazulloInsuficiente" or line[-1] == "MazulloDesaprobado":
        #     nombre = line[0:-6]
            
        #     if line[-1] == "MazulloInsuficiente" or line[-1] == "MazulloDesaprobado":
        #         nota = line[-1].split('Mazullo')[-1]
        #     # print(nota)
        # else:
        #     print(nota)
        #     nombre = line[0:-4]

        nombre = ' '.join(nombre)
        
        # print(nota, nombre)
        
        # print(line)
        if line in ['1', '2', '3', '4', '5', '6', '7', '8', '9', "10"]:
            a +=1


        with open('output.csv', 'a') as file:
            writer = csv.writer(file)
            writer.writerow([nombre, nota])

print(a)
print(lines)