#6.1
n = int(input("Nhap so luong phan tu: "))
mang = []
for i in range(n):
    x = int(input("Nhap phan tu " + str(i + 1) + ": "))
    mang.append(x)

so_chan = []
so_le = []
for x in mang:
    if x % 2 == 0:
        so_chan.append(x)
    else:
        so_le.append(x)

tong_chan = 0
for x in so_chan:
    tong_chan = tong_chan + x

tong_le = 0
for x in so_le:
    tong_le = tong_le + x

print("So chan:", so_chan, "- Tong:", tong_chan)
print("So le  :", so_le,  "- Tong:", tong_le)


#6.2
def la_nguyen_to(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i = i + 1
    return True

def la_hoan_hao(n):
    if n < 2:
        return False
    tong_uoc = 1
    i = 2
    while i * i <= n:
        if n % i == 0:
            tong_uoc = tong_uoc + i
            if i != n // i:
                tong_uoc = tong_uoc + n // i
        i = i + 1
    return tong_uoc == n

n = int(input("Nhap so luong phan tu: "))
mang = []
for i in range(n):
    x = int(input("Nhap phan tu " + str(i + 1) + ": "))
    mang.append(x)

ket_qua = []
for x in mang:
    if la_nguyen_to(x) or la_hoan_hao(x):
        ket_qua.append(x)

print("Cac so nguyen to hoac hoan hao:", ket_qua)


#6.3
n = int(input("Nhap so luong phan tu: "))
day_so = []
for i in range(n):
    x = float(input("Nhap phan tu " + str(i + 1) + ": "))
    day_so.append(x)

lon_nhat = day_so[0]
nho_nhat = day_so[0]
for x in day_so:
    if x > lon_nhat:
        lon_nhat = x
    if x < nho_nhat:
        nho_nhat = x

print("Gia tri lon nhat:", lon_nhat)
print("Gia tri nho nhat:", nho_nhat)


#6.4
n = int(input("Nhap so hang Fibonacci can lay: "))
fibonacci = [0, 1]
fibonacci = [0] + [1] + [fibonacci[i - 1] + fibonacci[i - 2] for i in range(2, n)]
print("Day Fibonacci:", fibonacci[:n])


#6.5
nguyen_to_duoi_100 = [x for x in range(2, 100) if la_nguyen_to(x)]
print("So nguyen to nho hon 100:", nguyen_to_duoi_100)


#6.6
n = int(input("Nhap so luong phan tu: "))
day = []
for i in range(n):
    x = int(input("Nhap phan tu " + str(i + 1) + ": "))
    day.append(x)

la_cap_so_cong = True
cong_sai = day[1] - day[0]
for i in range(1, len(day) - 1):
    if day[i + 1] - day[i] != cong_sai:
        la_cap_so_cong = False
        break

if la_cap_so_cong:
    print("Day so la cap so cong voi cong sai d =", cong_sai)
else:
    print("Day so khong phai cap so cong.")


#6.7
m = int(input("Nhap so hang m: "))
n = int(input("Nhap so cot  n: "))
ma_tran = []
for i in range(m):
    hang = []
    for j in range(n):
        x = int(input("Nhap phan tu [" + str(i) + "][" + str(j) + "]: "))
        hang.append(x)
    ma_tran.append(hang)

tong = 0
for hang in ma_tran:
    for x in hang:
        tong = tong + x

print("Tong cac phan tu ma tran:", tong)


#6.8
m1 = int(input("Nhap so hang ma tran A: "))
n1 = int(input("Nhap so cot  ma tran A: "))
A = []
for i in range(m1):
    hang = []
    for j in range(n1):
        x = int(input("A[" + str(i) + "][" + str(j) + "]: "))
        hang.append(x)
    A.append(hang)

m2 = int(input("Nhap so hang ma tran B: "))
n2 = int(input("Nhap so cot  ma tran B: "))

if n1 != m2:
    print("Khong the nhan hai ma tran: so cot A khac so hang B.")
else:
    B = []
    for i in range(m2):
        hang = []
        for j in range(n2):
            x = int(input("B[" + str(i) + "][" + str(j) + "]: "))
            hang.append(x)
        B.append(hang)

    C = []
    for i in range(m1):
        hang = []
        for j in range(n2):
            tong = 0
            for k in range(n1):
                tong = tong + A[i][k] * B[k][j]
            hang.append(tong)
        C.append(hang)

    print("Tich hai ma tran A x B:")
    for hang in C:
        print(hang)


#6.9
m = int(input("Nhap so hang: "))
n = int(input("Nhap so cot : "))
ma_tran = []
for i in range(m):
    hang = []
    for j in range(n):
        x = int(input("Nhap phan tu [" + str(i) + "][" + str(j) + "]: "))
        hang.append(x)
    ma_tran.append(hang)

# Tinh ma tran chuyen vi
chuyen_vi = []
for j in range(n):
    hang_moi = []
    for i in range(m):
        hang_moi.append(ma_tran[i][j])
    chuyen_vi.append(hang_moi)

print("Ma tran chuyen vi:")
for hang in chuyen_vi:
    print(hang)

if m == n:
    doi_xung = True
    for i in range(m):
        for j in range(n):
            if ma_tran[i][j] != ma_tran[j][i]:
                doi_xung = False
                break
    if doi_xung:
        print("Ma tran doi xung.")
    else:
        print("Ma tran khong doi xung.")
else:
    print("Ma tran khong vuong, khong kiem tra doi xung.")


#6.10
n = int(input("Nhap cap ma tran vuong n: "))
A = []
for i in range(n):
    hang = []
    for j in range(n):
        x = float(input("Nhap phan tu [" + str(i) + "][" + str(j) + "]: "))
        hang.append(x)
    A.append(hang)

# Tao ma tran mo rong [A | I] de dung khu Gauss-Jordan
mo_rong = []
for i in range(n):
    hang = A[i][:] + [1.0 if i == j else 0.0 for j in range(n)]
    mo_rong.append(hang)

kha_nghich = True
for col in range(n):
    # Tim hang pivot
    hang_pivot = -1
    for row in range(col, n):
        if mo_rong[row][col] != 0:
            hang_pivot = row
            break
    if hang_pivot == -1:
        kha_nghich = False
        break
    mo_rong[col], mo_rong[hang_pivot] = mo_rong[hang_pivot], mo_rong[col]

    he_so = mo_rong[col][col]
    for j in range(2 * n):
        mo_rong[col][j] = mo_rong[col][j] / he_so

    for row in range(n):
        if row != col and mo_rong[row][col] != 0:
            ti_le = mo_rong[row][col]
            for j in range(2 * n):
                mo_rong[row][j] = mo_rong[row][j] - ti_le * mo_rong[col][j]

if not kha_nghich:
    print("Ma tran suy bien, khong co ma tran nghich dao.")
else:
    ma_tran_nghich = []
    for i in range(n):
        hang = []
        for j in range(n, 2 * n):
            hang.append(round(mo_rong[i][j], 4))
        ma_tran_nghich.append(hang)

    print("Ma tran nghich dao:")
    for hang in ma_tran_nghich:
        print(hang)