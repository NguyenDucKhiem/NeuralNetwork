Project: Dự đoán số bệnh nhân nhập viện liên quan đến các bệnh về hô hấp Singapore.

Hàm đánh giá: MSE (Mean Square Error)
Thư viện sử dụng: Keras
Backend sử dụng thư viện: tensorflow

Mô hình mạng noron:
  Đầu vào: 4 trường year, week, chỉ số psi, chỉ số rain
  Lớp ẩn: 4 lớp ẩn với số lượng nút mạng tương ứng 5-5-5-3-1 và 2 lớp dropout, các lớp sử dụng hàm activation: tanh
  Đầu ra: 1 trường số lượng bênh nhân (2000~4000)
_________________________________________________________________
Layer (type)                 Output Shape              Param #
=================================================================
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
=================================================================
Total params: 107
Trainable params: 107
Non-trainable params: 0

Trước khi train dữ liệu cần được batch normalization (-1 ~ 1) để dễ dàng sử lí và tốt khi sử dụng hàm tanh
Phân chia tập dữ liệu ra làm 3 phần train(80%), val(11%), test(9%)

Quá trình train sử dùng optimizers Adam với learning rate 0.0001 để học tập
Sử dụng Callbacks:
    EarlyStopping: để kiểm tra loss của tập val. Nếu loss val trong 5 epochs không giảm thì tự động dừng quá trình train
    TensorBoard: để tạo sơ đồ quan sát quá trình train
    CSVLogger: ghi lại loss, val_loss với mi epoch
