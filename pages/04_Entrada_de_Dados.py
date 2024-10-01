# Entrada de Dados

import streamlit as st

st.set_page_config(
    page_title="Entrada de Dados",
    page_icon="images/logo.png",
    layout="centered",
    initial_sidebar_state="auto",
)


t1, t2 = st.tabs(["```cin```", "```getline```"])

# t1.title("Entrada de Dados – ```cin```")

t1.write("O comando cin controla a entrada de dados, permitindo ao usuário da aplicação entrar com dados via teclado.")

t1.write("A letra “c” de cin significa caractere e “in” significa input *(entrada em português)*.")

t1.write("Sintaxe: ```cin >> variável;```")

t1.write("Existem várias formas de entrar com dados usando o comando ```cin```. A melhor forma dependerá da solução desejada para a sua aplicação.")




t1.subheader('Exemplo 1')

t1.write("**Entrando com dados.**")

t1.write("Código")

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
t1.code(code, language="cpp")

t1.write('Saída:')


t1.text('''
Informe a altura: 1.81
Altura: 1.81
''')


t1.divider()



t1.subheader('Exemplo 2')

t1.write("**Entrando com dados em linhas separadas.**")

t1.write("Código")

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
t1.code(code, language="cpp")

t1.write('Saída:')


t1.text('''
Valor 1: 3
Valor 2: 7
Soma = 10
''')


t1.divider()



t1.subheader('Exemplo 3')

t1.write("**Entrando com dados na mesma linha.**")

t1.write("Código")

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
t1.code(code, language="cpp")

t1.write('Saída:')

t1.text('''
Informe 2 valores separados por um espaço: 3 7
Soma = 10
''')







# t2.title("Entrada de Dados – ```getline```")


t2.write("O comando ```getline``` permite a entrada de texto contendo o caractere “espaço em branco“.")

t2.info(":grey_exclamation: O comando ```getline``` pertence a biblioteca ```<string>```.")

t2.write("Sintaxe: ```getline(cin, variável);```")





t2.subheader('Exemplo')

t2.write("Código")

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
t2.code(code, language="cpp")

t2.write('Saída:')


t2.text('''
Nome completo: Pedro Silva
Bom jogo Pedro Silva!
''')

























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
