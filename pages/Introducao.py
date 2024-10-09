import streamlit as st


t1, t2, t3 = st.tabs(["Programação", "Linguagem", "IDE"])

t1.title('Programação Estruturada vs Orientada a Objetos')

t1.header("1. Programação Estruturada")

t1.write("**Programação Estruturada** é um método de desenvolvimento de programas. Este método usa três tipos de estruturas de controle.")

col1, col2, col3 = t1.columns(3)

with col1:
    t1.subheader("Sequência")
    t1.write("As instruções são executas de forma sequencial.")
    seq="images/sequencia.svg"
    t1.image(seq, caption= 'Sequência', width=200)
    
with col2:
    t1.subheader("Seleção")
    t1.write("As instruções são executadas com base em uma ou mais condições.")
    sel="images/selecao.svg"
    t1.image(sel, caption= 'Seleção', width=200)

with col3:
    t1.subheader("Repetição")
    t1.write("As instruções são executadas enquanto a condição for satisfeita.")
    rep="images/repeticao.svg"
    t1.image(rep, caption= 'Repetição', width=200)

t1.write("###")

t1.write("Exemplos:")

t1.markdown("- C")
t1.markdown("- C++")
t1.markdown("- Pascal")
t1.markdown("- Rust")

t1.divider()




t1.header("2. Programação Orientada a Objetos")

t1.write("**Programação Orientada a Objetos** é um método de desenvolvimento de programas. Este método é baseado no conceito de “**objetos**“. Os objetos podem conter **dados** e **códigos**.")

oop="images/orientacao-a-objetos.svg"
t1.image(oop, caption= 'Programação Orientada a Objetos', width=350)

t1.write("###")

t1.write("Exemplos:")

t1.markdown("- C++")
t1.markdown("- Python")
t1.markdown("- Java")





t2.title('Linguagem Compilada vs Interpretada')

t2.header("1. Linguagem Compilada")

t2.write("Na **linguagem compilada** o código fonte é convertido diretamente para a linguagem de máquina, para que o processador possa executar.")

t2.write("###")

t2.write("Exemplos:")

t2.markdown("- C/C++")
t2.markdown("- Pascal")
t2.markdown("- Rust")

t2.divider()

t2.header("1. Linguagem Interpretada")

t2.write("Na **linguagem interpretada** o código fonte é lido e executado linha por linha.")

t2.write("###")

t2.write("Exemplos:")

t2.markdown("- Python")
t2.markdown("- Javascript")
t2.markdown("- PHP")





t3.header("IDE")

t3.write("Uma **IDE** (Integrated Development Environment) é um editor de texto específico para escrita de código de programação. As IDEs oferecem benefícios aos desenvolvedores, otimizando o tempo de trabalho.")

t3.write("###")

t3.write("Exemplos:")

t3.markdown("- Code::Blocks")
t3.markdown("- Visual Studio Code")
