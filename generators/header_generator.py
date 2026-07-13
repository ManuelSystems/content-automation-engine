def generar_encabezado(
    juego,
    tipo,
    plataforma
):

    encabezado = (
        "========================================\n"
        "GAMECONTENTENGINE\n"
        "GENERADOR DE CONTENIDO GAMING\n"
        "========================================\n\n"

        f"🎮 Proyecto: FullRetroGaming\n"
        f"🎮 Juego: {juego}\n"
        f"🚀 Tipo: {tipo}\n"
        f"🕹️ Plataforma: {plataforma}\n"

        "========================================"
    )

    return encabezado