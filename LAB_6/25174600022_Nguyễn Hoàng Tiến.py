def kiem_tra_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def kiem_tra_so_hoan_hao(n):
    if n < 1:
        return False
    tong_uoc = 0
    for i in range(1, n):
        if n % i == 0:
            tong_uoc += i
    return tong_uoc == n

# 6.1
def bai_61():
    so_luong = int(input("So phan tu: "))
    danh_sach = []
    for i in range(so_luong):
        danh_sach.append(int(input()))
    
    so_chan = []
    so_le = []
    for x in danh_sach:
        if x % 2 == 0:
            so_chan.append(x)
        else:
            so_le.append(x)
    
    tong_chan = 0
    for c in so_chan:
        tong_chan += c
    
    tong_le = 0
    for l in so_le:
        tong_le += l
    
    print(f"Chan: {so_chan}, Tong: {tong_chan}")
    print(f"Le: {so_le}, Tong: {tong_le}")

# 6.2
def bai_62():
    so_luong = int(input("So phan tu: "))
    danh_sach = []
    for i in range(so_luong):
        danh_sach.append(int(input()))
    
    nguyen_to = []
    hoan_hao = []
    
    for x in danh_sach:
        if kiem_tra_nguyen_to(x):
            nguyen_to.append(x)
        if kiem_tra_so_hoan_hao(x):
            hoan_hao.append(x)
    
    print(f"Nguyen to: {nguyen_to}")
    print(f"Hoan hao: {hoan_hao}")

# 6.3
def bai_63():
    so_luong = int(input("So phan tu: "))
    danh_sach = []
    for i in range(so_luong):
        danh_sach.append(float(input()))
    
    max_val = danh_sach[0]
    for x in danh_sach:
        if x > max_val:
            max_val = x
    
    min_val = danh_sach[0]
    for x in danh_sach:
        if x < min_val:
            min_val = x
    
    print(f"Max: {max_val}, Min: {min_val}")

# 6.4
def bai_64():
    n = int(input("So hang Fibonacci: "))
    
    fib = [0, 1]
    
    for i in range(2, n):
        so_tiep = fib[i-1] + fib[i-2]
        fib.append(so_tiep)
    
    print(f"Fibonacci: {fib[:n]}")

# 6.5
def bai_65():
    danh_sach_nguyen_to = []
    
    for i in range(2, 100):
        if kiem_tra_nguyen_to(i):
            danh_sach_nguyen_to.append(i)
    
    print(f"Nguyen to < 100: {danh_sach_nguyen_to}")
    print(f"So luong: {len(danh_sach_nguyen_to)}")

# 6.6
def bai_66():
    so_luong = int(input("So phan tu: "))
    danh_sach = []
    for i in range(so_luong):
        danh_sach.append(int(input()))
    
    cong_sai = []
    for i in range(len(danh_sach)-1):
        sai_so = danh_sach[i+1] - danh_sach[i]
        cong_sai.append(sai_so)
    
    la_cap_so_cong = True
    for i in range(len(cong_sai)-1):
        if cong_sai[i] != cong_sai[i+1]:
            la_cap_so_cong = False
    
    print(f"Cong sai: {cong_sai[0] if la_cap_so_cong else 'Khong deu'}")
    print(f"La cap so cong: {la_cap_so_cong}")

# 6.7
def bai_67():
    hang = int(input("Hang: "))
    cot = int(input("Cot: "))
    
    ma_tran = []
    for i in range(hang):
        hang_i = []
        for j in range(cot):
            hang_i.append(int(input(f"[{i}][{j}]: ")))
        ma_tran.append(hang_i)
    
    tong = 0
    for i in range(len(ma_tran)):
        for j in range(len(ma_tran[i])):
            tong += ma_tran[i][j]
    
    print(f"Tong: {tong}")

# 6.8
def bai_68():
    hang1 = int(input("Hang m1: "))
    cot1 = int(input("Cot m1 = Hang m2: "))
    cot2 = int(input("Cot m2: "))
    
    print("Nhap m1:")
    m1 = []
    for i in range(hang1):
        hang = []
        for j in range(cot1):
            hang.append(int(input(f"m1[{i}][{j}]: ")))
        m1.append(hang)
    
    print("Nhap m2:")
    m2 = []
    for i in range(cot1):
        hang = []
        for j in range(cot2):
            hang.append(int(input(f"m2[{i}][{j}]: ")))
        m2.append(hang)
    
    ket_qua = []
    for i in range(hang1):
        hang = []
        for j in range(cot2):
            tong = 0
            for p in range(cot1):
                tong += m1[i][p] * m2[p][j]
            hang.append(tong)
        ket_qua.append(hang)
    
    print("Ket qua:")
    for hang in ket_qua:
        print(hang)

# 6.9
def bai_69():
    cap = int(input("Cap ma tran: "))
    
    ma_tran = []
    for i in range(cap):
        hang = []
        for j in range(cap):
            hang.append(int(input(f"[{i}][{j}]: ")))
        ma_tran.append(hang)
    
    chuyen_vi = []
    for i in range(cap):
        hang = []
        for j in range(cap):
            hang.append(ma_tran[j][i])
        chuyen_vi.append(hang)
    
    la_doi_xung = True
    for i in range(cap):
        for j in range(cap):
            if ma_tran[i][j] != chuyen_vi[i][j]:
                la_doi_xung = False
    
    print(f"Doi xung: {la_doi_xung}")

# 6.10
def bai_610():
    ma_tran = []
    for i in range(2):
        hang = []
        for j in range(2):
            hang.append(float(input(f"[{i}][{j}]: ")))
        ma_tran.append(hang)
    
    dinh_thuc = ma_tran[0][0] * ma_tran[1][1] - ma_tran[0][1] * ma_tran[1][0]
    
    if dinh_thuc == 0:
        print("Khong kha nghich")
    else:
        nghich_dao = [
            [ma_tran[1][1]/dinh_thuc, -ma_tran[0][1]/dinh_thuc],
            [-ma_tran[1][0]/dinh_thuc, ma_tran[0][0]/dinh_thuc]
        ]
        print("Ma tran nghich dao:")
        for hang in nghich_dao:
            print([round(x, 4) for x in hang])

if __name__ == "__main__":
    danh_sach_bai = [bai_61, bai_62, bai_63, bai_64, bai_65, bai_66, bai_67, bai_68, bai_69, bai_610]
    while True:
        lua_chon = input("Chon bai (1-10, 0=thoat): ")
        if lua_chon == "0": 
            break
        if lua_chon.isdigit() and 1 <= int(lua_chon) <= 10:
            danh_sach_bai[int(lua_chon)-1]()
        else:
            print("Lua chon khong hop le")
