# Variáveis
import streamlit as st



st.title("Variáveis")


st.write(":white_medium_square: 3.1 Introdução a Variáveis")
st.write(":white_medium_square: 3.2 Int")
st.write(":white_medium_square: 3.3 Double e float")
st.write(":white_medium_square: 3.4 Char")
st.write(":white_medium_square: 3.5 String")
st.write(":white_medium_square: 3.6 Bool")
st.write(":white_medium_square: 3.7 Regras de Nomenclatura")
# st.write(":white_medium_square: 3.8 Praticar")



st.write("###")

st.header(":arrow_forward: 3.1 Introdução a Variáveis")

st.subheader("Conceito de Variável")

st.write("Uma **variável** é uma posição denominada da memória onde um valor pode ser armazenado para ser utilizado pelo programa.")



st.write("As variáveis podem ser do tipo:")

st.write(":white_medium_square: ```int```")
st.write(":white_medium_square: ```double```")
st.write(":white_medium_square: ```float```")
st.write(":white_medium_square: ```string```")
st.write(":white_medium_square: ```char```")
st.write(":white_medium_square: ```bool```")

st.write("Declaração de Variável")

st.write("Para declarar uma variável, primeiro devemos definir o tipo e, logo em seguida, dar um nome a ela.")

st.write("Exemplo:")

code = '''
int Idade;

double Salario;

float Preco;

string Nome;
'''
st.code(code, language="cpp")


st.write("Atribuição de Valores")

code = '''
int Idade = 19;

double Salario = 1280;

float Preco = 5.99;

string Nome = "Maria";
'''
st.code(code, language="cpp")

st.write("É boa prática inicializar as variáveis numéricas igual a 0 (zero).")


code = '''
int Idade = 0;

double Salario = 0;

float Preco = 0;

string Nome;
'''
st.code(code, language="cpp")


st.write("As variáveis do tipo texto não precisam ser inicializadas.")

st.write("A definição de cada tipo de variável e exemplos serão apresentados a seguir.")






st.write("###")

st.header(":arrow_forward: 3.2 Int")

st.write("O tipo de dado ```int``` é utilizado para armazenar números inteiros, como **-7, 0, 33**. Ou seja, números sem parte decimal. Pode ser usado para armazenar **idade**, **quantidade**, **dia**, **mês**, etc.")


st.subheader('Exemplo')

st.write("Código")

code = '''
#include <iostream>
using namespace std;

int main()
{
  int Dia = 19;
  int Mes = 2;
  int Ano = 2020;

  cout << "Data: " << Dia << "/" << Mes << "/" << Ano << endl;
}
'''
st.code(code, language="cpp")

st.write('Saída:')


st.text('''
Data: 19/2/2020
''')




st.write("###")

st.header(":arrow_forward: 3.3 Double e float")

st.write("Esses tipos de dados armazenam números com ponto flutuante. O float e o double possuem algumas diferenças.")

st.write("```float``` – usa 4 bytes para armazenar dados")
st.write("```double``` – usa 8 bytes para armazenar dados")


st.subheader('Exemplo')


code = '''
#include <iostream>
#include <cmath>
using namespace std;

int main()
{
  float fPI = 3.14159265358979323846;
  
  double dPI = 3.14159265358979323846;

  cout << "PI como float: " << fPI << endl;

  cout << "PI como double: " << dPI << endl;
}
'''
st.code(code, language="cpp")

st.write('Saída:')


st.text('''
PI como float: 3.141593
PI como double: 3.141592653589793
''')





st.write("###")

st.header(":arrow_forward: 3.4 Char")



st.write("Um **caractere** pode ser qualquer número, letra ou símbolo.")

st.write("Esse tipo de dado pode armazenar um caractere ou um conjunto de caracteres (também chamado de string de caracteres).")

st.write("Um caractere é qualquer letra minúscula ou maiúscula (A, a, B, b, etc), número (1, 2, 3, etc) ou símbolo (+, *, @, etc).")

st.write("```char``` – armazena um caractere.")

st.write("```char[x]``` – armazena x caracteres, onde x pode ser qualquer valor numérico.")

st.write("Veja exemplos a seguir.")


st.subheader('Exemplo 1')

st.write("A variável cResposta armazena o caractere S e, em seguida, o dado é impresso na tela. Neste caso o dado deve estar entre aspas simples ( ‘ ‘).")

code = '''
#include <iostream>
using namespace std;

int main()
{
  char cResposta = 'S';

  cout << "Este é o caractere " << cResposta << "." << endl;
}
'''
st.code(code, language="cpp")

st.write('Saída:')


st.text('''
Este é o caractere S.
''')



st.subheader('Exemplo 2')

st.write("A variável cNome[8] (limitado a 8 caracteres) armazena o conjunto de caracteres Maria e, em seguida, o dado é impresso na tela. Neste caso o dado deve estar entre aspas duplas ( ” “).")

code = '''
#include <iostream>
using namespace std;

int main()
{
  char cNome[8] = "Maria";

  cout << "Nome: " << cNome << endl;
}
'''
st.code(code, language="cpp")

st.write('Saída:')


st.text('''
Nome: Maria
''')






st.write("###")

st.header(":arrow_forward: 3.5 String")

st.write("O tipo de dado string em C++ é utilizado para armazenar sequências de caracteres, ou seja, textos.")

# st.write(":warning: Caracteres são letras do alfabeto, números, sinais de pontuação, e símbolos, como @ ou #.")

st.warning(":warning: Caracteres são letras do alfabeto, números, sinais de pontuação, e símbolos, como @ ou #.")



st.subheader('Exemplo')

st.write("A variável sTexto armazena o conjunto de caracteres e, em seguida, o texto é impresso na tela. Neste caso o texto deve estar entre aspas duplas ( ” “).")

st.write('Código:')

code = '''
#include <iostream>
using namespace std;

int main()
{
  string Msg = "Resultado = ";

  cout << Msg << 10 + 2 << endl;
  
  cout << Msg << 10 - 2 << endl;
  
  cout << Msg << 10 * 2 << endl;
  
  cout << Msg << 10 / 2 << endl;
}
'''
st.code(code, language="cpp")


st.write('Saída:')

st.text('''
Resultado = 12

Resultado = 8

Resultado = 20

Resultado = 5
''')







st.write("###")

st.header(":arrow_forward: 3.6 Bool")


st.write("Um tipo de dado ```bool``` representa valores booleanos, ou seja, verdadeiro (```true```) ou falso (```false```), utilizado principalmente em operações lógicas e de controle de fluxo.")

st.write("O valor ```true``` é representado pelo número ```1``` e ```false``` pelo número ```0```.")


st.subheader('Exemplo')

st.write('Código:')

code = '''
#include <iostream>
using namespace std;

int main()
{
  bool x = true;
  bool y = false;

  cout << "x = " << x << endl;

  cout << "y = " << y << endl;
}
'''
st.code(code, language="cpp")


st.write('Saída:')

st.text('''
x = 1
y = 0
''')







st.write("###")

st.header(":arrow_forward: 3.7 Regras de Nomenclatura")



st.subheader("Regras de Nomenclatura")

st.write("Regras para nomear as variáveis")

st.divider()

st.subheader("Regra 1")

st.write("Primeiro caractere DEVE ser uma letra ou o caractere “_” sublinhado.")

st.write("Exemplos:")

st.write(":white_check_mark: **V**alor")
st.write(":white_check_mark: _valor")

st.divider()

st.subheader("Regra 2")

st.write("Pode conter letras **maiúsculas** ou **minúsculas**.")

st.write("Exemplos:")

st.write(":white_check_mark: QtdaProduto")
st.write(":white_check_mark: NomeCliente")

st.divider()

st.subheader("Regra 3")

st.write("Pode conter numerais de 0 a 9, mas o primeiro caractere não pode ser um numeral.")

st.write("Exemplos:")

st.write(":white_check_mark: Num1")
st.write(":white_check_mark: Num2")

st.divider()

st.subheader("Regra 4")

st.write("Pode conter o caractere “_” **sublinhado**.")

st.write("Exemplos:")

st.write(":white_check_mark: Num_1")
st.write(":white_check_mark: Num_2")

st.divider()

st.subheader("Regra 5")

st.write("**NÃO** pode conter **acentuação**.")

st.write("Exemplos:")

st.write(":x: Preço")
st.write(":x: Número")

st.divider()

st.subheader("Regra 6")

st.write("**NÃO** pode conter **espaço em branco**.")

st.write("Exemplos:")

st.write(":x: Nome do Produto")
st.write(":x: Nota do Aluno")

st.divider()

st.subheader("Regra 7")

st.write("**NÃO** pode conter o mesmo nome de uma **palavra-chave**.")

st.write("Exemplos:")

st.write(":x: double")
st.write(":x: else")



# st.header(":arrow_forward: 3.8 Praticar")

# A Streamlit Quizz Template
# https://medium.com/@hugoalmeidamoreira/a-streamlit-quizz-template-505ae87c387f















