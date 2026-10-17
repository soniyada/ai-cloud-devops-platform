from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

TRAINING_TEXTS = [
    "I love this product",
    "This is wonderful and amazing",
    "I am very happy",
    "Excellent service and great quality",
    "This is fantastic",
    "I hate this product",
    "This is terrible and awful",
    "I am very disappointed",
    "Poor service and bad quality",
    "This is horrible",
]

LABELS = [
    "positive", "positive", "positive", "positive", "positive",
    "negative", "negative", "negative", "negative", "negative",
]

model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("classifier", LogisticRegression(max_iter=500)),
])

model.fit(TRAINING_TEXTS, LABELS)


def predict_sentiment(text: str) -> str:
    return str(model.predict([text])[0])
