#Chức năng chính của code
Notebook này triển khai hai thuật toán tìm kiếm trên đồ thị vô hướng:
Thuật toán BFS (Breadth-First Search): Duyệt đồ thị theo chiều rộng, dùng cấu trúc hàng đợi để lần lượt thăm các nút theo từng tầng. Hàm bfs(graph, start, goal) trả về đường đi ngắn nhất (tính theo số bước) từ nút bắt đầu start đến nút đích goal trên đồ thị không trọng số
. Ngoài ra, biến thể bfs_weighted(graph, start, goal) được cung cấp để duyệt đồ thị có trọng số (vẫn dùng hàng đợi FIFO) và tính tổng trọng số trên đường đi tìm được.
Thuật toán DFS (Depth-First Search): Duyệt đồ thị theo chiều sâu, sử dụng đệ quy (tương đương với ngăn xếp) để đi sâu từng nhánh trước khi quay lại nhánh khác. Hàm dfs(graph, start, goal) tìm một đường đi từ start đến goal bằng cách ưu tiên đi sâu nhất có thể (không đảm bảo đó là đường đi ngắn nhất)
. Tương tự, hàm dfs_weighted(graph, start, goal) minh họa duyệt sâu trên đồ thị có trọng số.
Mỗi thuật toán đều in ra đường đi tìm được dưới dạng danh sách các đỉnh từ nguồn đến đích. Chẳng hạn, với Đồ thị mẫu 1 (đồ thị vô hướng không trọng số), cả BFS và DFS đều tìm ra đường đi S → B → E → G
. Tuy nhiên, BFS đảm bảo đây là đường đi ngắn nhất về số bước, trong khi DFS chỉ tìm được một đường (không nhất thiết ngắn nhất). Trên Đồ thị mẫu 5 (đồ thị có trọng số), kết quả cho thấy BFS tìm được đường đi S → A → G với tổng trọng số 4
, nhưng đó chưa chắc là đường tối ưu nhất vì BFS không xét trọng số cạnh (thuật toán BFS/DFS không đảm bảo tổng trọng số nhỏ nhất).

#Cách chạy notebook 
Mở Notebook: Tải file BFS-DFS.ipynb vào môi trường Jupyter Notebook hoặc Google Colab đã cài đặt Python 3.7+.
Chạy tuần tự các ô mã: Thực hiện lần lượt từng ô (cell) code theo thứ tự từ trên xuống dưới. Notebook được chia thành các phần chính:
Phần lý thuyết – Mô tả khái quát về BFS và DFS, sự khác biệt giữa đồ thị trọng số và không trọng số, kèm ví dụ minh họa.
Ví dụ minh họa thủ công – Các bước BFS và DFS được trình bày tuần tự bằng liệt kê (kèm sơ đồ Mermaid) để thấy rõ quá trình duyệt hàng đợi/ngăn xếp và tập đỉnh đã thăm. Ví dụ, quá trình BFS/DFS trên Đồ thị mẫu 1 được liệt kê từng bước, cho thấy trạng thái hàng đợi hoặc ngăn xếp và tập visited sau mỗi bước thăm nút.
Triển khai mã Python – Định nghĩa các hàm bfs, dfs và các biến thể có trọng số, sau đó chạy thử trên các đồ thị mẫu (được khai báo sẵn dưới dạng dictionary) để in ra kết quả tìm kiếm. Người dùng có thể đối chiếu kết quả này với phần minh họa thủ công ở trên để kiểm chứng tính đúng đắn.
Tương tác và thử nghiệm: Notebook có các bài tập yêu cầu người dùng tự thực hành, ví dụ: chỉnh sửa thuật toán BFS để đếm số nút đã thăm, hoặc chạy BFS/DFS trên đồ thị mới. Bạn có thể thử thay đổi cấu trúc đồ thị (danh sách kề) hoặc thay đổi nút bắt đầu/đích, rồi chạy lại hàm để quan sát kết quả. Việc này giúp hiểu sâu hơn cách thuật toán hoạt động trên các trường hợp khác nhau.

#Mục đích và ứng dụng
Notebook “BFS-DFS” được thiết kế cho mục đích giáo dục, thuộc học phần nhập môn Trí tuệ Nhân tạo về thuật toán tìm kiếm mù (uninformed search). Thông qua các ví dụ và bài tập trong notebook, người học có thể:
Hiểu và triển khai thuật toán BFS và DFS trên các đồ thị vô hướng, bao gồm cả trường hợp không trọng số và có trọng số. Điều này xây dựng nền tảng về cách duyệt đồ thị một cách có hệ thống.
So sánh đặc điểm của BFS và DFS: Nhận biết rằng BFS đảm bảo tìm được đường đi ngắn nhất trên đồ thị không trọng số (vì mỗi cạnh xem như chi phí bằng nhau)
, còn DFS thì không đảm bảo tối ưu về độ dài đường đi
. Trên đồ thị có trọng số, notebook cũng nhấn mạnh hạn chế của BFS/DFS – chúng không được thiết kế để tối ưu tổng trọng số, dẫn đến kết quả không tối ưu
. Từ đó gợi ý cần sử dụng thuật toán khác (như Dijkstra hoặc A*) để tìm đường đi tối ưu nhất khi các cạnh có trọng số.
Áp dụng vào thực tiễn: Kiến thức từ notebook có thể áp dụng vào các bài toán tìm đường trong mê cung, lưới ô vuông hoặc mạng lưới đồ thị. Thuật toán BFS thường được dùng để tìm đường đi ngắn nhất khi mỗi bước có chi phí như nhau (ví dụ: tìm đường ngắn nhất trong game, trên bản đồ lưới), trong khi DFS hữu ích cho duyệt cây trạng thái, giải các bài toán đòi hỏi thử – sai (backtracking), hoặc khám phá không gian tìm kiếm khi không ưu tiên độ dài đường đi.
