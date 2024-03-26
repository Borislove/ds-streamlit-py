import streamlit as st
import pandas as pd

DATA = pd.read_csv('data/series_data.csv')
df = pd.DataFrame(DATA)

txt = 'Full Table'
st.markdown(f''':rainbow[{txt}]''' + '''  📚''')

# кнопка, которая покажет всю табличку
if st.button('Показать всю таблицу'):
    df.loc[:, ~df.columns.isin(['Poster_Link'])]
    st.button('Скрыть таблицу')

txt_link = 'Link DataSet: '
st.write(txt_link + "[Dataset](https://www.kaggle.com/datasets/harshitshankhdhar/tv-series-dataset)")
