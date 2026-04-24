from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Empleado:
    nombre: str
    salario_base: float
    departamento: str
    antiguedad: str
    cargo_empleado: str = field(init = False, default = None)

    def calcular_salario(self) -> float:
        return self.salario_base

    def __str__(self) -> str:
        return f"Nombre: {self.nombre}\n Departamento:{self.departamento}\n Antiguedad: {self.antiguedad}\nsalario_base:{self.calcular_salario}\n"

@dataclass
class Gerente(Empleado):
    bono: float
    return super

@dataclass
class Desarrollador(Empleado):
    pass
@dataclass
class Contratista:
    pass


