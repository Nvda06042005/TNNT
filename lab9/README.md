
# Thực hành 20–24: DFS, BFS & Q‑learning

> **Môn học:** Nhập môn Học tăng cường (Reinforcement Learning)  
> **Tệp notebook:** `hoc_tang_cuong.ipynb`  
> **Ngôn ngữ:** Python 3.10 + Jupyter Notebook

Notebook này tổng hợp **5 bài thực hành liên tiếp (TH20 → TH24)** giúp bạn từng bước
khám phá ba thuật toán kinh điển – **DFS, BFS** và **Q‑learning** – trong bối cảnh
tìm đường trên lưới (maze/grid world).

| Mã bài | Thuật toán | Kịch bản | Mục tiêu chính |
|--------|------------|----------|----------------|
| TH20 | DFS | Mê cung 6 × 6 | Hiểu cơ chế ngăn xếp & back‑tracking |
| TH21 | DFS (biến thể) | Mê cung thay chướng ngại vật | So sánh hành vi DFS khi môi trường đổi |
| TH22 | BFS | Lưới 5 × 5 | Tìm đường *ngắn nhất* bằng hàng đợi |
| TH23 | BFS (nâng cao) | Lưới 6 × 6 nhiều chướng ngại | Thấy rõ tối ưu hoá độ dài đường đi |
| TH24 | Q‑learning | GridWorld 4 × 4 (16 trạng thái) | Học chính sách tối ưu không cần mô hình |

---

## 1. Nguyên lý hoạt động của mã

### 1.1 DFS (Depth‑First Search)

* **Ý tưởng:** Đi sâu nhất có thể theo một nhánh trước khi quay lui.  
* **Triển khai:**  
  * Dùng đệ quy hoặc *stack* (list) để lưu các ô kế tiếp.  
  * Mỗi ô có 4 hướng `(lên, xuống, trái, phải)`; bỏ qua ô vượt biên hoặc đã thăm.  
  * Dừng khi tới đích hoặc hết nước đi.  

### 1.2 BFS (Breadth‑First Search)

* **Ý tưởng:** Duyệt theo *lớp* (level‑order) đảm bảo đường đầu tiên tới đích là ngắn nhất.  
* **Triển khai:**  
  * Sử dụng `collections.deque` làm hàng đợi.  
  * Mỗi bước: `popleft()` một ô, thêm hàng xóm hợp lệ vào đuôi hàng đợi.  
  * Lưu mảng `parent` để truy vết đường đi sau khi tìm thấy đích.  

### 1.3 Q‑learning (Tabular RL)

* **Môi trường:** 4 × 4 = 16 trạng thái, 4 hành động (N, S, W, E), đích ở trạng thái 15.  
* **Cập nhật:**  
  ```python
  Q[s, a] += α * (r + γ * max(Q[s′]) - Q[s, a])
  ```  
  * `α` = 0.1 (learning‑rate), `γ` = 0.9 (discount), `ε`‑greedy để cân bằng *explore/exploit*.  
* **Kết quả:** Sau ~1 000 epoch, ma trận Q hội tụ; heat‑map cho thấy giá trị tăng dần
  khi tiến gần mục tiêu.

---

## 2. Hướng dẫn cài đặt

1. **Clone / tải** repository (hoặc chỉ tệp notebook):  
   ```bash
   git clone <repo-url>
   cd <repo>/   # chứa hoc_tang_cuong.ipynb
   ```
2. **Tạo môi trường & cài phụ thuộc** (khuyến nghị dùng `venv` hoặc `conda`):  
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```
   Nếu không có `requirements.txt`, cài nhanh:  
   ```bash
   pip install jupyter numpy matplotlib
   ```

---

## 3. Cách chạy notebook

```bash
jupyter notebook hoc_tang_cuong.ipynb
```

* Mở tệp trong trình duyệt ➜ **Run** ▶ từng ô từ trên xuống.  
* Mỗi bài thực hành nằm trong một tiêu đề Markdown bắt đầu bằng `## THỰC HÀNH XX`.  
* Sau khi chạy xong, quan sát:  
  * **DFS/BFS** in ra lộ trình & trực quan hoá trên ma trận.  
  * **Q‑learning** hiển thị biểu đồ nhiệt giá trị Q.

**Mẹo:** Nếu muốn chạy nhanh toàn bộ, vào menu **Kernel → Restart & Run All**.

---

## 4. Thử nghiệm nhanh trên CLI *(tuỳ chọn)*

Bạn có thể tách mã của từng thuật toán thành file `.py` và chạy:

```bash
python dfs_maze.py            # TH20 / TH21
python bfs_grid.py            # TH22 / TH23
python q_learning_grid.py     # TH24
```

Ví dụ cấu trúc tối thiểu của `dfs_maze.py` đã có sẵn trong ô code TH20.

---

## 5. Thư mục / tệp quan trọng

```
├─ hoc_tang_cuong.ipynb   # Notebook gốc (bạn đang đọc)
├─ README.md              # Tài liệu này
└─ requirements.txt       # (tùy chọn) Danh sách thư viện
```

---

## 6. Giấy phép

Mã nguồn & notebook phát hành theo giấy phép **MIT** –
thoải mái sử dụng cho mục đích học tập & nghiên cứu.

---

> **Chúc bạn thực hành vui vẻ!** Nếu gặp lỗi, hãy kiểm tra lần lượt:  
> 1. Phiên bản Python ≥ 3.8,  
> 2. Cài đủ `numpy`, `matplotlib`, `jupyter`,  
> 3. Chạy lại kernel & thực thi lại các ô (Restart & Run All).
