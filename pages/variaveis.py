import streamlit as st

st.title("📌 Variáveis", anchor=False)


st.header("1️⃣ Principais Tipos de Variáveis", anchor=False)


st.divider()


st.write('Em C++, **variáveis** armazenam valores e possuem **tipos específicos**. Aqui estão os mais comuns:')


st.write("###")


st.write('🔹 ```int``` (Inteiro) – Armazena números inteiros (positivos ou negativos).')

code = '''
int idade = 25;
'''
st.code(code, language="cpp")


st.write("###")


st.write('🔹 ```float``` **(Ponto Flutuante Simples)** – Armazena números decimais com **precisão menor** (aprox. 6-7 dígitos).')

code = '''
float preco = 19.99;
'''
st.code(code, language="cpp")


st.write("###")


st.write('🔹 ```double``` **(Ponto Flutuante Duplo)** – Semelhante ao ```float```, mas com **maior precisão** (aprox. 15-16 dígitos).')

code = '''
double pi = 3.1415926535;
'''
st.code(code, language="cpp")


st.write("###")


st.write('🔹 ```char``` **(Caractere Único)** – Armazena um único caractere, sempre entre **aspas simples** (' ').')

code = '''
char letra = 'A';
'''
st.code(code, language="cpp")


st.write("###")


st.write('🔹 ```string``` **(Texto)** – Armazena uma sequência de caracteres (palavras/frases), usada com a biblioteca ```<string>```.')

code = '''
#include <string>

string nome = "Alice";
'''
st.code(code, language="cpp")


st.write("###")


st.write('🔹 ```bool``` **(Booleano)** – Armazena apenas ```true``` (1) ou ```false``` (0).')

code = '''
bool ativo = true;
'''
st.code(code, language="cpp")


st.write("###")


st.write('📌 Resumo: Cada tipo de variável é usado conforme a necessidade do programa. 🚀')


st.write("###")


st.header("2️⃣ Exemplo com os diferentes tipos de variáveis", anchor=False)


st.write('🔹 Aqui está um exemplo prático que demonstra o uso de diferentes tipos de variáveis em C++:')


code = '''
#include <iostream>
#include <string> // Necessário para usar strings
using namespace std;

int main() {
    int idade = 25;             // Inteiro
    float altura = 1.75;        // Ponto flutuante (menos precisão)
    double pi = 3.1415926535;   // Ponto flutuante (mais precisão)
    char inicial = 'A';         // Caractere único
    string nome = "Carlos";     // Texto
    bool aprovado = true;       // Booleano (true ou false)

    // Exibindo os valores armazenados
    cout << "Nome: " << nome << endl;
    cout << "Idade: " << idade << endl;
    cout << "Altura: " << altura << "m" << endl;
    cout << "Valor de PI: " << pi << endl;
    cout << "Inicial do nome: " << inicial << endl;
    cout << "Aprovado? " << (aprovado ? "Sim" : "Não") << endl;
}
'''
st.code(code, language="cpp")

st.write('Saída:')

code = '''
Nome: Carlos  
Idade: 25  
Altura: 1.75m  
Valor de PI: 3.1415926535  
Inicial do nome: A  
Aprovado? Sim  
'''
st.code(code, language="cpp")


st.write("###")


st.header("3️⃣ Mais exemplos de variáveis", anchor=False)


st.write("###")


st.header("👉 Int", anchor=False)

# st.write("O tipo de dado ```int``` é utilizado para armazenar números inteiros, como **-7, 0, 33**. Ou seja, números sem parte decimal. Pode ser usado para armazenar **idade**, **quantidade**, **dia**, **mês**, etc.")


st.subheader('Exemplo:')

#st.write("Código")

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


code = '''
Data: 19/2/2020
'''
st.code(code, language="cpp")





st.write("###")

st.header("👉 Double e float", anchor=False)

#st.write("Esses tipos de dados armazenam números com ponto flutuante. O float e o double possuem algumas diferenças.")

#st.write("```float``` – usa 4 bytes para armazenar dados")
#st.write("```double``` – usa 8 bytes para armazenar dados")


st.subheader('Exemplo:', anchor=False)


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


code = '''
PI como float: 3.141593
PI como double: 3.141592653589793
'''
st.code(code, language="cpp")







st.write("###")

st.header("👉 Char", anchor=False)



#st.write("Um **caractere** pode ser qualquer número, letra ou símbolo.")

#st.write("Esse tipo de dado pode armazenar um caractere ou um conjunto de caracteres (também chamado de string de caracteres).")

#st.write("Um caractere é qualquer letra minúscula ou maiúscula (A, a, B, b, etc), número (1, 2, 3, etc) ou símbolo (+, *, @, etc).")

#st.write("```char``` – armazena um caractere.")

#st.write("```char[x]``` – armazena x caracteres, onde x pode ser qualquer valor numérico.")

#st.write("Veja exemplos a seguir.")


st.subheader('Exemplo:', anchor=False)

#st.write("A variável cResposta armazena o caractere S e, em seguida, o dado é impresso na tela. Neste caso o dado deve estar entre aspas simples ( ‘ ‘).")

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


code = '''
Este é o caractere S.
'''
st.code(code, language="cpp")









st.write("###")

st.header("👉 String", anchor=False)

#st.write("O tipo de dado string em C++ é utilizado para armazenar sequências de caracteres, ou seja, textos.")

#st.warning(":warning: Caracteres são letras do alfabeto, números, sinais de pontuação, e símbolos, como @ ou #.")



st.subheader('Exemplo:', anchor=False)

#st.write("A variável sTexto armazena o conjunto de caracteres e, em seguida, o texto é impresso na tela. Neste caso o texto deve estar entre aspas duplas ( ” “).")

#st.write('Código:')

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

code = '''
Resultado = 12

Resultado = 8

Resultado = 20

Resultado = 5
'''
st.code(code, language="cpp")









st.write("###")

st.header("👉 Bool", anchor=False)


#st.write("Um tipo de dado ```bool``` representa valores booleanos, ou seja, verdadeiro (```true```) ou falso (```false```), utilizado principalmente em operações lógicas e de controle de fluxo.")

#st.write("O valor ```true``` é representado pelo número ```1``` e ```false``` pelo número ```0```.")


st.subheader('Exemplo:', anchor=False)

#st.write('Código:')

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

code = '''
x = 1
y = 0
'''
st.code(code, language="cpp")









st.write("###")

st.header("4️⃣ Regras de Nomenclatura", anchor=False)


st.write("Regras para nomear as variáveis.")


st.divider()


st.subheader("Regra 1", anchor=False)

st.write("Primeiro caractere DEVE ser uma letra ou o caractere “_” sublinhado.")

st.write("Exemplos:")

st.write(":white_check_mark: **V**alor")
st.write(":white_check_mark: _valor")


st.divider()


st.subheader("Regra 2", anchor=False)

st.write("Pode conter letras **maiúsculas** ou **minúsculas**.")

st.write("Exemplos:")

st.write(":white_check_mark: QtdaProduto")
st.write(":white_check_mark: NomeCliente")


st.divider()


st.subheader("Regra 3", anchor=False)

st.write("Pode conter numerais de 0 a 9, mas o primeiro caractere não pode ser um numeral.")

st.write("Exemplos:")

st.write(":white_check_mark: Num1")
st.write(":white_check_mark: Num2")


st.divider()


st.subheader("Regra 4", anchor=False)

st.write("Pode conter o caractere “_” **sublinhado**.")

st.write("Exemplos:")

st.write(":white_check_mark: Num_1")
st.write(":white_check_mark: Num_2")


st.divider()


st.subheader("Regra 5", anchor=False)

st.write("**NÃO** pode conter **acentuação**.")

st.write("Exemplos:")

st.write(":x: Preço")
st.write(":x: Número")


st.divider()


st.subheader("Regra 6", anchor=False)

st.write("**NÃO** pode conter **espaço em branco**.")

st.write("Exemplos:")

st.write(":x: Nome do Produto")
st.write(":x: Nota do Aluno")


st.divider()


st.subheader("Regra 7", anchor=False)

st.write("**NÃO** pode conter o mesmo nome de uma **palavra-chave**.")

st.write("Exemplos:")

st.write(":x: double")
st.write(":x: else")



# st.header("3.8 Praticar")

# A Streamlit Quizz Template
# https://medium.com/@hugoalmeidamoreira/a-streamlit-quizz-template-505ae87c387f
