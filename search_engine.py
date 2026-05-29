# ==================================================
# MÓDULO: search_engine.py
# ==================================================
# Este módulo es el encargado de buscar
# videojuegos dentro de la base de datos.
#
# Funciones principales:
# - Buscar coincidencias exactas
# - Buscar coincidencias parciales
# - Mostrar sugerencias
# - Resolver automáticamente resultados
#
# Objetivo:
# Ayudar al usuario a encontrar juegos
# aunque no escriba el nombre completo.
# ==================================================


# ==================================================
# FUNCIÓN: buscar_juego
# ==================================================
# Busca un videojuego dentro de la base de datos.
#
# Parámetros:
#
# juego:
#     Nombre introducido por el usuario.
#
# game_database:
#     Diccionario cargado desde games.json
#
# Retorna:
#
# juego_encontrado:
#     Nombre final del juego encontrado.
#
# datos_juego:
#     Diccionario con toda la información
#     del juego.
#
# Ejemplo:
#
# Entrada:
#     "crash"
#
# Salida:
#     "Crash Bandicoot 3"
#
# ==================================================

def buscar_juego(juego, game_database):

    # ==============================================
    # BÚSQUEDA EXACTA
    # ==============================================
    #
    # Intentar encontrar el juego exactamente
    # como fue escrito por el usuario.
    #
    # Ejemplo:
    #
    # Usuario:
    #     Crash Bandicoot 3
    #
    # Resultado:
    #     Juego encontrado directamente
    #
    # ==============================================

    datos_juego = game_database.get(juego)

    # Si existe una coincidencia exacta
    if datos_juego:

        return juego, datos_juego

    # ==============================================
    # SISTEMA DE SUGERENCIAS
    # ==============================================
    #
    # Si no existe coincidencia exacta,
    # se buscarán juegos similares.
    #
    # ==============================================

    sugerencias = []

    # ==============================================
    # RECORRER BASE DE DATOS
    # ==============================================
    #
    # Analizar todos los juegos registrados.
    #
    # ==============================================

    for nombre_juego in game_database:

        # ==========================================
        # COINCIDENCIA PARCIAL
        # ==========================================
        #
        # Tomar los primeros 3 caracteres
        # escritos por el usuario.
        #
        # Ejemplo:
        #
        # Usuario:
        #     crash
        #
        # Se usa:
        #     cra
        #
        # ==========================================

        if juego[:3] in nombre_juego.lower():

            sugerencias.append(
                nombre_juego
            )

    # ==============================================
    # SI EXISTEN SUGERENCIAS
    # ==============================================

    if sugerencias:

        print("\n💡 Quizás quisiste decir:\n")

        # Mostrar todas las sugerencias encontradas
        for sugerencia in sugerencias:

            print(
                f"- {sugerencia}"
            )

        # ==========================================
        # AUTO MATCHING
        # ==========================================
        #
        # Seleccionar automáticamente
        # la primera coincidencia.
        #
        # Ejemplo:
        #
        # [
        #   "Crash Bandicoot 3"
        # ]
        #
        # sugerencias[0]
        #
        # ==========================================

        juego_encontrado = sugerencias[0]

        print(
            f"\n✅ Usando automáticamente: "
            f"{juego_encontrado}"
        )

        # ==========================================
        # DEVOLVER RESULTADO
        # ==========================================
        #
        # Retornar:
        #
        # - Nombre encontrado
        # - Datos completos del juego
        #
        # ==========================================

        return (
            juego_encontrado,
            game_database[juego_encontrado]
        )

    # ==============================================
    # JUEGO NO ENCONTRADO
    # ==============================================
    #
    # Si no hubo coincidencias exactas
    # ni sugerencias válidas.
    #
    # ==============================================

    print(
        "\n❌ Juego no encontrado."
    )

    # Retornar valores vacíos
    return None, None