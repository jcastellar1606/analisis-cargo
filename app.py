import streamlit as st
from groq import Groq

# Configuración de la página
st.set_page_config(page_title="Análisis de Cargos Inteligente", layout="centered")

# --- UI ---
st.title("🏢 Análisis de Cargos Inteligente")
st.markdown("Asistente experto de diseño organizacional.")

with st.sidebar:
    st.header("Configuración")
    cargo = st.text_input("Nombre del cargo", placeholder="Ej: Analista de Riesgos")
    area = st.selectbox("Área", ["Seguros", "Tecnología", "Finanzas", "Talento Humano"])
    btn_generar = st.button("Generar Análisis")

# --- Lógica de IA ---
if btn_generar and cargo:
    api_key = st.secrets.get("GROQ_API_KEY")
    
    if not api_key:
        st.error("❌ Error: No se encontró la API Key en los 'Secrets' de Streamlit.")
    else:
        client = Groq(api_key=api_key)
        
        with st.spinner('Construyendo perfil estratégico...'):
            try:
              # Instrucción para que use formato estético (Negritas y Encabezados)
                prompt = f"""Actúa como experto en diseño organizacional. Analiza el cargo '{cargo}' en el área de '{area}'.
                
                REGLAS DE FORMATO (Obligatorio para que se vea profesional):
                1. Usa un H2 (#) para el título del cargo.
                2. Usa H3 (###) para cada sección (Misión, Funciones, Hard Skills, Soft Skills).
                3. Para la Misión, usa una línea de texto normal debajo del título.
                4. Para las Funciones y Skills, usa una lista numerada (1.) o viñetas simples (-) pero asegúrate de que cada título de sección sea una línea separada.
                5. NO incluyas introducciones ni rellenos. Ve directo al grano."""
                
                response = client.chat.completions.create(
                    messages=[{"role": "user", "content": prompt}],
                    model="llama-3.3-70b-versatile",
                )
                
                # Resultado limpio
                st.success("¡Perfil generado con éxito!")
                st.markdown("---")
                st.markdown(response.choices[0].message.content)
                
            except Exception as e:
                st.error(f"🚨 Error al conectar con la IA: {e}")

st.divider()
st.caption("Gestión de Talento Humano")
