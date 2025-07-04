from abc import ABC, abstractmethod
from alumnos import *

class abc_asignaturas(ABC):
    def __init__(self, nombre, codigo, creditos, restriccion=None):
        self.nombre = nombre
        self.codigo = codigo
        self.creditos = creditos
        # las restricciones si un alumno debe estar cursando un tipo u otro
        self.restriccion = restriccion

    @abstractmethod
    def verificar(self, estudiante):
        pass

class pre_asignaturas(abc_asignaturas):
    pass

class post_asignaturas(abc_asignaturas):
    pass

class estudiante_asignaturas(abc_asignaturas):
    def verificar(self,estudiante):
        if self.restriccion is None or isinstance(estudiante, tuple(self.restriccion)):
            return True
        else:
            return False
    def getnombre(self):
        return self.nombre
    def getcodigo(self):
        return self.codigo
    def getcreditos(self):
        return self.creditos


class ayudante_asignaturas(abc_asignaturas):
    def verificar(self,estudiante):
        if self.restriccion is None or isinstance(estudiante, tuple(self.restriccion)):
            return True
        else:
            return False
    def getnombre(self):
        return self.nombre
    def getcodigo(self):
        return self.codigo
    def getcreditos(self):
        return self.creditos

class magister_asignaturas(abc_asignaturas):
    def verificar(self,estudiante):
        if self.restriccion is None or isinstance(estudiante, tuple(self.restriccion)):
            return True
        else:
            return False
    def getnombre(self):
        return self.nombre
    def getcodigo(self):
        return self.codigo
    def getcreditos(self):
        return self.creditos

class doctorado_asignaturas(abc_asignaturas):
    def verificar(self,estudiante):
        if self.restriccion is None or isinstance(estudiante, tuple(self.restriccion)):
            return True
        else:
            return False
    def getnombre(self):
        return self.nombre
    def getcodigo(self):
        return self.codigo
    def getcreditos(self):
        return self.creditos