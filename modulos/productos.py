import streamlit as st
from config.conexion import obtener_conexion

def mostrar_productos():
    st.header("📦 Registrar Nuevo Producto")
    
    with st.form("form_producto"):
        nombre = st.text_input("Nombre del artículo")
        precio = st.number_input("Precio unitario ($)", min_value=0.01, step=0.01)
        guardar = st.form_submit_button("Guardar en Inventario")
        
        if guardar:
            if nombre.strip() == "":
                st.warning("Debe ingresar el nombre del producto.")
            else:
                conexion = obtener_conexion()
                if conexion is not None:
                    try:
                        cursor = conexion.cursor()
                        consulta = "INSERT INTO PRODUCTOS (Nombre, Precio) VALUES (%s, %s)"
                        cursor.execute(consulta, (nombre, float(precio)))
                        conexion.commit()
                        st.success("¡Producto registrado exitosamente!")
                    except Exception as error:
                        conexion.rollback()
                        st.error(f"Error al guardar: {error}")
                    finally:
                        cursor.close()
                        conexion.close()
