# Mô tả công việc trong lab1 : Trong Lab 1, em xây dựng các bộ tách từ (tokenizers) và kiểm thử chúng trên văn bản mẫu cũng như dữ liệu thực tế từ bộ UD_English-EWT.

Cài đặt Tokenizer Interface (trong src/core/interfaces.py)

Xây dựng một lớp trừu tượng (abstract class) tên là Tokenizer.

Lớp này định nghĩa phương thức tokenize(text: str) -> List[str] mà tất cả các tokenizer khác đều phải triển khai.

Cài đặt SimpleTokenizer (trong src/preprocessing/simple_tokenizer.py)

Chuyển văn bản về chữ thường (lowercase).

Tách dấu câu cơ bản (. , ? !) ra khỏi từ bằng cách thêm khoảng trắng xung quanh chúng.

Tách token bằng cách split theo khoảng trắng.

Lọc bỏ các token rỗng.

chưa xử lý tốt các trường hợp phức tạp (ví dụ: "isn't" bị tách thành "isn" và "t").

Cài đặt RegexTokenizer (trong src/preprocessing/regex_tokenizer.py)

Sử dụng biểu thức chính quy (regex) \w+|[^\w\s].

\w+ bắt các từ hoặc số liên tiếp.

[^\w\s] bắt các ký tự không phải chữ/số và không phải khoảng trắng (tức là dấu câu).

Kiểm thử trên ví dụ thủ công trong main.py

Các câu kiểm thử:

"Hello, world! This is a test."

"NLP is fascinating... isn't it?"

"Let's see how it handles 123 numbers and punctuation!"

So sánh output giữa SimpleTokenizer và RegexTokenizer.

Kiểm thử trên dữ liệu thật (Task 3 – UD_English-EWT)

Viết hàm load_raw_text_data (trong src/core/dataset_loaders.py) để đọc file văn bản.

Lấy 500 ký tự đầu tiên của văn bản để kiểm thử.

Tokenize bằng cả 2 tokenizer, in ra 20 token đầu tiên để so sánh.

# kết quả chạy code

--- Tokenizing Sample Text from UD_English-EWT ---
Original Sample: Al-Zaman : American forces killed Shaikh Abdullah al-Ani, the preacher at the  
mosque in the town of ...
SimpleTokenizer Output (first 20 tokens): ['al-zaman', ':', 'american', 'forces', 'killed', 'shaikh', 'abdullah', 'al-ani', ',', 'the', 'preacher', 'at', 'the', 'mosque', 'in', 'the', 'town', 'of', 'qaim', ',']
RegexTokenizer Output (first 20 tokens): ['Al', '-', 'Zaman', ':', 'American', 'forces', 'killed', 'Shaikh', 'Abdullah', 'al', '-', 'Ani', ',', 'the', 'preacher', 'at', 'the', 'mosque', 'in', 'the']

# giải thích kết quả

Khi chạy thử nghiệm trên tập dữ liệu UD_English-EWT, ta thấy hai bộ tokenizer hoạt động theo cách khá khác nhau. Với SimpleTokenizer, toàn bộ câu được chuyển về dạng chữ thường và những dấu câu cơ bản như dấu phẩy, chấm, chấm hỏi hay chấm than được tách thành token riêng. Kết quả là chuỗi token khá sạch, dễ đọc và giữ được nghĩa cơ bản của văn bản. Ví dụ như “Al-Zaman” vẫn giữ nguyên thành một token duy nhất ở dạng viết thường “al-zaman”

Trong khi đó, RegexTokenizer lại có cách tiếp cận chi tiết hơn khi tách dấu gạch nối thành token riêng, khiến cho “Al-Zaman” bị chia thành ba phần “Al”, “-”, “Zaman”. Điều này làm số lượng token nhiều hơn nhưng đồng thời cung cấp mức độ chi tiết cao hơn, vì mọi dấu câu, ký tự đặc biệt đều được coi như một token riêng biệt. Kết quả là output của RegexTokenizer nhìn có phần rời rạc hơn nhưng lại chính xác trong việc phân tách cấu trúc văn bản thô.

Khi thử nghiệm với CountVectorizer, ta thấy sự khác biệt giữa việc áp dụng trên corpus nhỏ và toàn bộ dataset. Với văn bản mẫu ngắn, vocabulary khá hạn chế, thường chỉ xoay quanh vài chục từ và ma trận document-term còn nhỏ nên dễ quan sát. Nhưng khi áp dụng lên UD_English-EWT, số lượng từ vựng tăng lên rất nhiều, ma trận trở nên thưa thớt và kích thước lớn hơn đáng kể.

MMột trong những khó khăn lớn nhất là xử lý các trường hợp đặc biệt như dấu gạch nối hay chữ viết hoa. Nếu chọn cách đơn giản thì một số cụm từ cố định có thể bị tách rời mất ý nghĩa. Ngược lại, nếu xử lý chi tiết như RegexTokenizer thì sẽ tạo ra nhiều token rời rạc làm tăng độ phức tạp của vocabulary

## bài làm có sự trợ giúp của trí thông minh nhân tạo
