#7.1
n = int(input("Nhap so nguyen N: "))
luy_thua_ba = {}
for x in range(1, n + 1):
    luy_thua_ba[x] = x ** 3

print("Tu dien {x: x^3}:", luy_thua_ba)


#7.2
n = int(input("Nhap so luong sinh vien: "))
diem_sv = {}
for i in range(n):
    ten  = input("  Ten sinh vien: ")
    diem = float(input("  Diem thi     : "))
    diem_sv[ten] = diem

xep_loai_sv = {}
for ten in diem_sv:
    diem = diem_sv[ten]
    if diem >= 90:
        xep_loai = "A"
    elif diem >= 80:
        xep_loai = "B"
    elif diem >= 70:
        xep_loai = "C"
    elif diem >= 60:
        xep_loai = "D"
    else:
        xep_loai = "F"
    xep_loai_sv[ten] = xep_loai

print("Xep loai sinh vien:")
for ten in xep_loai_sv:
    print(" ", ten, ":", diem_sv[ten], "->", xep_loai_sv[ten])


#7.3
tan_suat_xep_loai = {}
for ten in xep_loai_sv:
    loai = xep_loai_sv[ten]
    if loai in tan_suat_xep_loai:
        tan_suat_xep_loai[loai] = tan_suat_xep_loai[loai] + 1
    else:
        tan_suat_xep_loai[loai] = 1

print("Bao cao so luong sinh vien theo hoc luc:")
for loai in ["A", "B", "C", "D", "F"]:
    so_luong = tan_suat_xep_loai.get(loai, 0)
    print("  Loai", loai, ":", so_luong, "sinh vien")


#7.4
van_ban = input("Nhap doan van ban tieng Anh: ")

# Lam sach chuoi: chuyen thuong, xoa ky tu dac biet
van_ban_sach = ""
for ky_tu in van_ban.lower():
    if ky_tu.isalpha() or ky_tu == " ":
        van_ban_sach = van_ban_sach + ky_tu

danh_sach_tu = van_ban_sach.split()

tan_suat_tu = {}
for tu in danh_sach_tu:
    if tu in tan_suat_tu:
        tan_suat_tu[tu] = tan_suat_tu[tu] + 1
    else:
        tan_suat_tu[tu] = 1

print("Tan suat xuat hien tung tu:")
for tu in tan_suat_tu:
    print(" ", tu, ":", tan_suat_tu[tu])


#7.5
tan_suat_cao_nhat = 0
tan_suat_thap_nhat = 0

# Lay tan suat cao va thap
for tu in tan_suat_tu:
    if tan_suat_tu[tu] > tan_suat_cao_nhat:
        tan_suat_cao_nhat = tan_suat_tu[tu]

tan_suat_thap_nhat = tan_suat_cao_nhat
for tu in tan_suat_tu:
    if tan_suat_tu[tu] < tan_suat_thap_nhat:
        tan_suat_thap_nhat = tan_suat_tu[tu]

tu_xuat_hien_nhieu = []
tu_xuat_hien_it = []
for tu in tan_suat_tu:
    if tan_suat_tu[tu] == tan_suat_cao_nhat:
        tu_xuat_hien_nhieu.append(tu)
    if tan_suat_tu[tu] == tan_suat_thap_nhat:
        tu_xuat_hien_it.append(tu)

print("Tu xuat hien nhieu nhat (" + str(tan_suat_cao_nhat) + " lan):", tu_xuat_hien_nhieu)
print("Tu xuat hien it nhat   (" + str(tan_suat_thap_nhat) + " lan):", tu_xuat_hien_it)


#7.6
hanh_ly = {
    "backpack": ["sword", "potion", "map", "torch", "shield"],
    "gold": 100,
    "food": 5
}

print("Hanh ly ban dau:", hanh_ly)

# Bo sung khoa pocket
hanh_ly["pocket"] = ["key", "coin", "note"]

# Cap nhat so luong gold
hanh_ly["gold"] = hanh_ly["gold"] + 50

print("Hanh ly sau khi cap nhat:")
for khoa in hanh_ly:
    print(" ", khoa, ":", hanh_ly[khoa])


#7.7
hanh_ly["backpack"].sort()
print("Backpack sau khi sap xep:", hanh_ly["backpack"])

vat_pham_xoa = input("Nhap vat pham can xoa khoi backpack: ")
if vat_pham_xoa in hanh_ly["backpack"]:
    hanh_ly["backpack"].remove(vat_pham_xoa)
    print("Da xoa '" + vat_pham_xoa + "' khoi backpack.")
else:
    print("'" + vat_pham_xoa + "' khong co trong backpack.")

print("Backpack sau khi xoa:", hanh_ly["backpack"])


#7.8
ton_kho = {
    "apple" : 10,
    "banana": 5,
    "orange": 8,
    "mango" : 3
}

don_gia = {
    "apple" : 5000,
    "banana": 3000,
    "orange": 7000,
    "mango" : 12000
}

print("-" * 40)
print(f"{'Mat hang':<12} {'So luong':>8} {'Don gia':>10} {'Thanh tien':>12}")
print("-" * 40)

tong_hoa_don = 0
for mat_hang in ton_kho:
    so_luong   = ton_kho[mat_hang]
    gia        = don_gia[mat_hang]
    thanh_tien = so_luong * gia
    tong_hoa_don = tong_hoa_don + thanh_tien
    print(f"{mat_hang:<12} {so_luong:>8} {gia:>10,} {thanh_tien:>12,}")

print("-" * 40)
print(f"{'TONG CONG':<32} {tong_hoa_don:>12,}")
print("-" * 40)


#7.9
don_hang = {
    "apple" : 3,
    "banana": 2,
    "mango" : 1
}

print("Xu ly don hang:")
for mat_hang in don_hang:
    so_ban = don_hang[mat_hang]
    if mat_hang in ton_kho:
        if ton_kho[mat_hang] >= so_ban:
            ton_kho[mat_hang] = ton_kho[mat_hang] - so_ban
            print(" ", mat_hang, ": ban", so_ban, "-> con lai", ton_kho[mat_hang])
        else:
            print(" ", mat_hang, ": khong du hang (chi con", ton_kho[mat_hang], ")")
    else:
        print(" ", mat_hang, ": khong co trong kho.")

print("Ton kho sau giao dich:", ton_kho)


#7.10
kho_hang  = {"apple", "banana", "orange", "mango", "grape", "pear"}
gio_hang  = {"apple", "mango", "grape"}

chua_duoc_chon = kho_hang - gio_hang

print("Kho hang  :", kho_hang)
print("Gio hang  :", gio_hang)
print("Hang chua duoc chon mua:", chua_duoc_chon)