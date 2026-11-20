
# ============================================================
# SERVICIOS - SISTEMA SOFTWARE FJ
# ============================================================

from abc import abstractmethod
from entidades import Entidad
from excepciones import ErrorServicio, DatosInvalidos


# ============================================================
# CLASE ABSTRACTA SERVICIO
# ============================================================

class Servicio(Entidad):
    """
    Clase abstracta que representa los servicios
    ofrecidos por la empresa Software FJ.
    """

    def __init__(self, identificador, nombre, tarifa_base):
        super().__init__(identificador)

        if not isinstance(nombre, str) or not nombre.strip():
            raise DatosInvalidos("El nombre del servicio es obligatorio.")

        self.nombre = nombre.strip()

        if not isinstance(tarifa_base, (int, float)) or isinstance(tarifa_base, bool) or tarifa_base <= 0:
            raise DatosInvalidos("La tarifa base debe ser mayor que cero.")

        self.tarifa_base = float(tarifa_base)

    def validar_duracion(self, duracion):
        """Valida que la duracion sea un numero positivo."""

        if isinstance(duracion, bool) or not isinstance(duracion, (int, float)):
            raise DatosInvalidos("La duracion debe ser numerica.")

        if duracion <= 0:
            raise DatosInvalidos("La duracion debe ser mayor que cero.")

        return duracion

    def calcular_costo(self, duracion, descuento=0, impuesto=0.19):
        """
        Calcula el costo del servicio.
        Los parametros opcionales permiten diferentes
        variantes de calculo.
        """

        self.validar_duracion(duracion)

        if not isinstance(descuento, (int, float)) or isinstance(descuento, bool) or not 0 <= descuento <= 100:
            raise DatosInvalidos("El descuento debe estar entre 0 y 100.")

        if not isinstance(impuesto, (int, float)) or isinstance(impuesto, bool) or not 0 <= impuesto <= 1:
            raise DatosInvalidos("El impuesto debe estar entre 0 y 1.")

        subtotal = self.tarifa_base * duracion
        subtotal -= subtotal * (descuento / 100)

        return round(subtotal * (1 + impuesto), 2)

    @abstractmethod
    def describir_servicio(self):
        pass

    @abstractmethod
    def validar_parametros(self, **parametros):
        pass

    def obtener_informacion(self):
        return (
            f"Servicio: {self.nombre}\n"
            f"Identificador: {self.identificador}\n"
            f"Tarifa base: ${self.tarifa_base:,.2f}\n"
            f"Estado: {'Activo' if self.activo else 'Inactivo'}"
        )


# ============================================================
# SERVICIO 1: RESERVA DE SALAS
# ============================================================

class ReservaSala(Servicio):
    """Servicio de reserva de salas empresariales."""

    def __init__(self, identificador, tarifa_base, capacidad):
        super().__init__(identificador, "Reserva de salas", tarifa_base)
        self.validar_parametros(capacidad=capacidad)
        self.capacidad = capacidad

    def validar_parametros(self, **parametros):
        capacidad = parametros.get("capacidad")

        if isinstance(capacidad, bool) or not isinstance(capacidad, int) or capacidad <= 0:
            raise DatosInvalidos("La capacidad de la sala debe ser un entero positivo.")

    def describir_servicio(self):
        return (
            f"Reserva de sala empresarial.\n"
            f"Capacidad maxima: {self.capacidad} personas."
        )

    def calcular_costo(self, duracion, descuento=0, impuesto=0.19):
        """Calcula el costo segun las horas de reserva."""
        return super().calcular_costo(duracion, descuento, impuesto)


# ============================================================
# SERVICIO 2: ALQUILER DE EQUIPOS
# ============================================================

class AlquilerEquipo(Servicio):
    """Servicio de alquiler de equipos tecnologicos."""

    def __init__(self, identificador, tarifa_base, tipo_equipo):
        super().__init__(identificador, "Alquiler de equipos", tarifa_base)
        self.validar_parametros(tipo_equipo=tipo_equipo)
        self.tipo_equipo = tipo_equipo.strip()

    def validar_parametros(self, **parametros):
        tipo = parametros.get("tipo_equipo")

        if not isinstance(tipo, str) or not tipo.strip():
            raise DatosInvalidos("Debe especificar el tipo de equipo.")

    def describir_servicio(self):
        return (
            f"Alquiler de equipos tecnologicos.\n"
            f"Equipo disponible: {self.tipo_equipo}."
        )

    def calcular_costo(self, duracion, descuento=0, impuesto=0.19):
        """Calcula el costo segun el tiempo de alquiler."""
        return super().calcular_costo(duracion, descuento, impuesto)


# ============================================================
# SERVICIO 3: ASESORIAS ESPECIALIZADAS
# ============================================================

class AsesoriaEspecializada(Servicio):
    """Servicio de asesoria y consultoria especializada."""

    def __init__(self, identificador, tarifa_base, especialidad):
        super().__init__(identificador, "Asesoria especializada", tarifa_base)
        self.validar_parametros(especialidad=especialidad)
        self.especialidad = especialidad.strip()

    def validar_parametros(self, **parametros):
        especialidad = parametros.get("especialidad")

        if not isinstance(especialidad, str) or not especialidad.strip():
            raise DatosInvalidos("Debe especificar la especialidad de la asesoria.")

    def describir_servicio(self):
        return (
            f"Asesoria especializada.\n"
            f"Especialidad: {self.especialidad}."
        )

    def calcular_costo(self, duracion, descuento=0, impuesto=0.19):
        """Calcula el costo segun las horas de asesoria."""
        return super().calcular_costo(duracion, descuento, impuesto)
