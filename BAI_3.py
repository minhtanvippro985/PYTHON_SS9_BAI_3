order_list = ["GE001", "GE002", "GE003"]

while True:
    choice = input("""
===== HỆ THỐNG QUẢN LÝ ĐƠN HÀNG GRAB EXPRESS =====
1. Hiển thị danh sách đơn hàng
2. Thêm đơn hàng mới
3. Xóa đơn hàng theo mã
4. Thoát chương trình\n 
Nhập lựa chọn của bạn :  """)
    
    match choice:
        case "4":
            print("Thoát chương trình")
            break
        case "1":
            if len(order_list) == 0:
                print("Hiện chưa có đơn hàng nào")
            else:
                print("\n------ DANH SÁCH ĐƠN HÀNG --------")
            for index , order in enumerate(order_list , start=1):
                print(f"{index}. {order}")

        case "2":
            new_order_name = input("Nhập mã đơn hàng mới của bạn : ").strip().upper()
            if new_order_name in order_list:
                print(f"Đơn hàng {new_order_name} đã tồn tại!")
                continue
            if new_order_name.count(" "):
                print("Không được để trống giữa cái từ!")
                continue
            if new_order_name:
                order_list.append(new_order_name)

        case "3":
            delete_order_input = input("Nhập mã đơn hàng mà bạn muốn xóa : ").strip().upper()
            if not delete_order_input in order_list:
                print(f"Mã đơn hàng {delete_order_input} không tồn tại")
                continue
            elif delete_order_input in order_list:
                print(f"Đã xóa đơn hàng {delete_order_input}")
                order_list.remove(delete_order_input)
        case _:
            print("Vui lòng nhập lựa chọn từ 1-4")