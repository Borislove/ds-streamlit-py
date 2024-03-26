import streamlit as st
import pandas as pd
txt = 'Compare Serials'
st.markdown(f''':rainbow[{txt}]''' + '''  🧐''')

DATA = pd.read_csv('../data/series_data.csv')
df = pd.DataFrame(DATA)


# мультиселект левое меню
df1 = df.loc[:, ~df.columns.isin(
    ['Poster_Link', 'Certificate', 'Star1', 'Star2', 'Star3', 'Star4', 'Runtime_of_Episodes',
     'Runtime_of_Series', 'Overview'])]
film = st.sidebar.multiselect(
    'Выбери сериалы',
    df1['Series_Title'].unique()
)
filtred = df1[(df1['Series_Title'].isin(film))]
st.table(filtred) # табличка что добавили
st.write(filtred) #   можно отстортировать
