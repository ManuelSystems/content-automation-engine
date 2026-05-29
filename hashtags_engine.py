# ==================================================
# FUNCIÓN: generar_hashtags
# ==================================================
# Genera hashtags automáticamente según:
# - Tipo de contenido
# - Plataforma del juego
# - Género del juego
#
# Parámetros:
# tipo:
#     walkthrough
#     shortplay
#
# datos_juego:
#     Diccionario obtenido desde games.json
#
# Retorna:
#     String con hashtags separados por espacios
#
# Ejemplo:
#     #walkthrough #gaming #retrogaming #PS1 #platformer
# ==================================================

def generar_hashtags(tipo, datos_juego):

    # Convertir el tipo a minúsculas para evitar
    # problemas con mayúsculas y minúsculas
    tipo = tipo.lower()

    # Lista vacía donde se almacenarán los hashtags
    hashtags = []

    # ==================================================
    # HASHTAGS POR TIPO DE CONTENIDO
    # ==================================================

    # Walkthrough (guía completa)
    if tipo == "walkthrough":

        hashtags.extend([
            "#walkthrough",
            "#gaming",
            "#retrogaming"
        ])

    # Shortplay (contenido corto)
    elif tipo == "shortplay":

        hashtags.extend([
            "#shorts",
            "#gaming",
            "#retrogaming"
        ])

    # ==================================================
    # HASHTAGS BASADOS EN METADATOS DEL JUEGO
    # ==================================================

    # Verificar que existan datos del juego
    if datos_juego:

        # ------------------------------------------
        # Plataforma
        # ------------------------------------------
        # Ejemplo:
        # PS1 -> #PS1
        # PS2 -> #PS2
        # SNES -> #SNES
        # ------------------------------------------

        hashtags.append(
            f"#{datos_juego['plataforma']}"
        )

        # ------------------------------------------
        # Género
        # ------------------------------------------

        genero = datos_juego["genero"].lower()

        # Juegos de plataformas
        if genero == "plataformas":

            hashtags.append(
                "#platformer"
            )

        # Juegos de carreras
        elif genero == "carreras":

            hashtags.append(
                "#racinggames"
            )

    # ==================================================
    # CONVERTIR LISTA A TEXTO
    # ==================================================
    #
    # Antes:
    #
    # [
    #   "#gaming",
    #   "#retrogaming",
    #   "#PS1"
    # ]
    #
    # Después:
    #
    # "#gaming #retrogaming #PS1"
    #
    # ==================================================

    return " ".join(hashtags)