import os

def guardar_contenido(
        nombre_archivo,
        encabezado,
        contenido
): 
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
            f"{encabezado}\n"
        )

        archivo.write(
            f"{contenido}\n"
        )