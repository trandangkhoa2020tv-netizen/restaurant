# ============================================================
# LỚP NGƯỜI DÙNG CHUNG (User)
# ============================================================
class User:
    def __init__(self, name, dob, gender, address, phone, email, password, role="customer"):
        self.name = name          # Họ tên
        self.dob = dob            # Ngày sinh
        self.gender = gender      # Giới tính
        self.address = address    # Địa chỉ
        self.phone = phone        # Số điện thoại
        self.email = email        # Email đăng nhập
        self.password = password  # Mật khẩu
        self.role = role          # Vai trò (customer / staff / admin)


# ============================================================
# LỚP KHÁCH HÀNG (Customer)
# ============================================================
class Customer(User):
    def __init__(self, name, dob, gender, address, phone, email, password):
        super().__init__(name, dob, gender, address, phone, email, password, "customer")


# ============================================================
# LỚP NHÂN VIÊN (Staff)
# ============================================================
class Staff(User):
    def __init__(self, name, dob, gender, address, phone, email, password):
        super().__init__(name, dob, gender, address, phone, email, password, "staff")


# ============================================================
# LỚP QUẢN TRỊ (Admin)
# ============================================================
class Admin(User):
    def __init__(self, name, dob, gender, address, phone, email, password):
        super().__init__(name, dob, gender, address, phone, email, password, "admin")
