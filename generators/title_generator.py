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