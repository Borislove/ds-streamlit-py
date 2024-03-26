import streamlit as st
import pandas as pd

#HOMEPAGE
DATA = pd.read_csv('data/series_data.csv')
df = pd.DataFrame(DATA)

st.set_page_config(
    page_title='First App',
    page_icon='🔂',
)

#st.title("Top IMDB TV Series")
#st.sidebar.success("select a page above.")

# Title
# по центру
txt = 'Топ-5 сериалов IMDB по количеству голосов'
st.markdown(f''':rainbow[{txt}]''' + '''  😎''')

# исключаем столбы
df.loc[:5,
~df.columns.isin(['Poster_Link', 'Certificate', 'Star1', 'Star2', 'Star3', 'Star4', 'Overview', 'Runtime_of_Episodes',
                  'Runtime_of_Series'])]
