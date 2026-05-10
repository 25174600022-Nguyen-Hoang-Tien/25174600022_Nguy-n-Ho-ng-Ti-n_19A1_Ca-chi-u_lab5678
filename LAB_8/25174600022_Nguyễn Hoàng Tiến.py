def kiem_tra_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def tinh_giai_thua(n):
    if n < 0:
        return None
    if n == 0 or n == 1:
        return 1
    ket_qua = 1
    for i in range(2, n+1):
        ket_qua *= i
    return ket_qua

# 8.1
def bai_81():
    print("Cap so nguyen to sinh doi < 1000:")
    danh_sach_cap = []
    
    for i in range(2, 998):
        if kiem_tra_nguyen_to(i) and kiem_tra_nguyen_to(i+2):
            danh_sach_cap.append((i, i+2))
            print(f"({i}, {i+2})", end="  ")
    
    print(f"\n\nTong cap: {len(danh_sach_cap)}")

# 8.2
def bai_82():
    n = int(input("n: "))
    ket_qua = tinh_giai_thua(n)
    print(f"{n}! = {ket_qua}")

# 8.3
def bai_83():
    def tinh_hoan_vi(n, r):
        if r > n or r < 0:
            return None
        return tinh_giai_thua(n) // tinh_giai_thua(n - r)
    
    def tinh_to_hop(n, r):
        if r > n or r < 0:
            return None
        return tinh_giai_thua(n) // (tinh_giai_thua(r) * tinh_giai_thua(n - r))
    
    n = int(input("n: "))
    r = int(input("r: "))
    
    hoan_vi = tinh_hoan_vi(n, r)
    to_hop = tinh_to_hop(n, r)
    
    print(f"P({n},{r}) = {hoan_vi}")
    print(f"C({n},{r}) = {to_hop}")

# 8.4
def bai_84():
    def tinh_tong_lap_phuong(n):
        tong = 0
        so = n
        while so > 0:
            chu_so = so % 10
            tong += chu_so ** 3
            so //= 10
        return tong
    
    n = int(input("n: "))
    tong = tinh_tong_lap_phuong(n)
    print(f"Tong lap phuong: {tong}")

# 8.5
def bai_85():
    def kiem_tra_armstrong(n):
        so_chu_so = len(str(n))
        tong = 0
        so = n
        while so > 0:
            chu_so = so % 10
            tong += chu_so ** so_chu_so
            so //= 10
        return tong == n
    
    print("So Armstrong < 10000:")
    danh_sach = []
    for i in range(1, 10000):
        if kiem_tra_armstrong(i):
            danh_sach.append(i)
    print(danh_sach)

# 8.6
def bai_86():
    def tinh_tong_uoc(n):
        tong = 0
        for i in range(1, n):
            if n % i == 0:
                tong += i
        return tong
    
    n = int(input("n: "))
    tong = tinh_tong_uoc(n)
    print(f"Tong uoc so: {tong}")

# 8.7
def bai_87():
    def tinh_tong_uoc(n):
        tong = 0
        for i in range(1, n):
            if n % i == 0:
                tong += i
        return tong
    
    def kiem_tra_amicable(a, b):
        return tinh_tong_uoc(a) == b and tinh_tong_uoc(b) == a
    
    print("Cap so Amicable < 10000:")
    danh_sach = []
    
    for i in range(1, 10000):
        j = tinh_tong_uoc(i)
        if i < j and kiem_tra_amicable(i, j):
            danh_sach.append((i, j))
            print(f"({i}, {j})")
    
    print(f"Tong cap: {len(danh_sach)}")

# 8.8
def bai_88():
    n = int(input("So luong: "))
    danh_sach = []
    
    for i in range(n):
        danh_sach.append(int(input()))
    
    so_chan = []
    so_le = []
    
    for x in danh_sach:
        if x % 2 == 0:
            so_chan.append(x)
        else:
            so_le.append(x)
    
    print(f"Chan: {so_chan}")
    print(f"Le: {so_le}")

# 8.9
def bai_89():
    n = int(input("So luong: "))
    danh_sach = []
    
    for i in range(n):
        danh_sach.append(int(input()))
    
    lap_phuong = []
    for x in danh_sach:
        lap_phuong.append(x ** 3)
    
    print(f"Goc: {danh_sach}")
    print(f"Lap phuong: {lap_phuong}")

# 8.10
def bai_810():
    n = int(input("So luong: "))
    danh_sach = []
    
    for i in range(n):
        danh_sach.append(int(input()))
    
    so_chan_lap_phuong = []
    for x in danh_sach:
        if x % 2 == 0:
            so_chan_lap_phuong.append(x ** 3)
    
    so_le_binh_phuong = []
    for x in danh_sach:
        if x % 2 != 0:
            so_le_binh_phuong.append(x ** 2)
    
    print(f"Goc: {danh_sach}")
    print(f"Chan lap phuong: {so_chan_lap_phuong}")
    print(f"Le binh phuong: {so_le_binh_phuong}")

if __name__ == "__main__":
    danh_sach_bai = [bai_81, bai_82, bai_83, bai_84, bai_85, bai_86, bai_87, bai_88, bai_89, bai_810]
    while True:
        lua_chon = input("Chon bai (1-10, 0=thoat): ")
        if lua_chon == "0": 
            break
        if lua_chon.isdigit() and 1 <= int(lua_chon) <= 10:
            danh_sach_bai[int(lua_chon)-1]()
        else:
            print("Lua chon khong hop le")
