import streamlit as st
from summa import summarizer

st.set_page_config(page_title="Resumidor de Textos PLN", page_icon="📝")

st.title("📝 Resumidor de Textos con PLN")
st.write("Aplicación interactiva que aplica algoritmos de resumen extractivo (**TextRank**) sobre textos en español.")

texto_ejemplo = (
    "El procesamiento del lenguaje natural (PLN) es un campo interdisciplinar de las ciencias de la "
    "computación, la inteligencia artificial y la lingüística que se ocupa de la interacción entre las "
    "computadoras y el lenguaje humano. En particular, se enfoca en cómo programar computadoras para "
    "procesar y analizar grandes cantidades de datos de lenguaje natural. Los resultados suelen ser útiles "
    "en tareas como la traducción automática, el análisis de sentimientos, el reconocimiento de entidades y "
    "la generación automática de resúmenes de texto."
)

texto_usuario = st.text_area(
    "Pega aquí el texto que deseas resumir:",
    value=texto_ejemplo,
    height=200
)

ratio = st.slider(
    "Ratio de resumen (porcentaje del texto original)",
    min_value=0.1,
    max_value=0.8,
    value=0.3,
    step=0.05
)

if st.button("Generar Resumen"):
    if not texto_usuario.strip():
        st.warning("Por favor, introduce un texto.")
    elif len(texto_usuario.split()) < 15:
        st.warning("El texto es muy corto para extraer un resumen significativo.")
    else:
        with st.spinner("Procesando resumen..."):
            resumen = summarizer.summarize(texto_usuario, ratio=ratio, language='spanish')
            if resumen:
                st.subheader("Resultado:")
                st.success(resumen)
            else:
                st.info("No se ha podido generar un resumen con este ratio. Prueba a aumentarlo.")
