import streamlit as st
import pandas as pd
import tools
#import firebase_adapter

st.title('Molestream')
top = st.slider('How many items in your top ?', 0, 50, 10)
df_gsheet = tools.spotifyGoogleSheet()
df_artist= df_gsheet.groupby('artist').count()
del df_artist['title']
df_artist = df_artist.sort_values(by=['played'], ascending=False)
title_top = 'Top '+str(top)+' listened artists'
st.header(title_top)
st.write('This top 10 is about listenings since the 22th of september 2021')
st.table(df_artist.head(top))
df_gsheet['played']= pd.to_datetime(df_gsheet['played'])
#df_gsheet['month'] = df_gsheet['played'].dt.strftime('%Y-%m')
df_played_by_month = df_gsheet.groupby(pd.Grouper(key='played',freq='M')).count()
print(df_played_by_month)
st.header('Played by month')
st.line_chart(df_played_by_month[['title']])

#st.table(firebase_adapter.movie_collection_to_panda().head(10))
