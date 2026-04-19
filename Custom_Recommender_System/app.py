import streamlit as st
import pandas as pd
import requests
import pickle

# 🔥 Cache function (important)
@st.cache_data
def load_pickle(url):
    response = requests.get(url)
    return pickle.loads(response.content)

st.title("Movie Recommender")

# 🔗 Load data from Google Drive
movies = load_pickle("https://drive.google.com/uc?id=1eL4DCggPcYJGOC5Zod9vVnwKs1TwqNRp")
movies = pd.DataFrame(movies)

similarity = load_pickle("https://drive.google.com/uc?id=1jr82QsZlLIrTePniLrc1mYjw81xf0Er2")

# 🎯 UI
selected_movie = st.selectbox(
    'Which movie do you like ?',
    movies['title'].tolist()
)

# 🧠 Recommendation logic
def recommend(movie):
    movie_idx = movies[movies['title'] == movie].index[0]
    
    movie_list = sorted(
        list(enumerate(similarity[movie_idx])),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    return [movies.iloc[i[0]].title for i in movie_list]

# 🎬 Output
st.subheader("Recommended Movies:")

if st.button("Recommend"):
    recommendations = recommend(selected_movie)

    for movie in recommendations:
        st.write(movie)