from abc import ABC, abstractmethod

# Interfaz base para todos los estudiantes
class Alumno(ABC):
    def __init__(self, nombre, edad, rut):
        self.nombre = nombre
        self.edad = edad
        self.rut = rut
    def getrut(self):
        return self.rut
    def getnombre(self):
        return self.nombre
    def getedad(self):
        return self.edad
    @abstractmethod
    def estudiar(self):
        pass

    @abstractmethod
    def ejecutar_dia_alumno(self):
        pass


class pre(Alumno):
    @abstractmethod
    def estudiar(self):
        pass

    @abstractmethod
    def ejecutar_dia_alumno(self):
        pass


class post(Alumno):
    @abstractmethod
    def estudiar(self):
        pass

    @abstractmethod
    def ejecutar_dia_alumno(self):
        pass
    @abstractmethod
    def hacer_clases(self):
        pass

# Interfaz para los post que pueden hacer investigaciones
class investigador(ABC):
    @abstractmethod
    def hacer_investigacion(self):
        pass
# Interfaz para los estudiantes que pueden hacer ayudantía
class Ayudante(ABC):
    @abstractmethod
    def hacer_ayudantia(self):
        pass


class abc_EstudianteRegular(pre):
    @abstractmethod
    def ejecutar_dia_alumno(self):
        pass
    @abstractmethod
    def estudiar(self):
        pass

class abc_EstudianteAyudante(pre):
    @abstractmethod
    def ejecutar_dia_alumno(self):
        pass
    @abstractmethod
    def estudiar(self):
        pass
    @abstractmethod
    def hacer_ayudantia(self):
        pass

class abc_EstudianteMagister(post):
    @abstractmethod
    def ejecutar_dia_alumno(self):
        pass
    @abstractmethod
    def estudiar(self):
        pass
    def  hacer_clases(self):
        pass

class abc_EstudianteDoctorado(post):
    @abstractmethod
    def ejecutar_dia_alumno(self):
        pass
    @abstractmethod
    def estudiar(self):
        pass
    @abstractmethod
    def hacer_clases(self):
        pass
    @abstractmethod
    def investigar(self):
        pass



"""
class abc_alumni(Alumno):
    @abstractmethod
    def ejecutar_dia_alumni(self):
        pass
class alumni(abc_alumni):
    def ejecutar_dia_alumni(self):
        print(f"Ejecutando dia alumni {self.nombre}")
"""
# Estudiante regular no necesita hacer ayudantía, solo implementa lo básico
class EstudianteRegular(abc_EstudianteRegular):
    def ejecutar_dia_alumno(self):
        self.estudiar()

    def estudiar(self):
        print(f"{self.nombre} está estudiando.")

# Estudiante ayudante implementa tanto estudiar como hacer ayudantía
class EstudianteAyudante(abc_EstudianteAyudante):
    def __init__(self, nombre, edad, rut, servicio_ayudantia):
        super().__init__(nombre, edad, rut)
        # La dependencia Ayudantia es pasada desde fuera (inyección de dependencias)
        self.servicio_ayudantia = servicio_ayudantia

    def ejecutar_dia_alumno(self):
        self.estudiar()
        self.hacer_ayudantia()

    def estudiar(self):
        print(f"{self.nombre} está estudiando.")

    def hacer_ayudantia(self):
        self.servicio_ayudantia.hacer_ayudantia()

# Dependencia de Ayudantia que EstudianteAyudante utilizará
class Ayudantia(Ayudante):
    def hacer_ayudantia(self):
        print("El ayudante está realizando la ayudantía.")

class EstudianteMagister(abc_EstudianteMagister):
    def ejecutar_dia_alumno(self):
        self.estudiar()
        self.hacer_clases()

    def estudiar(self):
        print(f"{self.nombre} está estudiando.")

    def hacer_clases(self):
        print(f"{self.nombre} esta haciendo clases")


class EstudianteDoctorado(abc_EstudianteDoctorado):
    def __init__(self, nombre, edad, rut, servicio_investigacion):
        super().__init__(nombre, edad, rut)
        # La dependencia Ayudantia es pasada desde fuera (inyección de dependencias)
        self.servicio_investigacion = servicio_investigacion

    def ejecutar_dia_alumno(self):
        self.estudiar()
        self.hacer_clases()
        self.investigar()

    def estudiar(self):
        print(f"{self.nombre} está estudiando.")

    def hacer_clases(self):
        print(f"{self.nombre} esta haciendo clases")
    def investigar(self):
        self.servicio_investigacion.hacer_investigacion()

# Dependencia de Ayudantia que EstudianteAyudante utilizará
class investigar(investigador):
    def hacer_investigacion(self):
        print("El investigador esta investigando")
