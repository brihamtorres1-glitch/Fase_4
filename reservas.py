
# ============================================================
# CLASE RESERVA - SISTEMA SOFTWARE FJ
# ============================================================

from clientes import Cliente
from servicios import Servicio
from excepciones import (
    ErrorReserva,
    ServicioNoDisponible,
    DatosInvalidos
)


class Reserva:
    """
    Representa una reserva realizada por un cliente
    para utilizar uno de los servicios de Software FJ.
    """

    ESTADOS_VALIDOS = (
        "Pendiente",
        "Confirmada",
        "Procesada",
        "Cancelada"
    )

    def __init__(self, identificador, cliente, servicio, duracion):

        if not identificador:
            raise DatosInvalidos(
                "El identificador de la reserva es obligatorio."
            )

        if not isinstance(cliente, Cliente):
            raise ErrorReserva(
                "La reserva debe estar asociada a un cliente valido."
            )

        if not isinstance(servicio, Servicio):
            raise ErrorReserva(
                "La reserva debe tener un servicio valido."
            )

        if not cliente.activo:
            raise ErrorReserva(
                "No se puede reservar con un cliente inactivo."
            )

        if not servicio.activo:
            raise ServicioNoDisponible(
                "El servicio seleccionado no esta disponible."
            )

        servicio.validar_duracion(duracion)

        self._identificador = identificador
        self._cliente = cliente
        self._servicio = servicio
        self._duracion = duracion
        self._estado = "Pendiente"
        self._costo = None

    # --------------------------------------------------------
    # PROPIEDADES
    # --------------------------------------------------------

    @property
    def identificador(self):
        return self._identificador

    @property
    def cliente(self):
        return self._cliente

    @property
    def servicio(self):
        return self._servicio

    @property
    def duracion(self):
        return self._duracion

    @property
    def estado(self):
        return self._estado

    @property
    def costo(self):
        return self._costo

    # --------------------------------------------------------
    # CONFIRMAR RESERVA
    # --------------------------------------------------------

    def confirmar(self):

        if self._estado != "Pendiente":
            raise ErrorReserva(
                "Solo se pueden confirmar reservas pendientes."
            )

        if not self._cliente.activo:
            raise ErrorReserva(
                "El cliente se encuentra inactivo."
            )

        if not self._servicio.activo:
            raise ServicioNoDisponible(
                "El servicio ya no esta disponible."
            )

        self._estado = "Confirmada"

        return f"Reserva {self._identificador} confirmada exitosamente."

    # --------------------------------------------------------
    # CANCELAR RESERVA
    # --------------------------------------------------------

    def cancelar(self):

        if self._estado in ("Cancelada", "Procesada"):
            raise ErrorReserva(
                "No se puede cancelar una reserva cancelada o procesada."
            )

        self._estado = "Cancelada"

        return f"Reserva {self._identificador} cancelada exitosamente."

    # --------------------------------------------------------
    # PROCESAR RESERVA
    # --------------------------------------------------------

    def procesar(self, descuento=0, impuesto=0.19):

        if self._estado != "Confirmada":
            raise ErrorReserva(
                "La reserva debe estar confirmada antes de procesarse."
            )

        try:
            if not self._cliente.activo:
                raise ErrorReserva("El cliente esta inactivo.")

            if not self._servicio.activo:
                raise ServicioNoDisponible(
                    "El servicio no esta disponible."
                )

            self._costo = self._servicio.calcular_costo(
                self._duracion,
                descuento,
                impuesto
            )

            self._estado = "Procesada"

            return (
                f"Reserva procesada correctamente.\n"
                f"Identificador: {self._identificador}\n"
                f"Costo total: ${self._costo:,.2f}"
            )

        except (ErrorReserva, ServicioNoDisponible, DatosInvalidos) as error:
            raise ErrorReserva(
                f"No fue posible procesar la reserva: {error}"
            ) from error

    # --------------------------------------------------------
    # INFORMACION DE LA RESERVA
    # --------------------------------------------------------

    def obtener_informacion(self):

        costo_texto = (
            f"${self._costo:,.2f}"
            if self._costo is not None
            else "Pendiente de calcular"
        )

        return (
            f"RESERVA: {self._identificador}\n"
            f"Cliente: {self._cliente.nombre}\n"
            f"Servicio: {self._servicio.nombre}\n"
            f"Duracion: {self._duracion} horas\n"
            f"Estado: {self._estado}\n"
            f"Costo: {costo_texto}"
        )

    def __str__(self):
        return (
            f"Reserva {self._identificador} - "
            f"{self._cliente.nombre} - {self._estado}"
        )
