def generar_contenido_completo(
        titulo,
        descripcion,
        hashtags,
        comentario,
        datagame,
        community_post
):
    contenido = (
        f"🎬 TITULO:\n"
        f"{titulo}\n\n"

        f"📝 DESCRIPCION:\n"
        f"{descripcion}\n\n"

        f"🏷️ HASHTAGS:\n"
        f"{hashtags}\n\n"

        f"📌 COMENTARIO:\n"
        f"{comentario}\n\n"

        f"📚 DATAGAME:\n"
        f"{datagame}\n\n"

        f"📢 COMMUNITY POST:\n"
        f"{community_post}\n"
    )

    return contenido