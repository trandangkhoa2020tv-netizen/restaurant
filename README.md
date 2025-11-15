# restaurant
sytem restaurant
I. Functional requirement
Nhà hàng cần xây dựng hệ thống quản lý đặt món trực tuyến với một số tính năng cơ bản sau:
- Xem và tìm kiếm món ăn:
 Khách hàng có thể xem danh sách món ăn theo loại thực đơn. Danh sách món có thể được sắp xếp (tăng hoặc giảm) theo giá, mức độ phổ biến, hoặc mức giảm giá (nếu có).
 Khách hàng có thể tìm kiếm món ăn bằng cách nhập từ khóa. Hệ thống sẽ trả về danh sách các món có tên hoặc mô tả chứa từ khóa đó. Danh sách kết quả có thể sắp xếp (tăng hoặc giảm) theo giá, mức độ phổ biến, hoặc đánh giá của khách hàng.
- Chọn và đặt món:
+Mỗi món ăn có mã số riêng, hình ảnh minh họa, mô tả chi tiết về nguyên liệu và khẩu vị, giá bán, tình trạng món (còn hay hết) và số lượt đặt. Mỗi món thuộc về một nhóm thực đơn cụ thể như món chính, món phụ, món chay hoặc thức uống.
 Khi khách hàng xem hoặc tìm kiếm món ăn, với mỗi món trong danh sách, khách có thể đưa món được chọn vào giỏ đặt món hiện tại, hoặc xem chi tiết thông tin về món ăn đó.
 Khi đang xem thông tin chi tiết về món ăn, khách hàng cũng có thể thêm món được chọn vào giỏ đặt món, đồng thời ghi chú các yêu cầu đặc biệt như “ít cay”, “không hành”, “thêm phô mai”, “nhiều đá”, v.v.
 Trong quá trình chọn và đặt món, khách hàng có thể xem danh sách các món đã thêm vào giỏ, cập nhật giỏ đặt món (thay đổi số lượng, chỉnh sửa ghi chú hoặc loại bỏ món ra khỏi giỏ).
 Sau khi đã chọn xong các món cần đặt, khách hàng chọn chức năng đặt bàn hoặc giao hàng để xác nhận đơn đặt món và tiến hành thanh toán.
+ Quy trình đặt món:
Hệ thống sẽ yêu cầu khách hàng đăng nhập hệ thống nếu khách hàng chưa đăng nhập, hoặc đăng ký khách hàng mới nếu khách chưa có tài khoản trong hệ thống (xem thêm chi tiết về cách đăng ký khách hàng mới).
Khách hàng nhập thông tin về đơn đặt món, bao gồm họ tên, số điện thoại, địa chỉ hoặc vị trí bàn (nếu ăn tại chỗ). Lưu ý là người đặt món có thể khác với người nhận món (ví dụ như khi khách đặt giúp bạn bè hoặc người thân).
Khách hàng chọn hình thức sử dụng món: ăn tại chỗ, mang đi, hoặc giao tận nơi.
Nếu đặt món thành công, hệ thống sẽ ghi nhận đơn đặt món của khách hàng, bao gồm thông tin các món được đặt (tên món, số lượng, đơn giá), thông tin người đặt và người nhận, hình thức phục vụ, tổng trị giá đơn đặt món, thời điểm đặt món và phương thức thanh toán.
-Đăng ký,cập nhật tài khoản khách hàng:
 Khách hàng có thể đăng ký tài khoản trong hệ thống để sử dụng các chức năng đặt món và theo dõi đơn hàng.
 Thông tin khách hàng bao gồm: họ tên, ngày sinh, giới tính, địa chỉ, số điện thoại, mật khẩu và địa chỉ email (email được dùng làm tên đăng nhập, đồng thời dùng cho việc nhận thông tin đơn đặt món hoặc khôi phục mật khẩu khi cần).
 Khách hàng có thể cập nhật tất cả các thông tin cá nhân của mình, ngoại trừ tên đăng nhập (địa chỉ email).
-Xem các món đã đặt:
+ Khách hàng có thể xem lại danh sách các đơn đặt món đã thực hiện và tình trạng của từng đơn (Mới đặt, Đã xác nhận, Đang chế biến, Đang giao, Hoàn tất, Đã hủy)
 Khách hàng có thể hủy đơn đặt món nếu trạng thái của đơn vẫn đang ở mức mới đặt.
- Quản lý đặt món ăn: 
            +Nhân viên có thể xem danh sách đơn hàng và cập nhật trạng thái (xác nhận, chế biến, hoàn tất, hủy).
- Phân quyền hệ thống: 
            + Người quản trị viên có quyền quản lý toàn bộ hệ thống.
            + Nhân viên có thể có quyền: quản lý đơn, cập nhật trạng thái, hoặc quản lý món trong khu vực phụ trách.
            + Việc tạo thêm nhân viên giúp phân quyền rõ ràng hơn và tăng tính bảo mật, tránh quản trị viên phải làm tất cả.
- Quản trị hệ thống: Người quản trị có các chức năng sau:
	+ Quản lý món ăn 
	+ Quản lý người dùng
	+ Quản lý đơn đặt món
    + Quản lý nhân viên 
    
II.Non-Functional Requirements
-Usability
    Giao diện thân thiện, dễ sử dụng cho cả khách hàng và nhân viên nhà hàng.Hỗ trợ tiếng việt,Tự động điều chỉnh bố cục theo kích thước màn hình trên các thiết bị
-Reliability
    Hệ thống phải hoạt động liên tục 24/7. Độ tin cậy > 99.9%.
-Performance
    Hệ thống có thể đáp ứng cùng lúc nhiều khách hàng truy cập đồng thời.
-Supportability
    Dễ dàng bảo trì và mở rộng trong tương lai.
-Security
    Khách hàng chỉ được phép xem và quản lý thông tin tài khoản và đơn đặt món của chính mình.
-Design Constraints
    ệ thống hoạt động trên nền tảng web, phát triển bằng Python.