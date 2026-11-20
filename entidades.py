
# ============================================================
# CLASE ABSTRACTA - SISTEMA SOFTWARE FJ
# ============================================================

from abc import ABC, abstractmethod


class Entidad(ABC):
    """
    Clase abstracta que representa las entidades generales
    del sistema Software FJ.
    """

    def __init__(self, identificador):
        if not identificador:
            raise ValueError("El identificador es obligatorio.")

        self._identificador = identificador
        self._activo = True

    @property
    def identificador(self):
        """Permite consultar el identificador."""
        return self._identificador

    @property
    def activo(self):
        """Permite consultar el estado de la entidad."""
        return self._activo

    def desactivar(self):
        """Desactiva la entidad."""
        self._activo = False

    def activar(self):
        """Activa nuevamente la entidad."""
        self._activo = True

    @abstractmethod
    def obtener_informacion(self):
        """
        Metodo abstracto que deben implementar
        las clases que hereden de Entidad.
        """
        pass
