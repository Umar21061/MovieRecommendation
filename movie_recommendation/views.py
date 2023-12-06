# movie_recommendation/views.py
from django.shortcuts import render
from .forms import MovieForm
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import os

# Use a relative path to the file
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'mi_data.csv')

df = pd.read_csv(file_path)

cv = CountVectorizer(max_features=5000, stop_words='english')
tag_matrix = cv.fit_transform(df['tag']).toarray()

similarity_matrix = cosine_similarity(tag_matrix)

def recommend_movie(movie_title):
    if movie_title not in df['title'].values:
        return [f"Movie '{movie_title}' not found in the dataset."]

    index = df[df['title'] == movie_title].index[0]
    distances = sorted(enumerate(similarity_matrix[index]), reverse=True, key=lambda x: x[1])
    recommended_movies = [df.iloc[i[0]]['title'] for i in distances[1:6]]
    return recommended_movies if recommended_movies else ["No recommendations available."]

def movie_recommendation(request):
    recommendations = None

    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie_title = form.cleaned_data['movie_title']
            recommendations = recommend_movie(movie_title)
    else:
        form = MovieForm()

    return render(request, 'movie_recommendation/recommendation.html', {'form': form, 'recommendations': recommendations})
