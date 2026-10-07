import argparse
import string
from collections import Counter
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize

DEFAULT_EMOTION_FILE = Path(__file__).with_name("emotions.txt")
DEFAULT_OUTPUT_FILE = Path(__file__).with_name("emotion_chart.png")


def ensure_nltk_data():
    """Download the minimal NLTK datasets needed by this project."""
    required = ["punkt_tab", "stopwords", "vader_lexicon"]
    for dataset in required:
        try:
            if dataset == "punkt_tab":
                nltk.data.find("tokenizers/punkt_tab")
            else:
                nltk.data.find(dataset)
        except LookupError:
            nltk.download(dataset, quiet=True)


def extract_features(text):
    ensure_nltk_data()
    text = text.lower()
    cleaned = text.translate(str.maketrans("", "", string.punctuation))
    tokens = word_tokenize(cleaned, language="english")
    filtered = []
    for word in tokens:
        if word not in stopwords.words("english") and word.strip():
            filtered.append(word)
    return filtered


def load_emotions(path):
    emotion_path = Path(path)
    if not emotion_path.exists():
        default_mapping = (
            "love:happy\n"
            "happy:happy\n"
            "amazing:happy\n"
            "great:happy\n"
            "good:happy\n"
            "excellent:happy\n"
            "hate:sad\n"
            "sad:sad\n"
            "bad:sad\n"
            "angry:angry\n"
            "fear:fear\n"
            "scared:fear\n"
            "surprised:surprise\n"
            "wow:surprise\n"
            "neutral:neutral\n"
        )
        emotion_path.write_text(default_mapping, encoding="utf-8")

    emotions = {}
    with emotion_path.open("r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line or ":" not in line:
                continue
            word, emotion = [part.strip().lower() for part in line.split(":", 1)]
            if word and emotion:
                emotions[word] = emotion
    return emotions


def count_emotions(text, emotion_map):
    matched = []
    for word in text:
        if word in emotion_map:
            matched.append(emotion_map[word])
    return Counter(matched)


def plot_emotions(counter, output_file, show_chart=False):
    output_path = Path(output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    fig, ax = plt.subplots(figsize=(8, 5))
    labels = list(counter.keys())
    values = list(counter.values())
    if labels:
        ax.bar(labels, values, color=["#4CAF50", "#F44336", "#FF9800", "#2196F3", "#9C27B0"][: len(labels)])
        ax.set_title("Emotion Distribution")
        ax.set_xlabel("Emotion")
        ax.set_ylabel("Count")
        fig.autofmt_xdate()
        fig.tight_layout()
        fig.savefig(output_path, dpi=150)
        if show_chart:
            plt.show()
    else:
        fig, ax = plt.subplots()
        ax.text(0.5, 0.5, "No matching emotions found", ha="center", va="center")
        ax.axis("off")
        fig.savefig(output_path, dpi=150)
        if show_chart:
            plt.show()
    plt.close(fig)


def analyse_sentiment(text):
    ensure_nltk_data()
    sentiment_score = SentimentIntensityAnalyzer().polarity_scores(text)
    negative = sentiment_score["neg"]
    positive = sentiment_score["pos"]
    if negative > positive:
        return "negative"
    if positive > negative:
        return "positive"
    return "neutral"


def main():
    parser = argparse.ArgumentParser(description="Sentiment analysis for short text input.")
    parser.add_argument("--text", "-t", help="Text to analyze.")
    parser.add_argument("--emotion-file", "-e", default=str(DEFAULT_EMOTION_FILE), help="Path to a word-to-emotion file.")
    parser.add_argument("--chart-output", "-c", default=str(DEFAULT_OUTPUT_FILE), help="Path for the saved emotion chart image.")
    parser.add_argument("--show-chart", action="store_true", help="Display the chart in a window.")
    args = parser.parse_args()

    ensure_nltk_data()

    user_text = args.text or input("Enter text to analyze: ").strip()
    if not user_text:
        raise SystemExit("No text provided.")

    cleaned_words = extract_features(user_text)
    emotion_map = load_emotions(args.emotion_file)
    emotion_counts = count_emotions(cleaned_words, emotion_map)

    if emotion_counts:
        print(f"Detected emotions: {dict(emotion_counts)}")
        plot_emotions(emotion_counts, args.chart_output, args.show_chart)
        print(f"Chart saved to: {args.chart_output}")
    else:
        print("No emotion keywords matched the provided text.")

    sentiment = analyse_sentiment(user_text)
    print(f"Overall sentiment: {sentiment}")


if __name__ == "__main__":
    main()
