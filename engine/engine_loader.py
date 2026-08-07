import json
from pathlib  import Path 

def cargar_estado_motor():
    """
    Lee el archivo engine_state.json
    y devuelve el del motor como diccionario.
    """

    ruta_estado = Path(__file__).parent / "engine_state.json"

    with open(ruta_estado, "r", encoding="utf-8") as archivo:
        estado_motor = json.load(archivo)

    return estado_motor
    
