import random
import string
from user import Customer, Staff, Admin

# Danh sách chứa tất cả user đã đăng ký
users = []

def register():
    print("\n=== ĐĂNG KÝ TÀI KHOẢN ===")
    name = input("Họ tên: ")
    dob = input("Ngày sinh (dd/mm/yyyy): ")
    gender = input("Giới tính (Nam/Nữ): ")
    address = input("Địa chỉ: ")
    phone = input("Số điện thoại: ")
    email = input("Email (dùng làm đăng nhập): ")
    password = input("Mật khẩu: ")

    while True:
        print("\nChọn vai trò:")
        print("1. Customer (Khách hàng)")
        print("2. Staff (Nhân viên)")
        print("3. Admin (Quản trị viên)")
        role_choice = input("Chọn(1-3): ")

        if role_choice == "1":
            role = "customer"
            user = Customer(name, dob, gender, address, phone, email, password)
            break

        elif role_choice == "2":
            role = "staff"
            user = Staff(name, dob, gender, address, phone, email, password)
            break

        elif role_choice == "3":
            role = "admin"
            user = Admin(name, dob, gender, address, phone, email, password)
            break

        else:
            print("Lựa chọn không hợp lệ, vui lòng chọn lại.")

    # Lưu user
    users.append(user)
    print(f"\nĐăng ký {role} thành công!\n")

def login():
    print("\n=== ĐĂNG NHẬP ===")
    email = input("Email: ")
    password = input("Mật khẩu: ")

    # --- Duyệt danh sách users để tìm user trùng email & password ---
    for u in users:
        if u.email == email and u.password == password:
            print(f"Đăng nhập thành công ({u.role})!")
            return u

    # Nếu không trùng
    print("Sai thông tin đăng nhập.")
    forgot = input("Bạn có muốn đặt lại mật khẩu? (y/n): ").lower()
    if forgot == "y":
        forgot_password(email)
    return None


def forgot_password(email):
    # Tìm user qua email
    for u in users:
        if u.email == email:
            new_password = generate_random_password()
            u.password = new_password
            print(f"Mật khẩu mới của bạn là: {new_password}")
            print("Hãy đổi lại mật khẩu sau khi đăng nhập!\n")
            return
    print("Không tìm thấy tài khoản với email này.\n")


def generate_random_password(length=8):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))
