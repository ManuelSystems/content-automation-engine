# 🎮 GameContent Engine V2
# -----------------------------------------
# Este sistema genera contenido automático
# para videos de gaming basado en reglas.
# -----------------------------------------


# -----------------------------------------
# FUNCIÓN: generar_titulo
# -----------------------------------------
# Genera un título dependiendo del tipo de contenido
# Parámetros:
# - juego: nombre del juego
# - nivel: nombre del nivel
# - tipo: tipo de contenido (walkthrough, shortplay, etc.)
# -----------------------------------------

import json
#✅ Tipos validos permitidos
tipos_validos = ["walkthrough", "shortplay"]

import random

#🎮 Base de datos simple de videojuegos

#📦 Cargar base de datos JSON
with open("games.json","r",encoding="utf-8") as file:
    game_database = json.load(file)

#funciones para generar contenido
def generar_titulo(juego, nivel, tipo):

    tipo = tipo.lower()

    if tipo == "walkthrough":
        opciones = [
            f"{nivel.upper()} 100% WALKTHROUGH SIN MORIR 🚀 | {juego}",
            f"GUÍA COMPLETA {nivel.upper()} 💯 | {juego}",
            f"{nivel.upper()} PERFECT RUN ⚡ SIN FALLOS | {juego}"
        ]

    elif tipo == "shortplay":
        opciones = [
            f"{nivel.upper()} ⚡ MOMENTOS CLAVE | {juego}",
            f"{nivel.upper()} EN 60 SEGUNDOS ⏱️ | {juego}",
            f"{nivel.upper()} HIGHLIGHTS 🔥 | {juego}"
        ]

    else:
        opciones = [
            f"{nivel.upper()} GAMEPLAY 🚀 | {juego}",
            f"{nivel.upper()} NIVEL COMPLETO 🎮 | {juego}"
        ]

    return random.choice(opciones)

# -----------------------------------------
# FUNCIÓN: generar_descripcion
# -----------------------------------------
# Genera una descripción larga con formato dinámico
# Usa plantillas de texto (templates)
# -----------------------------------------
def generar_descripcion(juego, nivel, tipo):

    tipo = tipo.lower()

    # Walkthrough (guía completa)
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

    # Shortplay (contenido corto)
    elif tipo == "shortplay":
        return f"""
🎮 {juego} - {nivel}

⚡ Momentos clave de este nivel en formato corto.

💡 Perfecto para ver jugadas rápidas y tips esenciales.

👉 ¿Quieres la guía completa? Dímelo en comentarios.

#shorts #gaming #retrogaming
"""

    # Caso por defecto
    else:
        return f"""
🎮 {juego} - {nivel}

Gameplay del nivel.

👉 ¿Quieres más contenido como este?

#gaming
"""


# -----------------------------------------
# FUNCIÓN: generar_hashtags
# -----------------------------------------
# Devuelve hashtags según el tipo de contenido
# -----------------------------------------
def generar_hashtags(tipo, datos_juego):

    tipo = tipo.lower()
    hashtags = []

    # hashtags por tipo 
    if tipo == "walkthrough":
        hashtags.extend([
            "#walkthrough",
            "#gaming",
            "#retrogaming"
        ])

    elif tipo == "shortplay":
        hashtags.extend([
            "#shorts",
            "#gaming",
            "#retrogaming"
        ])

    # Hashtags automaticos desde metadatos 
    if datos_juego:
        #Plataforma 
        hashtags.append(f"#{datos_juego['plataforma']}")

        #Genero 
        genero = datos_juego["genero"].lower()

        if genero == "plataformas":
            hashtags.append("#platformer")

        elif genero == "carreras": 
            hashtags.append("racinggames")

    #Convertir lista -> string
    return " ".join(hashtags)


# -----------------------------------------
# FUNCIÓN: generar_comentario
# -----------------------------------------
# Genera un comentario fijo para engagement
# Solo necesita el nivel
# -----------------------------------------
def generar_comentario(nivel):
    return f"🔥 ¿Te gustó {nivel}? Comenta qué nivel quieres ver después."


# -----------------------------------------
# INPUT (entrada de datos)
# -----------------------------------------
# Aquí el usuario introduce la información
# -----------------------------------------
juego = input("Nombre del juego: ").strip().lower()
nivel = input("Nombre del nivel: ").strip()
tipo = input("Tipo (Walkthrough / Shortplay): ").strip()
#Convertir a minusculas 
tipo = tipo.lower()

#Validar tipo 
if tipo not in tipos_validos:

    print("\n ❌ ERROR: Tipo de contenido no valido.")
    print("✅ Opciones validos:")

    for tipo_valido in tipos_validos: 
        print(f"- {tipo_valido}")

    exit()

#Obtener datos del juego desde la base de datos
datos_juego = game_database.get(juego)

#🔍 Smart Search System
datos_juego = None 
juego_encontrado = None 

#Recorrer todos  los juegos de la base de datos 
for nombre_juego in game_database:

    #Coincidencia parcial
    if juego in nombre_juego: 

        juego_encontrado = nombre_juego 
        datos_juego = game_database[nombre_juego]

        break 

# -----------------------------------------
# PROCESO (ejecución del sistema)
# -----------------------------------------
# Llamamos a cada función pasando los datos
# -----------------------------------------
titulo = generar_titulo(juego, nivel, tipo)
descripcion = generar_descripcion(juego, nivel, tipo)
hashtags = generar_hashtags(tipo)
comentario = generar_comentario(nivel)


# -----------------------------------------
# OUTPUT (salida del sistema)
# -----------------------------------------
# Mostramos los resultados en consola
# -----------------------------------------
print("\n🎬 TÍTULO:")
#Mostrar informacion extra del juego
if datos_juego:
    print(f"🎮 Juego: {juego_encontrado}")
    print(f"🕹️ Plataforma: {datos_juego['plataforma']}")
    print(f"🎭 Género: {datos_juego['genero']}")
    print(f"⚡ Dificultad: {datos_juego['dificultad']}")   
    print("\n📚 Niveles Disponibles:")
    for nivel_db in datos_juego["niveles"]:
        print(f"- {nivel_db}")

print(titulo)

print("\n📝 DESCRIPCIÓN:")
print(descripcion)

print("\n🏷️ HASHTAGS:")
print(hashtags)

print("\n📌 COMENTARIO FIJADO:")
print(comentario)