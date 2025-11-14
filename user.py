# ============================================================
# LỚP NGƯỜI DÙNG CHUNG (User)
# Đây là lớp cha (parent class) chứa các thông tin cơ bản của
# mọi loại người dùng trong hệ thống: Customer, Staff, Admin
# ============================================================

class User:
    def __init__(self, name, phone, email, password, role="customer"):
        # Thông tin chung cho mọi người dùng
        self.name = name            # Họ tên
        self.phone = phone          # Số điện thoại
        self.email = email          # Email đăng nhập
        self.password = password    # Mật khẩu
        self.role = role            # Vai trò (customer / staff / admin)


# ============================================================
# LỚP KHÁCH HÀNG (Customer)
# Kế thừa (inherit) từ User và đặt role mặc định là "customer"
# ============================================================

class Customer(User):
    def __init__(self, name, phone, email, password):
        # Gọi constructor của lớp cha (User)
        super().__init__(name, phone, email, password, "customer")


# ============================================================
# LỚP NHÂN VIÊN (Staff)
# Dùng để phân quyền nhân viên phục vụ
# ============================================================

class Staff(User):
    def __init__(self, name, phone, email, password):
        # role được đặt cố định là "staff"
        super().__init__(name, phone, email, password, "staff")


# ============================================================
# LỚP QUẢN TRỊ (Admin)
# Dành cho người có quyền cao nhất trong hệ thống
# ============================================================

class Admin(User):
    def __init__(self, name, phone, email, password):
        # role được đặt cố định là "admin"
        super().__init__(name, phone, email, password, "admin")
