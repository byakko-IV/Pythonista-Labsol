#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""script valida"""
import caso.datos as datos

# esta función valida los datos ingresados de acuerdo al campo indicado y si el dato cumple las validaciones indicadas para el campo
def reglas(dato, campo): # la funcion recibe dos argumentos dato y campo
    if campo == "Carrera" and dato not in datos.carreras: # si el campo es carrera el dato deberá existir dentro de la lista de carreras
        return False
    elif campo == "Semestre" and dato < 1: # si el campo es Semestre entonnces el dato deberá ser un numero mayor a cero
        return False
    elif campo == "Promedio" and (dato < 0 or dato > 10): # si el campo es semestre el dato deberá ser mayor a 0 y menor a 10
        return False
    elif (campo in ("Nombre", "Primer Apellido") and (dato == "")): # si el campo es primer apellido el dato no deberá estar vácio
        return False
    elif campo == "Segundo Apellido" and dato == "": # si el campo es igual segundo apellido inicializa un loop while
        while True:
            mensaje = "No ha ingresado el segundo apellido. ¿Es correcto? S/N: " # se le pide al usuario que indique si el capo no fue ingresado
            confirma = input(mensaje) 
            if confirma.upper() in ("S", "N"): # se valida que la respuesta sea s o n
                respuesta = True
                if confirma.upper() == "N":
                    respuesta = False
                return respuesta
    else:
        return True # si todo salio bien se regresa un valor de true indicando que los datos son correctos
