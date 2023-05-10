# Importar la librería streamlit
import streamlit as st

# Título del sitio web
st.title("Bienvenido al gimnasio")

# Menú lateral con opciones
st.sidebar.header("¿Qué quieres hacer?")
opciones = ["Ver planes", "Reservar clase", "Contactar"]
seleccion = st.sidebar.selectbox("", opciones)

# Mostrar el contenido según la opción seleccionada
if seleccion == "Ver planes":
    # Mostrar los planes disponibles con sus precios y características
    st.header("Estos son los planes que ofrecemos:")
    st.subheader("Plan básico")
    st.write("- Acceso ilimitado al gimnasio")
    st.write("- Precio: 20€ al mes")
    st.subheader("Plan premium")
    st.write("- Acceso ilimitado al gimnasio y a las clases")
    st.write("- Precio: 40€ al mes")
    st.subheader("Plan personalizado")
    st.write("- Acceso ilimitado al gimnasio y a las clases")
    st.write("- Entrenador personal y plan de nutrición")
    st.write("- Precio: 60€ al mes")

elif seleccion == "Reservar clase":
    # Mostrar las clases disponibles con sus horarios y plazas
    st.header("Estas son las clases que puedes reservar:")
    clases = ["Yoga", "Pilates", "Spinning", "Zumba", "Boxeo"]
    horarios = ["10:00 - 11:00", "11:30 - 12:30", "13:00 - 14:00", "17:00 - 18:00", "18:30 - 19:30"]
    plazas = [10, 8, 12, 15, 6]
    # Crear un dataframe con los datos de las clases
    import pandas as pd
    df = pd.DataFrame({"Clase": clases, "Horario": horarios, "Plazas": plazas})
    # Mostrar el dataframe en una tabla
    st.table(df)
    # Pedir al usuario que elija una clase y un horario
    st.subheader("Elige una clase y un horario:")
    clase = st.selectbox("Clase:", clases)
    horario = st.selectbox("Horario:", horarios)
    # Comprobar si hay plazas disponibles para la clase y el horario elegidos
    indice = clases.index(clase)
    if plazas[indice] > 0:
        # Si hay plazas, confirmar la reserva y restar una plaza
        st.success(f"Has reservado la clase de {clase} a las {horario}. ¡Te esperamos!")
        plazas[indice] -= 1
        df["Plazas"] = plazas
        # Actualizar la tabla con las plazas restantes
        st.table(df)
    else:
        # Si no hay plazas, mostrar un mensaje de error
        st.error(f"Lo sentimos, no hay plazas disponibles para la clase de {clase} a las {horario}. Por favor, elige otra opción.")

else:
    # Mostrar los datos de contacto del gimnasio
    st.header("Si tienes alguna duda o sugerencia, puedes contactarnos por estos medios:")
    st.write("- Teléfono: 555-1234")
    st.write("- Email: gimnasio@gmail.com")
    st.write("- Dirección: Calle Falsa 123")
