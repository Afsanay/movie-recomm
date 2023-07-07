import streamlit as st
import pandas as pd
import requests


def fetch_posters(movie_id):
    response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=6d228c21c003da645b2aaa6096eddd6a&language=en-US")
    data = response.json()
    # st.write(data)
    return "https://image.tmdb.org/t/p/w500" + data['poster_path']



def recommend(movie):
    movie_index = movies_list[movies_list['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for mo in movie_list:
        movie_id = movies_list.iloc[mo[0]].movie_id
        recommended_movies.append(movies_list.iloc[mo[0]].title)
        recommended_movies_posters.append(fetch_posters(movie_id))

    return recommended_movies, recommended_movies_posters


movies_list = pd.read_pickle('movies.pkl')
movies_name = movies_list['title'].values

similarity = pd.read_pickle('similarity.pkl')

st.title("Movie Recommendation System")
with st.sidebar:
    st.image('https://www.onepointltd.com/wp-content/uploads/2020/03/inno2.png')
    st.title("Movie Recommendation with Linear Regression")


selected_movie_name = st.selectbox(
    "Which movie recommendations you want?", movies_name
)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)
    col1, col2, col3 = st.columns(3)
    col4, col5 = st.columns(2)

    with col1:
        st.markdown(names[0])
        st.image(posters[0])
    with col2:
        st.markdown(names[1])
        st.image(posters[1])
    with col3:
        st.markdown(names[2])
        st.image(posters[2])
    with col4:
        st.markdown(names[3])
        st.image(posters[3])
    with col5:
        st.markdown(names[4])
        st.image(posters[4])
