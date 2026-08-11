import os 

def guardar_contenido(
        juego, 
        tipo, 
        contenido_id,
        encabezado,
        contenido
):
    carpeta_juego = juego.replace(" ","_")
    carpeta_tipo = tipo.strip().lower()

    ruta = os.path.join(
        "output",
        carpeta_juego,
        carpeta_tipo
    )

    os.makedirs(
        ruta, 
        exist_ok=True
    )

    nombre_id = contenido_id.replace(
        "ID: ",
        ""
    )

    ruta_archivo = os.path.join(
        ruta,
        f"{nombre_id}.txt"
    )

    with open(
        ruta_archivo,
        "w",
        encoding="utf-8"
    ) as archivo:

        archivo.write(
            f"{encabezado}\n"
        )

        archivo.write(
            f"{contenido}\n"
        )

