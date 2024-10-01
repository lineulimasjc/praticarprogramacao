# Saída de Dados
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Saída de Dados",
    page_icon="images/logo.png",
    layout="centered",
    initial_sidebar_state="auto",
)

st.title("Saída de Dados")

st.write(":white_medium_square: 2.1 Comando cout")
st.write(":white_medium_square: 2.2 Pulando Linha")
st.write(":white_medium_square: 2.3 Operadores Arirméticos")



st.header(':arrow_forward: 2.1 Comando `cout`')
# st.header('Comando `cout`')

st.divider()

# st.header('My header')
# st.subheader('My sub')

# st.write('Comando cout')

# inline code `code`

st.write('O `cout` é um comando de saída de dados, usado para imprimir mensagens na tela. Veja alguns exemplos a seguir.')

st.subheader('Exemplo 1')


code = '''
#include <iostream>
using namespace std;

int main()
{
    cout << "Nome: " << "Julia" << endl;
    cout << "Idade: " << 21 << endl;
}
'''
st.code(code, language="cpp")

st.write('Saída:')



st.text('''
Nome: Julia
Idade: 21
''')


st.divider()


st.subheader('Exemplo 2')


code = '''
#include <iostream>
using namespace std;

int main()
{
  cout << "1. Saldo" << endl;
  cout << "2. Extrato" << endl;
  cout << "3. Sair" << endl;
}
'''
st.code(code, language="cpp")

st.write('Saída:')



st.text('''
1. Saldo
2. Extrato
3. Sair
''')






st.write("###")


# ----- Pulando Linha -----

st.header(':arrow_forward: 2.2 Pulando Linha')

st.divider()

st.write('Existem 2 formas de pular linha na linguagem C++:')

st.write(':white_medium_square: `endl`')
st.write(':white_medium_square: `\\n`')



st.write('Veja exemplos a seguir:')

st.header('Exemplo 1: endl')


st.write('Código')


code = '''
#include <iostream>
using namespace std;

int main()
{
    cout << "Pulando linha" << endl;
  
    cout << "Pulando linha";
}
'''
st.code(code, language="cpp")

st.write('Saída:')





st.text('''
Pulando linha
Pulando linha
''')










st.write("###")


# ----- Operadores Aritméticos -----

st.header(":arrow_forward: 2.3 Operadores Aritméticos")

st.divider()


st.write("Os operadores aritméticos são fundamentais para a realização de cálculos matemáticos básicos dentro do código. Estes operadores permitem realizar operações como adição, subtração, multiplicação, divisão e obtenção do resto de uma divisão entre variáveis ou valores. Aqui está uma breve explicação dos principais operadores aritméticos em C++:")





df = pd.DataFrame({
  'Descrição': ['Adição', 'Subtração', 'Multiplicação', 'Divisão', 'Módulo'],
  'Operador': ['+', '-', '*', '/', '%'],
  'Exemplo': ['3 + 2', '5 - 3', '3 * 3', '10 / 2', '10 % 7'],
  'Resultado': ['5', '2', '9', '5', '3']
})

df



st.header("Exemplo de Adição (+)")


st.write("Código")


code = '''
#include <iostream>
using namespace std;
 
int main()
{
  cout << "5 + 3 = " << 5 + 3 << endl;
}
'''
st.code(code, language="cpp")

st.write('Saída:')



st.text('''
5 + 3 = 8
''')








st.header("Exemplo de Subtração (-)")


st.write("Código")


code = '''
#include <iostream>
using namespace std;
 
int main()
{
  cout << "8 - 2 = " << 8 - 2 << endl;
}
'''
st.code(code, language="cpp")

st.write('Saída:')



st.text('''
8 – 2 = 6
''')










st.header("Exemplo de Multiplicação (*)")


st.write("Código")


code = '''
#include <iostream>
using namespace std;
 
int main()
{
  cout << "8 * 4 = " << 8 * 4 << endl;
}
'''
st.code(code, language="cpp")

st.write('Saída:')



st.text('''
8 * 4 = 32
''')





st.header("Exemplo de Divisão (/)")


st.write("Código")


code = '''
#include <iostream>
using namespace std;
 
int main()
{
  cout << "15.6 / 3 = " << 15.6 / 3 << endl;
}
'''
st.code(code, language="cpp")

st.write('Saída:')



st.text('''
15.6 / 3 = 5.2
''')









st.header("Exemplo de Módulo (%)")


st.write("Código")


code = '''
#include <iostream>
using namespace std;
 
int main()
{
  cout << 15 / 7 << " semana(s) e ";

  cout << 15 % 7 << " dia(s)." << endl;
}
'''
st.code(code, language="cpp")

st.write('Saída:')



st.text('''
2 semana(s) e 1 dia(s).
''')













# ----- Footer implementation -----
footer = """
<style>
.footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    background-color: #f0f2f6;
    color: #31333f;;
    text-align: center;
}
</style>
<div class='footer'>
  <p>Praticar Programação ©</p>
</div>
"""
st.markdown(footer, unsafe_allow_html=True)
