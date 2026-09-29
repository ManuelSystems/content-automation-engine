from pathlib import path

def analizar_reparacion(resultado):

    if resultado["tipo"] == "shortplay":

        ruta_actual = resultado["ruta"]

        carpeta_correcta = (
            ruta_actual.parent.parent / "shortplays"
        )

        print("\n🔧 Reparando sistema...")
        print("=" * 40)

        print("Archivo:", resultado["archivo"])
        print("Ubicacion actual:", ruta_actual)
        print("Ubicacion correcta:", carpeta_correcta)

        return {
            "archivo": resultado["archivo"],
            "ruta_actual": ruta_actual,
            "ruta_correcta": carpeta_correcta
        }