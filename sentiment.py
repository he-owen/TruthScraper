from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

MODEL_NAME = "yiyanghkust/finbert-tone"

print("Loading FinBERT model")
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)

classifier = pipeline(
    "text-classification",
    model=model,
    tokenizer=tokenizer,
    top_k=None
)
print("FinBERT loaded.")


def analyze_post(text):
    scores = classifier(text)

    if isinstance(scores, list) and len(scores) > 0 and isinstance(scores[0], list):
        scores = scores[0]

    label_map = {"Positive": "Bullish", "Neutral": "Neutral", "Negative": "Bearish"}
    best = max(scores, key=lambda x: x["score"])
    return label_map.get(best["label"], "Neutral")

