# 7.1
def bai_71():
    n = int(input("N: "))
    tu_dien = {}
    for x in range(1, n+1):
        tu_dien[x] = x**3
    print(tu_dien)

# 7.2
def bai_72():
    n = int(input("So sinh vien: "))
    sinh_vien = {}
    
    for i in range(n):
        ten = input("Ten: ")
        diem = float(input("Diem: "))
        sinh_vien[ten] = diem
    
    for ten in sinh_vien:
        diem_so = sinh_vien[ten]
        if diem_so >= 8.5:
            hoc_luc = 'A'
        elif diem_so >= 7.5:
            hoc_luc = 'B'
        elif diem_so >= 6.5:
            hoc_luc = 'C'
        elif diem_so >= 5.5:
            hoc_luc = 'D'
        else:
            hoc_luc = 'F'
        print(f"{ten}: {diem_so} -> {hoc_luc}")

# 7.3
def bai_73():
    n = int(input("So sinh vien: "))
    diem_dict = {}
    
    for i in range(n):
        ten = input("Ten: ")
        diem = float(input("Diem: "))
        diem_dict[ten] = diem
    
    hoc_luc_dict = {}
    for ten in diem_dict:
        diem_so = diem_dict[ten]
        if diem_so >= 8.5:
            hoc_luc = 'A'
        elif diem_so >= 7.5:
            hoc_luc = 'B'
        elif diem_so >= 6.5:
            hoc_luc = 'C'
        elif diem_so >= 5.5:
            hoc_luc = 'D'
        else:
            hoc_luc = 'F'
        
        if hoc_luc in hoc_luc_dict:
            hoc_luc_dict[hoc_luc] += 1
        else:
            hoc_luc_dict[hoc_luc] = 1
    
    for hoc_luc in sorted(hoc_luc_dict, reverse=True):
        print(f"{hoc_luc}: {hoc_luc_dict[hoc_luc]}")

# 7.4
def bai_74():
    van_ban = input("Van ban: ").lower()
    
    ky_tu_xoa = ",.!?;:()"
    for ky in ky_tu_xoa:
        van_ban = van_ban.replace(ky, "")
    
    danh_sach_tu = van_ban.split()
    tu_dict = {}
    
    for tu in danh_sach_tu:
        if tu in tu_dict:
            tu_dict[tu] += 1
        else:
            tu_dict[tu] = 1
    
    for tu in tu_dict:
        print(f"{tu}: {tu_dict[tu]}")

# 7.5
def bai_75():
    van_ban = input("Van ban: ").lower()
    
    ky_tu_xoa = ",.!?;:()"
    for ky in ky_tu_xoa:
        van_ban = van_ban.replace(ky, "")
    
    danh_sach_tu = van_ban.split()
    tu_dict = {}
    
    for tu in danh_sach_tu:
        if tu in tu_dict:
            tu_dict[tu] += 1
        else:
            tu_dict[tu] = 1
    
    tu_cao_nhat = None
    tan_cao_nhat = 0
    for tu in tu_dict:
        if tu_dict[tu] > tan_cao_nhat:
            tan_cao_nhat = tu_dict[tu]
            tu_cao_nhat = tu
    
    tu_thap_nhat = None
    tan_thap_nhat = float('inf')
    for tu in tu_dict:
        if tu_dict[tu] < tan_thap_nhat:
            tan_thap_nhat = tu_dict[tu]
            tu_thap_nhat = tu
    
    print(f"Cao nhat: '{tu_cao_nhat}' ({tan_cao_nhat})")
    print(f"Thap nhat: '{tu_thap_nhat}' ({tan_thap_nhat})")

# 7.6
def bai_76():
    hanh_trang = {
        'vang': 50,
        'kiem': 1,
        'khien': 1,
        'thuoc': 5,
        'tui': []
    }
    
    print(f"Vang: {hanh_trang['vang']}")
    print(f"Kiem: {hanh_trang['kiem']}")
    print(f"Khien: {hanh_trang['khien']}")
    print(f"Thuoc: {hanh_trang['thuoc']}")
    print(f"Tui: {hanh_trang['tui']}")
    
    so_vat_pham = int(input("Vat pham: "))
    for i in range(so_vat_pham):
        vat = input()
        hanh_trang['tui'].append(vat)
    
    them_vang = int(input("Them vang: "))
    hanh_trang['vang'] += them_vang
    
    print(f"Vang: {hanh_trang['vang']}")
    print(f"Tui: {hanh_trang['tui']}")

# 7.7
def bai_77():
    hanh_trang = {'vat_pham': ['kiem', 'thuoc', 'tao', 'banh', 'khien']}
    
    print(f"Truoc: {hanh_trang['vat_pham']}")
    
    for i in range(len(hanh_trang['vat_pham'])):
        for j in range(i+1, len(hanh_trang['vat_pham'])):
            if hanh_trang['vat_pham'][i] > hanh_trang['vat_pham'][j]:
                temp = hanh_trang['vat_pham'][i]
                hanh_trang['vat_pham'][i] = hanh_trang['vat_pham'][j]
                hanh_trang['vat_pham'][j] = temp
    
    print(f"Sau: {hanh_trang['vat_pham']}")
    
    vat_xoa = input("Loai bo: ")
    if vat_xoa in hanh_trang['vat_pham']:
        vi_tri = -1
        for i in range(len(hanh_trang['vat_pham'])):
            if hanh_trang['vat_pham'][i] == vat_xoa:
                vi_tri = i
                break
        if vi_tri != -1:
            hanh_trang['vat_pham'].pop(vi_tri)
        print(f"Ket qua: {hanh_trang['vat_pham']}")

# 7.8
def bai_78():
    so_luong = {'tao': 5, 'banh': 3, 'sua': 2, 'trung': 10}
    gia = {'tao': 10000, 'banh': 25000, 'sua': 35000, 'trung': 2500}
    
    print("="*50)
    tong_cong = 0
    
    for vat_pham in so_luong:
        sl = so_luong[vat_pham]
        don_gia = gia[vat_pham]
        thanh_tien = sl * don_gia
        tong_cong += thanh_tien
        print(f"{vat_pham:15} | SL:{sl:3} | Don gia:{don_gia:8} | Thanh tien:{thanh_tien:12}")
    
    print("-"*50)
    print(f"TONG: {tong_cong}")

# 7.9
def bai_79():
    ton_kho = {'tao': 10, 'banh': 8, 'sua': 5, 'trung': 20}
    giao_dich = {'tao': 3, 'banh': 2, 'sua': 1, 'trung': 5}
    
    print(f"Ban dau: {ton_kho}")
    
    for vat_pham in giao_dich:
        ton_kho[vat_pham] -= giao_dich[vat_pham]
    
    print(f"Sau: {ton_kho}")

# 7.10
def bai_710():
    kho = {'tao', 'banh', 'sua', 'trung', 'pho mai', 'bo'}
    khach = {'tao', 'sua', 'trung', 'yogurt'}
    
    print(f"Kho: {kho}")
    print(f"Khach chon: {khach}")
    
    co_san = kho & khach
    khong_co = khach - kho
    chua_chon = kho - khach
    
    print(f"Co san: {co_san}")
    print(f"Khong co: {khong_co}")
    print(f"Chua chon: {chua_chon}")

if __name__ == "__main__":
    danh_sach_bai = [bai_71, bai_72, bai_73, bai_74, bai_75, bai_76, bai_77, bai_78, bai_79, bai_710]
    while True:
        lua_chon = input("Chon bai (1-10, 0=thoat): ")
        if lua_chon == "0": 
            break
        if lua_chon.isdigit() and 1 <= int(lua_chon) <= 10:
            danh_sach_bai[int(lua_chon)-1]()
        else:
            print("Lua chon khong hop le")
