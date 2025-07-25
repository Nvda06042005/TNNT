#minimax

1 – Mục đích & Nguyên lí hoạt động

Trò chơi được hiện thực trong thu.py dưới dạng một lớp duy nhất TicTacToe, có thể khởi tạo với mọi kích thước bàn cờ (N = 4, 5, 6, 8). Tại thời điểm khởi động, người dùng chọn N trên cửa sổ menu – sau đó cùng một mã nguồn điều khiển toàn bộ logic:

Tạo giao diện: vòng lặp hai cấp dựng ma trận Button theo self.size – không hard‑code từng ô【12†turn12file2†L11-L19】.

Xử lí lượt đi: mỗi ô gọi _on_click(r, c) thông qua functools.partial; hàm này gán ký tự X/O, kiểm tra trạng thái, tô màu ô thắng và khóa bàn cờ nếu cần【12†turn12file2†L28-L38】.

Kiểm tra thắng: chỉ một hàm _is_winning_move kiểm tra hàng, cột, đường chéo & chéo phụ ngay sau nước vừa đi, độ phức tạp O(N)【12†turn12file2†L47-L53】.

Nhờ cách thiết kế tổng quát, toàn bộ mã tránh trùng lặp (nguyên tắc DRY); kích thước mới (ví dụ 10×10) chỉ cần thêm một nút menu.

2 – Hướng dẫn chạy

# Cài đặt (Python >= 3.8; Tkinter có sẵn trên Windows/macOS/Linux)
python thu.py      # hoặc double‑click file

Chú ý: Nếu muốn khởi chạy bàn cờ cố định (ví dụ 6×6) mà bỏ qua menu, chỉ cần:

from thu import TicTacToe


3 – So sánh với mã slide mẫu (4×4)

Tiêu chí

Mẫu slide 4x4.py

Mã mới thu.py

Tạo giao diện

16 biến button1…button16, 48 dòng thiết lập & grid()

2 vòng for, 4 dòng code chính【12†turn12file2†L11-L19】

Điều kiện thắng

10 khối if/elif liệt kê tay【12†turn12file4†L18-L24】

1 hàm tổng quát _is_winning_move

Hỗ trợ kích thước khác

Cần sao chép file rồi viết lại toàn bộ danh sách nút & điều kiện

Không đổi logic; chỉ truyền size

Tính mở rộng / bảo trì

Cao độ trùng lặp → khó chỉnh sửa

Gọn gàng, dễ đọc, tuân theo KISS

Nhận xét tính đúng đắn

Với mọi N, hàm _is_winning_move kiểm tra đủ 4 hướng (hàng, cột, chéo chính, chéo phụ).

Sau mỗi nước đi hệ thống chỉ duyệt một hàng, một cột và tối đa hai đường chéo – đảm bảo hiệu năng tốt ngay cả N lớn.

Phần tô màu & khóa bàn cờ bảo đảm trạng thái GUI đồng bộ với logic.

4 – Giải thuật & Khác biệt so với slide

Mẫu trên slide sử dụng liệt kê tường minh (hard‑code) vì dễ nhìn nhưng:

Tăng nỗ lực gỡ lỗi: chỉ cần sai một biến button là điều kiện thắng sai.

Không mở rộng.

Trong mã mới, win‑check rút gọn thành:

row  = all(btn[r][j]['text'] == mark for j in range(n))
col  = all(btn[i][c]['text'] == mark for i in range(n))
diag = r == c and all(btn[i][i]['text'] == mark for i in range(n))
anti = r + c == n-1 and all(btn[i][n-1-i]['text'] == mark for i in range(n))

Kết quả tương đương nhưng sạch hơn, không cần chỉnh sửa khi thay đổi N.

Kết luận: thu.py cung cấp một kiến trúc generic và dễ bảo trì, giải quyết triệt để hạn chế của mã mẫu trên slide, đồng thời giữ nguyên trải nghiệm người dùng.


