# movie.py
import streamlit as st
import firebase_adapter
import pandas as pd
from st_aggrid import AgGrid

def load_data(user):
    return firebase_adapter.movie_collection_to_panda(user)

def app():
    st.title('Movies')
    data = load_data('CKTlQvlnkJZhqagNIls2arTxKxp2')    
    # movie_cay = data[data['user'] == 'CKTlQvlnkJZhqagNIls2arTxKxp2' ]
    st.metric('Viewed',str(len(data.index)))
    data['year_watched'] = data['date'].dt.year
    movie_cay = data.sort_values(by=['date'], ascending=False)
    movies_by_year = movie_cay.groupby(pd.Grouper(key='year_watched')).count()
    movies_by_year.rename(columns = {'cinema':'Count'}, inplace = True)
    st.header('Watched by year')
    st.bar_chart(movies_by_year[['Count']])
    st.header('Watched movies')
    AgGrid(movie_cay[["date","title", "director", "rating", "cinema", "releaseDate"]])
