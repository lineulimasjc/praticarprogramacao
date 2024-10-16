import streamlit as st

st.title("O que são funções?")

st.write("Uma **função** é um **bloco de código** que **executa uma determinada operação**. O objetivo da função é **dividir tarefas complexas em tarefas menores**.")

st.write("Uma **função** pode **receber um ou mais parâmetros** e pode também **retornar um valor**.")

st.write("Sintaxe:")

st.text('''
tipo_do_retorno nomeDaFuncao( lista de parâmetros )
{
    // bloco de código
}
''')

st.subheader("Funções Sem Retorno e Sem Parâmetro")

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

st.subheader("Funções Sem Retorno e Com Parâmetro(s)")

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

st.subheader("Funções Com Retorno e Com Parâmetro(s)")

