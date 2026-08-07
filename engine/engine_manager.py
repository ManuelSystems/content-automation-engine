import json 
from pathlib import Path

def guardar_estado_motor(estado_motor):
    """
    Guarda el estado actual del motor en engine_state.json
    """
    ruta_estado = Path(__file__).parent / "engine_state.json"

    with open(
        ruta_estado,
        "w",
        encoding="utf-8"
    ) as archivo: 

        json.dump(
            estado_motor,
            archivo,
            indent=4,
            ensure_ascii=False 
        )