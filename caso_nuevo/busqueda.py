#! /usr/bin/python3
# -*- coding: utf-8 -*-
import caso_nuevo.datos as datos 

def buscar(parametro):
    ruta = datos.ruta
    with open(ruta, 'r') as archivo:
        contador = 0
        for alumno in archivo:
            alumno = eval(alumno)
            if alumno["Nombre"] == parametro or alumno["Primer Apellido"] == parametro or alumno["Segundo Apellido"] == parametro:
               return tuple(alumno.values())
