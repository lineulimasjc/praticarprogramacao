# Registro

import streamlit as st

st.title("Registro")

st.subheader("1. O que é um Registro?")

st.write("Um **registro** é uma estrutura de dados definida pelo usuário contendo um conjunto de variáveis de diferentes tipos.")

st.subheader("2. Sintaxe")

st.text('''
struct NomeRegistro
{
  tipo_1 var_1;
  tipo_2 var_2;
    ...
  tipo_n var_n;
};
''')

st.subheader("3. Como criar um registro")

st.write("Imagine que você precisa armazenar os seguintes dados de uma pessoa: **nome**, **idade** e **altura**. O registro ficará assim:")

code = '''
struct Pessoa
{
    string Nome;
    int Idade;
    double Altura;
};
'''
st.code(code, language="cpp")

st.subheader("4. Declarando um registro")

st.write("O ```registro``` Pessoa agora é um tipo de dado. Desta forma, podemos declarar ```p1``` como sendo do tipo ```Pessoa```.")

code = '''
#include <iostream>
using namespace std;

struct Pessoa
{
    string Nome;
    int Idade;
    double Altura;
};

int main()
{
    Pessoa p1;
}
'''
st.code(code, language="cpp")

st.subheader("5. Atribuindo valores aos membros do registro")

st.write("Para acessar os membros de um registro usamos o operador ```.``` (ponto).")

st.write("Para atribuir um dado a um membro do registro, devemos usar o **nome da variável** e o **nome do membro** separado por um . (ponto).")

st.write("Exemplo: ```p1.Nome = \"Maria\";```")

code = '''
#include <iostream>
using namespace std;

struct Pessoa
{
    string Nome;
    int Idade;
    double Altura;
};

int main()
{
  Pessoa p1;

  p1.Nome = "Maria";
  p1.Idade = 28;
  p1.Altura = 1.72;
}
'''
st.code(code, language="cpp")

st.subheader("6. Imprimindo os dados do registro")

st.write("Para imprimir o valor armazenado de um membro do registro, devemos usar o **nome da variável** e o **nome do membro** separado por um ```.``` (ponto).")

st.write('Exemplo: ```cout << p1.Nome = \"Maria\";```')

code = '''
#include <iostream>
using namespace std;

struct Pessoa
{
    string Nome;
    int Idade;
    double Altura;
};

int main()
{
  Pessoa p1;

  p1.Nome = "Maria";
  p1.Idade = 28;
  p1.Altura = 1.72;

  cout << "Nome: " << p1.Nome << endl;
  cout << "Idade: " << p1.Idade << endl;
  cout << "Altura: " << p1.Altura << endl;
}
'''
st.code(code, language="cpp")










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
