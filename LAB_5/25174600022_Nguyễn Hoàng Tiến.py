# 5.1
def bai_51():
    so = int(input("Nhap so nguyen duong: "))
    if so == 0:
        print("Nhi phan: 0")
        return

    bits = []
    tam = so
    while tam > 0:
        bits.append(str(tam % 2))
        tam //= 2

    so_nhi_phan = ''.join(reversed(bits))
    print(f"Nhi phan: {so_nhi_phan}")

def bai_52():
    chuoi_1 = input("Nhap chuoi 1: ")
    chuoi_2 = input("Nhap chuoi 2: ")

    ngan_nhat = None

    for i in range(len(chuoi_1)):
        for j in range(i + 2, len(chuoi_1) + 1):   # độ dài tối thiểu 2
            con = chuoi_1[i:j]
            if con in chuoi_2:
                if ngan_nhat is None or len(con) < len(ngan_nhat):
                    ngan_nhat = con

    if ngan_nhat:
        print(f"Chuoi con chung ngan nhat: '{ngan_nhat}'")
    else:
        print("Khong co chuoi con chung co do dai >= 2")

# 5.3
def bai_53():
    van_ban = input("Nhap van ban: ")
    tu_khoa = input("Nhap tu khoa: ")
    
    vi_tri_list = []
    for i in range(len(van_ban) - len(tu_khoa) + 1):
        if van_ban[i:i+len(tu_khoa)] == tu_khoa:
            vi_tri_list.append(i)
    
    print(f"Vi tri: {vi_tri_list if vi_tri_list else 'Khong tim thay'}")
    
    danh_sach_tu = van_ban.lower().split()
    tan_suat_tu = {}
    for tu in danh_sach_tu:
        if tu in tan_suat_tu:
            tan_suat_tu[tu] += 1
        else:
            tan_suat_tu[tu] = 1
    
    tu_cao_nhat = max(tan_suat_tu, key=tan_suat_tu.get)
    print(f"Tu tan suat cao nhat: '{tu_cao_nhat}' ({tan_suat_tu[tu_cao_nhat]} lan)")

# 5.4
def kiem_tra_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def bai_54():
    xau = input("Nhap xau: ")
    chi_chu_so = ""
    for c in xau:
        if c.isdigit():
            chi_chu_so += c
    
    if chi_chu_so:
        so = int(chi_chu_so)
        print(f"Xau sau loc: {chi_chu_so}")
        print(f"So: {so}")
        print(f"La nguyen to: {kiem_tra_nguyen_to(so)}")
    else:
        print("Khong co chu so")

# 5.5
def bai_55():
    chuoi_1 = input("Nhap chuoi 1: ")
    chuoi_2 = input("Nhap chuoi 2: ")

    cac_ky_tu = []
    do_dai_max = max(len(chuoi_1), len(chuoi_2))

    for i in range(do_dai_max):
        if i < len(chuoi_1):
            cac_ky_tu.append(chuoi_1[i])
        if i < len(chuoi_2):
            cac_ky_tu.append(chuoi_2[i])

    ket_qua = '-'.join(cac_ky_tu)
    print(f"Ket qua: {ket_qua}")

# 5.6
def bai_56():
    xau = input("Nhap xau: ")
    ky_tu_dac_biet = {}
    
    for c in xau:
        if not c.isalnum():
            if c in ky_tu_dac_biet:
                ky_tu_dac_biet[c] += 1
            else:
                ky_tu_dac_biet[c] = 1
    
    for c, dem in ky_tu_dac_biet.items():
        ty_le = (dem / len(xau)) * 100
        print(f"'{c}': {dem} ({ty_le:.2f}%)")

# 5.7
def bai_57():
    xau = input("Nhap xau: ")
    
    chu_thuong = 0
    chu_hoa = 0
    chu_so = 0
    ky_tu_dac = 0
    
    for c in xau:
        if c.islower():
            chu_thuong += 1
        elif c.isupper():
            chu_hoa += 1
        elif c.isdigit():
            chu_so += 1
        else:
            ky_tu_dac += 1
    
    print(f"Chu thuong: {chu_thuong}")
    print(f"Chu hoa: {chu_hoa}")
    print(f"Chu so: {chu_so}")
    print(f"Ky tu dac biet: {ky_tu_dac}")

# 5.8
def bai_58():
    xau = input("Nhap xau (>10 ky tu): ")
    
    if len(xau) <= 10:
        print("Xau phai >10 ky tu")
        return
    
    print(f"Xau goc: {xau}")
    print(f"Trich tu vi tri 2 den 8: {xau[2:8]}")
    print(f"Trich 5 ky tu tu vi tri 5: {xau[5:10]}")
    print(f"3 ky tu cuoi: {xau[-3:]}")
    print(f"Chu hoa: {xau.upper()}")
    print(f"Chu thuong: {xau.lower()}")
    print(f"Dao nguoc: {xau[::-1]}")

# 5.9
def bai_59():
    xau_nguon = input("Xau nguon: ")
    xau_dich = input("Xau dich: ")
    
    m = len(xau_nguon)
    n = len(xau_dich)
    
    bang_dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
    
    for i in range(m+1):
        bang_dp[i][0] = i
    for j in range(n+1):
        bang_dp[0][j] = j
    
    for i in range(1, m+1):
        for j in range(1, n+1):
            if xau_nguon[i-1] == xau_dich[j-1]:
                bang_dp[i][j] = bang_dp[i-1][j-1]
            else:
                hang_tren = bang_dp[i-1][j]
                cot_trai = bang_dp[i][j-1]
                duong_cheo = bang_dp[i-1][j-1]
                bang_dp[i][j] = 1 + min(hang_tren, cot_trai, duong_cheo)
    
    print(f"Khoang cach: {bang_dp[m][n]}")

# 5.10
def bai_510():
    xau = input("Nhap xau: ")
    xau_sau = xau.replace(" ", "")
    print(f"Ket qua: '{xau_sau}'")

if __name__ == "__main__":
    danh_sach_bai = [bai_51, bai_52, bai_53, bai_54, bai_55, bai_56, bai_57, bai_58, bai_59, bai_510]
    while True:
        lua_chon = input("Chon bai (1-10, 0=thoat): ")
        if lua_chon == "0": 
            break
        if lua_chon.isdigit() and 1 <= int(lua_chon) <= 10:
            danh_sach_bai[int(lua_chon)-1]()
        else:
            print("Lua chon khong hop le")
