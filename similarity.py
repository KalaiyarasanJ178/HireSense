from sklearn.metrics.pairwise import cosine_similarity

def calculate_similarity(vectors):
    score = cosine_similarity(vectors[0:1], vectors[1:2])
    return round(float(score[0][0]) * 100, 2)
