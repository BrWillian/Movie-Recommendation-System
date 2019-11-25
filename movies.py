import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from preprocessing import split_genres, transform_to_str
from n_cluster_calc import kmens_plot
import matplotlib.pyplot as plt
import os

# To read dataset

new_data = pd.read_csv(os.getcwd()+'/tmdb_5000_movies.csv')


# Collect column 'genres'
genres = new_data['genres']

# Transform data in legible strings (split_genres, transform_to_str) / preprocessing.py
new_genres = split_genres(genres)

genres_str = transform_to_str(new_genres)


# Add new column with data normalized
new_data['genres_normalized'] = genres_str


#Get dummies and concat dummies and title
data = new_data[['title', 'genres_normalized']]
data_title = data['title']
data_dummies = data.genres_normalized.str.get_dummies()
data = pd.concat([data, data_dummies], axis=1)


#Create object of Scaler
scaler_data = StandardScaler()
data_dummies_scaler = scaler_data.fit_transform(data_dummies)


#Train model
model = KMeans(n_clusters=13)
model.fit(data_dummies_scaler)


#Create variable to alocate centroids
groups = pd.DataFrame(model.cluster_centers_, columns=data_dummies.columns)

var = model.labels_ == 2

for i, movies in enumerate(zip(data.title[var].sample(15), data.genres_normalized.sample(15))):
    print(f'{i+1} - Movie name: {movies[0]}, Genres: {movies[1]}', end='\n\n')

#Plot graphic bar
groups.transpose().plot.bar(subplots=True, figsize=(25, 75), sharex=False)
plt.show()

