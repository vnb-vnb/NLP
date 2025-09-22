from typing import List
from src.core.interfaces import Vectorizer, Tokenizer  # Import interface Vectorizer và Tokenizer đã định nghĩa trước đó


# ------------------ CountVectorizer ------------------
class CountVectorizer(Vectorizer):
    def __init__(self, tokenizer: Tokenizer):
        # Nhận vào một tokenizer để xử lý text thành token
        self.tokenizer = tokenizer
        # Từ điển ánh xạ: token -> chỉ số (index trong vector)
        self.vocabulary_: dict[str, int] = {}

    def fit(self, corpus: List[str]):
        """
        Xây dựng từ điển (vocabulary) từ toàn bộ corpus.
        - corpus: danh sách văn bản (List[str]).
        """

        unique_tokens = set()  # set là kiểu dữ liệu tập hợp không chứa phần tử trùng lặp,không có thứ tự, ở đây được dùng để lấy các kí tự duy nhất và trả về vd: [1, 2, 2, 3, 4, 4] -> {1, 2, 3, 4} hoặc "hello" -> {'h', 'e', 'l', 'o'} 
        for doc in corpus:
            tokens = self.tokenizer.tokenize(doc)  # Tokenize từng văn bản
            unique_tokens.update(tokens)           # Thêm token vào tập hợp, update() : thêm nhiều phần tử vào set một lần 

        # Sắp xếp token để đảm bảo thứ tự ổn định
        # Sau đó đánh index cho từng token (token -> index)
        self.vocabulary_ = {token: idx for idx, token in enumerate(sorted(unique_tokens))}

    def transform(self, documents: List[str]) -> List[List[int]]:
        """
        Biến đổi danh sách văn bản thành ma trận đếm (Count Vectors).
        - documents: danh sách văn bản cần biến đổi.
        - Output: List[List[int]], mỗi văn bản thành một vector số nguyên.
        """

        vectors = []                       # Danh sách lưu vector cho từng document
        vocab_size = len(self.vocabulary_) # Số lượng token trong từ điển

        for doc in documents:
            vector = [0] * vocab_size                # Khởi tạo vector đếm (ban đầu toàn 0)
            tokens = self.tokenizer.tokenize(doc)    # Tokenize văn bản
            for token in tokens:
                if token in self.vocabulary_:        # Nếu token có trong từ điển
                    idx = self.vocabulary_[token]    # Lấy chỉ số của token
                    vector[idx] += 1                 # Tăng số đếm cho token đó
            vectors.append(vector)                   # Thêm vector vào danh sách kết quả

        return vectors

    def fit_transform(self, corpus: List[str]) -> List[List[int]]:
        """
        Kết hợp fit và transform trong một bước.
        - corpus: danh sách văn bản.
        - Output: ma trận đếm cho toàn bộ corpus.
        """

        self.fit(corpus)             # Xây dựng từ điển từ corpus
        return self.transform(corpus) # Biến đổi corpus thành vector đếm
