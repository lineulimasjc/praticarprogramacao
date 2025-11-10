import streamlit as st
import random


# Dados das perguntas (com código C++ no enunciado)
perguntas = [
    {
        "numero": 1,
        "enunciado": "Qual é a saída do seguinte código C++?",
        "codigo": '''
        #include <iostream>
        using namespace std;

        void fn() {
            cout << "Bem-vindo ao estudo de funções em C++!" << endl;
        }

        int main() {
            fn();
        }
        ''',
        "alternativas": ["A) Bem-vindo ao estudo de funções em C++!", "B) Erro de compilação", "C) Nada é impresso", "D) main() não pode chamar funções"],
        "resposta_correta": "A"
    },
    {
        "numero": 2,
        "enunciado": "Qual é a saída do seguinte código C++?",
        "codigo": '''
        #include <iostream>
        using namespace std;

        void fn(int num) {
            cout << num << endl;
        }

        int main() {
            fn(42);
        }
        ''',
        "alternativas": ["A) 42", "B) Erro de compilação", "C) Nenhuma saída, pois a função não imprime nada.", "D) 0"],
        "resposta_correta": "A"
    },
    {
        "numero": 3,
        "enunciado": "Qual é a saída do seguinte código C++?",
        "codigo": '''
        #include <iostream>
        using namespace std;

        int fn(int a, int b) {
            return a + b;
        }

        int main() {
            int resultado = fn(10, 5);
            cout << "Resultado: " << resultado << endl;
        }
        ''',
        "alternativas": [
        "A) Resultado: 15",
        "B) Resultado: 105",
        "C) Erro de compilação",
        "D) Nenhuma saída"
        ],
        "resposta_correta": "A"
    },
]


# Inicializa o estado da sessão para armazenar alternativas embaralhadas
if 'alternativas_misturadas' not in st.session_state:
    st.session_state.alternativas_misturadas = {}
    for pergunta in perguntas:
        alternativas_misturadas = pergunta['alternativas'][:]
        random.shuffle(alternativas_misturadas)
        # Remove a letra inicial de cada alternativa
        alternativas_sem_letra = [alt.split(')', 1)[1].strip() for alt in alternativas_misturadas]
        st.session_state.alternativas_misturadas[pergunta['numero']] = alternativas_sem_letra


# Interface do quiz
st.title("Quiz", anchor=False)

for pergunta in perguntas:
    st.subheader(f"{pergunta['numero']}: {pergunta['enunciado']}", anchor=False)
    st.code(pergunta['codigo'], language='cpp')
    
    # Usa as alternativas embaralhadas sem letras iniciais do estado da sessão
    alternativas_misturadas = st.session_state.alternativas_misturadas[pergunta['numero']]
    resposta = st.radio("Escolha uma alternativa:", alternativas_misturadas, key=pergunta['numero'], index=None)
    if st.button(f"Enviar resposta {pergunta['numero']}"):
        # Recupera a letra correta da alternativa original
        alternativa_correta = next(alt for alt in pergunta['alternativas'] if alt.startswith(pergunta['resposta_correta']))
        alternativa_correta_texto = alternativa_correta.split(')', 1)[1].strip()
        if resposta == alternativa_correta_texto:
            st.success("Resposta correta!")
        else:
            st.error(f"Resposta errada. Tente novamente!")

st.write("Parabéns por estar estudando programação!")
