import sys
import os

# Asegurar que Python encuentra el módulo core
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from core.watsonx_llm import WatsonxLLM
from core.data_input import get_consumo_simulado  # Función para obtener datos simulados

# Configuración de la app
st.set_page_config(page_title="DeepWater", layout="wide")

st.title("💧 DeepWater - Optimiza tu consumo de agua")

# Inicializar Watsonx
llm = WatsonxLLM()

# Inicializar estado de datos si aún no existe
if "datos_consumo" not in st.session_state:
    st.session_state["datos_consumo"] = None

if "analisis_consumo" not in st.session_state:
    st.session_state["analisis_consumo"] = None

# Botón para analizar consumo de agua
if st.button("🚰 Analiza mi consumo de agua"):
    with st.spinner("Analizando tu consumo..."):
        datos_consumo = get_consumo_simulado()  # Obtener datos simulados
        st.session_state["datos_consumo"] = datos_consumo  # Guardar datos en sesión

        prompt_analisis = f"""
        Datos del hogar: {datos_consumo}

        Asistente:
        Analiza estos datos y proporciona un diagnóstico con recomendaciones prácticas para ahorrar agua.
        Responde en un máximo de 3 frases o en una lista de puntos.
        """
        respuesta_analisis = llm.invoke(prompt_analisis)
        st.session_state["analisis_consumo"] = respuesta_analisis  # Guardar análisis

    st.subheader("🔍 Análisis del consumo de agua")
    st.markdown(respuesta_analisis)

# Mostrar análisis si ya fue realizado
if st.session_state["analisis_consumo"]:
    st.subheader("🔍 Análisis del consumo de agua")
    st.markdown(st.session_state["analisis_consumo"])

# Sección de Chat
st.subheader("💬 Consulta sobre ahorro de agua")

# Inicializar historial de chat
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Mostrar historial de chat
for msg in st.session_state["messages"]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Entrada del usuario
user_input = st.chat_input("Haz tu pregunta sobre ahorro de agua...")

if user_input:
    # Mostrar mensaje del usuario en el chat
    st.session_state["messages"].append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Determinar si el usuario pregunta sobre su consumo
    if "consumo" in user_input.lower() and st.session_state["datos_consumo"]:
        prompt_chat = f"""
        Datos del hogar: {st.session_state["datos_consumo"]}
        Análisis previo: {st.session_state["analisis_consumo"]}

        Usuario: {user_input}
        Asistente (responde en máximo 3 frases o en una lista de puntos, usando los datos proporcionados):"""
    else:
        prompt_chat = f"""
        Usuario: {user_input}
        Asistente (responde en máximo 3 frases o en una lista de puntos):"""

    # Generar respuesta con Watsonx
    with st.spinner("DeepWater está pensando..."):
        response = llm.invoke(prompt_chat)

    # Mostrar respuesta en el chat
    st.session_state["messages"].append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)
