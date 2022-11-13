import streamlit as st
import pandas as pd

tipo_de_material = []
rugosidad = []
tipo_de_materialR = []
rugosidadR = []

#Funciones para realizar conversiones
def milimetros_metros(mm):
    return mm*0.001

def milimetros_pie(mm):
    return mm*0.00328084

def milimetros_pulgadas(mm):
    return mm*0.03937008

#Funcion para mostrar la informacion ordenada
def mostrarInformacion(nombre_del_material, mm):
    informacion = ""

    print(nombre_del_material.upper())

    if(len(mm) == 2): 
        informacion = {
            "Metros": "{:.8f} - {:.8f}".format(milimetros_metros(mm[0]), milimetros_metros(mm[0])),
            "Pies": "{:.8f} - {:.8f}".format(milimetros_pie(mm[0]), milimetros_pie(mm[0])),
            "Pulgadas":"{:.8f} - {:.8f}" .format(milimetros_pulgadas(mm[0]), milimetros_pulgadas(mm[1]))
        }
    else:   
        informacion = {
            "Metros: ": "{:.8f}".format(milimetros_metros(mm[0])),
            "Pies": "{:.8f}".format(milimetros_pie(mm[0])),
            "Pulgadas": "{:.8f}".format(milimetros_pulgadas(mm[0]))
        }

    return informacion

materiales = {
    "Drawn Copper":[0.001,0.002],
    "Lead":[0.001,0.002],
    "Brass":[0.001,0.002],
    "Aluminum (new) and the like":[0.001,0.002],
    "PVC":[0.0015,0.007],
    "PE and other smooth Plastic Pipes":[0.0015,0.007],
    "Stainless steel, turned":[0.0004,0.006],
    "Stainless steel, electron-polished":[0.0001,0.0008],
    "Comercial steel or wrought iron":[0.045,0.09],
    "Stretched steel":[0.015],
    "Weld steel":[0.045],
    "Galvanized steel":[0.15],
    "Rusted steel (corrosion)":[0.15,4],
    "New cast iron":[0.25,0.8],
    "Worn cast iron":[0.8,1.5],
    "Rusty cast iron":[1.5,2.5],
    "Sheet or asphalted cast iron":[0.01,0.015],
    "Smoothed cement":[0.3],
    "Ordinary concrete":[0.3,1],
    "Coarse concrete":[0.3,5],
    "Wood stove":[0.18,0.9],
    "Well planed wood":[0.18,0.9],
    "Ordinary wood":[5],
}

for i in materiales:
  tipo_de_material.append(i)
  rugosidad.append(materiales[i])

tabla_materiales = {
  "Materiales": tipo_de_material,
  "Rango De Rugosidad": rugosidad
}

if st.checkbox("Mostrar Tabla"):
  st.write(pd.DataFrame.from_dict(tabla_materiales))

with st.form("My Form"):
  st.title("Seleccione el material")
  material_elegido = st.radio(
        "",
        (tipo_de_material))

  submitted = st.form_submit_button("Calcular")
  if submitted:
    st.write("El material elegido es: {}".format(material_elegido))
    resultados = mostrarInformacion(material_elegido, materiales[material_elegido]) 

    for i in resultados:
      tipo_de_materialR.append(i)
      rugosidadR.append(resultados[i])

    tabla_resultados = {
        "Unidad de medida": tipo_de_materialR,
        "Rango De Rugosidad": rugosidadR
    }
    
    st.write(pd.DataFrame.from_dict(tabla_resultados))
