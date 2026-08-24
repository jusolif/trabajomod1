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
  st.markdown("Esta pequeña aplicación de registros financieros permite indicar cuántos movimientos desea registrar, agregar un concepto, tipo de movimiento y un valor.
    Finalmente se mostrará un flujo de caja que indicará un valor positivo, negativo o equilibrado")

  movimientos = []
  cantidad = st.number_input("¿Cuántos movimientos desea registrar?",min_value=1,step=1)

  for i in range(int(cantidad)):
    st.subheader("Movimiento " + str(i + 1))

    concepto = st.text_input("Concepto",key="concepto_" + str(i))

    tipo = st.selectbox("Tipo de movimiento",["Ingreso", "Gasto"],key="tipo_" + str(i))

    valor = st.number_input("Valor",min_value=0.0,step=0.01,key="valor_" + str(i))

    movimiento = {"Concepto": concepto,"Tipo": tipo,"Valor": valor}

    movimientos.append(movimiento)

  if st.button("Registrar movimientos"):

    total_ingresos = 0
    total_gastos = 0

    for movimiento in movimientos:

      if movimiento["Tipo"] == "Ingreso":
                total_ingresos = total_ingresos + movimiento["Valor"]

      else:
                total_gastos = total_gastos + movimiento["Valor"]

    saldo_final = total_ingresos - total_gastos

    st.subheader("Movimientos registrados")

    st.dataframe(movimientos)

    st.subheader("Resumen financiero")

    col1, col2, col3 = st.columns(3)

    with col1:
            st.metric("Ingresos Totales",f"S/ {total_ingresos:,.2f}")

    with col2:
            st.metric("Gastos totales",f"S/ {total_gastos:,.2f}")

    with col3:
            st.metric("Saldo final",f"S/ {saldo_final:,.2f}")

    

    if saldo_final > 0:
            st.success("Flujo de caja positivo")

    elif saldo_final < 0:
            st.error("Flujo de caja negativo")

    else:
            st.success("Flujo de caja equilibrado")
   

elif modulo == "Ejercicio 2":
  st.title("Ejercicio 2")
  st.write("En esta sección se desarrollará el Ejercicio 2.")

elif modulo == "Ejercicio 3":
  st.title("Ejercicio 3")
  st.write("En esta sección se desarrollará el Ejercicio 3.")

elif modulo == "Ejercicio 4":
  st.title("Ejercicio 4")
  st.write("En esta sección se desarrollará el Ejercicio 4.")





  
