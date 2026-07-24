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
from generators.search_generator import buscar_juego
from generators.header_generator import generar_encabezado
from generators.game_loader import cargar_juegos
from generators.id_generator import generar_id

from engine.engine_loader import cargar_estado_motor
estado_motor =  cargar_estado_motor()
print(estado_motor)

game_database = cargar_juegos()

juego = input(
    "Nombre del juego: "
)

nivel = input(
    "Nombre del nivel: "
)

tipo = input(
    "Tipo (Walkthrough/Shortplay): "
)

contenido_id = generar_id(tipo)
print(contenido_id)

#para saber que tipo de contenido se va a generar, si es un walkthrough o un shortplay👇
#print(tipo)

datos_juego = None
juego_encontrado = None 

juego_encontrado, datos_juego = buscar_juego(
    juego,
    game_database
)
                        
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

    encabezado = generar_encabezado(
        juego_encontrado,
        tipo, 
        datos_juego["plataforma"]
    )

    #salida completa de todo 
    print(contenido_completo)

    nombre_archivo = (
        juego_encontrado.replace(" ", "_")
    )

    guardar_contenido(
        nombre_archivo,
        encabezado,
        contenido_completo
    )

else:   
    print(
        "\n❌ Juego no encontrado."
    )
