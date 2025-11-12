# staff.py
from menu_order import orders, tables

def staff_menu():
    while True:
        print("\n=== MENU NHÂN VIÊN ===")
        print("1. Xem tất cả đơn hàng")
        print("2. Cập nhật trạng thái đơn")
        print("3. Quản lý bàn (xem/cập nhật)")
        print("0. Thoát")
        c = input("Chọn: ")

        if c == "1":
            view_orders()
        elif c == "2":
            update_order_status()
        elif c == "3":
            manage_tables()
        elif c == "0":
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại.")


# =======================
# 🔹 XEM & CẬP NHẬT ĐƠN HÀNG
# =======================
def view_orders():
    if not orders:
        print("Chưa có đơn hàng nào.")
        return

    print("\n=== DANH SÁCH ĐƠN HÀNG ===")
    for i, o in enumerate(orders, start=1):
        print(f"\nĐơn #{i}:")
        print(f"👤 Khách hàng: {o['customer']}")
        print(f"🍽 Món: {o['food']} x {o['quantity']}")
        print(f"Ghi chú: {o['note']}")
        print(f"Hình thức: {o['method']}")
        if o["table"] != "-":
            print(f"Bàn: {o['table']}")
        print(f"Tổng tiền: {o['total']:,}đ")
        print(f"Trạng thái: {o['status']}")
        print("-" * 40)


def update_order_status():
    if not orders:
        print("Không có đơn nào để cập nhật.")
        return

    try:
        order_index = int(input("Nhập số thứ tự đơn cần cập nhật: ")) - 1
        if 0 <= order_index < len(orders):
            new_status = input("Trạng thái mới (xác nhận / chế biến / hoàn tất / hủy): ").strip()
            orders[order_index]["status"] = new_status
            print("Đã cập nhật trạng thái đơn hàng!")

            # Nếu đơn là đặt bàn và bị hủy hoặc hoàn tất → giải phóng bàn
            order = orders[order_index]
            if order["table"] != "-" and new_status in ["hoàn tất", "hủy"]:
                table_id = order["table"]
                if table_id in tables:
                    tables[table_id] = "Trống"
                    print(f"🧹 Bàn {table_id} đã được dọn và chuyển về trạng thái trống.")
        else:
            print("Số thứ tự không hợp lệ.")
    except ValueError:
        print("Vui lòng nhập số hợp lệ.")


# =======================
# 🔹 QUẢN LÝ BÀN
# =======================
def manage_tables():
    while True:
        print("\n=== QUẢN LÝ BÀN ===")
        print("1. Xem danh sách bàn")
        print("2. Cập nhật trạng thái bàn")
        print("0. Quay lại")
        opt = input("Chọn: ")

        if opt == "1":
            show_tables()
        elif opt == "2":
            update_table_status()
        elif opt == "0":
            break
        else:
            print("Vui lòng chọn đúng số.")


def show_tables():
    print("\n===== DANH SÁCH BÀN =====")
    for t, status in tables.items():
        print(f"Bàn {t}: {status}")
    print("--------------------------")


def update_table_status():
    try:
        table_id = int(input("Nhập số bàn (1-10): "))
        if table_id in tables:
            new_status = input("Trạng thái mới (Trống / Đang phục vụ / Đã dọn): ").capitalize()
            tables[table_id] = new_status
            print(f"Đã cập nhật bàn {table_id} thành: {new_status}")
        else:
            print("Không tồn tại bàn này.")
    except ValueError:
        print("Nhập số bàn hợp lệ (1-10).")
