from auth import register, login
from customer import customer_menu
from staff import staff_menu
from admin import admin_menu

def main():
    while True:
        print("\n=== HỆ THỐNG ĐẶT MÓN NHÀ HÀNG ===")
        print("1. Đăng ký")
        print("2. Đăng nhập")
        print("0. Thoát")
        choice = input("Chọn: ")

        if choice == "1":
            register()
        elif choice == "2":
            user = login()
            if user:
                if user.role == "customer":
                    customer_menu(user)
                elif user.role == "staff":
                    staff_menu()
                elif user.role == "admin":
                    admin_menu()
        else:
            break

if __name__ == "__main__":
    main()
