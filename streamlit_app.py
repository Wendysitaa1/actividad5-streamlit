import streamlit as st
import math

st.set_page_config(
    page_title="Calculadora Geométrica",
    page_icon="📐"
)

st.title("📐 Calculadora de Áreas y Perímetros")

figura = st.selectbox(
    "Seleccione una figura:",
    ["Rectángulo", "Cuadrado", "Triángulo", "Círculo", "Paralelogramo"]
)

if figura == "Rectángulo":
    st.subheader("▭ Rectángulo")
    st.write("Área = base × altura")
    st.write("Perímetro = 2 × (base + altura)")

    base = st.number_input("Base", min_value=0.0)
    altura = st.number_input("Altura", min_value=0.0)

    if st.button("Calcular"):
        area = base * altura
        perimetro = 2 * (base + altura)

        st.success(f"Área: {area}")
        st.info(f"Perímetro: {perimetro}")


elif figura == "Cuadrado":
    st.subheader("□ Cuadrado")
    st.write("Área = lado²")
    st.write("Perímetro = 4 × lado")

    lado = st.number_input("Lado", min_value=0.0)

    if st.button("Calcular"):
        area = lado ** 2
        perimetro = 4 * lado

        st.success(f"Área: {area}")
        st.info(f"Perímetro: {perimetro}")


elif figura == "Triángulo":
    st.subheader("△ Triángulo")
    st.write("Área = (base × altura) / 2")
    st.write("Perímetro = lado1 + lado2 + lado3")

    base = st.number_input("Base", min_value=0.0)
    altura = st.number_input("Altura", min_value=0.0)
    lado1 = st.number_input("Lado 1", min_value=0.0)
    lado2 = st.number_input("Lado 2", min_value=0.0)
    lado3 = st.number_input("Lado 3", min_value=0.0)

    if st.button("Calcular"):
        area = (base * altura) / 2
        perimetro = lado1 + lado2 + lado3

        st.success(f"Área: {area}")
        st.info(f"Perímetro: {perimetro}")


elif figura == "Círculo":
    st.subheader("◯ Círculo")
    st.write("Área = π × radio²")
    st.write("Perímetro = 2 × π × radio")

    radio = st.number_input("Radio", min_value=0.0)

    if st.button("Calcular"):
        area = math.pi * radio ** 2
        perimetro = 2 * math.pi * radio

        st.success(f"Área: {area:.2f}")
        st.info(f"Perímetro: {perimetro:.2f}")


elif figura == "Paralelogramo":
    st.subheader("▱ Paralelogramo")
    st.write("Área = base × altura")
    st.write("Perímetro = 2 × (base + lado)")

    base = st.number_input("Base", min_value=0.0)
    altura = st.number_input("Altura", min_value=0.0)
    lado = st.number_input("Lado", min_value=0.0)

    if st.button("Calcular"):
        area = base * altura
        perimetro = 2 * (base + lado)

        st.success(f"Área: {area}")
        st.info(f"Perímetro: {perimetro}")
