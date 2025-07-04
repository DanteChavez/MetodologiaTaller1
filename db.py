from asignaturas import *
class db():
    def __init__(self):
        self.lista = {}
        self.lista2 = {}
    def agregarAsignatura(self,asignatura):
        self.lista[asignatura.getcodigo()] = asignatura
        print(f"asignatura {asignatura.getnombre()} agregado satisfactoriamente a la base de datos") # no deberían existir print aquí, pero asi es la vida
    def buscarAsignatura(self,codigo):
        print("Asignatura encontrada")
        return self.lista[codigo]
    def verificaralumno(self, codigo, nombre):
        if self.lista[codigo].verificar(nombre):
            print(f" {nombre.getnombre()} Agregado exitosamente a {self.lista[codigo].getnombre()}")
        else:
            print(f" {nombre.getnombre()} no cumple los requisitos para {self.lista[codigo].getnombre()}")

    def descargarNotas(self,alumno,codigo):
        print(f" {alumno.getnombre()} Esta descargando sus notas de {self.lista[codigo].getnombre()}")

    def agregaralumno(self,alumno):
        self.lista2[alumno.getrut()] = alumno
        print(f"Alumno {alumno.getnombre()} agregado satisfactoriamente a la base de datos")
    def buscaralumno(self,rut):
        print("Alumno encontrado exitosamente")
        return self.lista2[rut]

    def eliminaralumno(self,rut):
        print(f"Alumno {self.lista2[rut].getnombre()} eliminado exitosamente") #lol
        del self.lista2[rut]
