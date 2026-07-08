import streamlit as st

st.set_page_config(page_title="JobArchitect SURA", layout="wide")

st.title("🏢 JobArchitect: Análisis de Cargos - SURA")
st.subheader("Herramienta automatizada para la gestión de talento")

# Formulario de entrada
with st.sidebar:
    st.header("⚙️ Configurar nuevo cargo")
    cargo = st.text_input("Nombre del cargo")
    vicepresidencia = st.selectbox("Vicepresidencia", ["Seguros", "Innovación", "Financiero", "Talento Humano"])
    objetivo = st.selectbox("Objetivo Estratégico", ["Transformación Digital", "Eficiencia Operativa", "Expansión de Mercado"])
    generar = st.button("Generar Perfil Técnico")

# Lógica de simulación
if generar:
    st.success(f"Perfil generado para: {cargo}")
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("### 🎯 Misión del Cargo")
        st.info(f"Gestionar la estrategia de {objetivo} desde la vicepresidencia de {vicepresidencia}...")
        
        st.write("### 📋 Funciones Principales")
        st.write("- Análisis de datos y KPIs de desempeño.")
        st.write("- Liderazgo en proyectos de mejora continua.")
        st.write("- Alineación estratégica con los objetivos corporativos.")

    with col2:
        st.write("### 🛠️ Perfil Requerido (Hard Skills)")
        st.write("- Conocimientos avanzados en Excel y SQL.")
        st.write("- Experiencia previa en el sector asegurador.")
        st.write("- Certificación en metodologías ágiles.")
        
        st.write("### 🧠 Competencias Blandas (Soft Skills)")
        st.write("- Pensamiento analítico.")
        st.write("- Comunicación asertiva.")
        st.write("- Orientación a resultados.")

st.divider()
st.caption("Herramienta desarrollada para el equipo de Talento Humano - SURA | Competencia Etapa 1")
