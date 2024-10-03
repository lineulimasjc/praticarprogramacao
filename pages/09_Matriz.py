# Matriz

import streamlit as st

st.set_page_config(
    page_title="Matriz",
    page_icon="images/logo.png",
    layout="centered",
    initial_sidebar_state="auto",
)

st.title("O que são Matrizes?")

st.write("**Matriz** é uma estrutura de dados que armazena uma determinada quantidade de elementos do mesmo tipo de dado.")

st.write("O **acesso** aos elementos de uma matriz é feito através dos índices (linhas e colunas).")

mat="images/matrix.svg"
st.image(mat, caption= 'Matriz', width=350)

st.write("Sintaxe:")

st.text('''
tipo-de-dado NomeMatriz[n][m];
''')


st.subheader("Declarando Matrizes")

st.subheader("Exemplo 1a")

st.write("A matriz ```Numeros``` do tipo ```int``` é declarada e 4 valores são atribuídos a matriz. Em seguida, os valores são impressos na tela.")

st.write("Código:")

code = '''
#include <iostream>
using namespace std;

int main()
{
  // Declarando a matriz e atribuíndo 4 elementos
  int Numeros[2][2] = {{10, 20}, {30, 40}};

  int i, j;

  cout << "Elementos da matriz: " << endl;

  // Imprimindo os elementos da matriz
  for(i = 0; i < 2; i++)
    for(j = 0; j < 2; j++)
    {
      cout << Numeros[i][j] << "\t";
    }
}
'''
st.code(code, language="cpp")

st.write('Saída:')

st.text('''
Elementos da matriz:
10 20 30 40
''')

st.divider()






st.subheader("Exemplo 1b")

st.write("Quando aprendemos a trabalhar com matrizes, temos o desejo de imprimir a matriz no forma de uma matriz (linhas e colunas).")

st.write("Código:")

code = '''
#include <iostream>
using namespace std;

int main()
{
  // Declarando a matriz e atribuíndo 4 elementos
  int Numeros[2][2] = {{10, 20}, {30, 40}};

  int i, j;

  cout << "Elementos da matriz: " << endl;

  // Imprimindo os elementos da matriz
  for(i = 0; i < 2; i++)
  {
    for(j = 0; j < 2; j++)
    {
      cout << Numeros[i][j] << "\t";
    }
    cout << endl;
  }
}
'''
st.code(code, language="cpp")

st.write('Saída:')

st.text('''
Elementos da matriz:
10 20
30 40
''')

st.divider()







st.subheader("Exemplo 2")

st.write("A matriz ```Numeros``` do tipo ```double``` é declarado. A entrada de dados é feita pelo usuário. Em seguida, os valores são impressos na tela.")

st.write("Código:")

code = '''
#include <iostream>
using namespace std;

int main()
{
  // Declarando a matriz e atribuíndo 4 elementos
  int Numeros[2][2];

  int i, j;

  // Atribuindo elementos a matriz
  for(i = 0; i < 2; i++)
  {
    for(j = 0; j < 2; j++)
    {
      cout << "Informe valor " << i << "," << j << ": ";
      cin >> Numeros[i][j];
    }
  }

  cout << "Elementos da matriz: " << endl;

  // Imprimindo os elementos da matriz
  for(i = 0; i < 2; i++)
  {
    for(j = 0; j < 2; j++)
    {
      cout << Numeros[i][j] << "\t";
    }
    cout << endl;
  }
}
'''
st.code(code, language="cpp")

st.write('Saída:')

st.text('''
Informe valor 0,0: 1
Informe valor 0,1: 2
Informe valor 1,0: 3
Informe valor 1,1: 4
Elementos da matriz:
1 2
3 4
''')

st.divider()


st.subheader("Manipulando Matrizes")

st.write("É possível fazer várias operações com matrizes, como por exemplo:")

st.write(":white_medium_square: Soma;")
st.write(":white_medium_square: Média;")
st.write(":white_medium_square: Identificar o maior ou menor valor;")
st.write(":white_medium_square: Contar elementos com base em uma condição.")



st.subheader("Exemplo 1")

st.write("Calculando a **soma** dos elementos da matriz.")

st.write("Código:")

code = '''
#include <iostream>
using namespace std;

int main()
{
  // Declarando a matriz e atribuíndo 4 elementos
  double Numeros[2][2];

  double Soma = 0;

  int i, j;

  // Atribuindo elementos a matriz
  for(i = 0; i < 2; i++)
  {
    for(j = 0; j < 2; j++)
    {
      cout << "Informe valor " << i << "," << j << ": ";
      cin >> Numeros[i][j];
    }
  }

  // Imprimindo a soma dos elementos da matriz
  for(i = 0; i < 2; i++)
    for(j = 0; j < 2; j++)
    {
      Soma = Soma + Numeros[i][j];
    }
    cout << "Soma: " << Soma;
}
'''
st.code(code, language="cpp")

st.write('Saída:')

st.text('''
Informe valor 0,0: 5.5
Informe valor 0,1: 6.5
Informe valor 1,0: 7.5
Informe valor 1,1: 8.5
Soma: 28
''')

st.divider()





st.subheader("Exemplo 2")

st.write("Calculando a **média** dos elementos da matriz.")

st.write("Código:")

code = '''
#include <iostream>
using namespace std;

int main()
{
    // Declarando o vetor
    double Numeros[3];

    int i;
    double Soma = 0;

    // Atribuindo elementos ao vetor
    for(i = 0; i < 3; i++)
    {
        cout << "Informe valor " << i + 1 << ": ";
        cin >> Numeros[i];

        Soma = Soma + Numeros[i]; // Soma os elementos do vetor
    }

    // Imprime a média dos elementos do vetor
    cout << "\nMédia: " << Soma / i << endl;
}
'''
st.code(code, language="cpp")

st.write('Saída:')

st.text('''
Informe valor 0,0: 5.5
Informe valor 0,1: 6.5
Informe valor 1,0: 7.5
Informe valor 1,1: 8.5
Média: 7
''')

st.divider()





st.subheader("Exemplo 3")

st.write("Identificando o **maior** elemento em uma matriz.")

st.write("Código:")

code = '''
#include <iostream>
using namespace std;

int main()
{
  // Declarando a matriz e atribuíndo 4 elementos
  int Numeros[2][2];

  int MaiorValor;

  int i, j;

  // Atribuindo elementos a matriz
  for(i = 0; i < 2; i++)
  {
    for(j = 0; j < 2; j++)
    {
      cout << "Informe valor " << i << "," << j << ": ";
      cin >> Numeros[i][j];
    }
  }

  // Identificando maior elemento
  for(i = 0; i < 2; i++)
    for(j = 0; j < 2; j++)
    {
      if (MaiorValor < Numeros[i][j])
      {
        MaiorValor = Numeros[i][j];
      }
    }
  cout << "Maior elemento: " << MaiorValor << endl;
}
'''
st.code(code, language="cpp")

st.write('Saída:')

st.text('''
Informe valor 0,0: 1
Informe valor 0,1: 2
Informe valor 1,0: 4
Informe valor 1,1: 3
Maior elemento: 4
''')

st.divider()




st.subheader("Exemplo 4")

st.write("**Contando** a quantidade de elementos pares e ímpares de uma matriz.")

st.write("Código:")

code = '''
#include <iostream>
using namespace std;

int main()
{
  // Declarando a matriz e atribuíndo 4 elementos
  int Numeros[2][2];

  int ContaPar = 0, ContaImpar = 0;

  int i, j;

  // Atribuindo elementos a matriz
  for(i = 0; i < 2; i++)
  {
    for(j = 0; j < 2; j++)
    {
      cout << "Informe valor " << i << "," << j << ": ";
      cin >> Numeros[i][j];
    }
  }

  // Identificando maior elemento
  for(i = 0; i < 2; i++)
    for(j = 0; j < 2; j++)
    {
      if (Numeros[i][j] % 2 == 0)
      {
        ContaPar++;
      }
      else
      {
        ContaImpar++;
      }
    }
  cout << "Par: " << ContaPar << endl;
  cout << "Ímpar: " << ContaImpar << endl;
}
'''
st.code(code, language="cpp")

st.write('Saída:')

st.text('''
Informe valor 0,0: 1
Informe valor 0,1: 2
Informe valor 1,0: 3
Informe valor 1,1: 4
Par: 2
Ímpar: 2
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
