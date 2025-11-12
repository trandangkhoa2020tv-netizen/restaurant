# auth.py
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
    return None
