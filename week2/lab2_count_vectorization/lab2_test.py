import sys
import os

# Thêm đường dẫn của lab1_tokenization/src vào sys.path
sys.path.append(os.path.abspath("../lab1_tokenization/src"))

from preprocessing.regex_tokenizer import RegexTokenizer
from src.representations.count_vectorizer import CountVectorizer



def test_count_vectorizer():
    # Khởi tạo tokenizer
    tokenizer = RegexTokenizer()

    # Khởi tạo CountVectorizer với tokenizer
    vectorizer = CountVectorizer(tokenizer)

    # Corpus mẫu
    corpus = [
        "I love NLP.",
        "I love programming.",
        "NLP is a subfield of AI."
    ]

    # Fit và transform
    dt_matrix = vectorizer.fit_transform(corpus)

    # In ra vocabulary
    print("Vocabulary:", vectorizer.vocabulary_)

    # In ra Document-Term Matrix
    print("Document-Term Matrix:")
    for row in dt_matrix:
        print(row)


if __name__ == "__main__":
    test_count_vectorizer()
