from typing import List
from src.core.interfaces import Vectorizer, Tokenizer


class CountVectorizer(Vectorizer):
    def __init__(self, tokenizer: Tokenizer):
        self.tokenizer = tokenizer
        self.vocabulary_: dict[str, int] = {}

    def fit(self, corpus: List[str]):

        unique_tokens = set()
        for doc in corpus:
            tokens = self.tokenizer.tokenize(doc)
            unique_tokens.update(tokens)

        # sắp xếp để giữ tính ổn định
        self.vocabulary_ = {token: idx for idx, token in enumerate(sorted(unique_tokens))}

    def transform(self, documents: List[str]) -> List[List[int]]:

        vectors = []
        vocab_size = len(self.vocabulary_)

        for doc in documents:
            vector = [0] * vocab_size
            tokens = self.tokenizer.tokenize(doc)
            for token in tokens:
                if token in self.vocabulary_:
                    idx = self.vocabulary_[token]
                    vector[idx] += 1
            vectors.append(vector)

        return vectors

    def fit_transform(self, corpus: List[str]) -> List[List[int]]:

        self.fit(corpus)
        return self.transform(corpus)
