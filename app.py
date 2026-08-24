import streamlit as st
from summa import summarizer

# 1. Configuración de la página
st.set_page_config(
    page_title="Resumiendo - Síntesis de textos en castellano", 
    page_icon="✂️",
    layout="centered"
)

# 2. Encabezado y explicación (inspirado en la aplicación original)
st.title("Resumiendo")
st.markdown("### ✂️")
st.write(
    "Una aplicación web para realizar resúmenes de textos en castellano. "
    "Por defecto, los resúmenes tendrán aproximadamente un **20%** de la longitud del original. "
    "Para que la aplicación funcione correctamente, se recomienda que los textos tengan una longitud **superior a 100 palabras**."
)

st.write("---")

# 3. Formulario de entrada con texto de ayuda (placeholder) en blanco
texto_usuario = st.text_area(
    label="Pega el texto aquí:",
    value="",  # Se deja vacío para que no cargue texto por defecto
    placeholder="Introduce o pega aquí el texto en castellano que deseas resumir (mínimo recomendado: 100 palabras)...",
    height=220
)

# 4. Ajuste del ratio (con el 20% por defecto)
ratio_seleccionado = st.slider(
    label="Ratio de compresión",
    min_value=0.1,
    max_value=0.5,
    value=0.2,  # 20% por defecto tal como indica la aplicación
    step=0.05,
    help="El valor 0.2 equivale a generar un resumen con un 20% de la extensión del texto original."
)

# Contador orientativo de palabras
num_palabras = len(texto_usuario.strip().split()) if texto_usuario.strip() else 0
if num_palabras > 0:
    st.caption(f"Palabras detectadas: **{num_palabras}**")

# 5. Botón de acción
if st.button("Enviar"):
    if not texto_usuario.strip():
        st.warning("⚠️ Por favor, pega algún texto antes de pulsar en Enviar.")
    elif num_palabras < 30:
        st.warning("⚠️ El texto es demasiado corto para extraer oraciones representativas. Introduce un texto más extenso (preferiblemente más de 100 palabras).")
    else:
        with st.spinner("Generando resumen..."):
            # Llamada a Summa / TextRank
            resumen_generado = summarizer.summarize(
                texto_usuario, 
                ratio=ratio_seleccionado, 
                language='spanish'
            )
            
            if resumen_generado:
                st.write("### Resumen:")
                st.info(resumen_generado)
            else:
                st.error("No se ha podido extraer un resumen con este texto y ratio. Prueba a aumentar el ratio de compresión o a introducir un texto con más párrafos.")
