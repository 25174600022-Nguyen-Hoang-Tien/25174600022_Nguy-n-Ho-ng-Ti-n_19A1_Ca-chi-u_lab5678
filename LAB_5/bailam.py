# Bai 5.1
so = int(input("Nhap so nguyen duong: "))
nhi_phan = ""

tam = so
while tam > 0:
    nhi_phan = str(tam % 2) + nhi_phan
    tam = tam // 2

print("Ket qua nhi phan:", nhi_phan)



# Bai 5.2
chuoi_1 = input("Nhap chuoi thu nhat: ")
chuoi_2 = input("Nhap chuoi thu hai : ")

chuoi_con_chung = ""
do_dai = 1

while do_dai <= len(chuoi_1):
    vi_tri = 0
    while vi_tri + do_dai <= len(chuoi_1):
        chuoi_con = chuoi_1[vi_tri : vi_tri + do_dai]
        if chuoi_con in chuoi_2:
            chuoi_con_chung = chuoi_con
            break
        vi_tri = vi_tri + 1
    if chuoi_con_chung != "":
        break
    do_dai = do_dai + 1

if chuoi_con_chung != "":
    print("Chuoi con chung ngan nhat:", chuoi_con_chung)
    print("Do dai:", len(chuoi_con_chung))
else:
    print("Khong co chuoi con chung.")



# Bai 5.3
van_ban = input("Nhap chuoi van ban: ")
tu_khoa = input("Nhap tu khoa tim kiem: ")


print("Vi tri xuat hien cua tu khoa:")
vi_tri = van_ban.find(tu_khoa)
so_lan_xuat_hien = 0
while vi_tri != -1:
    print(" Chi so:", vi_tri)
    so_lan_xuat_hien = so_lan_xuat_hien + 1
    vi_tri = van_ban.find(tu_khoa, vi_tri + 1)

if so_lan_xuat_hien == 0:
    print(" Khong tim thay tu khoa.")
else:
    print("Tong so lan xuat hien:", so_lan_xuat_hien)


danh_sach_tu = van_ban.split()
tan_suat_cao_nhat = 0
tu_nhieu_nhat = ""

for tu in danh_sach_tu:
    dem = 0
    for t in danh_sach_tu:
        if t.lower() == tu.lower():
            dem = dem + 1
    if dem > tan_suat_cao_nhat:
        tan_suat_cao_nhat = dem
        tu_nhieu_nhat = tu

print("Tu xuat hien nhieu nhat:", tu_nhieu_nhat, "(" + str(tan_suat_cao_nhat) + " lan)")



# Bai 5.4
chuoi_nhap = input("Nhap chuoi bat ky: ")

chuoi_chi_so = ""
for ky_tu in chuoi_nhap:
    if ky_tu.isdigit():
        chuoi_chi_so = chuoi_chi_so + ky_tu

print("Chuoi sau khi loc chu so:", chuoi_chi_so)

if chuoi_chi_so == "":
    print("Chuoi khong chua chu so nao.")
else:
    so_nguyen = int(chuoi_chi_so)
    print("So nguyen thu duoc:", so_nguyen)

    la_nguyen_to = True
    if so_nguyen < 2:
        la_nguyen_to = False
    else:
        i = 2
        while i * i <= so_nguyen:
            if so_nguyen % i == 0:
                la_nguyen_to = False
                break
            i = i + 1

    if la_nguyen_to:
        print(so_nguyen, "la so nguyen to.")
    else:
        print(so_nguyen, "khong phai so nguyen to.")



# Bai 5.5
chuoi_a = input("Nhap chuoi thu nhat: ")
chuoi_b = input("Nhap chuoi thu hai : ")

ket_qua = ""
chieu_dai_max = len(chuoi_a) if len(chuoi_a) > len(chuoi_b) else len(chuoi_b)

for i in range(chieu_dai_max):
    if i < len(chuoi_a):
        if ket_qua == "":
            ket_qua = chuoi_a[i]
        else:
            ket_qua = ket_qua + "-" + chuoi_a[i]
    if i < len(chuoi_b):
        if ket_qua == "":
            ket_qua = chuoi_b[i]
        else:
            ket_qua = ket_qua + "-" + chuoi_b[i]

print("Chuoi sau khi tron:", ket_qua)



# Bai 5.6
chuoi_nhap = input("Nhap chuoi: ")
tong_do_dai = len(chuoi_nhap)

print("Thong ke ky tu dac biet:")
da_in = ""

for ky_tu in chuoi_nhap:
    if not ky_tu.isalpha() and not ky_tu.isdigit():
        if ky_tu not in da_in:
            so_lan = 0
            for c in chuoi_nhap:
                if c == ky_tu:
                    so_lan = so_lan + 1
            ti_le = (so_lan / tong_do_dai) * 100
            print(" '" + ky_tu + "': " + str(so_lan) + " lan | " + str(round(ti_le, 2)) + "%")
            da_in = da_in + ky_tu



# Bai 5.7
chuoi_nhap = input("Nhap chuoi: ")

so_hoa     = 0
so_thuong  = 0
so_so      = 0
so_dacbiet = 0

for ky_tu in chuoi_nhap:
    if ky_tu.isupper():
        so_hoa = so_hoa + 1
    elif ky_tu.islower():
        so_thuong = so_thuong + 1
    elif ky_tu.isdigit():
        so_so = so_so + 1
    else:
        so_dacbiet = so_dacbiet + 1

print("Chu hoa       :", so_hoa)
print("Chu thuong    :", so_thuong)
print("Chu so        :", so_so)
print("Ky tu dac biet:", so_dacbiet)
print("Tong cong     :", len(chuoi_nhap))



# Bai 5.8
chuoi_nhap = input("Nhap chuoi (hon 10 ky tu): ")

if len(chuoi_nhap) <= 10:
    print("Chuoi phai co do dai lon hon 10 ky tu.")
else:
    print("Chuoi goc          :", chuoi_nhap)
    print("Vi tri 2 den 8     :", chuoi_nhap[2:9])
    print("5 ky tu tu vi tri 5:", chuoi_nhap[5:10])
    print("3 ky tu cuoi       :", chuoi_nhap[-3:])
    print("Chu hoa            :", chuoi_nhap.upper())
    print("Chu thuong         :", chuoi_nhap.lower())
    print("Dao nguoc          :", chuoi_nhap[::-1])



# Bai 5.9
chuoi_nguon = input("Nhap chuoi nguon   : ")
chuoi_dich  = input("Nhap chuoi muc tieu: ")

m = len(chuoi_nguon)
n = len(chuoi_dich)

bang = []
for i in range(m + 1):
    hang = []
    for j in range(n + 1):
        hang = hang + [0]
    bang = bang + [hang]

for i in range(m + 1):
    bang[i][0] = i
for j in range(n + 1):
    bang[0][j] = j

for i in range(1, m + 1):
    for j in range(1, n + 1):
        if chuoi_nguon[i - 1] == chuoi_dich[j - 1]:
            bang[i][j] = bang[i - 1][j - 1]
        else:
            xoa      = bang[i - 1][j]
            them     = bang[i][j - 1]
            thay_the = bang[i - 1][j - 1]
            nho_nhat = xoa
            if them < nho_nhat:
                nho_nhat = them
            if thay_the < nho_nhat:
                nho_nhat = thay_the
            bang[i][j] = 1 + nho_nhat

so_thao_tac = bang[m][n]
print("So thao tac can thiet:", so_thao_tac)
if so_thao_tac == 0:
    print("Hai chuoi giong nhau hoan toan.")
elif so_thao_tac <= 3:
    print("Co the chuyen doi de dang.")
elif so_thao_tac <= 7:
    print("Can trung binh thao tac de chuyen doi.")
else:
    print("Hai chuoi khac nhau nhieu, can nhieu thao tac.")



#Bài 5.10
text = input("Nhập chuỗi: ")
result = text.replace(" ", "")
print("Chuỗi sau khi xóa khoảng trắng:", result)