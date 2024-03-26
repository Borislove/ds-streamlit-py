import streamlit as st
import pandas as pd
import time
from PIL import Image
import plotly.express as px
import numpy as np
import json

# DATA
DATA = pd.read_csv('../../data/series_data.csv')
df = pd.DataFrame(DATA)

# Title
# по центру
txt = 'Лучшие сериалы 2000 года по версии IMDB по количеству голосов'
st.markdown(f''':rainbow[{txt}]''' + '''  😎''')

# исключаем столбы
df.loc[:5,
~df.columns.isin(['Poster_Link', 'Certificate', 'Star1', 'Star2', 'Star3', 'Star4', 'Overview', 'Runtime_of_Episodes',
                  'Runtime_of_Series'])]

# мультиселект левое меню
df1 = df.loc[:, ~df.columns.isin(
    ['Poster_Link', 'Certificate', 'Star1', 'Star2', 'Star3', 'Star4', 'Runtime_of_Episodes',
     'Runtime_of_Series', 'Overview'])]
film = st.sidebar.multiselect(
    'Искать сериал',
    df1['Series_Title'].unique()
)
filtred = df1[(df1['Series_Title'].isin(film))]
st.write(filtred)

# кнопка, которая покажет всю табличку
if st.button('Показать все сериалы'):
    df.loc[:, ~df.columns.isin(['Poster_Link'])]
    st.button('Скрыть таблицу')

# ----SELECTBOX----
option = st.selectbox(
    'Top Serials',
    (' ', 'Top 10', 'Top 15', 'Top 25', 'Top 50', 'Top 100'))

st.write('You selected:', option)
if option == 'Top 10':
    df.loc[:10, ~df.columns.isin(
        ['Runtime_of_Episodes', 'Runtime_of_Series', 'Overview', 'Certificate', 'Poster_Link', 'Star1', 'Star2',
         'Star3', 'Star4'])]
if option == 'Top 15':
    df.loc[:15, ~df.columns.isin(
        ['Runtime_of_Episodes', 'Runtime_of_Series', 'Overview', 'Certificate', 'Poster_Link', 'Star1', 'Star2',
         'Star3', 'Star4'])]
if option == 'Top 25':
    df.loc[:25, ~df.columns.isin(
        ['Runtime_of_Episodes', 'Runtime_of_Series', 'Overview', 'Certificate', 'Poster_Link', 'Star1', 'Star2',
         'Star3', 'Star4'])]
if option == 'Top 50':
    df.loc[:50, ~df.columns.isin(
        ['Runtime_of_Episodes', 'Runtime_of_Series', 'Overview', 'Certificate', 'Poster_Link', 'Star1', 'Star2',
         'Star3', 'Star4'])]
if option == 'Top 100':
    df.loc[:100, ~df.columns.isin(
        ['Runtime_of_Episodes', 'Runtime_of_Series', 'Overview', 'Certificate', 'Poster_Link', 'Star1', 'Star2',
         'Star3', 'Star4'])]
# ----------------------------------------

# NAVI
txt_top = 'Top'
txt_serials = 'Serials'
txt10 = '🔟'
txt15 = '1️⃣5️⃣'
txt25 = '2️⃣5️⃣'
txt50 = '5️⃣0️⃣'
txt100 = '💯'

nav = st.sidebar.radio("Top Serials", [' ', 'Top 10', 'Top 15', 'Top 25', 'Top 50', 'Top 100'])
if nav == 'Top 10':
    st.markdown(f''':rainbow[{txt_top}]''' + f'''{txt10}''' + f''':rainbow[{txt_serials}]''')
    df.loc[:10, ~df.columns.isin(
        ['Runtime_of_Episodes', 'Runtime_of_Series', 'Overview', 'Certificate', 'Poster_Link', 'Star1', 'Star2',
         'Star3', 'Star4'])]
if nav == 'Top 15':
    st.markdown(f''':rainbow[{txt_top}]''' + f'''{txt15}''' + f''':rainbow[{txt_serials}]''')
    # st.write("Top 15")
    df.loc[:15, ~df.columns.isin(
        ['Runtime_of_Episodes', 'Runtime_of_Series', 'Overview', 'Certificate', 'Poster_Link', 'Star1', 'Star2',
         'Star3', 'Star4'])]
if nav == 'Top 25':
    st.markdown(f''':rainbow[{txt_top}]''' + f'''{txt25}''' + f''':rainbow[{txt_serials}]''')
    # st.write("Top 25")
    df.loc[:25, ~df.columns.isin(
        ['Runtime_of_Episodes', 'Runtime_of_Series', 'Overview', 'Certificate', 'Poster_Link', 'Star1', 'Star2',
         'Star3', 'Star4'])]
if nav == 'Top 50':
    st.markdown(f''':rainbow[{txt_top}]''' + f'''{txt50}''' + f''':rainbow[{txt_serials}]''')
    # st.write("Top 50")
    df.loc[:50, ~df.columns.isin(
        ['Runtime_of_Episodes', 'Runtime_of_Series', 'Overview', 'Certificate', 'Poster_Link', 'Star1', 'Star2',
         'Star3', 'Star4'])]
if nav == 'Top 100':
    st.markdown(f''':rainbow[{txt_top}]''' + f'''{txt100}''' + f''':rainbow[{txt_serials}]''')
    # st.write("Top 100")
    df.loc[:100, ~df.columns.isin(
        ['Runtime_of_Episodes', 'Runtime_of_Series', 'Overview', 'Certificate', 'Poster_Link', 'Star1', 'Star2',
         'Star3', 'Star4'])]
# -----------------------------


# left
st.sidebar.info("[Dataset](https://www.kaggle.com/datasets/harshitshankhdhar/tv-series-dataset)")
st.sidebar.info("[![Star](https://img.shields.io/github/stars/borislove)](https://github.com/Borislove)")

st.write("Собственные настройки")

# st.table(df2)
# st.dataframe(df2)

# print(df.index)
# del df2['Poster_Link']
# print(df2.columns)

# Test
# print(DATA) # вывод в консоль
# print(DATA.columns)  # наши колонки
# print(max(DATA.columns))

# print(DATA.describe()) что то показывает
# print(DATA.describe(include=object))


# CHECKBOX
df2 = pd.DataFrame(DATA)
# , col7, col8, col9, col10, col11, col12, col13
col1, col2, col3, col4 = st.columns(4)
with col1:
    poster_link = st.checkbox('Poster_Link')
    if poster_link:
        del df2['Poster_Link']
with col2:
    genre = st.checkbox('Genre')
    if genre:
        del df2['Genre']
with col3:
    series_title = st.checkbox('Series_Title')
    if series_title:
        del df2['Series_Title']
with col4:
    runtime_of_series = st.checkbox('Runtime_of_Series')
    if runtime_of_series:
        del df2['Runtime_of_Series']
# --------------
col5, col6, col7, col8 = st.columns(4)
with col5:
    runtime_of_episodes = st.checkbox('Runtime_of_Episodes')
    if runtime_of_episodes:
        del df2['Runtime_of_Episodes']
with col6:
    imdb_rating = st.checkbox('IMDB_Rating')
    if imdb_rating:
        del df2['IMDB_Rating']
with col7:
    over = st.checkbox('Overview')
    if over:
        del df2['Overview']
with col8:
    no_of_votes = st.checkbox('No_of_Votes')
    if no_of_votes:
        del df2['No_of_Votes']
# --------------
col9, col10, col11, col12 = st.columns(4)
with col9:
    star1 = st.checkbox('Star1')
    if star1:
        del df2['Star1']
with col10:
    star2 = st.checkbox('Star2')
    if star2:
        del df2['Star2']
with col11:
    star3 = st.checkbox('Star3')
    if star3:
        del df2['Star3']
with col12:
    star4 = st.checkbox('Star4')
    if star4:
        del df2['Star4']

col13,col14 = st.columns(2)
with col13:
    certificate = st.checkbox('Certificate')
    if certificate:
        del df2['Certificate']
df2.loc[:10]
# with col6:
#   st.checkbox('Overview')
