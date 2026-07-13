def buscar_juego(
        juego, 
        game_database,
):
    
    datos_juego = None
    juego_encontrado = None 

    for nombre_juego in game_database:

        if juego.lower() in nombre_juego.lower():
            juego_encontrado = nombre_juego
            datos_juego = game_database[nombre_juego]
            break

    return (juego_encontrado, datos_juego)