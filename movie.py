# movie.py
import streamlit as st
import firebase_adapter
import pandas as pd

def load_data():
    return firebase_adapter.movie_collection_to_panda()

def app():
    st.title('Movies')
    data = load_data()    
    movie_cay = data[data['user'] == 'CKTlQvlnkJZhqagNIls2arTxKxp2' ]
    st.metric('Viewed',str(len(movie_cay.index)))
    movie_cay['year_watched'] = movie_cay['date'].dt.year
    movie_cay = movie_cay.sort_values(by=['date'], ascending=False)
    movies_by_year = movie_cay.groupby(pd.Grouper(key='year_watched')).count()
    movies_by_year.rename(columns = {'cinema':'Count'}, inplace = True)
    st.header('Watched by year')
    st.bar_chart(movies_by_year[['Count']])
    st.header('Last 10 watched movies')
    st.table(movie_cay[["date","title", "director"]].head(10))
