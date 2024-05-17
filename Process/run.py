import os
import pandas as pd
import pprint
input = "/home/valen/Notas Taller/AnalisisDeNotasFacultad/Process/Data/"

#Para cada archivo que termina en .csv, lo leo y lo guardo en un diccionario
data = {}

for file in os.listdir(input):
    if file.endswith(".csv"):
        actual_file = pd.read_csv(input + file)

        #Para cada archivo, uso el nombre de alumno, que es la primera columna, como clave del diccionario data
        #Para cada alumno guardo sus notas que son la segunda columna
       
        #Iterar por cada fila
        for index, row in actual_file.iterrows():
            
            nombre = row[0].lower()
            nombre = nombre.split()[0:2]
            nombre = ' '.join(nombre)
            nota = row[1]

            #Agrego el alumno y nota al diccionario, si el alumno ya tiene nota, lo agrego a una lista de notas
            if nombre in data:
                data[nombre].append(nota)

            else:
                data[nombre] = [nota]

pprint.pprint(data)

#Graficos
import matplotlib.pyplot as plt
import numpy as np

#Mostrar cantidad de alumnos Desaprobados, Aprobados(tienen un numero entre 6 y 10) e Insuficientes

cursada_des = 0
cursada_apro = 0
promo = 0
flotante = 0

for alumno in data:
    nota_alumno = []
    desaprobados = 0
    aprobados = 0
    insuficientes = 0
    notas = data[alumno]
    for nota in notas:
        if nota == "Desaprobado" or nota == "DESAPROBADO" or nota == "D":
            desaprobados += 1
        elif nota == "Insuficiente" or nota == "INSUFICIENTE" or nota == "I":
            desaprobados += 1
        elif nota == "AUSENTE":
            pass
        else:
            try:
                if int(nota) >= 6:
                    aprobados += 1
            except:
                print(nota)
    if aprobados == 3:
        promo += 1
    elif aprobados >= 2:
        cursada_apro += 1
    elif aprobados == 1:
        flotante += 1
    else:
        cursada_des += 1
    print(f"El alumno {alumno} tiene {desaprobados} desaprobados")

#Grafico de barras
fig, ax = plt.subplots()
alumnos = [f'Promocion (Cracks {promo})',f'Desaprobados ({cursada_des})', f'Aprobados ({cursada_apro})', f'A Flotante ({flotante})']
cantidad = [promo, cursada_des, cursada_apro, flotante]
ax.bar(alumnos, cantidad)

#Grafico de torta
fig, ax = plt.subplots()
labels = ['Promocionados','Desaprobados', 'Aprobados', 'Flotantes']
sizes = [promo, cursada_des, cursada_apro, flotante]
explode = (0.4,0.1, 0, 0)
ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)

plt.show()  