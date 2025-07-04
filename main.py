#from alumnos import *
#from asignaturas import *
from db import *

#probar que funciona para distintos alumnos y distintas tareas cada uno
juan = EstudianteRegular("Juan", 20, "12.345.678-9")
ayudantia = Ayudantia()  # Creamos la instancia de la dependencia
maria = EstudianteAyudante("María", 22, "98.765.432-1", ayudantia)

Alonso = EstudianteMagister("Alonso", 30, "15.123.555.7")
investiga = investigar()  # Creamos la instancia de la dependencia
juana = EstudianteDoctorado("juana", 34, "55.445.348-7", investiga)

juan.ejecutar_dia_alumno()
maria.ejecutar_dia_alumno()
Alonso.ejecutar_dia_alumno()
juana.ejecutar_dia_alumno()

#los casos de uso que piden
print(f"\n\nCasos de uso:")

#buscar alumnos
print(f"\nBuscar alumnos:")
datos = db()
datos.agregaralumno(juan)
datos.buscaralumno("12.345.678-9")
datos.eliminaralumno("12.345.678-9")

#descargar Notas
print(f"\ndescargar Notas:")
datos.agregarAsignatura(estudiante_asignaturas("BaseDeDatos", "416","6"))
datos.descargarNotas(juan,"416")

print(f"\nAsignar asignaturas:")
#Ejemplo sin restricciones
MetodologiaDeDiseno = estudiante_asignaturas("MetodologiaDeDiseno", "414","4")
datos.agregarAsignatura(MetodologiaDeDiseno)
datos.verificaralumno("414", juan)

#Ejemplo Con restricciones
superProgramacion = magister_asignaturas("SuperProgramación", "705","4",[EstudianteMagister,EstudianteDoctorado])
datos.agregarAsignatura(superProgramacion)
datos.verificaralumno("705", juan)

