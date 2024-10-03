# Laço de Repetição

import streamlit as st

st.set_page_config(
    page_title="Laço de Repetição",
    page_icon="images/logo.png",
    layout="centered",
    initial_sidebar_state="auto",
)

st.title("Laço de Repetição")

t1, t2, t3, t4 = st.tabs(["Operadores de Incremento e Decremento", "```while```", "```do...while```", "```for```"])


t1.markdown("""
| Operador    | Exemplo     | Explicação                                                     |
| ----------- | ----------- | -------------------------------------------------------------- |
| ```++```    | ```cnt++``` | Usa o valor atual de ```cnt``` e incrementa ```cnt``` em 1.    |
| ```++```    | ```++cnt``` | Incrementa ```cnt``` em 1 e usa o novo valor.                  |
| ```--```    | ```cnt--``` | Usa o valor atual de ```cnt``` e decrementa ```cnt``` em 1.    |
| ```--```    | ```--cnt``` | Decrementa ```cnt``` em 1 e usa o novo valor.                  |
""")

t1.subheader("Pós-incremento (cnt++)")

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




t1.subheader("Pré-incremento (++cnt)")

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






t1.subheader("Pós-decremento (cnt−−)")

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





t1.subheader("Pré-decremento (−−cnt)")

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


# Adicionar o aqui aqui





# Footer implementation
footer = """
<style>
.footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    background-color: #f0f2f6;
    color: #31333f;
    text-align: center;
}
</style>
<div class='footer'>
  <p>Praticar Programação ©</p>
</div>
"""
st.markdown(footer, unsafe_allow_html=True)
