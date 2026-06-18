import json

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
print(tipo)

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

    print("\n🎬 TITULO:")
    print(titulo)
    print("\n📝 DESCRIPCIÓN:")
    print(descripcion)

else:   
    print(
        "\n❌ Juego no encontrado."
    )
        
