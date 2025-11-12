# auth.py
import random
import string
from user import Customer, Staff, Admin

users = []

def register():
    print("\n=== ĐĂNG KÝ TÀI KHOẢN ===")
    name = input("Họ tên: ")
    phone = input("Số điện thoại: ")
    email = input("Email (dùng làm đăng nhập): ")
    password = input("Mật khẩu: ")
    role = input("Vai trò (customer/staff/admin): ").lower()

    if role == "admin":
        user = Admin(name, phone, email, password)
    elif role == "staff":
        user = Staff(name, phone, email, password)
    else:
        user = Customer(name, phone, email, password)

    users.append(user)
    print(f"✅ Đăng ký {role} thành công!\n")


def login():
    print("\n=== ĐĂNG NHẬP ===")
    email = input("Email: ")
    password = input("Mật khẩu: ")

    for u in users:
        if u.email == email and u.password == password:
            print(f"✅ Đăng nhập thành công ({u.role})!")
            return u

    print("❌ Sai thông tin đăng nhập.")
    forgot = input("Bạn có muốn đặt lại mật khẩu? (y/n): ").lower()
    if forgot == "y":
        forgot_password(email)
    return None


def forgot_password(email):
    for u in users:
        if u.email == email:
            new_password = generate_random_password()
            u.password = new_password
            print(f"🔑 Mật khẩu mới của bạn là: {new_password}")
            print("⚠️ Hãy đổi lại mật khẩu sau khi đăng nhập!\n")
            return
    print("❌ Không tìm thấy tài khoản với email này.\n")


def generate_random_password(length=8):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))
