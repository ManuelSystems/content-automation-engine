# ==================================================
# MÓDULO: utils.py
# ==================================================
# Este módulo contiene funciones auxiliares
# reutilizables en todo el sistema.
#
# Actualmente incluye:
# - Limpieza de texto
# - Normalización de entradas
#
# Objetivo:
# Preparar los datos antes de ser procesados
# por otros módulos del sistema.
# ==================================================

# ==================================================
# IMPORTACIONES
# ==================================================

# Módulo de Expresiones Regulares (Regex)
# Permite buscar, reemplazar y validar texto
import re


# ==================================================
# FUNCIÓN: limpiar_texto
# ==================================================
# Limpia y normaliza el texto introducido
# por el usuario.
#
# Parámetros:
# texto:
#     Cadena de texto recibida como entrada.
#
# Retorna:
#     Texto limpio y normalizado.
#
# Ejemplo:
#
# Entrada:
#     "*** Crash Bandicoot 3 !!!"
#
# Salida:
#     "crash bandicoot 3"
#
# ==================================================

def limpiar_texto(texto):

    # ==============================================
    # ELIMINAR ESPACIOS Y NORMALIZAR MAYÚSCULAS
    # ==============================================
    #
    # strip():
    # Elimina espacios al inicio y al final.
    #
    # lower():
    # Convierte todo a minúsculas.
    #
    # Ejemplo:
    #
    # "  Crash Bandicoot 3  "
    #
    # ↓
    #
    # "crash bandicoot 3"
    #
    # ==============================================

    texto = texto.strip().lower()

    # ==============================================
    # LIMPIAR CARACTERES ESPECIALES
    # ==============================================
    #
    # Regex:
    #
    # r"[^a-z0-9\s]"
    #
    # Significa:
    #
    # ^      -> Negación
    # a-z    -> Letras minúsculas
    # 0-9    -> Números
    # \s     -> Espacios
    #
    # Todo lo que NO sea eso será eliminado.
    #
    # Ejemplo:
    #
    # "*** crash bandicoot 3 !!!"
    #
    # ↓
    #
    # "crash bandicoot 3"
    #
    # ==============================================

    texto = re.sub(
        r"[^a-z0-9\s]",
        "",
        texto
    )

    # ==============================================
    # RETORNAR TEXTO LIMPIO
    # ==============================================

    return texto