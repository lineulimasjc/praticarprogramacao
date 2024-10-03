# Introdução
import streamlit as st

st.set_page_config(
    page_title="Introdução",
    page_icon="images/logo.png",
    layout="centered",
    initial_sidebar_state="auto",
)

st.header('Programação Estruturada vs Orientada a Objetos')

st.subheader("1. Programação Estruturada")

st.write("**Programação Estruturada** é um método de desenvolvimento de programas. Este método usa três tipos de estruturas de controle.")

col1, col2, col3 = st.columns(3)

with col1:
    st.header("Sequência")
    st.write("As instruções são executas de forma sequencial.")
    seq="images/sequencia.svg"
    st.image(seq, caption= 'Sequência', width=200)
    
with col2:
    st.header("Seleção")
    st.write("As instruções são executadas com base em uma ou mais condições.")
    sel="images/selecao.svg"
    st.image(sel, caption= 'Seleção', width=200)

with col3:
    st.header("Repetição")
    st.write("As instruções são executadas enquanto a condição for satisfeita.")
    rep="images/repeticao.svg"
    st.image(rep, caption= 'Repetição', width=200)

st.write("###")

st.write("Exemplos:")

st.markdown("- C")
st.markdown("- C++")
st.markdown("- Pascal")
st.markdown("- Rust")

st.divider()




st.subheader("2. Programação Orientada a Objetos")

st.write("**Programação Orientada a Objetos** é um método de desenvolvimento de programas. Este método é baseado no conceito de “**objetos**“. Os objetos podem conter **dados** e **códigos**.")

oop="images/orientacao-a-objetos.svg"
st.image(oop, caption= 'Programação Orientada a Objetos', width=350)

# st.image("images/orientacao-a-objetos.svg")

st.write("###")

st.write("Exemplos:")

st.markdown("- C++")
st.markdown("- Python")
st.markdown("- Java")








# Footer implementation
footer = """
<style>
.footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    background-color: #f0f2f6;
    color: #31333f;
    text-align: center;
}
</style>
<div class='footer'>
  <p>Praticar Programação ©</p>
</div>
"""
st.markdown(footer, unsafe_allow_html=True)