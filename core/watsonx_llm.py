import os
import requests
from typing import List, Optional
from dotenv import load_dotenv
from pydantic import Field
from langchain_core.language_models.llms import LLM

# Cargar variables desde .env
load_dotenv()

class WatsonxLLM(LLM):
    model_id: str = Field(default=os.getenv("MODEL_ID"))
    base_url: str = Field(default=os.getenv("BASE_URL"))
    project_id: str = Field(default=os.getenv("PROJECT_ID"))
    api_key: str = Field(default=os.getenv("IBM_API_KEY"))
    version: str = Field(default="2024-03-29")
    token: Optional[str] = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        object.__setattr__(self, 'token', self.get_iam_token())

    def get_iam_token(self):
        """ Obtiene el token de autenticación IAM de IBM Cloud. """
        url = "https://iam.cloud.ibm.com/identity/token"
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        data = f"grant_type=urn:ibm:params:oauth:grant-type:apikey&apikey={self.api_key}"
        
        response = requests.post(url, headers=headers, data=data)
        if response.status_code != 200:
            raise Exception(f"Error al obtener el token IAM: {response.status_code} - {response.text}")
        
        return response.json()["access_token"]

    def _call(self, prompt: str, stop: Optional[List[str]] = None) -> str:
        """ Envía una consulta al modelo Watsonx con la identidad de Deep Water. """
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.token}"
        }

        # 🎯 Identidad del asistente Deep Water (Estricta para evitar respuestas fuera de tema)
        deep_water_prompt = """You are Deep Water, an expert assistant in efficient water usage. 
Your goal is to help people reduce their water consumption and adopt sustainable practices based on household data.

⚠️ If the user asks about a topic that is NOT related to water conservation, ONLY respond:
'I am Deep Water, an assistant specialized in water conservation. Let’s focus on saving water! 💧'
Do NOT provide any additional information or explanations.

Respond clearly, in a friendly and educational manner. 
Always provide personalized recommendations and useful data. 
If you detect an issue with water consumption, suggest practical solutions.

Structure your responses into simple steps and, if necessary, provide concrete examples. 
Avoid vague answers and focus on delivering actionable and practical information. 
Use a motivating and positive tone to encourage sustainable habit changes.
"""

        full_prompt = deep_water_prompt + "\n\n" + prompt  

        payload = {
            "model_id": self.model_id,
            "input": full_prompt,
            "project_id": self.project_id,
            "parameters": {
                "decoding_method": "greedy",
                "max_new_tokens": 500,
                "stop_sequences": stop or []
            }
        }

        url = f"{self.base_url}/ml/v1/text/generation?version={self.version}"
        response = requests.post(url, headers=headers, json=payload)

        if response.status_code != 200:
            raise Exception(f"Error en generación: {response.status_code} - {response.text}")

        # 🔹 Asegurar que solo devuelva la primera línea si se trata de una evasión de pregunta
        result = response.json()["results"][0]["generated_text"].strip()
        if "I am Deep Water" in result:
            return "I am Deep Water, an assistant specialized in water conservation. Let’s focus on saving water! 💧"

        return result

    @property
    def _llm_type(self) -> str:
        return "watsonx"
