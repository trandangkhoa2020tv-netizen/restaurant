# main.py

# Import các chức năng: đăng ký, đăng nhập, menu khách hàng, nhân viên, admin
# main.py (đúng khi chạy từ bên trong folder restaurant)
from auth import register, login
from customer import customer_menu
from staff import staff_menu
from admin import admin_menu


def main():
    # Vòng lặp chính của chương trình (chạy liên tục cho đến khi chọn Thoát)
    while True:
        print("\n=== HỆ THỐNG ĐẶT MÓN NHÀ HÀNG ===")
        print("1. Đăng ký")
        print("2. Đăng nhập")
        print("0. Thoát")
        choice = input("Chọn: ")

        # --- ĐĂNG KÝ TÀI KHOẢN ---
        if choice == "1":
            register()       # Gọi hàm register() trong auth.py

        # --- ĐĂNG NHẬP ---
        elif choice == "2":
            user = login()   # Hàm login() trả về 1 user object hoặc None

        
            if user:
                # Sau khi đăng nhập thành công → điều hướng theo role
                if user.role == "customer":
                    customer_menu(user)   # Menu cho khách hàng

                elif user.role == "staff":
                    staff_menu(user)      # Menu cho nhân viên

                elif user.role == "admin":
                    admin_menu()      # Menu cho admin

                else:
                    print("Vai trò người dùng không hợp lệ.")
            else:
                print("Đăng nhập thất bại. Hãy thử lại.\n")

        # --- THOÁT CHƯƠNG TRÌNH ---
        elif choice == "0":
            print("Tạm biệt! Cảm ơn bạn đã sử dụng hệ thống.")
            break  # Thoát vòng lặp → kết thúc chương trình

        # --- NHẬP SAI ---
        else:
            print("Lựa chọn không hợp lệ, vui lòng chọn lại.")


# Chỉ chạy main() nếu file này được chạy trực tiếp
if __name__ == "__main__":
    main()
