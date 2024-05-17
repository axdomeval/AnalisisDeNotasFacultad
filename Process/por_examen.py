import os
import pandas as pd
import pprint
input = "/home/valen/Notas Taller/AnalisisDeNotasFacultad/Process/Data/"

#Para cada archivo que termina en .csv, lo leo y lo guardo en un diccionario
data = {}

for file in os.listdir(input):
    if file.endswith(".csv"):
        actual_file = pd.read_csv(input + file)
        data[file] = {"Aprobados": 0, "Desaprobados": 0}

        #Sumo los aprobados
       
        #Iterar por cada fila
        for index, row in actual_file.iterrows():
            
            nota = row[1]

            #Agrego el alumno y nota al diccionario, si el alumno ya tiene nota, lo agrego a una lista de notas
            if nota == "Desaprobado" or nota == "DESAPROBADO" or nota == "D":
                data[file]["Desaprobados"] += 1

            else:
                data[file]["Aprobados"] += 1

pprint.pprint(data)

#Graficos
import matplotlib.pyplot as plt
import numpy as np

#Mostrar aprobados por examen
fig, ax = plt.subplots()
exams = list(data.keys())
aprobados = [data[exam]["Aprobados"] for exam in exams]
desaprobados = [data[exam]["Desaprobados"] for exam in exams]
ax.bar(exams, aprobados, label="Aprobados")
plt.show()