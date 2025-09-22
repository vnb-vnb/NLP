from abc import ABC, abstractmethod 
from typing import List 
# một khung chuẩn cho mọi tokenizer khác 
class Tokenizer(ABC):
    @abstractmethod 
    def tokenize(self, text : str) -> List[str]:

        pass 