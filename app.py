import streamlit as st

st.title('My first Streamlit app')

st.markdown('## Static Content')
# Can output different types
a = 12.34
st.write(a)

st.write('Some text here')

# Using markdown
st.markdown('Text can be **bold** and _italic_.')
st.markdown(r'''Raw strings can be very useful: we can
- create
- bullet
- lists

and other markdown things like horizontal lines
---
''' )

# Can display latex - also a latex specific method
st.markdown(r'''
$$
i\hbar\frac{\partial}{\partial t} \Psi(x,t) = \left [ - \frac{\hbar^2}{2m}\frac{\partial^2}{\partial x^2} + V(x,t)\right ] \Psi(x,t)
$$
''')

# As we can use MD we have access to code blocks
st.markdown(r'''
```c
int main() {
    return 0;
}
```
''')

st.markdown('## Dynamic Content')

st.checkbox('Tick me')

if st.checkbox('Tick me to see'):
    st.write(42)

selection = st.selectbox('Choose an option', ["Nothing here", "or here", "but something here"])

if selection == "but something here":
    st.write("You found me!")
else:
    st.write("Try again")

int_val = st.slider("Pick an integer", min_value=1, max_value=10, value=5)
st.write(int_val)

float_val = st.slider("Pick an float", min_value=1.0, max_value=10.0, value=5.0, step=0.1, format="%.1f")
st.write(float_val)

# Layout
st.sidebar.write("Adding texst to the sidebar...")