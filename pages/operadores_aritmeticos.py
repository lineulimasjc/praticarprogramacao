import streamlit as st

st.title("📌 Operadores Aritméticos", anchor=False)

st.header('Os operadores aritméticos são usados para realizar cálculos matemáticos em C++.', anchor=False)

st.write('Aqui estão os principais:')

st.markdown("""
| Operador | Descrição     | Exemplo (a = 10, b = 3) | Resultado  |
| -------- | ------------- | ----------------------- | ---------  |
|     ```+```    | Adição        |  ```a + b```      |     ```13```     |
|     ```-```    | Subtração     |  ```a - b```      |     ```7```      |
|     ```*```    | Multiplicação |  ```a * b```      |     ```30```     |
|     ```/```    | Divisão       |  ```a / b```      |     ```3``` (inteiros) ou ```3.33``` (float)     |
|     ```%```    | Módulo        |  ```a % b```      |     ```1```      |
""")

st.divider()

st.subheader('⚠️ **Atenção:**', anchor=False)

st.write('⚠️ A **divisão** entre inteiros (```int```) descarta a parte decimal.')

st.write('⚠️ O operador ```%``` só pode ser usado com **inteiros**.')

st.divider()

st.write('🔹 Exemplo:')

code = '''
#include <iostream>
using namespace std;

int main()
{
    int a = 10, b = 3;
    cout << "Soma: " << a + b << endl;
    cout << "Subtração: " << a - b << endl;
    cout << "Multiplicação: " << a * b << endl;
    cout << "Divisão: " << a / b << endl;
    cout << "Módulo: " << a % b << endl;
}
'''
st.code(code, language="cpp")

st.write('Saída:')

code = '''
Soma: 13
Subtração: 7
Multiplicação: 30
Divisão: 3
Módulo: 1
'''
st.code(code, language="cpp")

st.write('Esses operadores são essenciais para cálculos em qualquer programa C++! 🚀')
