# Lab 3 – Thuật Toán Di Truyền (Genetic Algorithm) với Python


## 0. Tại sao cần Thuật Toán Di Truyền?

- **Thuật Toán Di Truyền (GA)** mô phỏng cơ chế **tiến hoá tự nhiên**: chọn lọc – lai ghép – đột biến.  
- Dùng GA khi bài toán:
  * Hàm mục tiêu **khó đạo hàm** hoặc có nhiều cực trị.  
  * Không gian tìm kiếm **rộng**, không biết điểm khởi tạo tốt.  
  * Muốn **xấp xỉ nghiệm tốt** thay vì nghiệm chính xác tuyệt đối.

`lab3.ipynb` hướng dẫn bạn từng bước xây mô hình GA **từ con số 0**.

---

## 1. Thư viện & vì sao cần chúng

| Thư viện           | Lý do dùng                                                                                   |
|--------------------|----------------------------------------------------------------------------------------------|
| **numpy**          | Tính toán số học nhanh, đặc biệt là thao tác mảng (`np.argmax`, v.v.).                       |
| **random** (built-in) | Sinh số ngẫu nhiên, chọn mẫu ngẫu nhiên (`random.sample`, `random.uniform`).                |
| **matplotlib.pyplot** | Vẽ biểu đồ: đường học (fitness theo thế hệ), scatter plot quần thể.                         |
| **Jupyter Notebook**  | Môi trường chạy code + ghi chú Markdown tương tác (cực tiện cho bài lab).                  |

> ✅ **Không** cần pandas, scikit-learn, hay thư viện GA phức tạp – toàn bộ thuật toán được code **thủ công** để bạn thấy rõ cơ chế.

---

## 2. Cài đặt môi trường

```bash
git clone https://github.com/<username>/<repo>.git
cd <repo>

# (Tuỳ chọn) tạo và kích hoạt virtualenv
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate

# Cài thư viện tối thiểu
#pip install numpy matplotlib notebook
#Nếu muốn dùng pip install -r requirements.txt bạn chỉ việc tạo file yêu cầu.

## 3. Chạy notebook
#jupyter notebook lab3.ipynb
'''Chọn Kernel → Restart & Run All để chạy toàn bộ.

Mỗi cell có chú thích tiếng Việt, cứ đọc từ trên xuống dưới.

## 4. Giải phẫu Notebook
## 4.1. Bài 1 – GA tối ưu hàm 1 biến

| Thành phần                   | Code trong `lab3.ipynb`                                               | Giải thích nhanh                            |
| ---------------------------- | --------------------------------------------------------------------- | ------------------------------------------- |
| `fitness_function(x)`        | `return -(x**2) + 10*x + 50` (mẫu) **hoặc** `math.sin(x)+math.cos(x)` | Hàm mục tiêu, GA **muốn MAX** giá trị này.  |
| `initialize_population`      | Tạo danh sách `pop_size` số thực random                               | Quần thể khởi tạo.                          |
| `select_parents`             | **Tournament Selection** (k=3)                                        | Chọn cá thể tốt nhất trong 3 cá thể random. |
| `crossover`                  | Trung bình 2 cha mẹ (`(p1+p2)/2`)                                     | Sinh con mới.                               |
| `mutate`                     | Đột biến – thay cá thể = random nếu `rand < mutation_rate`            | Tạo đa dạng gen.                            |
| `genetic_algorithm_example1` | Vòng lặp GA đầy đủ                                                    | In kết quả & vẽ đồ thị tiến hoá.            |

## 4.2. Bài 2 – GA tối ưu hàm 2 biến
#Tương tự Bài 1 nhưng cá thể = cặp (x, y) và phương thức lai/đột biến xử lý 2 thành phần.

## 4.3. Bài 3 – Ảnh hưởng tham số
'''Bạn sẽ thay các tham số dưới đây ngay trong cell:
genetic_algorithm_example1(
    pop_size=100,
    generations=200,
    crossover_rate=0.9,
    mutation_rate=0.02
)
Quan sát đồ thị fitness: hội tụ nhanh/chậm thế nào?

4.4. Bài 4 – So sánh phương pháp chọn lọc
Thêm hàm select_parents_roulette (Roulette Wheel). Thay thế trong vòng lặp GA và đo tốc độ hội tụ so với Tournament.

4.5. Bài 5 – Trực quan hoá quần thể
Lưu toạ độ quần thể mỗi thế hệ → vẽ scatter plot (x, y).
Khi hàm tối ưu 3 biến, bạn có thể vẽ từng cặp: (x,y), (x,z), (y,z).

## 5. Ví dụ chạy nhanh

### 5.1  Tối ưu $h(x)=\sin x+\cos x$

```python
import math
best_x, best_h = genetic_algorithm_example1(
    pop_size=50,
    generations=100,
    min_val=0,
    max_val=2*math.pi
)
print(f"x* ≈ {best_x:.4f} rad, h(x*) ≈ {best_h:.4f}")
# Kỳ vọng x* ≈ π/4 (0.7854) với h(x*) ≈ √2 ≈ 1.4142

## 5&nbsp;· Ví dụ chạy nhanh — Hàm hai biến

Hàm gốc cần **cực tiểu**:  
$$f(x,y)=x^{2}+y^{2}$$

↳ Chuyển thành hàm **cực đại** để GA xử lý:  
$$g(x,y)=-(x^{2}+y^{2})$$

Nghiệm chuẩn: $(x^{\*},y^{\*})=(0,0)$ cho $f_{\min}=0$.

<p align="center">
  <img src="https://i.imgur.com/oqAgUGo.png" width="450" alt="Fitness chart">
</p>

*Biểu đồ: giá trị fitness tốt nhất giảm dần về 0 trong quá trình tiến hoá.*

```python
# Ví dụ chạy
best_xy, best_f = genetic_algorithm_example2(
    pop_size=60,
    generations=150,
    min_val=-5,
    max_val=5
)
print("Điểm gần tối ưu:", best_xy, "f≈", best_f)
# Kỳ vọng gần (0,0) với f ≈ 0









