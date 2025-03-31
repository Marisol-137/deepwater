from core.data_input import get_consumo_simulado
from core.analyzer import analizar_consumo
from core.prompt_builder import construir_prompt
from core.watsonx_llm import WatsonxLLM

# Paso 1: obtener datos simulados
datos = get_consumo_simulado()

# Paso 2: análisis básico
alertas = analizar_consumo(datos)

# Paso 3: construir el prompt
prompt = construir_prompt(datos, alertas)

# Paso 4: enviar a Watsonx
llm = WatsonxLLM()
respuesta = llm.invoke(prompt)

# Paso 5: mostrar resultado
print("\n🤖 DeepWater responde:\n")
print(respuesta)
