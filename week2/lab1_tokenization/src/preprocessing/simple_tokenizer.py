# src/preprocessing/simple_tokenization.py
from src.core.interfaces import Tokenizer 
from typing import List 
import re 

class SimpleTokenizer(Tokenizer): 
    def tokenize(self, text : str) -> List[str]:
        """
        Tokenizes the input text by converting to lowercase, splitting on whitespace,
        and handling basic punctuation as separate tokens.
        
        Args:
            text (str): The input text to tokenize.
        
        Returns:
            List[str]: A list of tokens.
        """
        # Convert text to lowercase
        text = text.lower()
        
        # Replace punctuation with a space before and after to split it as separate tokens
        # This handles . , ? ! as specified
        text = re.sub(r'([.,?!])', r' \1 ', text)
        
        # Split on whitespace and filter out empty tokens
        tokens = [token for token in text.split() if token]
        
        return tokens