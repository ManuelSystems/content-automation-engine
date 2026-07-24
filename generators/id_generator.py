def generar_id(tipo):
    if tipo.lower() == "walkthrough":
        return "ID: WT-001"
    elif tipo.lower() == "shortplay":
        return "ID: SP-001"
    else: 
        return "ID: CT-001"
