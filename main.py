import json
import os 

#importar generadores y funciones 
from generators.title_generator import generar_titulo
from generators.description_generator import generar_descripcion
from generators.hashtags_generator import generar_hashtags
from generators.comment_generator import generar_comentario
from generators.datagame_generator import generar_datagame
from generators.community_post_generator import generar_community_post
from generators.content_generator import generar_contenido_completo
from generators.save_generator import guardar_contenido

def generar_encabezado():
    encabezado = (
        "GAMECONTENTENGINE\n"
        "GENERADOR DE CONTENIDO GAMING" 
    )
    return encabezado

with open(
    "games.json",
    "r",
    encoding="utf-8"
) as file:

    game_database = json.load(file)

juego = input(
    "Nombre del juego: "
)

nivel = input(
    "Nombre del nivel: "
)

tipo = input(
    "Tipo (Walkthrough/Shortplay): "
)
#para saber que tipo de contenido se va a generar, si es un walkthrough o un shortplay👇
#print(tipo)

datos_juego = None
juego_encontrado = None 

for nombre_juego in game_database:
    if juego.lower() in nombre_juego.lower():
        juego_encontrado = nombre_juego
        datos_juego = game_database[nombre_juego]
        break

if datos_juego:

    print("\n🎮 Juego:", juego_encontrado)

    print(
        "🕹️ Plataforma:",
        datos_juego["plataforma"]
    )

    print(
        "🎭 Género:",
        datos_juego["genero"]
    )   

    titulo = generar_titulo(
        juego_encontrado,
        nivel,
        tipo
    )

    descripcion = generar_descripcion(
        juego_encontrado,
        nivel,
        tipo
    )

    hashtags = generar_hashtags(
        juego_encontrado
    )

    comentario = generar_comentario()

    datagame = generar_datagame(
        juego_encontrado,
        datos_juego
    )
    
    community_post = generar_community_post(
        juego_encontrado,
        nivel
    )

    contenido_completo = generar_contenido_completo(
        titulo,
        descripcion,
        hashtags,
        comentario,
        datagame,
        community_post
    )

    encabezado = generar_encabezado()

    #salida completa de todo 
    print(contenido_completo)

    nombre_archivo = (
        juego_encontrado.replace(" ", "_")
    )

    # os.makedirs(
    #    "output",
    #    exist_ok=True
    # )

    # with open(
    #     f"output/{nombre_archivo}.txt",
    #     "w",
    #     encoding="utf-8"
    # ) as archivo: 

    #     archivo.write(
    #         f"{encabezado}\n\n"
    #     )
      
    #     archivo.write(
    #         contenido_completo
    #     )

    guardar_contenido(
        nombre_archivo,
        encabezado,
        contenido_completo
    )

else:   
    print(
        "\n❌ Juego no encontrado."
    )
