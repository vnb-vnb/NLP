from abc import ABC, abstractmethod   # Dùng để định nghĩa lớp trừu tượng (Abstract Base Class)
from typing import List               # Dùng để khai báo kiểu dữ liệu (List)

# ---------------- Lớp Vectorizer ----------------
class Vectorizer(ABC):  # Lớp trừu tượng: đóng vai trò "interface" cho các vectorizer cụ thể
    @abstractmethod
    def fit(self, corpus: List[str]):
        """
        Học thông tin từ dữ liệu văn bản (corpus).
        - corpus: danh sách các văn bản (List[str]).
        - Mục đích: xây dựng "từ vựng" hoặc cấu trúc để vector hóa.
        Ví dụ: trong Bag-of-Words thì fit() sẽ đếm toàn bộ từ để lập từ điển.
        """
        pass

    @abstractmethod
    def transform(self, documents: List[str]) -> List[List[int]]:
        """
        Biến đổi một danh sách văn bản thành vector (sử dụng từ điển/tập từ đã học ở fit).
        - documents: danh sách văn bản cần biến đổi.
        - Output: danh sách vector (mỗi văn bản thành một vector số nguyên).
        """
        pass

    @abstractmethod
    def fit_transform(self, corpus: List[str]) -> List[List[int]]:
        """
        Thực hiện fit và transform cùng lúc.
        - corpus: danh sách văn bản.
        - Output: danh sách vector cho toàn bộ corpus.
        - Thường dùng khi vừa muốn học từ điển vừa muốn biến đổi dữ liệu ngay.
        """
        pass

# ---------------- Lớp Tokenizer ----------------
class Tokenizer(ABC):  # Lớp trừu tượng: chuẩn hóa "giao diện" cho các tokenizer
    @abstractmethod 
    def tokenize(self, text : str) -> List[str]:
        """
        Chia một chuỗi văn bản thành danh sách token (từ, dấu câu...).
        - text: chuỗi văn bản đầu vào.
        - Output: List[str] = danh sách token.
        - Cách tokenize cụ thể sẽ do lớp con định nghĩa (theo khoảng trắng, regex, BPE...).
        """
        pass
