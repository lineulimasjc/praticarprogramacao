import streamlit as st
import base64

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


cond3="images/switch_sintaxe.svg"
t5.image(cond3, caption= 'switch', width=350)





t5.subheader("Exemplo 1", anchor=False)

t5.write("Exemplo do comando ```switch```.")

code = '''
#include <iostream>
using namespace std;

int main()
{
  int idioma = 0;

  cout << "1. Português" << endl;
  cout << "2. English" << endl;
  cout << "3. Español" << endl;

  cout << "Escolha: ";
  cin >> idioma;

  switch (idioma)
  {
  case 1:
    cout << "Bem-vindo!" << endl;
    break;
  case 2:
    cout << "Welcome!" << endl;
    break;
  case 3:
    cout << "Bienvenido!" << endl;
    break;
  default:
    cout << "Welcome!" << endl;
  }
}
'''
t5.code(code, language="cpp")

t5.write('Saída:')


switch1 = open("images/switch1.gif", "rb")
contents = switch1.read()
data_url = base64.b64encode(contents).decode("utf-8")
switch1.close()

t5.markdown(
    f'<img src="data:image/gif;base64,{data_url}" alt="switch">',
    unsafe_allow_html=True,
)





t5.subheader("Exemplo 2", anchor=False)

t5.write("Exemplo do comando ```switch``` sem ```default```.")

code = '''
#include <iostream>
using namespace std;

int main()
{
  int idioma = 0;

  cout << "1. Português" << endl;
  cout << "2. English" << endl;
  cout << "3. Español" << endl;

  cout << "Escolha: ";
  cin >> idioma;

  switch (idioma)
  {
  case 1:
    cout << "Bem-vindo!" << endl;
    break;
  case 2:
    cout << "Welcome!" << endl;
    break;
  case 3:
    cout << "Bienvenido!" << endl;
    break;
  default:
    cout << "Welcome!" << endl;
  }
}
'''
t5.code(code, language="cpp")

t5.write('Saída:')


switch2 = open("images/switch2.gif", "rb")
contents = switch2.read()
data_url = base64.b64encode(contents).decode("utf-8")
switch2.close()

t5.markdown(
    f'<img src="data:image/gif;base64,{data_url}" alt="switch">',
    unsafe_allow_html=True,
)





t5.subheader("Exemplo 3", anchor=False)

t5.write("Exemplo do comando ```switch``` sem ```break```.")

code = '''
#include <iostream>
using namespace std;

int main()
{
  int idioma = 0;

  cout << "1. Português" << endl;
  cout << "2. English" << endl;
  cout << "3. Español" << endl;

  cout << "Escolha: ";
  cin >> idioma;

  switch (idioma)
  {
    case 1:
      cout << "Bem-vindo!" << endl;
    case 2:
      cout << "Welcome!" << endl;
    case 3:
      cout << "Bienvenido!" << endl;
  }
}
'''
t5.code(code, language="cpp")

t5.write('Saída:')


switch3 = open("images/switch3.gif", "rb")
contents = switch3.read()
data_url = base64.b64encode(contents).decode("utf-8")
switch3.close()

t5.markdown(
    f'<img src="data:image/gif;base64,{data_url}" alt="switch">',
    unsafe_allow_html=True,
)





t5.subheader("Exemplo 4", anchor=False)

t5.write("Exemplo do comando ```switch``` usando tipo de dado ```char```.")

code = '''
#include <iostream>
using namespace std;

int main()
{
  char idioma;

  cout << "P. Português" << endl;
  cout << "E. English" << endl;
  cout << "S. Español" << endl;

  cout << "Escolha: ";
  cin >> idioma;

  switch (idioma)
  {
  case 'P':
    cout << "Bem-vindo!" << endl;
    break;
  case 'E':
    cout << "Welcome!" << endl;
    break;
  case 'S':
    cout << "Bienvenido!" << endl;
    break;
  default:
    cout << "Welcome!" << endl;
  }
}
'''
t5.code(code, language="cpp")

t5.write('Saída:')


switch4 = open("images/switch4.gif", "rb")
contents = switch4.read()
data_url = base64.b64encode(contents).decode("utf-8")
switch4.close()

t5.markdown(
    f'<img src="data:image/gif;base64,{data_url}" alt="switch">',
    unsafe_allow_html=True,
)



t5.subheader("Exemplo 5", anchor=False)

t5.write("Resolvendo o problema da entrada de dados com caracteres maiúsculo ou minúsculo.")

code = '''
#include <iostream>
using namespace std;

int main()
{
  char idioma;

  cout << "P. Português" << endl;
  cout << "E. English" << endl;
  cout << "S. Español" << endl;

  cout << "Escolha: ";
  cin >> idioma;

  switch (idioma)
  {
  case 'P':
  case 'p':
    cout << "Bem-vindo!" << endl;
    break;
  case 'E':
  case 'e':
    cout << "Welcome!" << endl;
    break;
  case 'S':
  case 's':
    cout << "Bienvenido!" << endl;
    break;
  default:
    cout << "Welcome!" << endl;
  }
}
'''
t5.code(code, language="cpp")

t5.write('Saída:')


switch5 = open("images/switch5.gif", "rb")
contents = switch5.read()
data_url = base64.b64encode(contents).decode("utf-8")
switch5.close()

t5.markdown(
    f'<img src="data:image/gif;base64,{data_url}" alt="switch">',
    unsafe_allow_html=True,
)








t6.subheader("Operadores Lógicos", anchor=False)

t6.write("Existem **3 operadores lógicos** na linguagem C++.")

t6.markdown("""
|    Nome    | Tradução |        Operador        |
|:----------:|:--------:|:----------------------:|
| AND Lógico |     E    |  ```and``` ou ```&&``` |
|  OR Lógico |    OU    | ```or``` ou ```\|\|``` |
| NOT Lógico |    NÃO   |  ```not``` ou ```!```  |
""")

t6.write("Veja a seguir a explicação sobre cada operador lógico e exemplos.")

t6.divider()

t6.subheader("```AND``` Lógico", anchor=False)

t6.write("Esta é a tabela verdade do ```AND``` Lógico.")


t6.markdown("""
| **Condição 1** | **Condição 2** | **Resultado** |
|:--------------:|:--------------:|:-------------:|
|   Verdadeiro   |   Verdadeiro   |   Verdadeiro  |
|   Verdadeiro   |      Falso     |     Falso     |
|      Falso     |   Verdadeiro   |     Falso     |
|      Falso     |      Falso     |     Falso     |
""")




t6.subheader("Exemplo 1", anchor=False)

t6.write("Neste exemplo é possível saber se o aluno foi aprovado ou reprovado. Caso a situação do aluno esteja como reprovado, não é possível saber se o aluno reprovou por nota ou frequência.")

code = '''
#include <iostream>
using namespace std;

int main()
{
  double Media = 0;
  int Frequencia = 0;

  cout << "Informe a Média: ";
  cin >> Media;

  cout << "Informe a Frequência: ";
  cin >> Frequencia;

  if (Media >= 6.0 and Frequencia >= 75)
  {
    cout << "Aprovado" << endl;
  }
  else
  {
    cout << "Média e/ou Frequência insuficiente" << endl;
  }
}
'''
t6.code(code, language="cpp")

t6.write('Saída 1:')

t6.text('''
Informe a Média: 8
Informe a Frequência: 90
Aprovado
''')

t6.write('Saída 2:')

t6.text('''
Informe a Média: 5
Informe a Frequência: 90
Média Global e/ou Frequência insuficiente
''')




t6.subheader("Exemplo 2", anchor=False)

t6.write("Neste exemplo é possível saber se o aluno foi aprovado ou reprovado. Caso a situação do aluno esteja como reprovado, é possível saber o motivo, pois o programa contempla a análise de todas as condições.")

code = '''
#include <iostream>
using namespace std;

int main()
{
  float Media;
  int Frequencia;

  cout << "Informe a Média: ";
  cin >> Media;

  cout << "Informe a Frequência: ";
  cin >> Frequencia;

  if (Media >= 6.0 and Frequencia >= 75)
  {
    cout << "Aprovado" << endl;
  }
  else if (Media < 6.0 and Frequencia >= 75)
  {
    cout << "Média abaixo de 6" << endl;
  }
  else if (Media >= 6.0 and Frequencia < 75)
  {
    cout << "Frequência abaixo de 75%" << endl;
  }
  else
  {
    cout << "Média e Frequência insuficiente" << endl;
  }
}
'''
t6.code(code, language="cpp")

t6.write('Saída 1:')

t6.text('''
Informe a Média Global: 5
Informe a Frequência: 90
Média Global abaixo de 6
''')

t6.write('Saída 2:')

t6.text('''
Informe a Média Global: 8
Informe a Frequência: 50
Frequência abaixo de 75%
''')



t6.divider()

t6.subheader("```OR``` Lógico", anchor=False)

t6.markdown("""
| **Condição 1** | **Condição 2** | **Resultado** |
|:--------------:|:--------------:|:-------------:|
|   Verdadeiro   |   Verdadeiro   |   Verdadeiro  |
|   Verdadeiro   |      Falso     |   Verdadeiro  |
|      Falso     |   Verdadeiro   |   Verdadeiro  |
|      Falso     |      Falso     |     Falso     |
""")



t6.subheader("Exemplo", anchor=False)

t6.write("No programa abaixo a entrada pode ser **minúscula** ou **maiúscula**.")

code = '''
#include <iostream>
using namespace std;

int main()
{
  char Opcao;

  cout << "Deseja jogar novamente S/N? -> ";
  cin >> Opcao;

  if (Opcao == 's' || Opcao == 'S')
  {
    cout << "O jogo recomeçará em breve!" << endl;
  }
  else
  {
    cout << "O jogo será encerrado!" << endl;
  }
}
'''
t6.code(code, language="cpp")

t6.write('Saída 1:')

t6.text('''
Deseja jogar novamente S/N? -> s
O jogo recomeçará em breve!
''')

t6.write('Saída 2:')

t6.text('''
Deseja jogar novamente S/N? -> S
O jogo recomeçará em breve!
''')






t6.divider()

t6.subheader("```NOT``` Lógico", anchor=False)

t6.markdown("""
| **Condição** | **Resultado** |
|:------------:|:-------------:|
|  Verdadeiro  |     Falso     |
|     Falso    |   Verdadeiro  |
""")



t6.subheader("Exemplo", anchor=False)

code = '''
#include <iostream>
using namespace std;

int main()
{
    int status = 0;

    cout << "0 - Desligado\\n1 - Ligado\\nStatus: ";
    cin >> status;

    // Se status NÃO for igual a 0 (zero)
    if (!(status == 0))
    {
        cout << "Ligado" << endl;
    }
    else
    {
        cout << "Desligado" << endl;
    }
}
'''
t6.code(code, language="cpp")

t6.write('Saída 1:')

t6.text('''
0 – Desligado
1 – Ligado
Status: 1
Ligado
''')

t6.write('Saída 2:')

t6.text('''
0 – Desligado
1 – Ligado
Status: 0
Desligado
''')

t6.info('Veja abaixo 2 formas diferentes de reescrever o código acima e obter a mesma saída.', icon=":material/info:")


t6.subheader("Exemplo 1", anchor=False)

code = '''
#include <iostream>
using namespace std;

int main()
{
    int status = 0;

    cout << "0 - Desligado\n1 - Ligado\nStatus: ";
    cin >> status;

    // Se status for diferente de 0 (zero)
    if (status != 0)
    {
        cout << "Ligado" << endl;
    }
    else
    {
        cout << "Desligado" << endl;
    }
}
'''
t6.code(code, language="cpp")

t6.write('Saída 1:')

t6.text('''
0 – Desligado
1 – Ligado
Status: 1
Ligado
''')

t6.write('Saída 2:')

t6.text('''
0 – Desligado
1 – Ligado
Status: 0
Desligado
''')



t6.subheader("Exemplo 2", anchor=False)

code = '''
#include <iostream>
using namespace std;

int main()
{
    int status = 0;

    cout << "0 - Desligado\\n1 - Ligado\\nStatus: ";
    cin >> status;

    // Se status for igual a 1 (um)
    if (status == 1)
    {
        cout << "Ligado" << endl;
    }
    else
    {
        cout << "Desligado" << endl;
    }
}
'''
t6.code(code, language="cpp")

t6.write('Saída 1:')

t6.text('''
0 – Desligado
1 – Ligado
Status: 1
Ligado
''')

t6.write('Saída 2:')

t6.text('''
0 – Desligado
1 – Ligado
Status: 0
Desligado
''')
