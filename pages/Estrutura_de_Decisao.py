# Estrutura de Decisão
import streamlit as st

st.title("Estrutura de Decisão")

t1, t2, t3, t4, t5, t6 = st.tabs(["Operadores de Comparação",
                                  "```if…else``` Simples",
                                  "```if…else``` Aninhado",
                                  "```if``` de uma linha",
                                  "```switch```",
                                  "Operadores Lógicos"])

t1.subheader("Operadores de Comparação", anchor=False)

t1.write("A linguagem C++ possui 6 operadores de comparação. Veja a seguir quais são e alguns exemplos de cada um deles.")

t1.markdown("""
| **Operador** |   **Descrição**  |
|:------------:|:----------------:|
|   ```==```   |      igual a     |
|   ```!=```   |   diferente de   |
|    ```>```   |     maior que    |
|   ```>=```   | maior ou igual a |
|    ```<```   |     menor que    |
|   ```<=```   | menor ou igual a |
""")

t1.write("###")

t1.info('Uma **condição** pode ter 2 tipos de saída: **verdadeiro** ou **falso**.', icon=":material/info:")

t1.write("###")

t1.write("Os operadores de comparação são usados para criar condições. As condições são usadas em **estrutura de decisão** e **laço de repetição**.")


t1.subheader("Exemplo (```==```)", anchor=False)

t1.write("Código:")

code = '''
#include <iostream>
using namespace std;

int main()
{
  int x = 3;
  int y = 3;

  cout << (x == y);
}
'''
t1.code(code, language="cpp")

t1.write('Saída:')

t1.text('''
1
''')

t1.write("Explicação: retorna \'1\' (verdadeiro), pois \'x\' é **igual a** \'y\'.")



t1.subheader("Exemplo (```!=```)", anchor=False)

t1.write("Código:")

code = '''
#include <iostream>
using namespace std;

int main()
{
  int x = 3;
  int y = 5;

  cout << (x != y);
}
'''
t1.code(code, language="cpp")

t1.write('Saída:')

t1.text('''
1
''')

t1.write("Explicação: retorna \'1\' (verdadeiro), pois \'x\' **é diferente de** \'y\'.")



t1.subheader("Exemplo (```>```)", anchor=False)

t1.write("Código:")

code = '''
#include <iostream>
using namespace std;

int main()
{
  int x = 3;
  int y = 3;

  cout << (x > y);
}
'''
t1.code(code, language="cpp")

t1.write('Saída:')

t1.text('''
0
''')

t1.write("Explicação: retorna \'0\' (falso), pois \'x\' **não é maior que** \'y\'.")




t1.subheader("Exemplo (```>=```)", anchor=False)

t1.write("Código:")

code = '''
#include <iostream>
using namespace std;

int main()
{
  int x = 3;
  int y = 3;

  cout << (x >= y);
}
'''
t1.code(code, language="cpp")

t1.write('Saída:')

t1.text('''
1
''')

t1.write("Explicação: retorna \'1\' (verdadeiro), pois \'x\' é **maior ou igual a** \'y\'.")




t1.subheader("Exemplo (```<```)", anchor=False)

t1.write("Código:")

code = '''
#include <iostream>
using namespace std;

int main()
{
  int x = 3;
  int y = 3;

  cout << (x < y);
}
'''
t1.code(code, language="cpp")

t1.write('Saída:')

t1.text('''
0
''')

t1.write("Explicação: retorna \'0\' (falso), pois \'x\' **não é menor que** \'y\'.")



t1.subheader("Exemplo (```<=```)", anchor=False)

t1.write("Código:")

code = '''
#include <iostream>
using namespace std;

int main()
{
  int x = 3;
  int y = 3;

  cout << (x <= y);
}
'''
t1.code(code, language="cpp")

t1.write('Saída:')

t1.text('''
1
''')

t1.write("Explicação: retorna \'1\' (verdadeiro), pois \'x\' é **menor ou igual a** \'y\'.")





t2.subheader("```if…else``` Simples", anchor=False)

t2.write("A estrutura de decisão ```if…else``` é utilizada para executar um bloco de código se uma condição for **verdadeira** (```if```), e opcionalmente executar outro bloco de código se a mesma condição for **falsa** (```else```).")


t2.write("Sintaxe")

t2.text('''
if (condição)
{
    [se condição verdadeira, executar este bloco de código]
}
else
{
    [se condição falsa, executar este bloco de código]
}
''')


cond1="images/if-else-simples.svg"
t2.image(cond1, caption= 'if...else simples', width=350)


t2.subheader("Exemplo 1", anchor=False)

t2.write("O programa abaixo identifica se o valor é **par** ou **ímpar** com base no valor informado pelo usuário.")

t2.write("Código:")

code = '''
#include <iostream>
using namespace std;

int main()
{
  int Num = 0;

  cout << "Digite um número: ";
  cin >> Num;

  if (Num % 2 == 0)
  {
    cout << "Par" << endl;
  }
  else
  {
    cout << "Ímpar" << endl;
  }
}
'''
t2.code(code, language="cpp")

t2.write('Saída 1:')

t2.text('''
Digite um número: 6
Par
''')

t2.write('Saída 2:')

t2.text('''
Digite um número: 7
Ímpar
''')



t2.subheader("Exemplo 2", anchor=False)

t2.write("O programa abaixo é o mesmo do exemplo 1, porém sem o ```else```.")

t2.write("Código:")

code = '''
#include <iostream>
using namespace std;

int main()
{
  int Num = 0;

  cout << "Digite um número: ";
  cin >> Num;

  if (Num % 2 == 0)
  {
    cout << "Par" << endl;
  }
}
'''
t2.code(code, language="cpp")

t2.write('Saída 1:')

t2.text('''
Digite um número: 6
Par
''')

t2.write('Saída 2:')

t2.text('''
Digite um número: 7
''')

t2.info('O programa não possui saída, pois a entrada é ímpar.', icon=":material/info:")





t3.subheader("```if…else``` Aninhado", anchor=False)

t3.write("A estrutura condicional **aninhada** pode receber mais de uma condição booleana (verdadeiro ou falso). Desta forma, o sistema verifica se as condições são verdadeiras e então executa os comandos de acordo com o resultado.")


t3.write("Sintaxe")

t3.text('''
if (condição 1)
{
    [se condição 1 verdadeira, executar este bloco de código]
}
else if (condição 2)
{
    [se condição 2 verdadeira, executar este bloco de código]
}
else if (condição n)
{
    [se condição n verdadeira, executar este bloco de código]
}
else
{
    [se condições acima falso, executar este bloco de código]
}
''')


cond2="images/if-else-aninhado.svg"
t3.image(cond2, caption= 'if...else aninhado', width=350)


t3.subheader("Exemplo", anchor=False)

t3.write("Com base no valor informado pelo usuário, o programa identifica se o valor é positivo, negativo ou zero.")

t3.write("Código:")

code = '''
#include <iostream>
using namespace std;

int main()
{
  int Num = 0;

  cout << "Digite um número: ";
  cin >> Num;

  if (Num > 0)
  {
    cout << "Positivo" << endl;
  }
  else if (Num < 0)
  {
    cout << "Negativo" << endl;
  }
  else
  {
    cout << "Zero" << endl;
  }
}
'''
t3.code(code, language="cpp")

t3.write('Saída 1:')

t3.text('''
Digite um número: 2
Positivo
''')

t3.write('Saída 2:')

t3.text('''
Digite um número: -3
Negativo
''')

t3.write('Saída 3:')

t3.text('''
Digite um número: 0
Zero
''')






t4.subheader("```if``` de uma Linha", anchor=False)

t4.write("A estrutura condicional **simples** pode ser escrita em uma única linha de código.")


t4.write("Sintaxe")

t4.text('''
variável = (condição) ? expressão_verdadeira : expressão_falsa;
''')

t4.write("Veja abaixo a conversão do código if…else simples (exemplo 1) para o if de uma linha (exemplos 2 e 3).")


t4.subheader("Exemplo 1", anchor=False)

t4.write("Código: **if…else simples**.")

code = '''
#include <iostream>
using namespace std;

int main()
{
  int Num = 0;

  cout << "Digite um número: ";
  cin >> Num;

  if (Num % 2 == 0)
  {
    cout << "Par" << endl;
  }
  else
  {
    cout << "Ímpar" << endl;
  }
}
'''
t4.code(code, language="cpp")

t4.write('Saída:')

t4.text('''
Digite um número: 6
Par
''')



t4.subheader("Exemplo 2", anchor=False)

t4.write("Código: **if de uma linha** imprimindo resultado sem uso de variável.")

code = '''
#include <iostream>
using namespace std;

int main()
{
  int Num = 0;
  string Resultado;

  cout << "Digite um número: ";
  cin >> Num;

  Resultado = ((Num % 2 == 0) ? "Par" : "Ímpar");

  cout << Resultado;
}
'''
t4.code(code, language="cpp")

t4.write('Saída:')

t4.text('''
Digite um número: 6
Par
''')



t4.subheader("Exemplo 3", anchor=False)

t4.write("Código: if de uma linha imprimindo resultado sem uso de variável")

code = '''
#include <iostream>
using namespace std;

int main()
{
  int Num = 0;

  cout << "Digite um número: ";
  cin >> Num;

  cout << ((Num % 2 == 0) ? "Par" : "Ímpar");
}
'''
t4.code(code, language="cpp")

t4.write('Saída:')

t4.text('''
Digite um número: 7
Ímpar
''')




t5.subheader("```switch```", anchor=False)

t5.write("Com base no valor da variável que o ```switch``` recebe, um ou mais casos são executados.")


t5.write("Sintaxe")

t5.text('''
switch (variável)
{
  case valor_1:
    Instruções;
    break;

  case valor_2:
    Instruções;
    break;

  case valor_n:
    Instruções;
    break;

  default:
    Instruções;
}
''')


cond3="images/switch.svg"
t5.image(cond3, caption= 'switch', width=350)
