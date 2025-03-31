def construir_prompt(data, alertas):
    prompt = f"""Eres un asesor inteligente en ahorro de agua para el hogar.

El hogar tiene {data['habitantes']} personas.

El consumo mensual por zona es:
"""
    for zona, litros in data["consumo"].items():
        prompt += f"- {zona.capitalize()}: {litros} litros\n"

    if alertas:
        prompt += "\nSe detectaron las siguientes alertas:\n"
        for mensaje in alertas.values():
            prompt += f"- {mensaje}\n"

    prompt += "\nCon base en esta información, proporciona recomendaciones prácticas para reducir el consumo de agua en este hogar."

    return prompt
