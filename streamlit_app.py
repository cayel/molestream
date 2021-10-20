import streamlit as st
import pandas as pd
import tools
#import firebase_adapter

st.title('Molestream')
df_gsheet = tools.spotifyGoogleSheet()
df_artist= df_gsheet.groupby('artist').count()
del df_artist['title']
df_artist = df_artist.sort_values(by=['played'], ascending=False)
st.header('Top 10 listened artists')
st.write('This top 10 is about listenings since the 22th of september 2021')
st.table(df_artist.head(10))

#st.table(firebase_adapter.movie_collection_to_panda().head(10))
