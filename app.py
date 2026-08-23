
import streamlit as st
import pandas as pd

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

# Crear la lista una sola vez
if "movimientos" not in st.session_state:
    st.session_state.movimientos = []

# Entradas
concepto = st.text_input("Concepto")

tipo = st.selectbox(
    "Tipo de movimiento",
    ["Ingreso", "Gasto"]
)

valor = st.number_input(
    "Valor",
    min_value=0.0,
    step=10.0
)

# Botón agregar
if st.button("Agregar movimiento"):

    if concepto != "" and valor > 0:

        movimiento = {
            "Concepto": concepto,
            "Tipo": tipo,
            "Valor": valor
        }

        st.session_state.movimientos.append(movimiento)

        st.success("Movimiento agregado correctamente")

    else:
        st.error("Complete todos los campos")

# Mostrar movimientos
if len(st.session_state.movimientos) > 0:

    df = pd.DataFrame(st.session_state.movimientos)

    st.subheader("Movimientos registrados")
    st.dataframe(df)

    total_ingresos = df[df["Tipo"] == "Ingreso"]["Valor"].sum()
    total_gastos = df[df["Tipo"] == "Gasto"]["Valor"].sum()
    saldo = total_ingresos - total_gastos

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total Ingresos", f"S/ {total_ingresos:,.2f}")

    with col2:
        st.metric("Total Gastos", f"S/ {total_gastos:,.2f}")

    with col3:
        st.metric("Saldo Final", f"S/ {saldo:,.2f}")

    if saldo > 0:
        st.success("✅ Flujo de caja a favor")

    elif saldo < 0:
        st.error("❌ Flujo de caja en contra")

    else:
        st.warning("⚠️ Saldo igual a cero")






elif menu == "📦 Ejercicio 2":
    st.header("Registro con NumPy")

elif menu == "⚙️ Ejercicio 3":
    st.header("Funciones Externas")

elif menu == "🗂️ Ejercicio 4":
    st.header("CRUD con Clases")

#EJERCICIO 1




