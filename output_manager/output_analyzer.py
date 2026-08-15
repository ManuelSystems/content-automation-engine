from pathlib import Path

#importacion de librerias 
#====================================================================

def analizar_archivo(ruta_archivo):

    nombre_archivo = ruta_archivo.name

    errores = [] 
    advertencias = []

    print("\n📃 ANALIZANDO ARCHIVO")
    print("=" * 40)

    print("Nombre:", nombre_archivo)
    print("Ruta:", ruta_archivo)

    tipo = "desconocido"
    
    if "SP-" in nombre_archivo:
        tipo = "shortplay"

    elif "WT-" in nombre_archivo:
        tipo = "walkthrough"

    print("Tipo:", tipo)

    if tipo == "desconocido": 
        errores.append(
            "Tipo de contenido desconocido"
        )

    nombre_limpio = nombre_archivo.replace(
        "ID: ",
        ""
    )

    nombre_limpio = nombre_limpio.replace(
        ".txt",
        ""
    )

    print("ID: ", nombre_limpio)

    partes = ruta_archivo.parts

    if len(partes) < 4: 
        errores.append(
            "Archivo ubicado directamente en output"
        )

    print("Partes:", partes)

    if len(partes) >= 4:
        juego = partes[1]
    else: 
        juego = "desconocido"

    print("Juego: ", juego)

    if errores:
        print("\n🚨 ERRORES ENCONTRADOS:")
        for error in errores: 
            print(f"  ❌ {error}")

    if advertencias:
        print("\n⚠️ADVERTENCIAS ENCONTRADAS:")
        for advertiencia in advertencias: 
            print(f"   ⚠️ {advertiencia}")

    if not errores and not advertencias: 
        print("\n ✅")

    return{
        "archivo": nombre_archivo,
        "ruta": ruta_archivo,
        "tipo": tipo,
        "id": nombre_limpio,
        "juego": juego,
        "errores": errores, 
        "advertencias": advertencias
    }
#====================================================================

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

    resultados = []

    for archivo in archivos:

        print(
            f"   └── {archivo}"
        )

        resultado = analizar_archivo(archivo)

        resultados.append(resultado)

        print("\n=====================================")
        print("📊 RESUMEN DE ANALISIS")
        print("=====================================")
        
        print(
            f"📄 Archivos Analizados: {len(resultados)}"
        )        