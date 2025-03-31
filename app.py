from core.watsonx_llm import WatsonxLLM

llm = WatsonxLLM()
prompt = "Dame un consejo para ahorrar agua al lavar los platos."
respuesta = llm.invoke(prompt)

print("\n🤖 Watsonx responde:\n", respuesta)
