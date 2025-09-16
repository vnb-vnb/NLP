# mô tả công việc trong lab 2

định nghĩa một interface cho Vectorizer và Tokenizer, đảm bảo rằng mọi lớp con sau này phải tuân thủ những phương thức chung như fit, transform, fit_transform đối với Vectorizer và tokenize đối với Tokenizer.

Triển khai CountVectorizer bằng việc kết hợp trực tiếp với RegexTokenizer đã có ở Lab 1,Trong CountVectorizer, đã cài đặt được cơ chế học vocabulary từ một tập văn bản, ánh xạ từng token sang một chỉ số, sau đó chuyển từng tài liệu thành vector số, trong đó giá trị tại mỗi vị trí thể hiện số lần token đó xuất hiện -> hoàn thiện được mô hình Bag-of-Words cơ bản.
sau đó thử nghiệm CountVectorizer với một corpus nhỏ gồm ba câu.

# kết quả chạy code

Vocabulary: {'.': 0, 'AI': 1, 'I': 2, 'NLP': 3, 'a': 4, 'is': 5, 'love': 6, 'of': 7, 'programming': 8, 'subfield': 9}
Document-Term Matrix:
[1, 0, 1, 1, 0, 0, 1, 0, 0, 0]
[1, 0, 1, 0, 0, 0, 1, 0, 1, 0]
[1, 1, 0, 1, 1, 1, 0, 1, 0, 1]

# giải thích kết quả

đã mã hóa thành công 3 đoạn văn bản theo định nghĩa trong vocabvocab
# có sự hỗ trợ của AI 