# Home
import streamlit as st

# st.markdown(":page_facing_up: # Home")
# st.sidebar.markdown("# Home")

# st.set_page_config(page_title = "Document Chat", page_icon = " :dvd: ", layout = "wide")

st.title(':house: Home')

st.header("Linguagem C++")

st.subheader("Explore os tópicos de programação em C++")




st.text('Fixed width text')
st.markdown('_Markdown_') # see #*
st.caption('Balloons. Hundreds of them...')
st.latex(r''' e^{i\pi} + 1 = 0 ''')
st.write('Most objects') # df, err, func, keras!
st.write(['st', 'is <', 3]) # see *
st.title('My title')
st.header('My header')
st.subheader('My sub')
st.code('for i in range(8): foo()')

# * optional kwarg unsafe_allow_html = True

st.divider()

st.code('for i in range(8): foo()')

# * optional kwarg unsafe_allow_html = True

st.write(':one:')


code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language="python")


code = '''#include <iostream>
using namespace std;
 
// Main() function: where the execution of program begins
int main()
{
    // Prints hello world
    cout << "Hello World";
 
    return 0;
}'''
st.code(code, language="cpp")





# Insert out of order.
st.write("It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).")





container = st.container(border=True)
container.write("This is inside the container")
st.write("This is outside the container")

# Now insert some more in the container
container.write("This is inside too")





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