# 🧩 Lab 02 – Artificial Intelligence  
## TH 06 & TH 07 · Backtracking giải Bài toán **4‑Queens** & **8‑Queens**

> **File Notebook:** `TH_2.ipynb`  
> **Ngôn ngữ:** Python 3.8 +   |   **Thuật toán:** Backtracking

---

## 1 · Bài toán & Mục tiêu

| Thực hành | Bàn cờ | Số quân hậu | Số lời giải *(kỳ vọng)* |
|-----------|--------|-------------|-------------------------|
| **TH 06** | 4 × 4  | 4 | 2 |
| **TH 07** | 8 × 8  | 8 | 92 |

Đặt *N* quân hậu lên bàn cờ *N × N* sao cho **không quân hậu nào tấn công nhau** (hàng, cột, và hai đường chéo).  
Notebook giúp bạn:

1. Hiểu quy tắc tấn công của quân hậu.  
2. Triển khai **thuật toán Backtracking** sinh tất cả cấu hình hợp lệ.  
3. Đếm & hiển thị lời giải, in tọa độ và minh họa bàn cờ.

---

## 2 · Tại sao backtracking hoạt động?

### Đại diện trạng thái  
- `state = [c₀, c₁, …, cₖ]` – cột của quân hậu đã đặt ở mỗi **hàng**.  
- Số hàng đã đặt = `len(state)`.

### Hàm ứng viên `get_candidates()`  
Ở hàng `r = len(state)` cần thử mọi cột `0…N‑1`, loại bỏ cột **bị tấn công** bởi các quân trước:

```text
• Cùng cột:            c == cᵢ
• Đường chéo chính:    c == cᵢ + (r - rᵢ)
• Đường chéo phụ:      c == cᵢ - (r - rᵢ)
```

### Thuật toán `search()`  

```python
def search(state):
    if len(state) == N:          # đặt đủ N quân hậu
        solutions.append(state); return

    for col in get_candidates(state):
        state.append(col)        # bước đi ↘
        search(state)            # đệ quy
        state.pop()              # back‑track ↩
```

Nhờ **pruning** ở `get_candidates`, không gian tìm kiếm được cắt giảm mạnh; ví dụ 8‑Queens chỉ còn ~15k nhánh thay vì 8⁸ (~16 triệu).

---

## 3 · Cấu trúc mã

| Hàm | Vai trò |
|-----|---------|
| `is_valid_state()` | (phiên bản demo) kiểm tra khi đã đặt đủ N |
| `get_candidates()` | Sinh cột hợp lệ kế tiếp |
| `search()` | Backtracking (đệ quy + back‑track) |
| `solve()` | Bao hàm `search`, trả về *list* lời giải |
| `main` block | Nhập N, in bảng trống, gọi `solve`, hiển thị kết quả |

---

## 4 · Hướng dẫn sử dụng

```bash
git clone https://github.com/<user>/AI-Lab02-Queens.git
cd AI-Lab02-Queens
pip install notebook numpy
jupyter notebook TH_2.ipynb
```

1. **Chạy** từng ô (*Shift + Enter*).  
2. Khi được hỏi, nhập `N = 4` (TH 06) hoặc `N = 8` (TH 07).  
3. Notebook sẽ:  
   - In **bảng cờ trống** *N × N*.  
   - Tìm tất cả lời giải (`solve`).  
   - In tổng số lời giải và hiển thị từng lời giải với toạ độ.

### CLI nhanh (tùy chọn)

```bash
python th2_cli.py 8      # in 92 lời giải 8‑Queens
```

---

## 5 · Ví dụ đầu ra

### 4‑Queens

```
Tổng số lời giải tìm được: 2

🔹 Lời giải 1: [1, 3, 0, 2]
- Q - -
- - - Q
Q - - -
- - Q -
tọa độ: [(1,0),(3,1),(0,2),(2,3)]
```

### 8‑Queens (hiển thị 2 lời giải ngẫu nhiên)

```
Tổng số lời giải tìm được: 92

random 2 lời giải ... 1: [0, 6, 3, 5, 7, 1, 4, 2]
Q - - - - - - -
- - - - - - Q -
- - - Q - - - -
- - - - - Q - -
- - - - - - - Q
- Q - - - - - -
- - - - Q - - -
- - Q - - - - -
```

---

## 6 · Nếu chương trình “bị gì”…

| Dấu hiệu | Nguyên nhân | Cách khắc phục |
|----------|-------------|----------------|
| **Không dừng** ở 8‑Queens | `is_valid_state` thiếu check `len(state) == N` | Bảo đảm trả về **True** khi đủ N quân hậu |
| **Lời giải > 92** | Quên `state.pop()` khi back‑track | Thêm `state.pop()` sau lời gọi đệ quy |
| **IndexError** ở `candidates.discard(col ± dist)` | `col ± dist` vượt `0…N‑1` nhưng `discard()` an toàn – kiểm tra lại phép trừ | Giữ nguyên `discard` (an toàn), hoặc thêm `if 0 <= value < N` |

---

## 7 · Mở rộng

- **Dòng lệnh `-v`** in chi tiết quá trình back‑track.  
- Lọc **lời giải khác biệt hình học** (sử dụng phép xoay / phản chiếu).  
- Thử **Heuristic Search** (Hill‑Climbing, Min‑Conflicts) cho N lớn (N = 100+).

---

## 8 · License
MIT


