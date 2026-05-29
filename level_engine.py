def validar_nivel(nivel, datos_juego):

    niveles = datos_juego["niveles"]

    if nivel in niveles:
        return True

    print("\n❌ Nivel no encontrado.")

    print("\n📚 Niveles disponibles:")

    for nivel_db in niveles:
        print(f"- {nivel_db}")

    return False