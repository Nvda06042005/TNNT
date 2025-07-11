

#  Convolutional Neural Network – Minh hoạ với **Số 0**
> Notebook thực hành: **`CNN_ZERO_theory_practice.ipynb`**

Một hướng dẫn từ A → Z về cách CNN trích xuất đặc trưng và phân loại ảnh, minh hoạ **bằng chữ số 0** viết tay (ma trận 6 × 6) và huấn luyện trên **MNIST**.

---

## 📂 Cấu trúc notebook

| Phần | Nội dung | Cell |
|------|----------|------|
| **1 · Giới thiệu CNN** | Vì sao CNN “thấy” được ảnh, so sánh với mạng fully‑connected. | Markdown |
| **2 · Bóc tách thủ công** | Ảnh `6×6` số 0 → Convolution → ReLU → Max Pooling → FC → Softmax. Tính tay *feature map* kích thước `4×4`. | Code + bảng |
| **3 · Mô hình PyTorch** | Hai tầng `Conv → ReLU → Pool` + `FC` (10 lớp). | lớp `MNIST_CNN` |
| **4 · Huấn luyện MNIST** | 5 epoch, SGD `lr=0.01`, hiển thị Loss & Accuracy. | Loop + plot |
| **5 · Đánh giá & Trực quan** | Accuracy test ≈ 98 %, hiển thị 5 ảnh dự đoán & 2 feature maps đầu. | Hàm `visualize_…` |

---

## 🔧 Cài đặt nhanh

```powershell
:: Windows PowerShell
python -m venv .venv
.\.venv\Scripts\Activate.ps1          # macOS / Linux: source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install torch torchvision matplotlib notebook
```

> **Lưu ý Windows:** nếu `python` mở Microsoft Store, tắt *App execution aliases* → **Settings ▸ Apps ▸ Advanced app settings ▸ App execution aliases**.

---

## 🚀 Chạy notebook  

### 1 · Mở giao diện Jupyter

```bash
jupyter notebook CNN_ZERO_theory_practice.ipynb
```

Sau khi trình duyệt mở, chọn **Kernel ▸ Restart & Run All**.

### 2 · Chạy headless (CI / batch)

```bash
jupyter nbconvert --to notebook --execute CNN_ZERO_theory_practice.ipynb                   --output CNN_ZERO_run.ipynb
```

File *CNN_ZERO_run.ipynb* chứa toàn bộ kết quả (tính toán xong, không cần GUI).

---

## 📊 Kết quả mong đợi

| Bước | Hình minh hoạ | Mô tả |
|------|---------------|-------|
| Ảnh gốc (6×6) | ![zero](assets/zero6x6.png) | Số 0 viền ngoài = 1, bên trong = 0. |
| Feature Map (Conv) | ![fm](assets/conv_map.png) | Đường ngang trên sáng rõ (`3`). |
| Sau ReLU | ![relu](assets/relu_map.png) | Giá trị âm → 0, chỉ giữ đặc trưng mạnh. |
| Max Pooling 2×2 | ![pool](assets/pool_map.png) | Kích thước ↓, vẫn giữ điểm sáng. |
| Softmax FC | — | `P(0) ≈ 0.92`, `P(!0) ≈ 0.08`. |

> *Hình trong thư mục `assets/` do notebook sinh tự động.*

---

## 🎓 Tham khảo

* LeCun Y. *et al.*, “Gradient-based learning applied to document recognition”, 1998.  
* Stanford CS231n – *Convolutional Neural Networks for Visual Recognition*.

---

