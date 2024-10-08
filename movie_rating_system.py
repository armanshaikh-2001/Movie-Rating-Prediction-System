# -*- coding: utf-8 -*-
"""MOVIE RATING SYSTEM.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1uQ7_7oQMejYH11lN5znNyftqemmESiM9

TITLE : Movie Recommendation System
  *   AUTHOR: Arman Shaikh
  *   DOMAIN: DATA SCIENCE
  *   AIM   : To build a model to predict the rating of a movie and estimte the rating accurately

**Install and Import Libraries**
* Install the Surprise library , and then import the necessary Python libraries:
"""

pip install scikit-surprise

import pandas as pd
from surprise import Dataset, Reader, SVD
from surprise.model_selection import train_test_split
from surprise import accuracy

""" **Load and Prepare the Dataset**
 * Load the dataset using pandas and prepare it for the Surprise library:
"""

# Load the dataset
movie = pd.read_csv('/content/IMDb Movies India.csv', encoding='latin-1')

# Display the first few rows of the dataset
print(movie.head())

# Display basic information about the dataset
print(movie.info())

# Display the first few rows of the dataset
print(movie.head())

"""**Prepare the Data for the Surprise Library**
* Convert the data into the format required by the Surprise library
"""

# Define the format for reading the data
reader = Reader(rating_scale=(1, 5))  # Assuming ratings are on a scale of 1 to 5

# Load the dataset into Surprise's data structure
data = Dataset.load_from_df(movie[['Name', 'Votes', 'Rating']], reader)

""" **Split the Dataset**
* Split the dataset into training and testing sets
"""

# Split the data into training and test sets
trainset, testset = train_test_split(data, test_size=0.2, random_state=42)

"""**Train the Model**
* Use the Singular Value Decomposition (SVD) algorithm to train the model. SVD is a popular collaborative filtering algorithm for rating prediction
"""

# Initialize the SVD algorithm
model = SVD()

# Train the model on the training set
model.fit(trainset)

"""**Evaluate the Model**
* Evaluate the model’s performance using the test set:
"""

# Make predictions on the test set
predictions = model.test(testset)

# Calculate the Root Mean Squared Error (RMSE)
rmse = accuracy.rmse(predictions)

print(f"Root Mean Squared Error: {rmse}")

"""**Make Movie Rating Predictions**
* To predict the rating that a user would give to a specific movie:
"""

# Example: Predict the rating for a specific user and movie
user_id = 1
movie_id = 10

predicted_rating = model.predict(user_id, movie_id)

print(f"Predicted Rating for User {user_id} and Movie {movie_id}: {predicted_rating.est}")

"""#Explanation
* Install and Import Libraries: We install the Surprise library and import necessary libraries for data handling and model creation.

* Load and Prepare the Dataset: Load the dataset using pandas and examine its structure. This dataset contains user ratings for various movies.

* Prepare the Data for the Surprise Library: Convert the data into a format that the Surprise library can use. This involves specifying the rating scale and loading the data into the Surprise data structure.

* Split the Dataset: Split the dataset into training and test sets. This helps evaluate the model's performance on unseen data.

* Train the Model: We use the Singular Value Decomposition (SVD) algorithm to train the model on the training set. SVD is effective for collaborative filtering tasks.

* Evaluate the Model: After training, we evaluate the model using the test set. We use the Root Mean Squared Error (RMSE) to measure how well the predicted ratings match the actual ratings.

* Make Movie Rating Predictions: The predict() function is used to estimate the rating a user would give to a particular movie.

"""