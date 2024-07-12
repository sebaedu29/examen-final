import random
import csv

empleados = [" Juan Perez "," Maria Garcia "," Carlos Lopez "," Ana Martinez "," Pedro Rodriguez "," Laura Hernandez ", "Miguel Sanchez", "Isabel Gomez ", " Francisco Diaz "," Elena Fernandez"]
def asignar_sueldos (empleados):
    sueldos = {empleado: random.randint(300000, 250000)for empleado in empleados}
    return sueldos

def clasificar_sueldos (sueldos):
    clasificacion = {"< $800,000":[], "$800,000 - $2,000,000": [], "> $2,000,000": []}
    for empleado, sueldo in sueldos.items():
        if sueldo < 800000:
            clasificacion["< $800,000": sueldo in sueldos]
        if sueldo > 2000000:
            clasificacion["> $2,000,000": sueldo in sueldos]
            
def ver_estadistica ():
    suma_sueldos = sum (sueldos)
    promedio_sueldos = suma_sueldos / len sueldos
    sueldo_max = max (sueldos)
    sueldo_min = min (sueldos)
        print("f suma de sueldos: $(suma_sueldos)")
        print("f promedio de sueldos: $(promedio_sueldos)")
        print("f sueldo maximo: $(sueldo_maximo)")
        print("f sueldo minimo: $(sueldo_minimo)")

def reportes_de_sueldo ():
    for empleados, sueldo in range sueldos
        print("f descuento salud:" 7%)
        print("f decuento AFP:" 12%)
        print("f sueldo liquido:" menos (0,7)
        print("f sueldo liquido:" menos (0,12)
              
def menu ():
    while True:
    print("Menu")
    print("1: Asignar sueldos aleatorios")
    print("2: Clasificar sueldos")
    print("3: Ver estadisticas")
    print("4: Reporte de sueldos")
    print("5: Salir del progama")
    print("6: Generar archivo csv")

break
 while True:
     print("finalizando progama, desarrollado por Sebastian Benavides, Rut: 21827434-k")
    

    
    
