# Fase_4
Componente practico 
# ============================================================
# CLASE CLIENTE - SISTEMA SOFTWARE FJ
# ============================================================

import re
from entidades import Entidad
from excepciones import DatosInvalidos


class Cliente(Entidad):
    """
    Representa un cliente de Software FJ.
    Hereda de la clase abstracta Entidad.
    """

    def __init__(self, identificador, nombre, correo, telefono):
        super().__init__(identificador)

        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono

    # --------------------------------------------------------
    # VALIDACION DEL NOMBRE
    # --------------------------------------------------------

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise DatosInvalidos(
                "El nombre del cliente es obligatorio."
            )

        if len(valor.strip()) < 3:
            raise DatosInvalidos(
                "El nombre debe tener al menos 3 caracteres."
            )

        self._nombre = valor.strip()

    # --------------------------------------------------------
    # VALIDACION DEL CORREO
    # --------------------------------------------------------

    @property
    def correo(self):
        return self._correo

    @correo.setter
    def correo(self, valor):
        if not isinstance(valor, str):
            raise DatosInvalidos(
                "El correo debe ser un texto."
            )

        patron = r"^[\w.+-]+@[\w-]+\.[\w.-]+$"

        if not re.match(patron, valor.strip()):
            raise DatosInvalidos(
                "El correo electronico no es valido."
            )

        self._correo = valor.strip().lower()

    # --------------------------------------------------------
    # VALIDACION DEL TELEFONO
    # --------------------------------------------------------

    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, valor):
        if not isinstance(valor, str) or not valor.isdigit():
            raise DatosInvalidos(
                "El telefono debe contener solamente numeros."
            )

        if len(valor) != 10:
            raise DatosInvalidos(
                "El telefono debe tener 10 digitos."
            )

        self._telefono = valor

    # --------------------------------------------------------
    # INFORMACION DEL CLIENTE
    # --------------------------------------------------------

    def obtener_informacion(self):
        """Devuelve la informacion completa del cliente."""

        return (
            f"ID: {self.identificador}\n"
            f"Nombre: {self.nombre}\n"
            f"Correo: {self.correo}\n"
            f"Telefono: {self.telefono}\n"
            f"Estado: {'Activo' if self.activo else 'Inactivo'}"
        )

    def __str__(self):
        return f"{self.nombre} - {self.correo}"
