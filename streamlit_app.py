import music
import movie
import streamlit as st

PAGES = {
    "Music": music,
    "Movie": movie
}
st.sidebar.title('Molestream')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()