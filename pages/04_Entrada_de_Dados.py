# Entrada de Dados

import streamlit as st

st.set_page_config(
    page_title="Entrada de Dados",
    page_icon="images\logo.png",
    layout="centered",
    initial_sidebar_state="auto",
)


st.title("Entrada de Dados – ```cin```")

st.write("O comando cin controla a entrada de dados, permitindo ao usuário da aplicação entrar com dados via teclado.")

st.write("A letra “c” de cin significa caractere e “in” significa input *(entrada em português)*.")

st.write("Sintaxe: ```cin >> variável;```")

st.write("Existem várias formas de entrar com dados usando o comando ```cin```. A melhor forma dependerá da solução desejada para a sua aplicação.")




st.subheader('Exemplo 1')

st.write("**Entrando com dados.**")

st.write("Código")

code = '''
#include <iostream>
using namespace std;

int main()
{
  double Altura = 0;

  cout << "Informe a altura: ";
  cin >> Altura;

  cout << "Altura: " << Altura << endl;
}
'''
st.code(code, language="cpp")

st.write('Saída:')


st.text('''
Informe a altura: 1.81
Altura: 1.81
''')






st.subheader('Exemplo 2')

st.write("**Entrando com dados em linhas separadas.**")

st.write("Código")

code = '''
#include <iostream>
using namespace std;

int main()
{
  int Num1 = 0;
  int Num2 = 0;

  cout << "Valor 1: ";
  cin >> Num1;

  cout << "Valor 2: ";
  cin >> Num2;

  cout << "Soma = " << Num2 + Num1 << endl;
}
'''
st.code(code, language="cpp")

st.write('Saída:')


st.text('''
Valor 1: 3
Valor 2: 7
Soma = 10
''')






st.subheader('Exemplo 3')

st.write("**Entrando com dados na mesma linha.**")

st.write("Código")

code = '''
#include <iostream>
using namespace std;

int main()
{
  int Num1 = 0;
  int Num2 = 0;

  cout << "Informe 2 valores separados por um espaço: ";
  cin >> Num1 >> Num2;

  cout << "Soma = " << Num2 + Num1 << endl;
}
'''
st.code(code, language="cpp")

st.write('Saída:')

st.text('''
Informe 2 valores separados por um espaço: 3 7
Soma = 10
''')

st.divider()


st.subheader('Exemplo')

st.write("Código")

code = '''
#include <iostream>
#include <string>
using namespace std;

int main()
{
  string Nome;

  cout << "Nome completo: ";
  getline(cin, Nome);

  cout << "Bom jogo " << Nome << "!" << endl;
}
'''
st.code(code, language="cpp")

st.write('Saída:')


st.text('''
Nome completo: Pedro Silva
Bom jogo Pedro Silva!
''')





st.title("Entrada de Dados – ```getline```")


st.write("O comando ```getline``` permite a entrada de texto contendo o caractere “espaço em branco“.")

st.info(":grey_exclamation: O comando ```getline``` pertence a biblioteca ```<string>```.")

st.write("Sintaxe: ```getline(cin, variável);```")






















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

