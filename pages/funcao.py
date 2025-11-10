import streamlit as st

st.title("O que é uma função?")

st.write("Uma **função** é um **bloco de código** que **executa uma determinada operação**. O objetivo da função é **dividir tarefas complexas em tarefas menores**.")

st.write("Uma **função** pode **receber um ou mais parâmetros** e pode também **retornar um valor**.")

st.write("Sintaxe:")

st.text('''
tipo_do_retorno nomeDaFuncao( lista de parâmetros )
{
    // bloco de código
}
''')

st.subheader("Função Sem Retorno e Sem Parâmetro")

st.write("Exemplo:")

st.write("A função **exibirMensagem não recebe parâmetro** e também **não tem retorno**. Para deixar explícito que a função não tem retorno e nem recebe parâmetros, usa-se a palavra ```void``` (que significa **nada**).")

st.write("Código:")

code = '''
#include <iostream>
using namespace std;

// função exibirMensagem
void exibirMensagem(void)
{
  cout << "Bom estudo!" << endl;
}

int main()
{
  exibirMensagem(); // chamando a função
}
'''
st.code(code, language="cpp")

st.write('Saída:')

st.text('''
Bom estudo!
''')

st.divider()

st.subheader("Função Sem Retorno e Com Parâmetro(s)")

st.write("Exemplo:")

st.write("Neste outro exemplo, a função ```exibirMensagem``` recebe um parâmetro** (horas do tipo ```int```) e **não tem retorno**. Com base no valor da variável ```Horas```, uma mensagem será impressa na tela.")

st.write("Código:")

code = '''
#include <iostream>
using namespace std;

// função exibirMensagem
void exibirMensagem(int Horas)
{
  if (Horas < 12)
  {
    cout << "Bom dia!" << endl;
  }
  else if (Horas < 18)
  {
    cout << "Boa tarde!" << endl;
  }
  else
  {
    cout << "Boa noite!" << endl;
  }
}

int main()
{
  int Horario = 0;

  cout << "Digite somente o valor da hora: ";
  cin >> Horario;

  exibirMensagem(Horario); // chamando a função
}
'''
st.code(code, language="cpp")

st.write('Saída:')

st.text('''
Digite somente o valor da hora: 11
Bom dia!
''')


st.divider()

st.subheader("Função Com Retorno e Com Parâmetro(s)")

st.write("A função **calculaSoma recebe dois parâmetros** (```Valor1``` e ```Valor2```, ambas do tipo ```double```) e tem **retorno** do tipo ```double```.")

st.write("Código:")

code = '''
#include <iostream>
using namespace std;

// função calculaSoma
double calculaSoma(double Valor1, double Valor2)
{
  return Valor1 + Valor2;
}

int main()
{
  double Val1 = 0;
  double Val2 = 0;
  double Resultado = 0;

  cout << "Digite valor 1: ";
  cin >> Val1;

  cout << "Digite valor 2: ";
  cin >> Val2;

  // dResultado recebe o retorno da chamada da função
  Resultado = calculaSoma(Val1, Val2);

  cout << "Resultado = " << Resultado << endl;
}
'''
st.code(code, language="cpp")

st.write('Saída:')

st.text('''
Digite valor 1: 1.2
Digite valor 2: 2.3
Resultado = 3.5
''')






# Adiciona um link para o quiz


st.markdown("[Abra o quiz online clicando aqui](https://praticarprogramacao.streamlit.app/quiz)")

#st.markdown("[Abra o quiz online clicando aqui](http://localhost:8502/quiz)")

