from pathlib import Path

def analizar_output():

    ruta_output = Path("output")

    if not ruta_output.exists():
        print("❌ La carpeta output no existe.")
        return

    juegos = []
    archivos = []
    carpetas = []

    for elemento in ruta_output.rglob("*"):

        if elemento.is_dir():
            carpetas.append(elemento)

        elif elemento.is_file():
            archivos.append(elemento)

    for carpeta in ruta_output.iterdir():

        if carpeta.is_dir():
            juegos.append(carpeta)

    print("\n 📂 OUTPUT ANAILZER")
    print("=" * 40)

    print(
        f"🎮 Juegos encontrados: {len(juegos)}"
    )
    print(
        f"📂 Carpetas encontradas: {len(carpetas)}"
    )
    print(
        f"📄 Archivos encontrados: {len(archivos)}"
    )

    print("\n 🎮 JUEGOS: ")

    for juego in juegos: 

        print(
            f"\n📦 {juego.name}"
        )

    print("\n 📄 ARCHIVOS: ")

    for archivo in archivos:

        print(
            f"   └── {archivo}"
        )