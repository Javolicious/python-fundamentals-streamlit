
import streamlit as st

st.title("Proyecto Python Fundamentals")
st.image(
"dmc.jpg",
width=150
)
st.subheader("Javier Artieda Burgos")
st.write("Especialización Python for Analytics")

st.set_page_config(
    page_title="Proyecto Python Fundamentals",
    page_icon="🐍",
    layout="wide"
)

menu = st.sidebar.selectbox(
    "Menú",
    (
        "🏠 Home",
        "📊 Ejercicio 1",
        "📦 Ejercicio 2",
        "⚙️ Ejercicio 3",
        "🗂️ Ejercicio 4"
    )
)

if menu == "🏠 Home":
    st.title("Proyecto Aplicado en Streamlit")
    st.write("Javier Artieda Burgos")

elif menu == "📊 Ejercicio 1":
    st.header("Flujo de Caja")

elif menu == "📦 Ejercicio 2":
    st.header("Registro con NumPy")

elif menu == "⚙️ Ejercicio 3":
    st.header("Funciones Externas")

elif menu == "🗂️ Ejercicio 4":
    st.header("CRUD con Clases")
`
