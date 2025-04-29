import streamlit as st

st.set_page_config(
    page_title="Praticar Programação",
    page_icon="images/logo.png",
    layout="centered",
    initial_sidebar_state="auto",
)

pgs = {
    "C++ Estruturado": [
        st.Page("pages/home.py", title="Home", icon="🏡"), #house_with_garden
        st.Page("pages/introducao.py", title="Introdução", icon="📝"), #pencil
        st.Page("pages/saida_de_dados.py", title="Saída de Dados", icon="📊"), #bar_chart

        st.Page("pages/pulando_linha.py", title="Pulando Linha", icon="↩️"), #bar_chart
        st.Page("pages/operadores_aritmeticos.py", title="Operadores Aritméticos", icon="✖️"), #bar_chart


        st.Page("pages/variaveis.py", title="Variáveis", icon="🗄️"), #file_cabinet
        st.Page("pages/entrada_de_dados.py", title="Entrada de Dados", icon="⌨️"), #keyboard
        st.Page("pages/estrutura_de_decisao.py", title="Estrutura de Decisão", icon="❓"), #question
        st.Page("pages/laco_de_repeticao.py", title="Laço de Repetição", icon="🔁"), #repeat
        st.Page("pages/funcao.py", title="Função", icon="⚙️"), #gear
        st.Page("pages/vetor.py", title="Vetor", icon="📏"), #straight_ruler
        st.Page("pages/matriz.py", title="Matriz", icon="📋"), #clipboard
        st.Page("pages/registro.py", title="Registro", icon="📦"), #package
    ],
    # "C++ Orientado a Objetos": [
    #      st.Page("pages/example_three.py", title="Learn about us"),
    #      st.Page("pages/example_two.py", title="Try it out"),
    # ],
    "OBI": [
        st.Page("pages/obi/entrada.py", title="Entrada de Dados", icon="⌨️"),
        st.Page("pages/obi/string.py", title="Extraindo Dados de Strings", icon="🔤"),
        st.Page("pages/obi/array_dinamico.py", title="Arrays Dinâmicos", icon="📶"),
    #      st.Page("pages/example_two.py", title="Try it out"),
    ],
}

pg = st.navigation(pgs)

pg.run()
