import pandas as pd
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import streamlit as st
import logging
import datetime as dt

def convert_date_firebase(date):
    return pd.Timestamp(date, unit='ms')

def transform_collection(movies):
    new_movies = []
    for movie_user in movies:
        for movie in movies[movie_user]:            
            movies[movie_user][movie]['user'] = movie_user
        new_movies.append(movies[movie_user])
    return new_movies

def movie_collection_to_panda2(user):
    if not firebase_admin._apps:
        cred = credentials.Certificate(st.secrets["firebase_service_account"])
        firebase_admin.initialize_app(cred, options={
            'databaseURL': st.secrets["moleskine_database_url"]
        })
        
    # Get the data at that reference.
    movies = db.reference('movies').get()
    movies_list = transform_collection(movies)

    data = []
    df_movies = pd.DataFrame(data)

    df_movies = pd.DataFrame(columns=['id','date','year', 'title', 'director', 'rating', 'cinema', 'idMovieDb', 'releaseDate'])
    i = 1
    for items_batch in movies_list:
        for item_id, item_data in items_batch.items():
            if item_data.get('user') == user:
                df_movies.loc[i] = [item_id,convert_date_firebase(item_data.get('date')),convert_date_firebase(item_data.get('date')).year,item_data.get('title'),item_data.get('director'),str(item_data.get('rating')),str(item_data.get('cinema')),item_data.get('idMovieDb'),convert_date_firebase(item_data.get('releaseDate')).year]
                i+=1

    return df_movies

def movie_collection_to_panda(user):
    if not firebase_admin._apps:
        cred = credentials.Certificate(st.secrets["firebase_service_account"])
        firebase_admin.initialize_app(cred, options={
            'databaseURL': st.secrets["moleskine_database_url"]
        })
        
    # Get the data at that reference.
    movies = db.reference('movies/'+user).get()
    
    data = []
    for key in movies:
        data.append(movies[key])
    df = pd.DataFrame(data)
    df['releaseDate'] = df['releaseDate'].apply(lambda x: convert_date_firebase(x))
    df['date'] = df['date'].apply(lambda x: convert_date_firebase(x))
    return df