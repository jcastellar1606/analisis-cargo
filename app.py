import streamlit as st
import os
from groq import Groq

# Aseguramos que la clave se lea desde los secrets
api_key = st.secrets.get("GROQ_API_KEY")

if not api_key:
    st.error("No se encontró la API Key en los secretos. Por favor, configúrala en Streamlit.")
else:
    client = Groq(api_key=api_key)

    if generar and cargo:
        with st.spinner('Generando perfil con IA...'):
            try:
                prompt = f"Crea un análisis de cargo profesional para '{cargo}' en el área de '{area}'. Incluye Misión, 3 Funciones, 3 Hard Skills y 3 Soft Skills."
                
                chat_completion = client.chat.completions.create(
                    messages=[{"role": "user", "content": prompt}],
                    model="llama3-8b-8192",
                )
                st.markdown(chat_completion.choices[0].message.content)
            except Exception as e:
                st.error(f"Ocurrió un error: {e}")
