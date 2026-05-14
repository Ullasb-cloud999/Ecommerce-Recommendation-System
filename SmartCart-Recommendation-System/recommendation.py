import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
data = pd.read_csv("products.csv")

# Convert category text into vectors
cv = CountVectorizer()
matrix = cv.fit_transform(data['category'])

# Calculate similarity
similarity = cosine_similarity(matrix)

def recommend(product_name):
    try:
        # Find selected product index
        index = data[data['name'] == product_name].index[0]

        # Get similarity scores
        distances = list(enumerate(similarity[index]))

        # Sort products
        products = sorted(distances, key=lambda x: x[1], reverse=True)[1:4]

        recommended_products = []

        for i in products:
            recommended_products.append(data.iloc[i[0]]['name'])

        return recommended_products

    except:
        return ["Product not found"]