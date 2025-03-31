def analizar_consumo(data):
    umbrales = {
        "ducha": 1400,
        "cocina": 1000,
        "lavandería": 800,
        "jardín": 300
    }

    alertas = {}
    for zona, valor in data["consumo"].items():
        if valor > umbrales[zona]:
            alertas[zona] = f"Alerta: consumo alto en {zona} ({valor} L)"

    return alertas
