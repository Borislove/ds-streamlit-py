import streamlit as st
import pandas as pd

# ---TOP SERIAL---
DATA = pd.read_csv('data/series_data.csv')
df = pd.DataFrame(DATA)

txt = 'Top Serials'
st.markdown(f''':rainbow[{txt}]''' + '''  ⭐''')

# убираем лишнее
del df['Poster_Link']
del df['Certificate']
del df['Runtime_of_Episodes']
del df['Runtime_of_Series']
del df['Overview']
del df['Star1']
del df['Star2']
del df['Star3']
del df['Star4']

# NAVI
txt_top = 'Top'
txt_serials = 'Serials'
txt10 = '🔟'
txt15 = '1️⃣5️⃣'
txt25 = '2️⃣5️⃣'
txt50 = '5️⃣0️⃣'
txt100 = '💯'

nav = st.sidebar.radio("Top Serials", ['Top 10', 'Top 15', 'Top 25', 'Top 50', 'Top 100'])
if nav == 'Top 10':
    st.markdown(f''':rainbow[{txt_top}]''' + f'''{txt10}''' + f''':rainbow[{txt_serials}]''')
    st.table(df.head(10))
if nav == 'Top 15':
    st.markdown(f''':rainbow[{txt_top}]''' + f'''{txt15}''' + f''':rainbow[{txt_serials}]''')
    st.table(df.head(15))
if nav == 'Top 25':
    st.markdown(f''':rainbow[{txt_top}]''' + f'''{txt25}''' + f''':rainbow[{txt_serials}]''')
    st.table(df.head(25))
if nav == 'Top 50':
    st.markdown(f''':rainbow[{txt_top}]''' + f'''{txt50}''' + f''':rainbow[{txt_serials}]''')
    st.table(df.head(50))
if nav == 'Top 100':
    st.markdown(f''':rainbow[{txt_top}]''' + f'''{txt100}''' + f''':rainbow[{txt_serials}]''')
    st.table(df.head(100))
# -----------------------------
