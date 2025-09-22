import re
from typing import List
from src.core.interfaces import Tokenizer


class RegexTokenizer(Tokenizer):
    def tokenize(self, text: str) -> List[str]:
        """
\w+ : match các từ hoặc số (ví dụ "hello", "123").

[^\w\s] : match ký tự không phải từ (\w) và không phải khoảng trắng (\s) → tức là dấu câu (.,!?;...)

Dấu | : nghĩa là "hoặc".

Kết hợp lại → tách text thành từ/cụm số và dấu câu riêng biệt. """
        tokens = re.findall(r"\w+|[^\w\s]", text)# re.findall() sẽ tìm các kí tự đáp ứng yêu cầu của chúng ta bên trong dấu ngoặc 
        return tokens
