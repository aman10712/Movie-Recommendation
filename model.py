import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel, cosine_distances
movie_df = pd.read_excel('Nlp with images.xlsx')
indexed = pd.Series(data= movie_df.index ,index=movie_df["Movie Title"])
tfidf = TfidfVectorizer()
def movies_recommend(name, n=10):
    try:
        matrixs = tfidf.fit_transform(movie_df["genre"])
        simalar = linear_kernel(matrixs[indexed[name]], matrixs)
        movie_df["similar"] = simalar[0]
        result = movie_df.sort_values(by="similar", ascending=False).head(10)
        result_dict = result[['Movie Title', 'Ratinng', 'genre', 'img']].to_dict(orient='records')
        return result_dict
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return []