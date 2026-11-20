
# ============================================================
# SISTEMA DE REGISTRO LOG - SOFTWARE FJ
# ============================================================

import logging
import os


# Crear la carpeta de registros si no existe
CARPETA_LOGS = "logs"

os.makedirs(CARPETA_LOGS, exist_ok=True)

RUTA_LOG = os.path.join(CARPETA_LOGS, "sistema.log")


# Configuracion del registro
logging.basicConfig(
    filename=RUTA_LOG,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    encoding="utf-8",
    force=True
)


# ============================================================
# FUNCIONES DE REGISTRO
# ============================================================

def registrar_evento(mensaje):
    """Registra una operacion exitosa."""
    logging.info(mensaje)


def registrar_advertencia(mensaje):
    """Registra una advertencia del sistema."""
    logging.warning(mensaje)


def registrar_error(mensaje):
    """Registra un error controlado."""
    logging.error(mensaje)


def registrar_excepcion(mensaje):
    """Registra un error junto con su informacion tecnica."""
    logging.exception(mensaje)


def registrar_error_inesperado(mensaje):
    """Registra una excepcion inesperada."""
    logging.exception(mensaje)


# Confirmar inicializacion
registrar_evento("Sistema de registro LOG inicializado.")
