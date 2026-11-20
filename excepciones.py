
# ============================================================
# EXCEPCIONES PERSONALIZADAS - SISTEMA SOFTWARE FJ
# ============================================================

class ErrorSistema(Exception):
    """Excepcion base para los errores del sistema."""
    pass


class ErrorCliente(ErrorSistema):
    """Error relacionado con los datos de los clientes."""
    pass


class ErrorServicio(ErrorSistema):
    """Error relacionado con los servicios disponibles."""
    pass


class ErrorReserva(ErrorSistema):
    """Error relacionado con la gestion de reservas."""
    pass


class ServicioNoDisponible(ErrorServicio):
    """Se genera cuando un servicio no esta disponible."""
    pass


class DatosInvalidos(ErrorSistema):
    """Se genera cuando los datos ingresados no son validos."""
    pass
