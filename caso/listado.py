#! /usr/bin/python3
# -*- coding: utf-8 -*-
import caso.datos as datos

#módulo que sirve para desplegar la lista de todos los alumnos
def despliega_uno(elemento): #esta funcion recive un diccionario con la información del alumno
    for campo in datos.orden: # se recorre el diccionario orden que se encuentra en datos que contien la lista de campos
        print(campo + ": " + str(elemento[campo])) # se imprime en pantalla el campo y el valor dentro de la lista elemento


def despliega_todos(): # Esta función recorre la lista de alumnos uno a uno
    contador = 0
    for alumno in datos.alumnos:
        contador += 1
        print("\nAlumno: ", contador) #indica el numero que corresponde al alumno dentro de la lista
        despliega_uno(alumno) #pasa el diccionario con los datos del alumno a la función que imprime la información en pantalla
