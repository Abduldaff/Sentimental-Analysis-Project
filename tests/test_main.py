import unittest
from pathlib import Path
import tempfile

import main


class SentimentAnalysisTests(unittest.TestCase):
    def test_extract_features_removes_punctuation_and_stopwords(self):
        features = main.extract_features("I love this product! It is amazing.")
        self.assertIn("love", features)
        self.assertIn("product", features)
        self.assertIn("amazing", features)
        self.assertNotIn("i", features)

    def test_analyse_sentiment_positive(self):
        self.assertEqual(main.analyse_sentiment("I love this product and it is amazing"), "positive")

    def test_load_emotions_handles_missing_file(self):
        missing_path = Path(tempfile.gettempdir()) / "missing_emotion_file.txt"
        data = main.load_emotions(missing_path)
        self.assertIsInstance(data, dict)


if __name__ == "__main__":
    unittest.main()
