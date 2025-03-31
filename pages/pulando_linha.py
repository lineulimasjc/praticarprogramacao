import streamlit as st

st.title("📌 Pulando Linha", anchor=False)

st.header('Em C++, existem duas formas principais de pular linha ao exibir texto no console:', anchor=False)

st.subheader('1️⃣ Usando ```\\n``` (escape character)', anchor=False)

st.write('🔹 Inserido dentro da string, representa uma quebra de linha.')

st.write('🔹 Exemplo:')

code = '''
#include <iostream>
using namespace std;

int main()
{
    cout << "Linha 1\\nLinha 2";
}
'''
st.code(code, language="cpp")

st.write('Saída:')

code = '''
Linha 1
Linha 2
'''
st.code(code, language="cpp")


st.divider()


st.subheader('2️⃣ Usando ```endl``` (manipulador de fluxo)', anchor=False)

st.write('🔹 É escrito fora da string e também quebra a linha.')

st.write('🔹 Exemplo:')

code = '''
#include <iostream>
using namespace std;

int main()
{
    cout << "Linha 1" << endl << "Linha 2";
}
'''
st.code(code, language="cpp")

st.write('Saída:')

code = '''
Linha 1
Linha 2
'''
st.code(code, language="cpp")

st.divider()

st.subheader('⚠️ Diferença principal: ```endl``` força a limpeza do buffer de saída, o que pode impactar o desempenho em loops, enquanto ```\\n``` apenas pula a linha. 🚀')
