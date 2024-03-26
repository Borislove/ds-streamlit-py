import streamlit as st
import pandas as pd

txt = 'Advanced search'
st.markdown(f''':rainbow[{txt}]''' + '''  🧐''')

DATA = pd.read_csv('data/series_data.csv')
df = pd.DataFrame(DATA)

# CHECKBOX
df2 = pd.DataFrame(DATA)
# , col7, col8, col9, col10, col11, col12, col13
col1, col2, col3, col4 = st.columns(4)
with col1:
    poster_link = st.checkbox('Poster_Link', True)
    if poster_link:
        del df2['Poster_Link']
with col4:
    certificate = st.checkbox('Certificate', True)
    if certificate:
        del df2['Certificate']
with col2:
    series_title = st.checkbox('Series_Title')
    if series_title:
        del df2['Series_Title']
with col3:
    runtime_of_series = st.checkbox('Runtime_of_Series', True)
    if runtime_of_series:
        del df2['Runtime_of_Series']
# --------------
col5, col6, col7, col8 = st.columns(4)
with col5:
    runtime_of_episodes = st.checkbox('Runtime_of_Episodes', True)
    if runtime_of_episodes:
        del df2['Runtime_of_Episodes']
with col6:
    genre = st.checkbox('Genre')
    if genre:
        del df2['Genre']

with col7:
    imdb_rating = st.checkbox('IMDB_Rating')
    if imdb_rating:
        del df2['IMDB_Rating']

with col8:
    over = st.checkbox('Overview', True)
    if over:
        del df2['Overview']

# --------------
col9, col10, col11, col12 = st.columns(4)
with col9:
    star1 = st.checkbox('Star1', True)
    if star1:
        del df2['Star1']
with col10:
    star2 = st.checkbox('Star2', True)
    if star2:
        del df2['Star2']
with col11:
    star3 = st.checkbox('Star3', True)
    if star3:
        del df2['Star3']
with col12:
    star4 = st.checkbox('Star4', True)
    if star4:
        del df2['Star4']

col13, col14 = st.columns(2)
with col13:
    no_of_votes = st.checkbox('No_of_Votes')
    if no_of_votes:
        del df2['No_of_Votes']
# ------------------------------------------------

# ----SELECTBOX----
option = st.selectbox(
    'Top Serials',
    ('Top 10', 'Top 15', 'Top 25', 'Top 50', 'Top 100'))

st.write('You selected:', option)
if option == 'Top 10':
    # st.dataframe(df2.head(10))
    st.table(df2.head(10))
if option == 'Top 15':
    # st.dataframe(df2.head(15))
    st.table(df2.head(15))
if option == 'Top 25':
    # st.dataframe(df2.head(25))
    st.table(df2.head(25))
if option == 'Top 50':
    # st.dataframe(df2.head(50))
    st.table(df2.head(50))
if option == 'Top 100':
    # st.dataframe(df2.head(100))
    st.table(df2.head(100))
# ----------------------------------------
# df2.loc[:10]
