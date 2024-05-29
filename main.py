import streamlit as st
import pickle
import requests

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=314af30c5b842a0e5bc7a947cf1ce4d2'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    movie_index = movies_list[movies_list['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_l = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    rec_movies = []
    rec_movies_posters=[]
    for i in movies_l:
        movie_id = movies_list.iloc[i[0]].movie_id
        rec_movies.append(movies_list.iloc[i[0]].title)
        rec_movies_posters.append(fetch_poster(movie_id))
    return rec_movies,rec_movies_posters

movies_list = pickle.load(open('movies.pkl','rb'))   #array of all the 5000 movies
movies_list1 = movies_list['title'].values
similarity = pickle.load(open('sim.pkl','rb'))
st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    "What do you want us to recommend today",
    movies_list1)


if st.button("Recommend"):
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
