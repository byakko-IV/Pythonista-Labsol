#! /usr/bin/python3
# -*- coding: utf-8 -*-
import caso.datos as datos 

def buscar(parametro):
    coincidencias = ()
    for alumno in datos.alumnos:
        if alumno["Nombre"] == parametro or alumno["Primer Apellido"] == parametro or alumno["Segundo Apellido"] == parametro:
            return tuple(alumno.values())
