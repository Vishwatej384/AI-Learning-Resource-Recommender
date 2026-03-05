from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def rank_videos(topic, videos):

    titles = [title for title, link in videos]

    documents = [topic] + titles

    vectorizer = TfidfVectorizer()

    tfidf_matrix = vectorizer.fit_transform(documents)

    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()

    ranked = sorted(
        zip(videos, similarity),
        key=lambda x: x[1],
        reverse=True
    )

    ranked_videos = [video for video, score in ranked]

    return ranked_videos