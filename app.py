import streamlit as st

st.title('My first Streamlit app')

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

