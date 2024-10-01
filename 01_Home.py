# Home
import streamlit as st

st.set_page_config(
    page_title=":house: Home",
    page_icon="https://github.com/lineulimasjc/praticarprogramacao/blob/main/images/logo.png",
    layout="centered",
    initial_sidebar_state="auto",
)

st.title(':house: Home')

st.header("Linguagem C++")

st.subheader("Explore os tópicos de programação em C++")






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
