import streamlit as st

st.title("Laço de Repetição")

t1, t2, t3, t4 = st.tabs(["Operadores", "```while```", "```do...while```", "```for```"])

t1.subheader("Operadores de Incremento e Decremento", anchor=False)

t1.markdown("""
| Operador    | Exemplo     | Explicação                                                     |
| ----------- | ----------- | -------------------------------------------------------------- |
| ```++```    | ```cnt++``` | Usa o valor atual de ```cnt``` e incrementa ```cnt``` em 1.    |
| ```++```    | ```++cnt``` | Incrementa ```cnt``` em 1 e usa o novo valor.                  |
| ```--```    | ```cnt--``` | Usa o valor atual de ```cnt``` e decrementa ```cnt``` em 1.    |
| ```--```    | ```--cnt``` | Decrementa ```cnt``` em 1 e usa o novo valor.                  |
""")

t1.subheader("Pós-incremento (cnt++)", anchor=False)

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




t1.subheader("Pré-incremento (++cnt)", anchor=False)

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






t1.subheader("Pós-decremento (cnt−−)", anchor=False)

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





t1.subheader("Pré-decremento (−−cnt)", anchor=False)

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


# while tab

t2.subheader("While", anchor=False)

t2.write("O comando ```while``` executa a repetição de um bloco de instruções enquanto a condição é verdadeira.")

t2.write("Sintaxe")

t2.text('''
while (condição)
{
  Instrução ou bloco de instruções;
}
''')



t2.subheader("Exemplo 1", anchor=False)

t2.write("Ao exercutar o código abaixo, será impresso na tela os números de 0 a 9.")

# t2.write("A variável ```i``` na instrução ```i = i + 1``` é um contador, que funciona como um acumulador ou somatório. O contador é usado para controlar o número de vezes que o laço repetirá, sendo incrementado em 1 a cada execução do laço.")
t2.write("A variável ```i``` na instrução ```i = i + 1``` é um **contador**, que funciona como um **acumulador** ou **somatório**. O contador é usado para controlar o número de vezes que o laço repetirá, sendo **incrementado em 1 a cada execução do laço**.")


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



t2.subheader("Exemplo 2", anchor=False)

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




t2.subheader("Exemplo 3", anchor=False)

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




t3.subheader("Do…while", anchor=False)

t3.write("O comando ```do...while``` executa a repetição de um bloco de instruções enquanto a condição é verdadeira.")

t3.subheader("Diferenças entre ```do…while``` e ```while```", anchor=False)


t3.write(":small_blue_diamond: No ```while```, a condição é testada no **início** do bloco de instruções. No ```do…while```, a condição é testada no **final** do bloco de instruções.")

t3.write(":small_blue_diamond: No ```do…while```, o laço é executado pelo menos uma vez, independente do resultado da expressão lógica, pois a condição é testada no final do bloco de instruções.")

t3.write(":small_blue_diamond: É importante lembrar que no ```do…while```, no final da linha do while, é obrigatório o uso do ( ```;``` ) **ponto e vírgula**.")

t3.write("Sintaxe")

t3.text('''
do
{
  Instrução ou bloco de instruções;
} while (condição);
''')



t3.warning('Os mesmos exemplos apresentados com o comando ```while``` serão apresentados com o comando ```do...while```. Compare os exemplos para ver as diferenças.', icon=":material/warning:")



t3.subheader("Exemplo 1", anchor=False)

t3.write("Ao exercutar o código abaixo, será impresso na tela os números de 0 a 9.")

t3.write("A variável ```i``` na instrução ```i = i + 1``` é um **contador**, que funciona como um **acumulador** ou **somatório**. O contador é usado para controlar o número de vezes que o laço repetirá, sendo **incrementado em 1 a cada execução do laço**.")


code = '''
#include <iostream>
using namespace std;

int main()
{
  int i = 0;

  do
  {
    cout << i << endl;

    i = i + 1;
  } while (i < 10);
}
'''
t3.code(code, language="cpp")

t3.write('Saída:')

t3.text('''
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



t3.subheader("Exemplo 2", anchor=False)

t3.write("Neste exemplo, o usuário poderá ***entrar com os dados** e, quando desejar **finalizar o programa**, deverá **digitar -1**.")

t3.write("Este exemplo é muito útil para **manter o programa em execução até que o usuário decida fechá-lo**.")

t3.info(":information_source: Como será permitida a entrada de pelo menos um valor, não há necessidade de entrar com dados fora do laço de repetição.")

code = '''
#include <iostream>
using namespace std;

int main()
{
  int Numero = 0;

  do
  {
    cout << "Digite um número ou -1 para finalizar: ";
    cin >> Numero;
  } while (Numero != -1);

  cout << "FIM" << endl;
}
'''
t3.code(code, language="cpp")

t3.write('Saída:')

t3.text('''
Digite um número ou -1 para fechar o programa: 3
Digite um número ou -1 para fechar o programa: 6
Digite um número ou -1 para fechar o programa: 9
Digite um número ou -1 para fechar o programa: -1
FIM
''')




t3.subheader("Exemplo 3", anchor=False)

t3.write("Neste exemplo, o usuário deverá **digitar um número entre 1 e 3**, pois são os valores de entrada esperados pela aplicação. Caso o **número digitado não esteja neste intervalo**, o **usuário receberá uma mensagem e deverá fazer uma nova entrada de dados**.")

t3.write("Este exemplo é muito útil para **validar as entradas de dados realizadas pelo usuário**, a fim de evitar falhas na aplicação.")

t3.write("_Como será permitida a entrada de pelo menos um valor, não há necessidade de entrar com dados fora do laço de repetição._")

code = '''
#include <iostream>
using namespace std;

int main()
{
  int Numero = 0;

  do
  {
    cout << "Número inválido, tente novamente!" << endl;

    cout << "Digite um número entre 1 e 3: ";
    cin >> Numero;
  } while (Numero < 1 || Numero > 3);

  cout << "Parabéns, esse número é válido!" << endl;
}
'''
t3.code(code, language="cpp")

t3.write('Saída:')

t3.text('''
Digite um número entre 1 e 3: 0
Número inválido, tente novamente!
Digite um número entre 1 e 3: 5
Número inválido, tente novamente!
Digite um número entre 1 e 3: 1
Parabéns, esse número é válido!
''')




# for tab

t4.subheader("For", anchor=False)

t4.write("O comando ```for``` é normalmente usado quando sabemos a **quantidade de vezes que o laço executará**.")

t4.write("Sintaxe")

t4.text('''
for (inicialização; condição; incremento/decremento)
{
  Instrução ou bloco de instruções;
}
''')



t4.subheader("Exemplo 1", anchor=False)

t4.write("Ao exercutar o código abaixo, será impresso na tela os números de 0 a 9.")

t4.write("A variável **i** na instrução ```i++``` é outra forma de escrever ```i = i + 1```. Funciona como um **acumulador** ou **somatório**. O contador é usado para controlar o número de vezes que o laço repetirá, sendo **incrementado em 1 a cada execução do laço**.")


code = '''
#include <iostream>
using namespace std;

int main()
{
  int i = 0;

  for (i = 0; i < 10; i++)
  {
    cout << i << endl;
  }
}
'''
t4.code(code, language="cpp")

t4.write('Saída:')

t4.text('''
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




t4.subheader("Exemplo 2", anchor=False)

t4.write("Neste exemplo, o usuário deve **informar quantos valores deseja entrar**, para que o programa possa identificar a **condição de término** de execução.")

code = '''
#include <iostream>
using namespace std;

int main()
{
  int Numero = 0;
  int QtdaValores = 0;
  int i;

  cout << "Quantos valores deseja informar: ";
  cin >> QtdaValores;

  for(i = 0; i < QtdaValores; i++)
  {
    cout << "Valor: " << i + 1 << ": ";
    cin >> Numero;
  }

  cout << "FIM" << endl;
}
'''
t4.code(code, language="cpp")

t4.write('Saída:')

t4.text('''
Quantos valores deseja informar: 3
Valor 1: 3
Valor 2: 6
Valor 3: 9
FIM
''')
