from word_embedder import WordEmbedder 

# --- 1. Khởi tạo WordEmbedder ---
embedder = WordEmbedder("glove-wiki-gigaword-50")

# --- 2. Lấy vector của từ 'king' ---
vector_king = embedder.get_vector("king")
print("Vector của 'king':")
print(vector_king[:10])  # In 10 giá trị đầu tiên

# --- 3. Tính độ tương đồng ---
sim_king_queen = embedder.get_similarity("king", "queen")
sim_king_man = embedder.get_similarity("king", "man")
print(f"\nSimilarity (king, queen): {sim_king_queen:.4f}")
print(f"Similarity (king, man): {sim_king_man:.4f}")

# --- 4. Lấy 10 từ tương tự với 'computer' ---
print("\n10 từ giống 'computer' nhất:")
for word, score in embedder.get_most_similar("computer", top_n=10):
    print(f"{word:15s} {score:.4f}")

# --- 5. Nhúng câu (Document Embedding) ---
sentence = "The queen rules the country."
doc_vector = embedder.embed_document(sentence)
print("\nVector biểu diễn câu:")
print(doc_vector[:10])  # In 10 phần tử đầu tiên
