# Laço de Repetição

import streamlit as st

st.set_page_config(
    page_title="Laço de Repetição",
    page_icon="images/logo.png",
    layout="centered",
    initial_sidebar_state="auto",
)

st.title("Laço de Repetição")

t1, t2, t3, t4 = st.tabs(["Operadores", "```while```", "```do...while```", "```for```"])

t1.subheader("Operadores de Incremento e Decremento")

t1.markdown("""
| Operador    | Exemplo     | Explicação                                                     |
| ----------- | ----------- | -------------------------------------------------------------- |
| ```++```    | ```cnt++``` | Usa o valor atual de ```cnt``` e incrementa ```cnt``` em 1.    |
| ```++```    | ```++cnt``` | Incrementa ```cnt``` em 1 e usa o novo valor.                  |
| ```--```    | ```cnt--``` | Usa o valor atual de ```cnt``` e decrementa ```cnt``` em 1.    |
| ```--```    | ```--cnt``` | Decrementa ```cnt``` em 1 e usa o novo valor.                  |
""")

t1.subheader("Pós-incremento (cnt++)")

code = '''
#include <iostream>
using namespace std;

int main()
{
  int cnt = 2;

  // Usa o valor atual de cnt e incrementa cnt em 1.
  cout << "Contador = " << cnt++ << endl;

  cout << "Contador = " << cnt << endl;
}
'''
t1.code(code, language="cpp")

t1.write('Saída:')



t1.text('''
Contador = 2
Contador = 3
''')




t1.subheader("Pré-incremento (++cnt)")

code = '''
#include <iostream>
using namespace std;

int main()
{
  int cnt = 2;

  // Incrementa cnt em 1 e usa o novo valor.
  cout << "Contador = " << ++cnt << endl;

  cout << "Contador = " << cnt << endl;
}
'''
t1.code(code, language="cpp")

t1.write('Saída:')



t1.text('''
Contador = 3
Contador = 3
''')






t1.subheader("Pós-decremento (cnt−−)")

code = '''
#include <iostream>
using namespace std;

int main()
{
  int cnt = 2;

  // Usa o valor atual de cnt e decrementa cnt em 1.
  cout << "Contador = " << cnt-- << endl;

  cout << "Contador = " << cnt << endl;
}
'''
t1.code(code, language="cpp")

t1.write('Saída:')



t1.text('''
Contador = 2
Contador = 1
''')





t1.subheader("Pré-decremento (−−cnt)")

code = '''
#include <iostream>
using namespace std;

int main()
{
  int cnt = 2;

  // Decrementa cnt em 1 e usa o novo valor.
  cout << "Contador = " << --cnt << endl;

  cout << "Contador = " << cnt << endl;
}
'''
t1.code(code, language="cpp")

t1.write('Saída:')

t1.text('''
Contador = 1
Contador = 1
''')


# Adicionar o aqui aqui





# while tab

t2.subheader("While")

t2.write("O comando ```while``` executa a repetição de um bloco de instruções enquanto a condição é verdadeira.")

t2.write("Sintaxe")

t2.text('''
while (condição)
{
  Instrução ou bloco de instruções;
}
''')

t2.subheader("Exemplo 1")

t2.write("Ao exercutar o código abaixo, será impresso na tela os números de 0 a 9.")

t2.write("A variável ```i``` na instrução ```i = i + 1``` é um contador, que funciona como um acumulador ou somatório. O contador é usado para controlar o número de vezes que o laço repetirá, sendo incrementado em 1 a cada execução do laço.")


code = '''
#include <iostream>
using namespace std;

int main()
{
  int i = 0;

  while (i < 10)
  {
    cout << i << endl;

    i = i + 1;
  }
}
'''
t2.code(code, language="cpp")

t2.write('Saída:')

t2.text('''
0
1
2
3
4
5
6
7
8
9
''')



t2.subheader("Exemplo 2")

t2.write("Neste exemplo, o usuário poderá ***entrar com os dados** e, quando desejar **finalizar o programa**, deverá **digitar -1**.")

t2.write("Este exemplo é muito útil para **manter o programa em execução até que o usuário decida fechá-lo**.")


code = '''
#include <iostream>
using namespace std;

int main()
{
  int Numero = 0;

  cout << "Digite um número ou -1 para finalizar: ";
  cin >> Numero;

  while (Numero != -1)
  {
    cout << "Digite um número ou -1 para finalizar: ";
    cin >> Numero;
  }

  cout << "FIM" << endl;
}
'''
t2.code(code, language="cpp")

t2.write('Saída:')

t2.text('''
Digite um número ou -1 para fechar o programa: 3
Digite um número ou -1 para fechar o programa: 6
Digite um número ou -1 para fechar o programa: 9
Digite um número ou -1 para fechar o programa: -1
FIM
''')




t2.subheader("Exemplo 3")

t2.write("Neste exemplo, o usuário deverá **digitar um número entre 1 e 3**, pois são os valores de entrada esperados pela aplicação. Caso o **número digitado não esteja neste intervalo**, o **usuário receberá uma mensagem e deverá fazer uma nova entrada de dados**.")

t2.write("Este exemplo é muito útil para **validar as entradas de dados realizadas pelo usuário**, a fim de evitar falhas na aplicação.")


code = '''
#include <iostream>
using namespace std;

int main()
{
  int Numero = 0;

  cout << "Digite um número entre 1 e 3: ";
  cin >> Numero;

  while (Numero < 1 || Numero > 3)
  {
    cout << "Número inválido, tente novamente!" << endl;

    cout << "Digite um número entre 1 e 3: ";
    cin >> Numero;
  }

  cout << "Parabéns, esse número é válido!" << endl;
}
'''
t2.code(code, language="cpp")

t2.write('Saída:')

t2.text('''
Digite um número entre 1 e 3: 0
Número inválido, tente novamente!
Digite um número entre 1 e 3: 5
Número inválido, tente novamente!
Digite um número entre 1 e 3: 1
Parabéns, esse número é válido!
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
