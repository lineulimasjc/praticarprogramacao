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
