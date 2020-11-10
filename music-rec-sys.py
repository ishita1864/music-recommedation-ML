import pandas as pd
import numpy as np
import math
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv("MusicDataSheet2.csv")
features = ['SongName', 'Genre']


feature: str
for feature in features:
    df[feature] = df[feature].fillna('')


def combine_features(row):
    return row['SongName'] + " " + row['Genre']


df['combined_features'] = df.apply(combine_features, axis=1)


selected_song = 'Rescue me'
index = df[df.SongName == selected_song].index[0]
selected_features = str(df['combined_features'].values[index]).split(' ')

page_profile_matrix = []


for i in range( len(df.index)):
    page_profile_matrix.append(list())
    for j in range(len(selected_features)):
        if selected_features[j] in str(df['combined_features'].values[i]).split(' '):
            page_profile_matrix[i].append(1)
        else:
            page_profile_matrix[i].append(0)


cosine_sim = cosine_similarity(page_profile_matrix)


scores_series=pd.Series(cosine_sim[4]).sort_values(ascending=False)
recommended_songs_indexes=list(scores_series[0:3].index)
print(recommended_songs_indexes)


recommended_songs=[]
for i in recommended_songs_indexes:
	recommended_songs.append(df['SongName'][i])
print(recommended_songs)

