#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""Ejemplo de modulos en el curso de Python"""
#Importa los demás los demas archivos del módulo
import caso.altas as altas
import caso.listado as listado
import caso.datos as datos
import caso.busqueda as bosqueda

def principal():
    while True: #inicia un loop while para pedir el numero de alumnos a capturar
        try:
            #se hace dentro de un try para gestionar los errores
            alumnos = input("Número de alumnos:")
            alumnos = int(alumnos)
            print()
        except (ValueError) as error:
            print(error) #imprimirá el error en caso de que no se ingrese un número
            continue
        else:
            break # Saldrá del loop si no ocurren errores
    for contador in range(alumnos): #inicia un loop que se repetira la veces que el usuario haya inidicado
        print("\nAlumno nuevo", contador + 1) #se imprime la cantidad de alumonos que se van registrando
        datos.alumnos.append(altas.alta()) #sea agrega al final de la lista de alumnos el resultado devuelto por altas.alta
    listado.despliega_todos() #Se imprime la lista de alumnos
