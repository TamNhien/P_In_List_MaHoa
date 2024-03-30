def ma_hoa_list(L):
    D = {}  # Khởi tạo dictionary mã hóa
    L_mahoa = []  # Khởi tạo list mã hóa

    for phan_tu in L:  # Duyệt qua từng phần tử trong list L
        if phan_tu not in D:  # Kiểm tra xem phần tử đã được mã hóa chưa
            D[phan_tu] = len(D)  # Thêm phần tử vào dictionary với giá trị là số thứ tự
        L_mahoa.append(D[phan_tu])  # Thêm giá trị mã hóa của phần tử vào list mã hóa

    return L_mahoa  # Trả về list đã được mã hóa

# Ví dụ sử dụng:
L = ["đen","vàng","xanh","vàng","xanh","đỏ","hồng"]
L_mahoa = ma_hoa_list(L)
print("List đã được mã hóa: ", L_mahoa)
