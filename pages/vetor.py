import streamlit as st

st.title("O que um vetor?")

st.write("**Vetor** é uma estrutura de dados que armazena uma determinada quantidade de elementos do mesmo tipo.")

st.write("Sintaxe:")

st.text('''
tipo-de-dado NomeVetor[n];
''')

st.write("Podemos dizer que um vetor nada mais é que uma lista de valores.")

st.write("Os valores armazenados em um vetor são chamados de **elementos**.")

st.write("Para acessar os elementos de uma vetor, usamos os **índices** das posições.")

st.subheader("Declarando Vetores")

st.write("Exemplo 1")

st.write("O vetor ```Numeros``` do tipo ```int``` é declarado e 3 valores são atribuídos ao vetor. Em seguida, os valores são impressos na tela.")

st.write("Codigo:")

code = '''
#include <iostream>
using namespace std;

int main()
{
  // Declarando o vetor e atribuíndo 3 elementos
  int Numeros[3] = {10, 20, 30};

  int i;

  cout << "Elementos do vetor: " << endl;

  // Imprimindo os elementos do vetor
  for(i = 0; i < 3; i++)
  {
    cout << Numeros[i] << "\t";
  }
}
'''
st.code(code, language="cpp")

st.write('Saída:')

st.text('''
Elementos do vetor:
10 20 30
''')

st.divider()






st.write("Exemplo 2")

st.write("O vetor ```Numeros``` do tipo ```int``` é declarado. A entrada de dados é feita pelo usuário. Em seguida, os valores são impressos na tela.")

st.write("Codigo:")

code = '''
#include <iostream>
using namespace std;

int main()
{
  // Declarando o vetor e atribuíndo 3 elementos
  int Numeros[3];

  int i;

  // Atribuindo elementos ao vetor
  for(i = 0; i < 3; i++)
  {
    cout << "Informe valor " << i + 1 << ": ";
    cin >> Numeros[i];
  }

  cout << "Elementos do vetor: " << endl;

  // Imprimindo os elementos do vetor
  for(i = 0; i < 3; i++)
  {
    cout << Numeros[i] << "\t";
  }
}
'''
st.code(code, language="cpp")

st.write('Saída:')

st.text('''
Informe valor 1: 5
Informe valor 2: 10
Informe valor 3: 15
Elementos do vetor:
5 10 15
''')

st.divider()




st.write("Exemplo 3")

st.write("O vetor ```Numeros``` do tipo ```double``` é declarado. A entrada de dados é feita pelo usuário. Em seguida, os valores são impressos na tela.")

st.write("Codigo:")

code = '''
#include <iostream>
using namespace std;

int main()
{
  // Declarando o vetor
  double Numeros[3];

  int i;

  // Atribuindo elementos ao vetor
  for(i = 0; i < 3; i++)
  {
    cout << "Informe valor " << i + 1 << ": ";
    cin >> Numeros[i];
  }

  cout << "Elementos do vetor: " << endl;

  // Imprimindo os elementos do vetor
  for(i = 0; i < 3; i++)
  {
    cout << Numeros[i] << "\t";
  }
}
'''
st.code(code, language="cpp")

st.write('Saída:')

st.text('''
Informe valor 1: 2.3
Informe valor 2: 5.1
Informe valor 3: 6.9
Elementos do vetor:
2.3 5.1 6.9
''')

st.divider()





st.write("Exemplo 4")

st.write("O vetor ```Palavras``` do tipo ```string``` é declarado. As palavras são informadas pelo usuário. Em seguida, as palavras são impressas na tela.")

st.write("Codigo:")

code = '''
#include <iostream>
using namespace std;

int main()
{
  // Declarando o vetor
  string Palavras[3];

  int i;

  // Atribuíndo elementos ao vetor
  for(i = 0; i < 3; i++)
  {
    cout << "Informe palavra " << i + 1 << ": ";
    cin >> Palavras[i];
  }

  cout << "\nPalavras do vetor: " << endl;

  // Imprimindo os elementos do vetor
  for(i = 0; i < 3; i++)
  {
    cout << Palavras[i] << endl;
  }
}
'''
st.code(code, language="cpp")

st.write('Saída:')

st.text('''
Informe palavra 1: Morango
Informe palavra 2: Banana
Informe palavra 3: Pera

Palavras do vetor:
Morango
Banana
Pera
''')

st.divider()




st.subheader("Manipulando Vetores")

st.write("É possível fazer várias operações com vetores, como::")

st.markdown("- Soma")
st.markdown("- Média")
st.markdown("- Identificar o maior ou menor valor")
st.markdown("- Contar elementos com base em uma condição")





st.write("Exemplo 1")

st.write("Calculando a **soma** dos elementos do vetor.")

st.write("Codigo:")

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

  // Imprime a soma dos elementos do vetor
  cout << "\nSoma: " << Soma << endl;
}
'''
st.code(code, language="cpp")

st.write('Saída:')

st.text('''
Informe valor 1: 6.5
Informe valor 2: 7.5
Informe valor 3: 8.5

Soma: 22.5
''')

st.divider()




st.write("Exemplo 2")

st.write("Calculando a **média** dos elementos do vetor.")

st.write("Codigo:")

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
Informe valor 1: 6.5
Informe valor 2: 7.5
Informe valor 3: 8.5

Média: 7.5
''')

st.divider()







st.write("Exemplo 3")

st.write("Identificando o **maior** elemento de um vetor.")

st.write("Codigo:")

code = '''
#include <iostream>
using namespace std;

int main()
{
  // Declarando o vetor
  int Numeros[3];

  int i, MaiorValor = 0;

  // Atribuindo elementos ao vetor
  for(i = 0; i < 3; i++)
  {
    cout << "Informe valor " << i + 1 << ": ";
    cin >> Numeros[i];
  }

  // Identificando maior elemento
  MaiorValor = Numeros[0];

  for(i = 1; i < 3; i++)
  {
    if (MaiorValor < Numeros[i])
    {
      MaiorValor = Numeros[i];
    }
  }
  cout << "Maior elemento: " << MaiorValor << endl;
}
'''
st.code(code, language="cpp")

st.write('Saída:')

st.text('''
Informe valor 1: 3
Informe valor 2: 6
Informe valor 3: 1
Maior elemento: 6
''')

st.divider()




st.write("Exemplo 4")

st.write("**Contando** a quantidade de elementos pares e ímpares do vetor.")

st.write("Codigo:")

code = '''
#include <iostream>
using namespace std;

int main()
{
  // Declarando o vetor
  int Numeros[3];

  int i, ContaPar = 0, ContaImpar = 0;

  // Atribuindo elementos ao vetor
  for(i = 0; i < 3; i++)
  {
    cout << "Informe valor " << i + 1 << ": ";
    cin >> Numeros[i];
  }

  // Contando elementos pares e ímpares do vetor
  for(i = 0; i < 3; i++)
  {
    if (Numeros[i] % 2 == 0)
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
Informe valor 1: 1
Informe valor 2: 2
Informe valor 3: 3
Par: 1
Ímpar: 2
''')
