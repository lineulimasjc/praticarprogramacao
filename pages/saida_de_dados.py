import streamlit as st

st.title("📌 Saída de Dados", anchor=False)

st.subheader('1️⃣ Comando cout em C++')

st.write('O ```cout``` (**c**onsole **out**put) é usado para exibir mensagens e valores na tela. Ele faz parte da biblioteca ```iostream``` e pertence ao namespace ```std```.')

st.write('🔹 Exemplo 1:')

code = '''
#include <iostream>
using namespace std;

int main()
{
    cout << "Olá, mundo!";
}
'''
st.code(code, language="cpp")

st.write('Saída:')

code = '''
Olá, mundo!
'''
st.code(code, language="cpp")


st.divider()


st.subheader('2️⃣ Concatenando valores com ```cout```')

st.write('Podemos exibir múltiplos valores usando ```<<```:')

st.write('🔹 Exemplo 2:')

code = '''
#include <iostream>
using namespace std;

int main()
{
    int idade = 25;
    cout << "Minha idade é " << idade << " anos." << endl;
}
'''
st.code(code, language="cpp")

st.write('Saída:')

code = '''
Minha idade é 25 anos.
'''
st.code(code, language="cpp")





st.subheader('3️⃣ Desenvolvendo com Code::Blocks no Windows')

st.write('Para quem utiliza o **Code::Blocks**, o código abaixo já inclui a biblioteca necessária para exibir caracteres acentuados corretamente.')

st.write('🔹 Exemplo 3:')

code = '''
#include <iostream>
#include <locale.h>
using namespace std;

int main()
{
    // Variáveis


    setlocale(LC_ALL,"");
    system("color F1");

    // Código


}
'''
st.code(code, language="cpp")
