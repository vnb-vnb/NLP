import re
from typing import List
from src.core.interfaces import Tokenizer


class RegexTokenizer(Tokenizer):
    def tokenize(self, text: str) -> List[str]:
        """
        Tokenize text using regex.
        Splits words and keeps punctuation as separate tokens.

        Example regex: \w+|[^\w\s]
        """
        # \w+ matches words/numbers, [^\w\s] matches punctuation
        tokens = re.findall(r"\w+|[^\w\s]", text)
        return tokens
