from engine.engine_loader import cargar_estado_motor
from engine.engine_manager import guardar_estado_motor

def generar_id(tipo):

    estado_motor =  cargar_estado_motor()

    if tipo.lower() == "walkthrough":

        estado_motor["last_walkthrough"] += 1

        guardar_estado_motor(estado_motor)

        print(estado_motor)

        return f"ID: WT-{estado_motor['last_walkthrough']:03d}"

    elif tipo.lower() == "shortplay":

        estado_motor["last_shortplay"] += 1

        guardar_estado_motor(estado_motor)

        print(estado_motor)

        return f"ID: SP-{estado_motor['last_shortplay']:03d}"

    else: 
        return "ID: CT-001"