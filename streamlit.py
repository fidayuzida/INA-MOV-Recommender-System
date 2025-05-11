import streamlit as st
import pickle
import pandas as pd
import requests


def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=111f82ee0c48ef47c323c74c9f7c781b&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
    

def recommend(movie):
    movie_index = mov[mov['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse = True, key=lambda x: x[1])[1:6]
    recommend_mov = []
    recommend_mov_posters = []
    for i in movies_list:
        movie_id = mov.iloc[i[0]].movie_id
        
        recommend_mov.append(mov.iloc[i[0]].title)
        #menambahkan poster dari API
        recommend_mov_posters.append(fetch_poster(movie_id))
    return recommend_mov, recommend_mov_posters


mov_dict = pickle.load(open('movies_dict.pkl', 'rb'))
mov = pd.DataFrame(mov_dict)
similarity = pickle.load(open('similarity.pkl','rb'))


st.title('Movie Recommender System')
selected_movie_name = st.selectbox(
'Mau Cari Film Apa?', 
mov['title'].values)


if st.button('Recommend'):
    names,posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])






