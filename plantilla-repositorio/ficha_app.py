"""Ficha técnica de una aplicación móvil antes de publicarla en la tienda."""

from decimal import Decimal, ROUND_HALF_UP
import platform

# Datos de la aplicación APP-05 (Pareja 5)
CODIGO: str = "APP-05"
NOMBRE: str = "Gastos del Piso"
PAQUETE: str = "es.hogar.gastospiso"
VERSION_MAYOR: int = 4
VERSION_MENOR: int = 2
VERSION_PARCHE: int = 19
TAMANO_BYTES: int = 22_020_096
DESCARGAS: int = 9_750
PRECIO: float = 1.49
VALORACIONES: int = 640
ESTRELLAS: int = 2_976
PERMISOS: int = 0b0010001
COLOR_ICONO: int = 0xFF00897B

# Datos del programa
VERSION_PROGRAMA: str = "1.0.0"
AUTORES: str = "Nombre1 y Nombre2"
PENDIENTE: str = "Opción pendiente de implementar"

# Constantes de formato y cálculo (sin números mágicos)
ANCHO: int = 42
COLUMNA: int = 18
ANCHO_NUM: int = 10
ANCHO_DEC_COLOR: int = 3
ANCHO_HEX_COLOR: int = 2
ANCHO_HEX_VER: int = 6
ANCHO_BIN_PERM: int = 7
ANCHO_BIN_COLOR: int = 8

BYTES_MB: int = 1_000_000
BYTES_MIB: int = 1_048_576
CIEN: int = 100
COMISION: float = 0.15

BITS_24: int = 24
BITS_16: int = 16
BITS_8: int = 8
MASCARA_BYTE: int = 0xFF
MASCARA_7_BITS: int = 0b1111111
MAX_COLOR: int = 255

PERMISO_INTERNET: int = 0b0000001
PERMISO_NOTIFICACIONES: int = 0b0000010
PERMISO_CAMARA: int = 0b0000100
PERMISO_UBICACION: int = 0b0001000
PERMISO_CONTACTOS: int = 0b0010000
PERMISO_MICROFONO: int = 0b0100000
PERMISO_ALMACENAMIENTO: int = 0b1000000

UN_DECIMAL: int = 1
DOS_DECIMALES: int = 2
PREC_1_DEC: str = "0.1"
PREC_2_DEC: str = "0.01"


def fila(etiqueta: str, valor: str) -> str:
    """Devuelve una fila con la etiqueta alineada a la izquierda y su valor."""
    return f"{etiqueta:<{COLUMNA}}{valor}"


def opcion_1() -> None:
    """Muestra el código, nombre, paquete y versión de la aplicación."""
    version = f"{VERSION_MAYOR}.{VERSION_MENOR}.{VERSION_PARCHE}"
    print(fila("Código:", CODIGO))
    print(fila("Nombre:", NOMBRE))
    print(fila("Paquete:", PAQUETE))
    print(fila("Versión:", version))


def opcion_2() -> None:
    """Calcula y muestra el tamaño del APK en B, MB, MiB y su diferencia."""
    mb = TAMANO_BYTES / BYTES_MB
    mib = TAMANO_BYTES / BYTES_MIB
    diferencia = (mb - mib) / mb * CIEN

    print("TAMAÑO DEL APK")
    print(fila("Bytes:", f"{TAMANO_BYTES:>{ANCHO_NUM}} B"))
    print(fila("En la tienda:", f"{mb:>{ANCHO_NUM}.2f} MB"))
    print(fila("En el móvil:", f"{mib:>{ANCHO_NUM}.2f} MiB"))
    print(fila("Diferencia:", f"{diferencia:>{ANCHO_NUM}.1f} %"))


def opcion_3() -> None:
    """Calcula y muestra los ingresos brutos, la comisión y los netos."""
    brutos = DESCARGAS * PRECIO
    comision_tienda = brutos * COMISION
    netos = brutos - comision_tienda

    print("INGRESOS")
    print(fila("Descargas:", f"{DESCARGAS:>{ANCHO_NUM}} uds."))
    print(fila("Precio:", f"{PRECIO:>{ANCHO_NUM}.2f} €"))
    print(fila("Ingresos brutos:", f"{brutos:>{ANCHO_NUM}.2f} €"))
    print(fila("Comisión tienda:", f"{comision_tienda:>{ANCHO_NUM}.2f} €"))
    print(fila("Ingresos netos:", f"{netos:>{ANCHO_NUM}.2f} €"))


def opcion_4() -> None:
    """Empaqueta y desempaqueta el versionCode con operadores de bit."""
    version = f"{VERSION_MAYOR}.{VERSION_MENOR}.{VERSION_PARCHE}"
    parte_mayor = VERSION_MAYOR << BITS_16
    parte_menor = VERSION_MENOR << BITS_8
    version_code = parte_mayor | parte_menor | VERSION_PARCHE

    mayor = (version_code >> BITS_16) & MASCARA_BYTE
    menor = (version_code >> BITS_8) & MASCARA_BYTE
    parche = version_code & MASCARA_BYTE
    desempaquetado = f"{mayor}.{menor}.{parche}"

    print("VERSIONCODE")
    print(fila("Versión:", version))
    print(fila("versionCode:", str(version_code)))
    print(fila("En hexadecimal:", f"0x{version_code:0{ANCHO_HEX_VER}X}"))
    print(fila("Desempaquetado:", desempaquetado))


def opcion_5() -> None:
    """Comprueba qué permisos pide la aplicación usando máscaras de bit."""
    internet = (PERMISOS & PERMISO_INTERNET) != 0
    notificaciones = (PERMISOS & PERMISO_NOTIFICACIONES) != 0
    camara = (PERMISOS & PERMISO_CAMARA) != 0
    ubicacion = (PERMISOS & PERMISO_UBICACION) != 0
    contactos = (PERMISOS & PERMISO_CONTACTOS) != 0
    microfono = (PERMISOS & PERMISO_MICROFONO) != 0
    almacenamiento = (PERMISOS & PERMISO_ALMACENAMIENTO) != 0
    sin_ubicacion = (PERMISOS & ~PERMISO_UBICACION) & MASCARA_7_BITS

    print("PERMISOS")
    print(fila("En binario:", f"{PERMISOS:0{ANCHO_BIN_PERM}b}"))
    print(fila("Internet:", str(internet)))
    print(fila("Notificaciones:", str(notificaciones)))
    print(fila("Cámara:", str(camara)))
    print(fila("Ubicación:", str(ubicacion)))
    print(fila("Contactos:", str(contactos)))
    print(fila("Micrófono:", str(microfono)))
    print(fila("Almacenamiento:", str(almacenamiento)))
    print(fila("Sin ubicación:", f"{sin_ubicacion:0{ANCHO_BIN_PERM}b}"))


def opcion_6() -> None:
    """Extrae los canales del color ARGB y muestra su código CSS."""
    alfa = (COLOR_ICONO >> BITS_24) & MASCARA_BYTE
    rojo = (COLOR_ICONO >> BITS_16) & MASCARA_BYTE
    verde = (COLOR_ICONO >> BITS_8) & MASCARA_BYTE
    azul = COLOR_ICONO & MASCARA_BYTE
    opacidad = (alfa / MAX_COLOR) * CIEN

    r_txt = (
        f"{rojo:>{ANCHO_DEC_COLOR}} "
        f"{rojo:0{ANCHO_BIN_COLOR}b} "
        f"{rojo:0{ANCHO_HEX_COLOR}X}"
    )
    v_txt = (
        f"{verde:>{ANCHO_DEC_COLOR}} "
        f"{verde:0{ANCHO_BIN_COLOR}b} "
        f"{verde:0{ANCHO_HEX_COLOR}X}"
    )
    a_txt = (
        f"{azul:>{ANCHO_DEC_COLOR}} "
        f"{azul:0{ANCHO_BIN_COLOR}b} "
        f"{azul:0{ANCHO_HEX_COLOR}X}"
    )
    css = (
        f"#{rojo:0{ANCHO_HEX_COLOR}X}"
        f"{verde:0{ANCHO_HEX_COLOR}X}"
        f"{azul:0{ANCHO_HEX_COLOR}X}"
    )

    print("COLOR DEL ICONO")
    print(fila("ARGB:", f"0x{COLOR_ICONO:0{ANCHO_BIN_COLOR}X}"))
    print(fila("Rojo:", r_txt))
    print(fila("Verde:", v_txt))
    print(fila("Azul:", a_txt))
    print(fila("Opacidad:", f"{opacidad:.1f}%"))
    print(fila("Para CSS:", css))


def opcion_7() -> None:
    """Muestra el tipo de dato y el valor de siete variables del programa."""
    # Conversión implícita de int a float al dividir
    media = ESTRELLAS / VALORACIONES
    pide_camara = (PERMISOS & PERMISO_CAMARA) != 0
    # Conversión explícita de int a str con str()
    texto_descargas = str(DESCARGAS)
    mayor_desp = VERSION_MAYOR << BITS_16
    menor_desp = VERSION_MENOR << BITS_8
    codigo = mayor_desp | menor_desp | VERSION_PARCHE

    print("TIPOS DE DATOS")
    print(fila("NOMBRE:", f"{str(type(NOMBRE)):<{COLUMNA}} {NOMBRE}"))
    print(fila("DESCARGAS:", f"{str(type(DESCARGAS)):<{COLUMNA}} {DESCARGAS}"))
    print(fila("PRECIO:", f"{str(type(PRECIO)):<{COLUMNA}} {PRECIO}"))
    print(fila("media:", f"{str(type(media)):<{COLUMNA}} {media}"))
    print(
        fila(
            "pide_camara:",
            f"{str(type(pide_camara)):<{COLUMNA}} {pide_camara}",
        )
    )
    print(
        fila(
            "texto_descargas:",
            f"{str(type(texto_descargas)):<{COLUMNA}} {texto_descargas}",
        )
    )
    print(fila("codigo:", f"{str(type(codigo)):<{COLUMNA}} {codigo}"))


def opcion_8() -> None:
    """Compara el redondeo de round() frente al redondeo escolar."""
    media = ESTRELLAS / VALORACIONES
    media_dec = Decimal(ESTRELLAS) / Decimal(VALORACIONES)

    r_1 = round(media, UN_DECIMAL)
    esc_1 = media_dec.quantize(Decimal(PREC_1_DEC), rounding=ROUND_HALF_UP)
    r_2 = round(media, DOS_DECIMALES)
    esc_2 = media_dec.quantize(Decimal(PREC_2_DEC), rounding=ROUND_HALF_UP)

    print("REDONDEO DE LA VALORACIÓN MEDIA")
    print(fila("Valor exacto:", str(media)))
    print(fila("round(), 1 dec.:", str(r_1)))
    print(fila("Escolar, 1 dec.:", str(esc_1)))
    print(fila("round(), 2 dec.:", str(r_2)))
    print(fila("Escolar, 2 dec.:", str(esc_2)))


def opcion_9() -> None:
    """Muestra la ficha completa llamando a las funciones de la 1 a la 4."""
    borde = "=" * ANCHO
    linea = "-" * ANCHO

    print(borde)
    print("FICHA DE LA APLICACIÓN".center(ANCHO))
    print(borde)
    opcion_1()
    print(linea)
    opcion_2()
    print(linea)
    opcion_3()
    print(linea)
    opcion_4()
    print(borde)


def opcion_10() -> None:
    """Muestra la descripción del módulo, versión, autores y Python."""
    print("ACERCA DE")
    print(__doc__)
    print()
    print(fila("Versión:", VERSION_PROGRAMA))
    print(fila("Autores:", AUTORES))
    print(fila("Python:", platform.python_version()))