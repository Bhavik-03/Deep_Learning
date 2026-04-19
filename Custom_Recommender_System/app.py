import streamlit as st
import pickle
import pandas as pd


st.title("Movie Recommender")

movies = pickle.load(open('movies.pkl','rb'))
movies = pd.DataFrame(movies)
similarity=pickle.load(open('similarity.pkl','rb'))

selected_movie = st.selectbox('Which movie do you like ?',(movies['title'].values))

def recommend(movie):
    movie_idx=movies[movies['title']==movie].index[0]
    recommend_movies=[]
    movie_list=sorted(list(enumerate(similarity[movie_idx])),reverse=True,key=lambda x:x[1])[1:6]

    for i in movie_list:
        recommend_movies.append(movies.iloc[i[0]].title)
    return recommend_movies

st.subheader("Recommended Movies:")

if st.button("Recommend"):
    recommendations=recommend(selected_movie)

    for movie in recommendations:
        st.write(movie)