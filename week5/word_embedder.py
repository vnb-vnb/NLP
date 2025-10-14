from gensim.downloader import load
import numpy as np

class WordEmbedder:
    def __init__(self, model_name: str = "glove-wiki-gigaword-50"):
        """
        Tải mô hình word embedding pre-trained từ gensim.
        """
        print(f"🔹 Loading model '{model_name}'")
        self.model = load(model_name)
        print("Model loaded successfully!")

    def get_vector(self, word: str):
        """
        Trả về vector embedding của từ.
        Nếu từ không có trong vocabulary → trả về vector 0.
        """
        if word in self.model:
            return self.model[word]
        else:
            print(f" '{word}' không có trong từ điển (OOV).")
            return np.zeros(self.model.vector_size)

    def get_similarity(self, word1: str, word2: str):
        """
        Tính độ tương đồng cosine giữa 2 từ.
        """
        if word1 not in self.model or word2 not in self.model:
            print(f" Một trong hai từ '{word1}', '{word2}' không có trong từ điển.")
            return 0.0
        return self.model.similarity(word1, word2)

    def get_most_similar(self, word: str, top_n: int = 10):
        """
        Trả về top N từ gần nghĩa nhất với từ cho trước.
        """
        if word not in self.model:
            print(f" '{word}' không có trong từ điển (OOV).")
            return []
        return self.model.most_similar(word, topn=top_n)

    def get_document_vector(self, text: str):
        """
        Nhúng một câu/văn bản bằng cách lấy trung bình vector của các từ trong đó.
        """
        tokens = text.lower().split()
        vectors = [self.model[word] for word in tokens if word in self.model]
        if not vectors:
            print(" Không có từ nào trong văn bản thuộc vocabulary của mô hình.")
            return np.zeros(self.model.vector_size)
        return np.mean(vectors, axis=0)
    
    def embed_document(self, document: str):
        """
        Nhúng cả một văn bản (document) thành 1 vector duy nhất.
        Sử dụng trung bình vector của các từ có trong mô hình (bỏ qua OOV).
        """
        import re
        from gensim.utils import simple_preprocess

        # Tách token đơn giản (giống Lab 1)
        tokens = simple_preprocess(document)

        # Lấy vector cho những từ có trong mô hình
        vectors = [self.model[word] for word in tokens if word in self.model]

        if not vectors:
            print(" Không có từ nào thuộc vocabulary trong document.")
            return np.zeros(self.model.vector_size)

        # Tính trung bình cộng các vector từ
        return np.mean(vectors, axis=0)
