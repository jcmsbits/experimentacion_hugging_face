import streamlit  as st
   
x = st.slider("Selecciona un valor")
st.write(x, "al cuadrado es", x * x)

## Reproduce en tu browser con "streamlit run first_app.py"