import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=52d6454c2e5b3c0029b58a17393d0e15&language=en-US'.format(movie_id))
    data =response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    movies_list=sorted(list(enumerate(similarity[movie_index])),reverse=True,key=lambda x:x[1])[1:6]

    recommended_movies=[]
    recommended_movies_posters =[]
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_posters

movie_dict= pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movie_dict)
similarity = pickle.load(open('similarity.pkl','rb'))
st.title('Movie Recommendation System')

selected_movie_name = st.selectbox('Type or select a movie from the dropdown menu.',movies['title'].values)

if st.button('Recommend'):
    recommended_movies ,recommended_movies_posters = recommend(selected_movie_name)
    #for i in recommendations:
        #st.write(i)
    col1, col2, col3, col4, col5 = st.beta_columns(5)
    with col1:
            st.text(recommended_movies[0])
            st.image(recommended_movies_posters[0])
    with col2:
            st.text(recommended_movies[1])
            st.image(recommended_movies_posters[1])

    with col3:
            st.text(recommended_movies[2])
            st.image(recommended_movies_posters[2])
    with col4:
            st.text(recommended_movies[3])
            st.image(recommended_movies_posters[3])
    with col5:
            st.text(recommended_movies[4])
            st.image(recommended_movies_posters[4])