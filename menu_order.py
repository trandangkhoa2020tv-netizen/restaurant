menu = [
    {"id": 1, "name": "Phở bò", "price": 40000, "category": "main"},
    {"id": 2, "name": "Cà phê sữa", "price": 25000, "category": "drink"},
]

orders = []

def show_menu():
    print("\n=== DANH SÁCH MÓN ĂN ===")
    for m in menu:
        print(f"{m['id']}. {m['name']} - {m['price']}đ")

def order_food(customer):
    cart = []
    while True:
        show_menu()
        choice = input("Nhập ID món muốn thêm (hoặc 0 để đặt hàng): ")
        if choice == "0":
            break
        for m in menu:
            if str(m['id']) == choice:
                quantity = int(input("Số lượng: "))
                cart.append({"item": m, "qty": quantity})
                print("Đã thêm vào giỏ hàng!")
    if cart:
        orders.append({"customer": customer.name, "items": cart, "status": "Mới đặt"})
        print("Đơn hàng đã được tạo!")
