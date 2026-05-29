# 🎮 GameContent Engine V11
# ==================================================
# Archivo principal del sistema
#
# Responsabilidades:
# 1. Cargar la base de datos gaming
# 2. Recibir datos del usuario
# 3. Validar entradas
# 4. Buscar juegos
# 5. Generar contenido
# 6. Mostrar resultados
# ==================================================

# ==================================================
# IMPORTACIONES
# ==================================================

from level_engine import validar_nivel 

# Permite trabajar con archivos JSON
import json

# Funciones auxiliares
from utils import limpiar_texto

# Motor de búsqueda
from search_engine import buscar_juego

# Generador de contenido
from content_generator import (
    generar_titulo,
    generar_descripcion,
    generar_comentario
)

# Motor de hashtags
from hashtags_engine import generar_hashtags


# ==================================================
# CONFIGURACIÓN DEL SISTEMA
# ==================================================

# Tipos de contenido permitidos
tipos_validos = [
    "walkthrough",
    "shortplay"
]


# ==================================================
# CARGAR BASE DE DATOS
# ==================================================

# Abrir archivo JSON y convertirlo
# a diccionario Python
with open(
    "games.json",
    "r",
    encoding="utf-8"
) as file:

    game_database = json.load(file)


# ==================================================
# INPUT DEL USUARIO
# ==================================================

# Solicitar nombre del juego
# y limpiar caracteres especiales
juego = limpiar_texto(
    input("Nombre del juego: ")
)

# Solicitar nivel
nivel = input(
    "Nombre del nivel: "
).strip()

# Solicitar tipo de contenido
tipo = input(
    "Tipo (Walkthrough / Shortplay): "
).strip().lower()


# ==================================================
# VALIDACIÓN DE DATOS
# ==================================================

# Verificar que el tipo sea válido
if tipo not in tipos_validos:

    print("\n❌ ERROR: Tipo de contenido no válido.")
    print("✅ Opciones válidas:")

    for tipo_valido in tipos_validos:
        print(f"- {tipo_valido}")

    exit()



# ==================================================
# BÚSQUEDA DEL JUEGO
# ==================================================

# Buscar juego dentro de la base de datos
juego_encontrado, datos_juego = buscar_juego(
    juego,
    game_database
)

# Si no existe, terminar programa
if not datos_juego:
    exit()

#-----------Motor Engine nivel-------------
if not validar_nivel(
    nivel,
    datos_juego
):
    exit()


# ==================================================
# GENERACIÓN DE CONTENIDO
# ==================================================

# Generar título dinámico
titulo = generar_titulo(
    juego_encontrado,
    nivel,
    tipo
)

# Generar descripción
descripcion = generar_descripcion(
    juego_encontrado,
    nivel,
    tipo
)

# Generar hashtags inteligentes
hashtags = generar_hashtags(
    tipo,
    datos_juego
)

# Generar comentario fijado
comentario = generar_comentario(
    nivel
)


# ==================================================
# SALIDA DE RESULTADOS
# ==================================================

print("\n🎬 TÍTULO:")

# Mostrar información del juego
print(f"🎮 Juego: {juego_encontrado}")
print(f"🕹️ Plataforma: {datos_juego['plataforma']}")
print(f"🎭 Género: {datos_juego['genero']}")
print(f"⚡ Dificultad: {datos_juego['dificultad']}")

# Mostrar niveles registrados
print("\n📚 Niveles Disponibles:")

for nivel_db in datos_juego["niveles"]:
    print(f"- {nivel_db}")

# Mostrar contenido generado
print("\n" + titulo)

print("\n📝 DESCRIPCIÓN:")
print(descripcion)

print("\n🏷️ HASHTAGS:")
print(hashtags)

print("\n📌 COMENTARIO FIJADO:")
print(comentario)