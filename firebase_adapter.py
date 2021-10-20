import pandas as pd
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import streamlit as st

def convert_date_firebase(date):
    return pd.Timestamp(date, unit='ms')

def transform_collection(movies):
    new_movies = []
    for movie_user in movies:
        for movie in movies[movie_user]:            
            movies[movie_user][movie]['user'] = movie_user
        new_movies.append(movies[movie_user])
    return new_movies

def movie_collection_to_panda():
    if not firebase_admin._apps:
        cred = credentials.Certificate(st.secrets["firebase_service_account"])
        firebase_admin.initialize_app(cred, options={
            'databaseURL': st.secrets["moleskine_database_url"]
        })

    # Then get the data at that reference.
    movies = db.reference('movies').get()
    movies_list = transform_collection(movies)

    data = []
    df_movies = pd.DataFrame(data)

    for items_batch in movies_list:
        for item_id, item_data in items_batch.items():
            new_row = pd.Series(data={'id':item_id, 'user':item_data.get('user'),'date':convert_date_firebase(item_data.get('date')), 'year':convert_date_firebase(item_data.get('date')).year, 'title': item_data.get('title'), 'director': item_data.get('director'), 'rating':str(item_data.get('rating')), 'cinema':str(item_data.get('cinema')),'idMovieDb':item_data.get('idMovieDb'), 'releaseDate' :convert_date_firebase(item_data.get('releaseDate')).year})        
            df_movies = df_movies.append(new_row, ignore_index=True)
    
    return df_movies