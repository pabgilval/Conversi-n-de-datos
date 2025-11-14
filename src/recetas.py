import csv
from typing import NamedTuple
from datetime import date, datetime


Ingrediente = NamedTuple("Ingrediente",
					[("nombre",str),
					 ("cantidad",float),
					 ("unidad",str)])
						 
Receta = NamedTuple("Receta", 
                    [("denominacion", str),
                     ("tipo", str),
                     ("dificultad", str),
                     ("ingredientes", list[Ingrediente]),
                     ("tiempo", int),
                     ("calorias", int),
                     ("fecha", date),
                     ("precio", float)])

def lee_recetas(fichero: str) -> list[Receta]:
    with open(fichero, mode='r', encoding='utf-8') as f:
        lector = csv.reader(f, delimiter=';')
        next(f)

        recetas = []

        for denominacion, tipo, dificultad, ingredientes, tiempo, calorias, fecha, precio in lector:
            
            denominacion = denominacion.strip()
            tipo = tipo.strip()
            dificultad = dificultad.strip()
            ingredientes = parsea_ingredientes()
            tiempo = int(tiempo)
            calorias = int(calorias)
            fecha = datetime.strptime(fecha, '%d/%m/%Y').date()
            precio = float(precio)

            tupla = (denominacion, tipo, dificultad, ingredientes, tiempo, calorias, fecha, precio)
            recetas.append(tupla)

    return recetas

def parsea_ingredientes(ingredientes_str: str) -> list[Ingrediente]:
    lista = []

    if len(ingredientes_str) >0:
        lista_ingredientes = ingredientes_str.split(',')

        for ingredientes in lista_ingredientes:
            lista.append(parsea_ingrediente(ingrediente_str))
    
    return lista

def parsea_ingrediente(ingrediente_str: str) -> Ingrediente:
    nombre, cantidad, unidad = ingrediente_str.split('-')
    return Ingrediente(nombre, float(cantidad), unidad)

def ingredientes_en_unidad(recetas:list[Receta], unidad: str=None) -> int:
    ingredientes = set()

    for r in recetas:
        for i in r.ingredientes:
            if i.unidad is None or i.unidad == unidad:
                ingredientes.add(i.nombre)
    
    return len(ingredientes)