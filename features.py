from sklearn.feature_extraction.text import TfidfVectorizer

def get_tfidf_vectors(resume, jd):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([resume, jd])
    return vectors
