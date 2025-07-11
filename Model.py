from transformers import pipeline

# Load pre-trained sentiment analysis pipeline (or any other classification task)
model = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

def predict(text: str):
    return model(text)
if __name__ == "__main__":
    result = predict("I love this product!")
    print(result)
