import re
from gensim.utils import simple_preprocess
from gensim.models import Word2Vec
import os

file_path = r"D:\\project\\nlp\\week2\\lab1_tokenization\\src\data\\en_ewt-ud-train.txt"

print(f"🔹 Đang đọc dữ liệu từ: {file_path}")
with open(file_path, "r", encoding="utf-8") as f:
    text = f.read()

# Chia nhỏ văn bản thành câu, rồi tokenize từng câu
sentences = [simple_preprocess(sent) for sent in re.split(r"[.!?]", text) if sent.strip()]
print(f"✅ Số câu thu được: {len(sentences)}")
print(f"➡️  Ví dụ token đầu tiên: {sentences[0][:10]}")

# --- 2️⃣ Huấn luyện mô hình Word2Vec ---
print("\n🔹 Đang huấn luyện mô hình Word2Vec...")
model = Word2Vec(
    sentences=sentences,
    vector_size=100,   # Số chiều vector
    window=5,          # Kích thước cửa sổ ngữ cảnh
    min_count=2,       # Bỏ qua từ xuất hiện <2 lần
    workers=4,         # Sử dụng 4 luồng CPU
    sg=1               # 1 = Skip-gram, 0 = CBOW
)

print("✅ Huấn luyện xong mô hình Word2Vec!")

# --- 3️⃣ Lưu mô hình ---
os.makedirs("results", exist_ok=True)
save_path = os.path.join("results", "word2vec_ewt.model")
model.save(save_path)
print(f"💾 Mô hình đã được lưu tại: {save_path}")

# --- 4️⃣ Tải lại mô hình ---
loaded_model = Word2Vec.load(save_path)
print("✅ Mô hình đã được tải lại thành công!")

# --- 5️⃣ Demo sử dụng mô hình ---
word = "computer"
if word in loaded_model.wv:
    print(f"\n🔹 Từ tương tự với '{word}':")
    for w, s in loaded_model.wv.most_similar(word, topn=10):
        print(f"{w:15s} {s:.4f}")
else:
    print(f"⚠️ Từ '{word}' không có trong từ điển.")

# Thử độ tương đồng giữa các từ
pairs = [("king", "queen"), ("king", "man"), ("woman", "man")]
for w1, w2 in pairs:
    if w1 in loaded_model.wv and w2 in loaded_model.wv:
        sim = loaded_model.wv.similarity(w1, w2)
        print(f"\n🔹 Similarity({w1}, {w2}) = {sim:.4f}")
    else:
        print(f"⚠️ Một trong hai từ '{w1}', '{w2}' không có trong từ điển.")
