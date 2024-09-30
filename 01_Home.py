# Home
import streamlit as st

# st.markdown(":page_facing_up: # Home")
# st.sidebar.markdown("# Home")

# st.set_page_config(page_title = "Document Chat", page_icon = " :dvd: ", layout = "wide")

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
