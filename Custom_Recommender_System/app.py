import streamlit as st
import pandas as pd
import pickle
import gdown

# 🔥 Cache + download once
@st.cache_data
def load_pickle_from_drive(file_id, output):
    url = f"https://drive.google.com/uc?id={file_id}"
    gdown.download(url, output, quiet=True)
    
    with open(output, 'rb') as f:
        return pickle.load(f)

st.title("Movie Recommender")

# 🔗 Load data
movies = load_pickle_from_drive(
    "1eL4DCggPcYJGOC5Zod9vVnwKs1TwqNRp",
    "movies.pkl"
)

similarity = load_pickle_from_drive(
    "1jr82QsZlLIrTePniLrc1mYjw81xf0Er2",
    "similarity.pkl"
)

movies = pd.DataFrame(movies)

# 🎯 UI
selected_movie = st.selectbox(
    'Which movie do you like ?',
    movies['title'].tolist()
)

# 🧠 Logic
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
    for movie in recommend(selected_movie):
        st.write(movie)