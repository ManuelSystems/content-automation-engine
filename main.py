import json
import os 

def generar_titulo(juego,nivel,tipo):
    if tipo.lower() == "walkthrough":
        titulo = (
            f"{nivel.upper()} "
            f"100% WALKTHROUGH 🚀" 
        )
    elif tipo.lower() == "shortplay":
        titulo = (
            f"{nivel.upper()} "
            f"⚡Momento Clave"
        )    
    else: 
        titulo = (
            f"{nivel.upper()} "
            f"Gameplay Completo 🚀"
        )
    return titulo

def generar_descripcion(
        juego,
        nivel,
        tipo,
):

    descripcion = (
        f"🎮{juego}\n\n"
        f"📍 Nivel: {nivel}\n\n"
        f"🚀 Tipo: {tipo}"
    )
    return descripcion

def generar_hashtags(juego):
    palabras = juego.split()
    hashtags = [] 

    for palabra in palabras: 
        hashtags.append(
            f"#{palabra}"
        )
    
    hashtags.append("#LegacyGaming")
    hashtags.append("#RetroGaming")
    hashtags.append("#FullRetroGaming")

    return " ".join(hashtags)

def generar_comentario():

    comentario = (
        "🔥 Si te gustó este contenido, "
        "suscríbete para más videojuegos.\n\n"
        "🎮 FullRetroGaming"
    )

    return comentario

def generar_datagame(
        juego,
        datos_juego
):
    datagame = (
        f"📚 DATAGAME\n\n"
        f"🎮 {juego}\n\n"
        f"🕹️ Plataforma: {datos_juego['plataforma']}\n"
        f"🎭 Género: {datos_juego['genero']}\n"
        f"🏢 Desarrolador: {datos_juego['desarrollador']}\n"
        f"📅 Año de lanzamiento: {datos_juego['año']}\n"
    )
    return datagame

def generar_community_post(
        juego,
        nivel
):
    post = (
        f"🔥 Nuevo video disponible\n\n"
        f"🎮 {juego}\n"
        f"📍 {nivel}\n\n"
        f"¿Recuerdas este clasico?\n\n"
        f"👇 Déjame tu opinión de los comentarios"
    )
    return post 

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

datos_juego = game_database.get(juego)

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

    encabezado = generar_encabezado()

    print("\n🎬 TITULO:")
    print(titulo)
    print("\n📝 DESCRIPCIÓN:")
    print(descripcion)
    print("\n🏷️ HASHTAGS:")
    print(hashtags)
    print("\n📌 COMENTARIO:")
    print(comentario)
    print("\n📚 DATAGAME:")
    print(datagame)
    print("\n📢 COMMUNITY POST:")
    print(community_post)

    nombre_archivo = (
        juego_encontrado.replace(" ", "_")
    )

    os.makedirs(
       "output",
       exist_ok=True
    )

    with open(
        f"output/{nombre_archivo}.txt",
        "w",
        encoding="utf-8"
    ) as archivo: 
        
        archivo.write(
            f"{encabezado}\n\n"
        )

        archivo.write(
            f"TITULO:\n{titulo}\n\n"
        )

        archivo.write(
            f"DESCRIPCIÓN:\n{descripcion}\n\n"
        )

        archivo.write(
            f"HASHTAGS:\n{hashtags}\n\n"
        )

        archivo.write(
            f"COMENTARIO:\n{comentario}\n\n"
        )
 
        archivo.write(
            f"DATAGAME:\n{datagame}\n\n"
        )

        archivo.write(
            f"COMMUNITY POST:\n"
            f"{community_post}\n\n"
        )
else:   
    print(
        "\n❌ Juego no encontrado."
    )
        
