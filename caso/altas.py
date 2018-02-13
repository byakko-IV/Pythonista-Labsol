#! /usr/bin/python3
# -*-coding: utf-8 -*-
import caso.datos as datos
import caso.valida as valida
"""Módulo que contiene la funcion de altas."""
""""""


def alta():
    """Realiza las altas."""
    
    
    def ingresa(campo): #función que verifica si el dato ingresado corresponde con lo especificado para el campo a ingresar
        while True: # inicia un loop para capturar el dato especificado
            mensaje = "Ingrese " + campo.lower() + ": " 
            dato = input(mensaje)
            if datos.campos[campo] != str: # valida si el campo a ingresar se requiere como string
                try:
                    if eval(dato) == datos.campos[campo](dato): # valida que el dato ingresado sea del mismo tipo requerido por el campo
                        dato = datos.campos[campo](dato)
                    else:
                        continue
                except:
                    continue #se continua con el loop si el dato ingresado no corresponde al tipo
            if valida.reglas(dato, campo): #valida que el dato compla con las reglas requeridas por el campo especificadas en el modulo valida
                return dato
                  
    return {campo: ingresa(campo) for campo in datos.orden} #aquí se usa lo visto en la lección completado de elemntos
    # en donde regresa un elemento de tipo diccionario con el campo listado en la lista de orden y la información ingresada por el usuario
