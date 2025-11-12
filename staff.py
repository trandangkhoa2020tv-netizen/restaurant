# staff.py
from menu_order import orders

def staff_menu():
    while True:
        print("\n=== MENU NHÂN VIÊN ===")
        print("1. Xem tất cả đơn hàng")
        print("2. Cập nhật trạng thái đơn")
        print("0. Thoát")
        c = input("Chọn: ")

        if c == "1":
            for i, o in enumerate(orders):
                print(f"{i+1}. {o}")
        elif c == "2":
            i = int(input("Nhập số thứ tự đơn cần cập nhật: ")) - 1
            if 0 <= i < len(orders):
                new_status = input("Trạng thái mới (xác nhận/chế biến/hoàn tất/hủy): ")
                orders[i]["status"] = new_status
                print("✅ Đã cập nhật!")
        else:
            break
