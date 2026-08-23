
import streamlit as st
import pandas as pd
import numpy as np

from libreria_funciones_proyecto1 import calcular_disponibilidad_sistema
from libreria_clases_proyecto1 import InventarioProducto

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
            st.metric(
                "Total Ingresos",
                f"S/ {total_ingresos:,.2f}"
            )

        with col2:
            st.metric(
                "Total Gastos",
                f"S/ {total_gastos:,.2f}"
            )

        with col3:
            st.metric(
                "Saldo Final",
                f"S/ {saldo:,.2f}"
            )

        if saldo > 0:
            st.success("✅ Flujo de caja a favor")

        elif saldo < 0:
            st.error("❌ Flujo de caja en contra")

        else:
            st.warning("⚠️ Saldo igual a cero")
#-------------------------------------------------------------------------------------------------------------------
#EJERCICIO 2
def ejercicio_2():

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


#-------------------------------------------------------------------------------------------------------------------

#EJERCICIO 3

def ejercicio_3():

    st.markdown("""
    En este ejercicio se utiliza una función externa para calcular
    la disponibilidad de un sistema informático.

    La disponibilidad representa el porcentaje de tiempo durante
    el cual el sistema se mantuvo operativo.
    """)

    # Crear el histórico en la sesión
    if "historico_disponibilidad" not in st.session_state:
        st.session_state.historico_disponibilidad = []

    # Selector de función
    funcion_seleccionada = st.selectbox(
        "Seleccione una función",
        ["Calcular disponibilidad del sistema"]
    )

    # Parámetros de entrada
    tiempo_total = st.number_input(
        "Tiempo total del periodo en horas",
        min_value=0.01,
        value=0.1,
        step=1.0,
        key="tiempo_total_ejercicio_3"
    )

    tiempo_caida = st.number_input(
        "Tiempo de caída en horas",
        min_value=0.1,
        value=0.1,
        step=0.5,
        key="tiempo_caida_ejercicio_3"
    )

    # Ejecutar la función externa
    if st.button(
        "Ejecutar función",
        key="boton_ejercicio_3"
    ):

        if tiempo_caida > tiempo_total:
            st.error(
                "El tiempo de caída no puede ser mayor "
                "que el tiempo total."
            )

        else:
            try:
                resultado = calcular_disponibilidad_sistema(
                    tiempo_total,
                    tiempo_caida
                )

                st.success("Función ejecutada correctamente")

                # Mostrar el resultado completo
                st.subheader("Resultado")
                st.json(resultado)

                # Preparar registro para el histórico
                registro = {
                    "Función": funcion_seleccionada,
                    "Tiempo total (horas)": tiempo_total,
                    "Tiempo de caída (horas)": tiempo_caida
                }

                # La función externa devuelve un diccionario
                if isinstance(resultado, dict):
                    registro.update(resultado)
                else:
                    registro["Resultado"] = resultado

                # Agregar al histórico
                st.session_state.historico_disponibilidad.append(
                    registro
                )

            except ValueError as error:
                st.error(f"Error de validación: {error}")

            except Exception as error:
                st.error(f"No se pudo ejecutar la función: {error}")

    # Mostrar histórico
    if len(st.session_state.historico_disponibilidad) > 0:

        st.subheader("Histórico de resultados")

        df_historico = pd.DataFrame(
            st.session_state.historico_disponibilidad
        )

        st.dataframe(
            df_historico,
            use_container_width=True,
            hide_index=True
        )

        # Botón para eliminar el histórico
        if st.button(
            "Limpiar histórico",
            key="limpiar_historico_ejercicio_3"
        ):
            st.session_state.historico_disponibilidad = []
            st.rerun()

    else:
        st.info(
            "Todavía no existen resultados en el histórico."
        )


#-------------------------------------------------------------------------------------------------------------------

#Ejercicio 4
    
def ejercicio_4():

    # Reiniciar datos antiguos del CRUD

    if "version_inventario" not in st.session_state:
        st.session_state.inventario = []
        st.session_state.version_inventario = 2

    st.markdown("""
    Gestión de inventario utilizando la clase
    InventarioProducto y operaciones CRUD.
    """)

    if "inventario" not in st.session_state:
        st.session_state.inventario = []

    tab1, tab2, tab3, tab4 = st.tabs(
        ["Crear", "Leer", "Actualizar", "Eliminar"]
    )


    # CREAR


    with tab1:

        st.subheader("Crear Producto")

        nombre = st.text_input(
            "Nombre",
            key="crear_nombre"
        )

        costo = st.number_input(
            "Costo Unitario",
            min_value=0.01,
            value=1.0,
            key="crear_costo"
        )

        precio = st.number_input(
            "Precio Unitario",
            min_value=0.01,
            value=1.0,
            key="crear_precio"
        )

        stock = st.number_input(
            "Stock Actual",
            min_value=0,
            value=0,
            key="crear_stock"
        )

        stock_minimo = st.number_input(
            "Stock Mínimo",
            min_value=0,
            value=0,
            key="crear_stock_minimo"
        )

        if st.button("Crear Producto"):

            try:

                producto = InventarioProducto(
                    nombre=nombre,
                    costo_unitario=costo,
                    precio_unitario=precio,
                    stock_actual=stock,
                    stock_minimo=stock_minimo
                )

                st.session_state.inventario.append(
                    producto
                )

                st.success(
                    "Producto creado correctamente"
                )

            except Exception as error:

                st.error(
                    f"Error: {error}"
                )


    # LEER


    with tab2:

        st.subheader(
            "Productos Registrados"
        )

        if len(st.session_state.inventario) > 0:

            datos = []

            for producto in st.session_state.inventario:

                datos.append(
                    producto.resumen()
                )

            df = pd.DataFrame(datos)

            st.dataframe(
                df,
                use_container_width=True
            )

            st.metric(
                "Total Productos",
                len(df)
            )

        else:

            st.info(
                "No existen productos registrados"
            )

    # ACTUALIZAR


    with tab3:

        st.subheader(
            "Actualizar Producto"
        )

        if len(st.session_state.inventario) > 0:

            nombres = [
                p.nombre
                for p
                in st.session_state.inventario
            ]

            nombre_seleccionado = st.selectbox(
                "Seleccione un producto",
                nombres,
                key="actualizar_producto"
            )

            producto = next(
                p
                for p
                in st.session_state.inventario
                if p.nombre
                == nombre_seleccionado
            )

            nuevo_nombre = st.text_input(
                "Nuevo Nombre",
                value=producto.nombre
            )

            nuevo_costo = st.number_input(
                "Nuevo Costo",
                min_value=0.01,
                value=float(
                    producto.costo_unitario
                )
            )

            nuevo_precio = st.number_input(
                "Nuevo Precio",
                min_value=0.01,
                value=float(
                    producto.precio_unitario
                )
            )

            nuevo_stock = st.number_input(
                "Nuevo Stock",
                min_value=0,
                value=int(
                    producto.stock_actual
                )
            )

            nuevo_stock_minimo = st.number_input(
                "Nuevo Stock Mínimo",
                min_value=0,
                value=int(
                    producto.stock_minimo
                )
            )

            if st.button(
                "Actualizar Producto"
            ):

                producto.nombre = nuevo_nombre
                producto.costo_unitario = nuevo_costo
                producto.precio_unitario = nuevo_precio
                producto.stock_actual = nuevo_stock
                producto.stock_minimo = nuevo_stock_minimo

                st.success(
                    "Producto actualizado"
                )

                st.rerun()

        else:

            st.info(
                "No existen productos para actualizar"
            )


    # ELIMINAR


    with tab4:

        st.subheader(
            "Eliminar Producto"
        )

        if len(st.session_state.inventario) > 0:

            nombres = [
                p.nombre
                for p
                in st.session_state.inventario
            ]

            nombre_eliminar = st.selectbox(
                "Seleccione un producto",
                nombres,
                key="eliminar_producto"
            )

            if st.button(
                "Eliminar Producto"
            ):

                st.session_state.inventario = [
                    p
                    for p
                    in st.session_state.inventario
                    if p.nombre
                    != nombre_eliminar
                ]

                st.success(
                    "Producto eliminado"
                )

                st.rerun()

        else:

            st.info(
                "No existen productos para eliminar"
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
    st.header("Funciones Externas - Calculo de Capacidades de baterías")
    ejercicio_3()

elif menu == "🗂️ Ejercicio 4":
    st.header("CRUD con Clases")
    ejercicio_4()


