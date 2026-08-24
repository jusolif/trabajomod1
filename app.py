import streamlit as st

modulo = st.sidebar.selectbox("Seleccione una sección:",["Home","Ejercicio 1","Ejercicio 2","Ejercicio 3","Ejercicio 4"])

if modulo == "Home":
  st.title("Proyecto Aplicado en Streamlit – Fundamentos de Programación ")
  st.image("DMC.png",width=150)
  st.image("Python_logo.png",width=300)
  st.subheader("Julio Humberto Solis Flores")
  st.markdown("Módulo 1: Python Fundamentals")
  st.write("Ingeniero Industrial con experiencia en Business Intelligence")
  st.write("2026")
  st.write("Trabajo práctico número 1 para el curso de Especialización en Python for Analytics")
  st.write("Para este trabajo se usaron tecnologías como Google Colab, Python, GitHub y Streamlit")

elif modulo == "Ejercicio 1":
  st.title("Ejercicio 1")
  st.write("Registro de Movimientos Financieros")
   

elif modulo == "Ejercicio 2":
  st.title("Ejercicio 2")
  st.write("En esta sección se desarrollará el Ejercicio 2.")

elif modulo == "Ejercicio 3":
  st.title("Ejercicio 3")
  st.write("En esta sección se desarrollará el Ejercicio 3.")

elif modulo == "Ejercicio 4":
  st.title("Ejercicio 4")
  st.write("En esta sección se desarrollará el Ejercicio 4.")





  
