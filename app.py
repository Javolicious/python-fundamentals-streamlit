
import streamlit as st
import pandas as pd
import numpy as np

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
    ejercicio_1()


elif menu == "📦 Ejercicio 2":
    st.header("Registro con NumPy")
    ejercicio_2()


elif menu == "⚙️ Ejercicio 3":
    st.header("Funciones Externas")

elif menu == "🗂️ Ejercicio 4":
    st.header("CRUD con Clases")

#----------------------------------------------------------------------------------------------------------------------------------------------------

#EJERCICIO 1

def ejercicio_1():

# Crear la lista
    if "movimientos" not in st.session_state:
    st.session_state.movimientos = []

# Valores de entrada
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

pass
#-------------------------------------------------------------------------------------------------------------------
#EJERCICIO 2
def ejercicio_2():

    st.title("Ejercicio 2 - Registro con NumPy y DataFrame")

    st.markdown("""
    Registre productos utilizando widgets de Streamlit.
    Los registros son almacenados en arrays de NumPy y mostrados
    posteriormente en un DataFrame.
    """)

    # Crear lista en memoria
    if "productos" not in st.session_state:
        st.session_state.productos = []

    # Formulario
    nombre = st.text_input("Nombre del producto")

    categoria = st.selectbox(
        "Categoría",
        ["Electrónica", "Accesorios", "Hogar", "Tecnología"]
    )

    precio = st.number_input(
        "Precio",
        min_value=0.0,
        step=1.0
    )

    cantidad = st.number_input(
        "Cantidad",
        min_value=1,
        step=1
    )

    # Botón agregar
    if st.button("Agregar Producto"):

        total = precio * cantidad

        nuevo_producto = [
            nombre,
            categoria,
            precio,
            cantidad,
            total
        ]

        st.session_state.productos.append(nuevo_producto)

        st.success("Producto agregado correctamente")

    # Mostrar tabla
    if len(st.session_state.productos) > 0:

        productos_array = np.array(
            st.session_state.productos,
            dtype=object
        )

        df = pd.DataFrame(
            productos_array,
            columns=[
                "Producto",
                "Categoría",
                "Precio",
                "Cantidad",
                "Total"
            ]
        )

        st.subheader("Productos Registrados")

        st.dataframe(
            df,
            use_container_width=True
        )

        st.metric(
            "Venta Total",
            f"S/ {df['Total'].astype(float).sum():,.2f}"
        )

pass
