import json
from pathlib  import Path 

def cargar_estado_motor():
    """
    Carga el estado del motor desde engine_state.json 
    y devuelve un diccionario con toda la informacion del motor.
    """

    ruta_estado = Path(__file__).parent / "engine_state.json"

    with open(ruta_estado, "r", encoding="utf-8") as archivo:
        estado_motor = json.load(archivo)
        return estado_motor
    
