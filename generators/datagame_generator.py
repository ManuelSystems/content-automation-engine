def generar_datagame(
        juego,
        datos_juego
):
    datagame = (
        #f"📚 DATAGAME\n\n"
        f"🎮 {juego}\n\n"
        f"🕹️ Plataforma: {datos_juego['plataforma']}\n"
        f"🎭 Género: {datos_juego['genero']}\n"
        f"🏢 Desarrolador: {datos_juego['desarrollador']}\n"
        f"📅 Año de lanzamiento: {datos_juego['año']}\n"
    )
    return datagame