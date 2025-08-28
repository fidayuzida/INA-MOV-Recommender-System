# 🎬 Movie Recommender System (Content-Based)

Sistem rekomendasi film berbasis konten yang menggunakan **bag-of-words** (CountVectorizer) dan **cosine similarity** untuk menemukan film mirip berdasarkan **title, genre, actors, dan description**.

## ✨ Fitur
- Menggabungkan `title + genre + actors + description` menjadi fitur teks `tags`.
- Vectorization dengan **CountVectorizer** (`max_features=500`, stop_words='english').
- Perhitungan **cosine similarity** untuk mencari film paling mirip.
- Fungsi rekomendasi yang mengembalikan Top-5 film terdekat.
- Ekspor artefak model: 
  - `movies.pkl`  
  - `movies_dict.pkl`  
  - `similarity.pkl`

## 🧱 Metodologi
1. **Preprocessing**  
   - Menghapus data duplikat dan nilai kosong.  
   - Membuat kolom `tags` sebagai gabungan metadata film.

2. **Vectorization**  
   - Menggunakan CountVectorizer untuk mengubah teks menjadi representasi numerik.

3. **Similarity Computation**  
   - Menggunakan **cosine similarity** untuk mengukur kemiripan antar film.

4. **Inference**  
   - Memberikan rekomendasi film mirip berdasarkan judul input.
