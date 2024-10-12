import streamlit as st

st.set_page_config(
    page_title="Praticar Programação",
    page_icon="images/logo.png",
    layout="centered",
    initial_sidebar_state="auto",
)

pgs = {
    "C++ Estruturado": [
        st.Page("pages/Home.py", title="Home", icon="🏡"), #house_with_garden
        st.Page("pages/Introducao.py", title="Introdução", icon="📝"), #pencil
        st.Page("pages/Saida_de_Dados.py", title="Saída de Dados", icon="📊"), #bar_chart
        st.Page("pages/Variaveis.py", title="Variáveis", icon="🗄️"), #file_cabinet
        st.Page("pages/Entrada_de_Dados.py", title="Entrada de Dados", icon="⌨️"), #keyboard
        st.Page("pages/Estrutura_de_Decisao.py", title="Estrutura de Decisão", icon="❓"), #question
        st.Page("pages/Laco_de_Repeticao.py", title="Laço de Repetição", icon="🔁"), #repeat
        st.Page("pages/Funcao.py", title="Função", icon="⚙️"), #gear
        st.Page("pages/Vetor.py", title="Vetor", icon="📏"), #straight_ruler
        st.Page("pages/Matriz.py", title="Matriz", icon="📋"), #clipboard
        st.Page("pages/Registro.py", title="Registro", icon="📦"), #package
    ],
    # "C++ Orientado a Objetos": [
    #      st.Page("pages/example_three.py", title="Learn about us"),
    #      st.Page("pages/example_two.py", title="Try it out"),
    # ],
    # "Linguagem SQL": [
    #      st.Page("pages/example_three.py", title="Learn about us"),
    #      st.Page("pages/example_two.py", title="Try it out"),
    # ],
}

pg = st.navigation(pgs)

pg.run()
