import streamlit as st

st.title("📌 Extraindo Dados de Strings", anchor=False)

st.subheader('📑 Extraindo Dados de Strings com `istringstream`', anchor=False)

st.write('🔹 Exemplo 1:')

code = '''
#include <iostream>
#include <sstream>
#include <string>
using namespace std;

int main()
{
    string data = "  12  34 56\t78\\n90";

    istringstream iss(data);

    int a, b, c, d, e;

    iss >> a >> b >> c >> d >> e;

    cout << "a: " << a << endl; // Saída: a: 12
    cout << "b: " << b << endl; // Saída: b: 34
    cout << "c: " << c << endl; // Saída: c: 56
    cout << "d: " << d << endl; // Saída: d: 78
    cout << "e: " << e << endl; // Saída: e: 90
}
'''
st.code(code, language="cpp")

st.write('**Explicação:**')

st.write('[1] O operador `>>` é o mesmo operador usado para ler dados de `cin` (o fluxo de entrada padrão). Quando usado com um `istringstream`, ele se comporta de maneira semelhante, mas em vez de ler da entrada do usuário, ele lê da `string` associada ao `istringstream`.')

st.write('[2] Por padrão, o operador `>>` ignora espaços em branco iniciais (espaços, tabulações, novas linhas) ao tentar ler um valor.')

st.write('[3] Ele então lê caracteres da `string` até encontrar outro espaço em branco ou até que a leitura falhe (por exemplo, tentar ler um caractere quando se espera um número).')

st.write('[4] O valor lido é então convertido para o tipo da variável para a qual está sendo extraído (por exemplo, `int`, `float`, `string`).')



st.divider()



st.write('🔹 Exemplo 2:')

code = '''
#include <iostream>
#include <sstream>
#include <string>

using namespace std;

int main()
{
    string data = "10 20 30 40";

    istringstream iss(data); // Cria um istringstream com a string "data"

    int num1, num2, num3, num4;

    iss >> num1 >> num2 >> num3 >> num4; // Extrai os inteiros da string

    cout << "num1: " << num1 << endl; // Imprime os inteiros
    cout << "num2: " << num2 << endl;
    cout << "num3: " << num3 << endl;
    cout << "num4: " << num4 << endl;
}
'''
st.code(code, language="cpp")
