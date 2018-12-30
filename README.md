Project: Dự đoán số bệnh nhân nhập viện liên quan đến các bệnh về hô hấp Singapore.

Hàm đánh giá: MSE (Mean Square Error)
Thư viện sử dụng: Keras
Backend sử dụng thư viện: tensorflow
Thư viện phân chia dữ liệu: sklearn
Thư viện làm việc dữ liệu: numpy
Thư viện đọc ghi file csv: csv

Thư mục:
  ./dataset: chứa các dữ liệu. Phải có 3 file .
		Weekly infectious.csv (lưu dữ liệu số lượng bênh nhân theo tuần).
		rainfall-monthly-number-of-rain-days.csv(lưu dữ liệu lượng mưa theo từng tháng).
		psi.csv (lưu dữ liệu chỉ số psi).
                                              
  ReadCSV.py: đọc các file dữ liệu và chuyển đổi dữ liệu sang dạng số.
  ReadFile.py: đọc 3 file dữ liệu và mix dữ liệu.
  Training.py: chứa model, đọc dữ liệu đã mix, normalize dữ liệu, training, trả về kết quả trong thư mục ./seed_*.
  Plot.py đọc kết quả train và vẽ biểu đồ.
  
  ./seed_*: gồm thư mục logs chứa TensorBoard mỗi lần training.
		log.txt: chứa thông tin mỗi lần training.
		logger.csv: chứa giá trị loss, val_loss mỗi epoch lần training cuối cùng.
		result.csv: chứa dữ liệu và kết quả sau đi qua mạng.

Mô hình mạng noron:
  Đầu vào: 4 trường year, week, chỉ số psi, chỉ số rain.
  Lớp ẩn: 4 lớp ẩn với số lượng nút mạng tương ứng 5-5-5-3-1 và 2 lớp dropout, các lớp sử dụng hàm activation: tanh.
  Đầu ra: 1 trường số lượng bênh nhân (2000~4000).
  
_________________________________________________________________
Layer (type)                 Output Shape              Param #
_________________________________________________________________
data (InputLayer)            (None, 4)                 0
_________________________________________________________________
layer (Dense)                (None, 5)                 25
_________________________________________________________________
layer_2 (Dense)              (None, 5)                 30
_________________________________________________________________
dropout_1 (Dropout)          (None, 5)                 0
_________________________________________________________________
layer_3 (Dense)              (None, 5)                 30
_________________________________________________________________
layer_4 (Dense)              (None, 3)                 18
_________________________________________________________________
dropout_2 (Dropout)          (None, 3)                 0
_________________________________________________________________
layer_output (Dense)         (None, 1)                 4
_________________________________________________________________
Total params: 107
Trainable params: 107
Non-trainable params: 0

Trước khi train dữ liệu cần được batch normalization (-1 ~ 1) để dễ dàng sử lí và tốt khi sử dụng hàm tanh.
Phân chia tập dữ liệu ra làm 3 phần train(80%), val(11%), test(9%).

Quá trình train sử dùng optimizers Adam với learning rate 0.0001 để học tập.
Sử dụng Callbacks:
    EarlyStopping: để kiểm tra loss của tập val. Nếu loss val trong 5 epochs không giảm thì tự động dừng quá trình train.
    TensorBoard: để tạo sơ đồ quan sát quá trình train.
    CSVLogger: ghi lại loss, val_loss với mỗi epoch.

Cách cài đặt:
	Các thư viện cần cài: keras, tensorflow, numpy, csv, sklearn.
	Tạo thư mục dataset với 3 file dữ liệu (bệnh nhân, psi, lượng mưa). Nếu tên file dữ liệu thay đổi chỉnh sửa trong file ReadCSV.py
	Tạo file mix dữ liệu bằng cách chạy file ReadFile.py terminal: python3 ReadFile.py
	Chỉnh sửa seed, phân chia tập dữ liệu (biến test_size, val_size, random_state) trong file Tranning.py
	Training bằng cách chạy file Trainning.py terminal: python3 Trainning.py
	Xem TensorBoard bằng lệnh terminal: tensorboard --logdir=./seed_*/logs
Xem biểu đồ kết quả đạt được bằng chạy Plot.py terminal: python3 Graph.py [<đường dẫn result>]. Ví dụ: python3 Graph.py ./seed_52/result.csv có thể nhập nhiều đường dẫn liên tiếp
