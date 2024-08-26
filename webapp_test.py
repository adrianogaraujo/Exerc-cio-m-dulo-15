import streamlit as st
import pandas as pd
import numpy as np

st.title('Aplicação de Data Science com Streamlit')
st.write('Aqui está um simples exemplo de uso do Streamlit.')

# Slider
age = st.slider('Escolha sua idade', 0, 100, 25)

# Checkbox
show_data = st.checkbox('Mostrar dados')

# Selectbox
option = st.selectbox(
    'Qual o seu fruto favorito?',
    ('Maçã', 'Banana', 'Cereja')
)

st.write('Você selecionou:', option)

# Gerando dados aleatórios
data = pd.DataFrame(
   np.random.randn(50, 3),
   columns=['a', 'b', 'c']
)

if show_data:
    st.write(data)

st.line_chart(data)

@st.cache_data
def load_data(nrows):
    data = pd.DataFrame(
        np.random.randn(nrows, 5),
        columns=('col %d' % i for i in range(5))
    )
    return data

def main():
    data_load_state = st.text('Loading data...')
    data = load_data(10000)
    data_load_state.text("Done! (using st.cache_data)")

    if st.checkbox('Show data'):
        st.write(data)

if __name__ == "__main__":
    main()

if 'count' not in st.session_state:
    st.session_state.count = 0

increment = st.button('Increment')
if increment:
    st.session_state.count += 1

st.write('Count:', st.session_state.count)

add_selectbox = st.sidebar.selectbox(
    "Como você gostaria de ser contatado?",
    ("Email", "Home phone", "Mobile phone")
)

add_slider = st.sidebar.slider(
    'Selecione um intervalo de valores',
    0.0, 100.0, (25.0, 75.0)
)
