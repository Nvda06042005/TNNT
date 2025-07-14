# 🔎 BÀI TẬP CNN - PHÂN LOẠI CHỮ SỐ VIẾT TAY (MNIST)

Đây là một **bài thực hành đầy đủ** hướng dẫn cách xây dựng và huấn luyện mạng nơ-ron tích chập (CNN) đơn giản với tập dữ liệu MNIST.  
File `CNN-LAB.ipynb` đã được **hoàn thiện** với đầy đủ lời giải, biểu đồ và giải thích chi tiết bằng tiếng Việt.

---

## 📚 Mục tiêu bài tập

1. Hiểu và áp dụng được các khái niệm cơ bản của CNN:
   - Tầng **Conv2D** (tích chập)
   - **ReLU** (hàm kích hoạt)
   - **MaxPooling** (giảm kích thước ảnh)
   - **Fully Connected Layer** (phân loại)
2. Huấn luyện mạng để nhận dạng ảnh chữ số viết tay kích thước 28x28.
3. Thay đổi các siêu tham số để thấy được ảnh hưởng đến kết quả:
   - Số **epoch**
   - Số tầng **tích chập**
   - Giá trị **learning rate**
4. Trực quan hóa **feature map** để thấy mô hình học cái gì bên trong.

---

## 🧑‍💻 Dành cho người mới bắt đầu

> Nếu bạn chưa biết gì, chỉ cần làm theo 5 bước sau:

### ✅ Cài đặt và chạy thử

```bash
# 1. Tải project về (nếu dùng GitHub)
git clone <LINK_GITHUB_CỦA_BẠN>
cd cnn-lab

# 2. Tạo môi trường ảo (khuyến khích)
python -m venv .venv
# Bật môi trường:
# Windows:
.venv\Scripts\activate
# macOS / Linux:
source .venv/bin/activate

# 3. Cài đặt thư viện cần thiết
pip install torch torchvision matplotlib notebook

# 4. Mở Jupyter Notebook
jupyter notebook
# => Trình duyệt mở ra, chọn file CNN-LAB.ipynb

📝 Gợi ý: Bạn cũng có thể mở notebook này bằng VS Code (mở file .ipynb là chạy được).

📁 Các tệp trong thư mục
| Tên tệp                | Chức năng                                                     |
| ---------------------- | ------------------------------------------------------------- |
| `CNN-LAB.ipynb`        | File chính: chứa toàn bộ code, biểu đồ và lời giải 4 câu hỏi. |
| `CNN-LAB_backup.ipynb` | Bản sao lưu của file gốc (chưa chỉnh sửa).                    |
| `README.md`            | Tệp bạn đang đọc – hướng dẫn cách cài đặt và sử dụng.         |
| `data/`                | Thư mục chứa dữ liệu MNIST (sẽ tự tạo khi chạy lần đầu).      |

📌 Nội dung notebook CNN-LAB.ipynb
Bạn chỉ cần chạy lần lượt từng ô lệnh trong notebook (từ trên xuống) là được.

Câu hỏi 1: Tăng số epoch
Mục tiêu: thấy được khi huấn luyện lâu hơn thì mô hình sẽ chính xác hơn như thế nào.

Kết quả: loss giảm, accuracy tăng nhẹ.

Câu hỏi 2: Thêm tầng conv3
Mục tiêu: tăng độ sâu mạng để học được đặc trưng phức tạp hơn.

Kết quả: mạng mạnh hơn → độ chính xác cao hơn (~99%).

Câu hỏi 3: Thử nghiệm learning rate
Mục tiêu: hiểu sự ảnh hưởng của learning rate (quá nhỏ thì học chậm, quá lớn thì dao động).

So sánh 3 trường hợp: 0.001, 0.01, 0.1

Câu hỏi 4: Trực quan feature map
Mục tiêu: xem được các đặc trưng (biên, cạnh, họa tiết) mà mạng học được qua từng tầng.

📈 Kết quả kỳ vọng
| Mô hình    | Epoch | Learning rate | Độ chính xác test |
| ---------- | ----- | ------------- | ----------------- |
| CNN 2 tầng | 5     | 0.01          | \~98.4%           |
| CNN 2 tầng | 10    | 0.01          | \~98.8%           |
| CNN 3 tầng | 10    | 0.01          | \~99.1%           |
| CNN 3 tầng | 10    | 0.001         | \~97.8%           |
| CNN 3 tầng | 10    | 0.1           | ⚠️ Không ổn định  |
Mỗi lần chạy có thể khác nhau ± 0.2% tùy vào dữ liệu và máy tính.

💡 Mở rộng thêm (tự nghiên cứu)
Thêm Dropout hoặc BatchNorm2d để chống overfitting.

Thử thay SGD bằng Adam.

Thêm các phép biến đổi ảnh (rotation, flip, noise...).

Thay dataset từ MNIST → FashionMNIST để thử thách hơn.

📌 Lưu ý & Giải đáp nhanh
| Câu hỏi                            | Trả lời                                                                 |
| ---------------------------------- | ----------------------------------------------------------------------- |
| Không có GPU thì sao?              | Mã sẽ tự chạy bằng CPU. Huấn luyện chậm hơn một chút nhưng vẫn OK.      |
| Có cần Internet không?             | Lần đầu chạy cần tải dữ liệu (\~11MB). Sau đó không cần nữa.            |
| Chạy bằng Google Colab được không? | Có thể. Chỉ cần upload file `.ipynb` vào Colab, bật GPU và chạy từng ô. |

📚 Tài liệu tham khảo
Tài liệu chính thức PyTorch

CS231n - Stanford CNN Notes

Bài giảng CNN cơ bản – DeepLearning.AI
