import streamlit as st

st.title("📌 Arrays Dinâmicos", anchor=False)

st.subheader('📑 Manipulando Arrays Dinâmicos:', anchor=False)

st.write('🔹 Exemplo 1:')

code = '''
#include <iostream>
#include <vector>     // Inclui a biblioteca vector para usar arrays dinâmicos (vetores).
using namespace std;

int main()
{
    vector<int> numeros; // Declara um vetor de inteiros chamado "numeros".

    int quantidade;
    int numero;

    cout << "Digite a quantidade de números a serem inseridos: ";
    cin >> quantidade;



    cout << "Digite os " << quantidade << " números:" << endl;



    // Loop para ler os números e adicioná-los ao vetor
    for (int i = 0; i < quantidade; ++i)
    {
        cin >> numero;              // Lê cada número do usuário.
        numeros.push_back(numero);  // Adiciona o número ao final do vetor.
    }



    // Acessa e imprime os elementos do vetor
    cout << "\\nNúmeros inseridos: ";

    for (int i = 0; i < numeros.size(); ++i)
    {
        cout << numeros[i] << " "; // Imprime cada número seguido de um espaço.
    }



    // Exemplo de uso do loop "for" com base em intervalo
    cout << "\\nNúmeros inseridos (usando range-based for): ";

    for (int num : numeros)
    {
        cout << num << " ";
    }
}
'''
st.code(code, language="cpp")


st.divider()



st.write('🔹 Exemplo 2:')

st.subheader('Lendo e armazenando dados de string em arrays dinâmicos usando `istringstream`.')

code = '''
#include <iostream>
#include <vector>    // Inclui a biblioteca vector para usar arrays dinâmicos (vetores).
#include <sstream>   // Inclui a biblioteca sstream para operações com string streams.
#include <string>    // Inclui a biblioteca string para trabalhar com strings.

using namespace std;

int main()
{
    string linha;

    vector<int> numbers;

    int n;

    getline(cin, linha);

    // Cria um string stream de entrada 'iss' inicializado com a string 'linha'.
    istringstream iss(linha);

    // Extrai inteiros de 'iss' e continua enquanto a extração for bem-sucedida.
    while (iss >> n)
    {
        numbers.push_back(n); // Adiciona o inteiro extraído 'n' ao final do vetor 'numbers'.
    }

    cout << "\\nValores informados: ";

    for (int num : numbers)   // Itera por cada inteiro 'num' no vetor 'numbers'.
    {
        cout << num << " ";
    }

    cout << "\\n";
}
'''
st.code(code, language="cpp")