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
