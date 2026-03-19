data = []

def guardar_temperatura(valor: float):
    data.append(valor)
    return {
        "mensaje": "Dato guardado correctamente",
        "valor": valor
    }

def obtener_datos(min_temp: float = None, max_temp: float = None):
    resultado = data

    if min_temp is not None:
        resultado = [x for x in resultado if x >= min_temp]

    if max_temp is not None:
        resultado = [x for x in resultado if x <= max_temp]

    return {
        "total": len(resultado),
        "datos": resultado
    }
