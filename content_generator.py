# ==================================================
# MÓDULO: content_generator.py
# ==================================================
# Este módulo es el encargado de generar
# contenido dinámico para videos gaming.
#
# Funciones principales:
# - Generar títulos
# - Generar descripciones
# - Generar comentarios fijados
#
# Objetivo:
# Automatizar la creación de contenido
# reutilizando plantillas inteligentes.
# ==================================================

# ==================================================
# IMPORTACIONES
# ==================================================

# Permite seleccionar elementos aleatorios
# de una lista.
import random


# ==================================================
# FUNCIÓN: generar_titulo
# ==================================================
# Genera títulos dinámicos según:
# - Juego
# - Nivel
# - Tipo de contenido
#
# Parámetros:
#
# juego:
#     Nombre del videojuego.
#
# nivel:
#     Nombre del nivel o misión.
#
# tipo:
#     walkthrough
#     shortplay
#
# Retorna:
#     Un título generado aleatoriamente.
#
# Ejemplo:
#
# "ORIENT EXPRESS PERFECT RUN ⚡ SIN FALLOS"
#
# ==================================================

def generar_titulo(juego, nivel, tipo):

    # Normalizar el tipo para evitar
    # problemas con mayúsculas
    tipo = tipo.lower()

    # ==============================================
    # TÍTULOS PARA WALKTHROUGH
    # ==============================================

    if tipo == "walkthrough":

        opciones = [

            f"{nivel.upper()} 100% WALKTHROUGH SIN MORIR 🚀 | {juego}",

            f"GUÍA COMPLETA {nivel.upper()} 💯 | {juego}",

            f"{nivel.upper()} PERFECT RUN ⚡ SIN FALLOS | {juego}"
        ]

    # ==============================================
    # TÍTULOS PARA SHORTPLAY
    # ==============================================

    elif tipo == "shortplay":

        opciones = [

            f"{nivel.upper()} ⚡ MOMENTOS CLAVE | {juego}",

            f"{nivel.upper()} EN 60 SEGUNDOS ⏱️ | {juego}",

            f"{nivel.upper()} HIGHLIGHTS 🔥 | {juego}"
        ]

    # ==============================================
    # TÍTULOS POR DEFECTO
    # ==============================================

    else:

        opciones = [

            f"{nivel.upper()} GAMEPLAY 🚀 | {juego}",

            f"{nivel.upper()} NIVEL COMPLETO 🎮 | {juego}"
        ]

    # ==============================================
    # SELECCIONAR TÍTULO ALEATORIO
    # ==============================================
    #
    # random.choice()
    #
    # Escoge una opción aleatoria
    # de la lista de títulos.
    #
    # Esto evita que todos los videos
    # tengan exactamente el mismo formato.
    #
    # ==============================================

    return random.choice(opciones)


# ==================================================
# FUNCIÓN: generar_descripcion
# ==================================================
# Genera descripciones dinámicas
# según el tipo de contenido.
#
# Parámetros:
#
# juego:
#     Nombre del videojuego.
#
# nivel:
#     Nombre del nivel.
#
# tipo:
#     walkthrough
#     shortplay
#
# Retorna:
#     Descripción completa del video.
#
# ==================================================

def generar_descripcion(juego, nivel, tipo):

    # Normalizar tipo
    tipo = tipo.lower()

    # ==============================================
    # DESCRIPCIÓN PARA WALKTHROUGH
    # ==============================================

    if tipo == "walkthrough":

        return f"""
🎮 {juego} - {nivel}

🚀 Guía completa para completar este nivel al 100% y sin morir.

💡 Aprende:
✔ Rutas óptimas
✔ Estrategias clave
✔ Cómo evitar errores

🔥 TIP: Mantén el ritmo y anticipa obstáculos.

👉 ¿Qué nivel quieres ver después?

#retrogaming #walkthrough #gaming
"""

    # ==============================================
    # DESCRIPCIÓN PARA SHORTPLAY
    # ==============================================

    elif tipo == "shortplay":

        return f"""
🎮 {juego} - {nivel}

⚡ Momentos clave de este nivel en formato corto.

💡 Perfecto para ver jugadas rápidas y tips esenciales.

👉 ¿Quieres la guía completa? Dímelo en comentarios.

#shorts #gaming #retrogaming
"""

    # ==============================================
    # DESCRIPCIÓN POR DEFECTO
    # ==============================================

    else:

        return f"""
🎮 {juego} - {nivel}

Gameplay del nivel.

👉 ¿Quieres más contenido como este?

#gaming
"""


# ==================================================
# FUNCIÓN: generar_comentario
# ==================================================
# Genera un comentario fijado para
# aumentar la interacción del público.
#
# Parámetros:
#
# nivel:
#     Nombre del nivel actual.
#
# Retorna:
#
# Comentario listo para fijar.
#
# Ejemplo:
#
# 🔥 ¿Te gustó Orient Express?
# Comenta qué nivel quieres ver después.
#
# ==================================================

def generar_comentario(nivel):

    return (
        f"🔥 ¿Te gustó {nivel}? "
        f"Comenta qué nivel quieres ver después."
    )