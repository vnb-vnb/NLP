from abc import ABC, abstractmethod 
from typing import List 
class Tokenizer(ABC):
    @abstractmethod 
    def tokenize(self, text : str) -> List[str]:
        """
        Tokenizes the input text into a list of tokens.
        
        Args:
            text (str): The input text to tokenize.
        
        Returns:
            List[str]: A list of tokens.
        """
        pass 