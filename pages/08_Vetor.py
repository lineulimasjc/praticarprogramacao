# Vetor

import streamlit as st

st.title("Vetor")





















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
