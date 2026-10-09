# Sentiment Analysis & Emotion Detection Project

A Python-based NLP tool for analyzing overall sentiment and detailed emotion breakdown from text input. Built for Micro-IT, this project uses **NLTK (VADER & tokenization)** to classify sentiment and **Matplotlib** to generate emotion distribution charts.

---

## 🌟 Features

- **Overall Sentiment Polarity Analysis**: Uses NLTK's `SentimentIntensityAnalyzer` (VADER) to classify text as `positive`, `negative`, or `neutral`.
- **Emotion Keyword Mapping**: Parses tokens and matches them against a customizable `emotions.txt` dictionary (`happy`, `sad`, `angry`, `fear`, `surprise`, `neutral`, etc.).
- **Visual Chart Generation**: Automatically generates a bar chart saved as `emotion_chart.png` representing the breakdown of detected emotions.
- **Flexible CLI Interface**: Accepts text input via command-line flags or interactive prompts, with options for custom emotion dictionaries and output image locations.

---

## 📁 Project Structure

```text
Sentimental-Analysis-Project/
│
├── main.py              # Main execution script (CLI, tokenization, sentiment analysis, chart plotting)
├── emotions.txt         # Word-to-emotion mapping file
├── requirements.txt     # Python dependencies (matplotlib, nltk)
├── emotion_chart.png    # Output chart generated after execution
└── README.md            # Project documentation
```

---

## ⚙️ Installation & Setup

1. **Clone or navigate to the workspace**:
   ```bash
   cd Sentimental-Analysis-Project
   ```

2. **Create and activate a virtual environment** *(optional but recommended)*:
   ```bash
   python -m venv .venv
   # Windows (PowerShell)
   .\.venv\Scripts\Activate.ps1
   # Linux/macOS
   source .venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   *Note: On first run, `main.py` will automatically download the necessary NLTK datasets (`punkt_tab`, `stopwords`, `vader_lexicon`).*

---

## 🚀 Usage

### 1. Interactive Mode
Run `main.py` without arguments to enter text interactively:
```bash
python main.py
```
**Prompt:**
```text
Enter text to analyze: I had an amazing and happy day, but I felt scared for a moment!
```

### 2. Command Line Mode
Pass text directly via the `--text` or `-t` flag:
```bash
python main.py --text "I love this amazing product! It made me so happy and excited."
```

### 3. CLI Command Options

| Argument | Short | Description | Default |
| :--- | :--- | :--- | :--- |
| `--text` | `-t` | Text string to analyze | Interactive prompt if omitted |
| `--emotion-file` | `-e` | Path to custom word-to-emotion map file | `emotions.txt` |
| `--chart-output` | `-c` | Destination path for saved chart image | `emotion_chart.png` |
| `--show-chart` | | Display the generated matplotlib chart in a popup window | `False` |

---

## 📊 Example Output

**Console Output:**
```text
Detected emotions: {'happy': 2, 'fear': 1}
Chart saved to: emotion_chart.png
Overall sentiment: positive
```

---

## 📝 Customizing Emotions

You can edit `emotions.txt` or create your own custom emotion mapping file using the `word:emotion` format:
```text
love:happy
happy:happy
amazing:happy
hate:sad
scared:fear
wow:surprise
```

---

## 📄 License

This project was developed for Micro-IT.4
