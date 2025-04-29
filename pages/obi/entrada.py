import streamlit as st

st.title("📌 Entrada de Dados", anchor=False)

st.subheader('📑 Entrada de dados em linhas separadas ou na mesma linha:', anchor=False)

st.write('🔹 Exemplo:')

code = '''
#include <iostream>
using namespace std;

int main()
{
    int A, B, C;



    cout << "Entrada de dados em linhas separadas:" << endl;

    cin >> A;
    cin >> B;
    cin >> C;


    cout << "\\nA = " << A << endl;
    cout << "B = " << B << endl;
    cout << "C = " << C << endl;


    /*******************************************************/


    cout << "\\nEntrada de dados na mesma linha:" << endl;

    cin >> A >> B >> C;


    cout << "\\nA = " << A << endl;
    cout << "B = " << B << endl;
    cout << "C = " << C << endl;

}
'''
st.code(code, language="cpp")