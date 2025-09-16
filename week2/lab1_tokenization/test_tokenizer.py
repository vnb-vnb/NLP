# test_tokenizer.py
from src.preprocessing.simple_tokenizer import SimpleTokenizer

def test_simple_tokenizer():
    tokenizer = SimpleTokenizer()
    
    # Test cases
    test_cases = [
        ("Hello, world!", ["hello", ",", "world", "!"]),
        ("This is a test.", ["this", "is", "a", "test", "."]),
        ("What's up? Let's go!", ["what's", "up", "?", "let's", "go", "!"]),
        ("No punctuation", ["no", "punctuation"]),
        ("", [])  # Empty input
    ]
    
    for input_text, expected in test_cases:
        result = tokenizer.tokenize(input_text)
        assert result == expected, f"Failed for input '{input_text}'. Expected {expected}, but got {result}"
        print(f"Input: {input_text}\nOutput: {result}\n")
    
    print("All tests passed!")

if __name__ == "__main__":
    test_simple_tokenizer()