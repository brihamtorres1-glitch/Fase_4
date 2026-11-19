# ============================================================
# SOFTWARE FJ - SISTEMA INTEGRAL DE GESTION
# ARCHIVO PRINCIPAL
# ============================================================

from clientes import Cliente
from servicios import (
    ReservaSala,
    AlquilerEquipo,
    AsesoriaEspecializada
)
from reservas import Reserva
from excepciones import ErrorSistema, DatosInvalidos
from registro import (
    registrar_evento,
    registrar_advertencia,
    registrar_error,
    registrar_excepcion
)

# ============================================================
# LISTAS INTERNAS DEL SISTEMA
# ============================================================

clientes = []
servicios = []
reservas = []


# ============================================================
# FUNCIONES AUXILIARES
# ============================================================

def buscar_por_id(lista, identificador):
    for elemento in lista:
        if elemento.identificador == identificador:
            return elemento
    return None


def pedir_numero(mensaje, minimo=None):
    try:
        valor = float(input(mensaje))
    except ValueError as error:
        raise DatosInvalidos(
            "Debe ingresar un valor numerico valido."
        ) from error
    else:
        if minimo is not None and valor < minimo:
            raise DatosInvalidos(
                f"El valor debe ser igual o mayor que {minimo}."
            )
        return valor


def pausar():
    input("\nPresione ENTER para continuar...")


# ============================================================
# REGISTRAR CLIENTE
# ============================================================

def registrar_cliente():

    print("\n--- REGISTRO DE CLIENTE ---")

    identificador = input("Identificador: ").strip()

    if not identificador:
        raise DatosInvalidos("El identificador es obligatorio.")

    if buscar_por_id(clientes, identificador):
        raise DatosInvalidos("Ya existe un cliente con ese identificador.")

    nombre = input("Nombre completo: ")
    correo = input("Correo electronico: ")
    telefono = input("Telefono (10 digitos): ")

    cliente = Cliente(
        identificador,
        nombre,
        correo,
        telefono
    ) # type: ignore

    clientes.append(cliente)
    registrar_evento(
    f"Cliente {identificador} registrado correctamente."
)

    print("\nCliente registrado correctamente.")
    print(cliente.obtener_informacion())


# ============================================================
# CONSULTAR CLIENTES
# ============================================================

def consultar_clientes():

    print("\n--- LISTA DE CLIENTES ---")

    if not clientes:
        print("No hay clientes registrados.")
        return

    for cliente in clientes:
        print("\n" + cliente.obtener_informacion())
        print("-" * 40)


# ============================================================
# CREAR SERVICIO
# ============================================================

def crear_servicio():

    print("\n--- CREACION DE SERVICIOS ---")
    print("1. Reserva de salas")
    print("2. Alquiler de equipos")
    print("3. Asesoria especializada")

    opcion = input("Seleccione el tipo de servicio: ")

    identificador = input("Identificador del servicio: ").strip()

    if not identificador:
        raise DatosInvalidos("El identificador es obligatorio.")

    if buscar_por_id(servicios, identificador):
        raise DatosInvalidos("Ya existe un servicio con ese identificador.")

    tarifa = pedir_numero("Tarifa base: $", 0.01)

    if opcion == "1":
        capacidad = pedir_numero("Capacidad de la sala: ", 1)

        if not capacidad.is_integer():
            raise DatosInvalidos("La capacidad debe ser un numero entero.")

        servicio = ReservaSala(
            identificador,
            tarifa,
            int(capacidad)
        )

    elif opcion == "2":
        tipo = input("Tipo de equipo: ")
        servicio = AlquilerEquipo(
            identificador,
            tarifa,
            tipo
        )

    elif opcion == "3":
        especialidad = input("Especialidad de la asesoria: ")
        servicio = AsesoriaEspecializada(
            identificador,
            tarifa,
            especialidad
        )

    else:
        raise DatosInvalidos("La opcion de servicio no es valida.")

    servicios.append(servicio)
    registrar_evento(
    f"Servicio {identificador} creado correctamente."
)

    print("\nServicio creado correctamente.")
    print(servicio.obtener_informacion())


# ============================================================
# CONSULTAR SERVICIOS
# ============================================================

def consultar_servicios():

    print("\n--- SERVICIOS DISPONIBLES ---")

    if not servicios:
        print("No hay servicios registrados.")
        return

    for servicio in servicios:
        print("\n" + servicio.obtener_informacion())
        print(servicio.describir_servicio())
        print("-" * 40)


# ============================================================
# CREAR RESERVA
# ============================================================

def crear_reserva():

    print("\n--- CREACION DE RESERVA ---")

    if not clientes or not servicios:
        raise DatosInvalidos(
            "Primero debe registrar al menos un cliente y un servicio."
        )

    consultar_clientes()
    id_cliente = input("\nIdentificador del cliente: ").strip()

    cliente = buscar_por_id(clientes, id_cliente)

    if cliente is None:
        raise DatosInvalidos("El cliente no existe.")

    consultar_servicios()
    id_servicio = input("\nIdentificador del servicio: ").strip()

    servicio = buscar_por_id(servicios, id_servicio)

    if servicio is None:
        raise DatosInvalidos("El servicio no existe.")

    id_reserva = input("Identificador de la reserva: ").strip()

    if not id_reserva:
        raise DatosInvalidos("El identificador es obligatorio.")

    if buscar_por_id(reservas, id_reserva):
        raise DatosInvalidos("Ya existe una reserva con ese identificador.")

    duracion = pedir_numero("Duracion en horas: ", 0.01)

    reserva = Reserva(
        id_reserva,
        cliente,
        servicio,
        duracion
    )

    reservas.append(reserva)
    registrar_evento(
    f"Reserva {id_reserva} creada correctamente."
)

    print("\nReserva creada correctamente.")
    print(reserva.obtener_informacion())


# ============================================================
# CONSULTAR RESERVAS
# ============================================================

def consultar_reservas():

    print("\n--- LISTA DE RESERVAS ---")

    if not reservas:
        print("No hay reservas registradas.")
        return

    for reserva in reservas:
        print("\n" + reserva.obtener_informacion())
        print("-" * 40)


# ============================================================
# BUSCAR RESERVA PARA UNA OPERACION
# ============================================================

def solicitar_reserva():

    if not reservas:
        raise DatosInvalidos("No existen reservas registradas.")

    identificador = input("Identificador de la reserva: ").strip()

    reserva = buscar_por_id(reservas, identificador)

    if reserva is None:
        raise DatosInvalidos("La reserva no existe.")

    return reserva


# ============================================================
# CONFIRMAR RESERVA
# ============================================================

def confirmar_reserva():

    print("\n--- CONFIRMAR RESERVA ---")

    reserva = solicitar_reserva()

    print(reserva.confirmar())
    registrar_evento(
    f"Reserva {reserva.identificador} confirmada."
)


# ============================================================
# CANCELAR RESERVA
# ============================================================

def cancelar_reserva():

    print("\n--- CANCELAR RESERVA ---")

    reserva = solicitar_reserva()

    print(reserva.cancelar())
    registrar_advertencia(
    f"Reserva {reserva.identificador} cancelada."
)
    


# ============================================================
# PROCESAR RESERVA
# ============================================================

def procesar_reserva():

    print("\n--- PROCESAR RESERVA ---")

    reserva = solicitar_reserva()

    descuento = pedir_numero(
        "Porcentaje de descuento (0 a 100): ",
        0
    )

    if descuento > 100:
        raise DatosInvalidos(
            "El descuento no puede superar el 100 por ciento."
        )

    print(reserva.procesar(descuento))
    registrar_evento(
    f"Reserva {reserva.identificador} procesada. "
    f"Costo: ${reserva.costo:,.2f}"
)


# ============================================================
# MENU PRINCIPAL
# ============================================================

def mostrar_menu():

    print("\n" + "=" * 55)
    print("       SISTEMA INTEGRAL DE GESTION SOFTWARE FJ")
    print("=" * 55)

    print("1. Registrar cliente")
    print("2. Consultar clientes")
    print("3. Crear servicio")
    print("4. Consultar servicios")
    print("5. Crear reserva")
    print("6. Confirmar reserva")
    print("7. Cancelar reserva")
    print("8. Procesar reserva")
    print("9. Consultar reservas")
    print("0. Salir")

    print("=" * 55)


# ============================================================
# EJECUCION DEL SISTEMA
# ============================================================

def ejecutar_sistema():

    while True:

        mostrar_menu()

        opcion = input("Seleccione una opcion: ").strip()

        try:

            if opcion == "1":
                registrar_cliente()

            elif opcion == "2":
                consultar_clientes()

            elif opcion == "3":
                crear_servicio()

            elif opcion == "4":
                consultar_servicios()

            elif opcion == "5":
                crear_reserva()

            elif opcion == "6":
                confirmar_reserva()

            elif opcion == "7":
                cancelar_reserva()

            elif opcion == "8":
                procesar_reserva()

            elif opcion == "9":
                consultar_reservas()

            elif opcion == "0":
                print("\nGracias por utilizar Software FJ.")
                break

            else:
                raise DatosInvalidos(
                    "Debe seleccionar una opcion entre 0 y 9."
                )

        except ErrorSistema as error:
            print(f"\nERROR CONTROLADO: {error}")
            registrar_error(str(error))

        except Exception as error:
            print(f"\nERROR INESPERADO: {error}")
            registrar_excepcion("Error inesperado durante la ejecucion.")

        finally:
            print("\nOperacion finalizada.")

        if opcion != "0":
            pausar()


# ============================================================
# PUNTO DE ENTRADA
# ============================================================

if __name__ == "__main__":
    ejecutar_sistema()
