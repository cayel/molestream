# movie.py
import streamlit as st
import firebase_adapter

def load_data():
    return firebase_adapter.movie_collection_to_panda()

def app():
    st.title('Movies')
    data = load_data()
    st.metric('Viewed',str(len(data.index)))