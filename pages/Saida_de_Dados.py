import streamlit as st

st.title("Saída de Dados")


t1, t2, t3 = st.tabs(["Comando ```cout```", "Pulando Linha", "Operadores Arirméticos"])


t1.write('O `cout` é um comando de saída de dados, usado para imprimir mensagens na tela. Veja alguns exemplos a seguir.')

t1.subheader('Exemplo 1')


code = '''
#include <iostream>
using namespace std;

int main()
{
    cout << "Nome: " << "Julia" << endl;
    cout << "Idade: " << 21 << endl;
}
'''
t1.code(code, language="cpp")

t1.write('Saída:')


t1.text('''
Nome: Julia
Idade: 21
''')




t1.divider()




t1.subheader('Exemplo 2')


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
t1.code(code, language="cpp")

t1.write('Saída:')



t1.text('''
1. Saldo
2. Extrato
3. Sair
''')




t2.write('Existem 2 formas de pular linha na linguagem C++:')

t2.write(':white_medium_square: `endl`')
t2.write(':white_medium_square: `\\n`')



t2.write('Veja exemplos a seguir:')


t2.header('Exemplo 1: ```endl```')

t2.write('Código')


code = '''
#include <iostream>
using namespace std;

int main()
{
    cout << "Pulando linha" << endl;
  
    cout << "Pulando linha";
}
'''
t2.code(code, language="cpp")

t2.write('Saída:')





t2.text('''
Pulando linha
Pulando linha
''')



t2.header('Exemplo 2: ```\\n```')

t2.write('Código')


code = '''
#include <iostream>

using namespace std;

int main()
{
  cout << "Pulando linha\\n";
  
  cout << "Pulando linha";
}
'''
t2.code(code, language="cpp")

t2.write('Saída:')




t2.text('''
Pulando linha
Pulando linha
''')




t3.write("Os operadores aritméticos são fundamentais para a realização de cálculos matemáticos básicos dentro do código. Estes operadores permitem realizar operações como **adição, subtração, multiplicação, divisão** e obtenção do **resto** de uma divisão entre variáveis ou valores. Aqui está uma breve explicação dos principais operadores aritméticos em C++:")




t3.markdown("""
| Descrição     | Operador | Exemplo | Resultado |
| ------------- | -------- | ------- | --------- |
| Adição        |     +    |  3 + 2  |     5     |
| Subtração     |     -    |  5 - 3  |     2     |
| Multiplicação |     *    |  3 * 3  |     9     |
| Divisão       |     /    |  10 / 2 |     5     |
| Módulo        |     %    |  10 % 7 |     3     |
""")


t3.header("Exemplo de Adição (+)")


t3.write("Código")


code = '''
#include <iostream>
using namespace std;
 
int main()
{
  cout << "5 + 3 = " << 5 + 3 << endl;
}
'''
t3.code(code, language="cpp")

t3.write('Saída:')



t3.text('''
5 + 3 = 8
''')








t3.header("Exemplo de Subtração (-)")


t3.write("Código")


code = '''
#include <iostream>
using namespace std;
 
int main()
{
  cout << "8 - 2 = " << 8 - 2 << endl;
}
'''
t3.code(code, language="cpp")

t3.write('Saída:')



t3.text('''
8 – 2 = 6
''')










t3.header("Exemplo de Multiplicação (*)")


t3.write("Código")


code = '''
#include <iostream>
using namespace std;
 
int main()
{
  cout << "8 * 4 = " << 8 * 4 << endl;
}
'''
t3.code(code, language="cpp")

t3.write('Saída:')



t3.text('''
8 * 4 = 32
''')





t3.header("Exemplo de Divisão (/)")


t3.write("Código")


code = '''
#include <iostream>
using namespace std;
 
int main()
{
  cout << "15.6 / 3 = " << 15.6 / 3 << endl;
}
'''
t3.code(code, language="cpp")

t3.write('Saída:')



t3.text('''
15.6 / 3 = 5.2
''')









t3.header("Exemplo de Módulo (%)")

t3.write("Código")


code = '''
#include <iostream>
using namespace std;
 
int main()
{
  cout << 15 / 7 << " semana(s) e ";

  cout << 15 % 7 << " dia(s)." << endl;
}
'''
t3.code(code, language="cpp")

t3.write('Saída:')



t3.text('''
2 semana(s) e 1 dia(s).
''')
