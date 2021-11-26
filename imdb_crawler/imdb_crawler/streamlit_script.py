import streamlit as st
import pandas as pd

df_films = pd.read_csv("films.csv")
df_series = pd.read_csv("series.csv")

time = df_films["duree"].str.replace(" ", "")
time = time.str.replace("m", "")
time = time.str.replace(",", "")
heures = time.str.extract(r"(\d+)h")
minutes = time.str.extract(r'h(\d+)')



df_films['duree']=heures.astype("float", errors="ignore")*60 + minutes.astype("float", errors="ignore")

container_dataset = st.container()

filter_1 = st.sidebar.radio('Which category you want to chose ?',('Films', 'Séries'))

if filter_1 == 'Films':
    filter = st.sidebar.radio('Which filter you want to chose ?',( 'Title', 'Score', 'Actor', 'Type', 'Time'))

    if filter == 'Title': 
        titles = df_films['titre'].unique()
        titles_choice = st.sidebar.selectbox('Select your movie:', titles)

    if filter == 'Score': 
        score = df_films['score'].unique()
        score_choice = st.sidebar.selectbox('Score', score)

    if filter =='Actor': 
        acteur = df_films['acteurs'].unique()
        actor_choice = st.sidebar.selectbox('Acteurs', acteur)

    if filter =='Type': 
        genre = df_films['genre'].unique()
        genre_choice = st.sidebar.selectbox('Genre', genre)

    if filter =='Time': 
        duree = df_films['duree'].unique()
        duree_choice = st.sidebar.selectbox('Duree', duree)

    with container_dataset:

        if filter =='Time':
            mask_duree = df_films['duree'] == duree_choice 
            st.dataframe(data = df_films[mask_duree])

        elif filter == 'Score':
            mask_score = df_films['score'] == score_choice
            st.dataframe(data = df_films[mask_score])

        elif filter =='Actor':
            mask_acteur = df_films['acteurs'] == actor_choice
            st.dataframe(data = df_films[mask_acteur])

        elif filter =='Type':
            mask_genre = df_films['genre'] == genre_choice
            st.dataframe(data = df_films[mask_genre])

        elif filter == 'Title':
            mask_title = df_films['titre'] == titles_choice
            st.dataframe(data = df_films[mask_title])

elif filter_1 == 'Séries':
    filter_2 = st.sidebar.radio('Which filter you want to chose ?',( 'Title', 'Score', 'Actor', 'Type', 'Time'))

    if filter_2 == 'Title': 
        titles_series = df_series['titre'].unique()
        titles_choice_series = st.sidebar.selectbox('Select your movie:', titles_series)

    if filter_2 == 'Score': 
        score_series = df_series['score'].unique()
        score_choice_series = st.sidebar.selectbox('Score', score_series)

    if filter_2 =='Actor': 
        acteur_series = df_series['acteurs'].unique()
        actor_choice_series = st.sidebar.selectbox('Acteurs', acteur_series)

    if filter_2 =='Type': 
        genre_series = df_series['genre'].unique()
        genre_choice_series = st.sidebar.selectbox('Genre', genre_series)

    if filter_2 =='Time': 
        duree_series = df_series['duree'].unique()
        duree_choice_series = st.sidebar.selectbox('Duree', duree_series)

    with container_dataset:

        if filter_2 =='Time':
            mask_duree_series = df_series['duree'] == duree_choice_series 
            st.dataframe(data = df_series[mask_duree_series])

        elif filter_2 == 'Score':
            mask_score_series = df_series['score'] == score_choice_series
            st.dataframe(data = df_series[mask_score_series])

        elif filter_2 =='Actor':
            mask_acteur_series = df_series['acteurs'] == actor_choice_series
            st.dataframe(data = df_series[mask_acteur_series])

        elif filter_2 =='Type':
            mask_genre_series = df_series['genre'] == genre_choice_series
            st.dataframe(data = df_series[mask_genre_series])

        elif filter_2 == 'Title':
            mask_title_series = df_series['titre'] == titles_choice_series
            st.dataframe(data = df_series[mask_title_series])


#score_choice = st.select_slider('Slide to select', options=[1,'2'])

#score_choice = st.sidebar.selectbox('', score)

#outil de recherche par nom 



#outil de recherche par acteur

#outil de recherche par genre

#outil de recherche par durée

#outil de recherche par note

