#8.1
def la_nguyen_to(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i = i + 1
    return True

print("Cac cap so nguyen to sinh doi (< 1000):")
cap_sinh_doi = []
for p in range(2, 998):
    if la_nguyen_to(p) and la_nguyen_to(p + 2):
        cap_sinh_doi.append((p, p + 2))

for cap in cap_sinh_doi:
    print(" ", cap)
print("Tong so cap:", len(cap_sinh_doi))


#8.2
def giai_thua(n):
    if n == 0 or n == 1:
        return 1
    ket_qua = 1
    for i in range(2, n + 1):
        ket_qua = ket_qua * i
    return ket_qua

n = int(input("Nhap so nguyen duong de tinh giai thua: "))
print(str(n) + "! =", giai_thua(n))


#8.3
def hoan_vi(n, r):
    if r > n:
        return 0
    return giai_thua(n) // giai_thua(n - r)

def to_hop(n, r):
    if r > n:
        return 0
    return giai_thua(n) // (giai_thua(r) * giai_thua(n - r))

n = int(input("Nhap n: "))
r = int(input("Nhap r: "))
print("Hoan vi P(" + str(n) + "," + str(r) + ") =", hoan_vi(n, r))
print("To hop  C(" + str(n) + "," + str(r) + ") =", to_hop(n, r))


#8.4
def cubesum(n):
    tong = 0
    chuoi_so = str(n)
    for ky_tu in chuoi_so:
        chu_so = int(ky_tu)
        tong = tong + chu_so ** 3
    return tong

n = int(input("Nhap so nguyen de tinh cubesum: "))
print("Cubesum(" + str(n) + ") =", cubesum(n))


#8.5
def isArmstrong(n):
    return n == cubesum(n)

print("Cac so Armstrong (3 chu so, cubesum bang chinh no):")
danh_sach_armstrong = []
for so in range(100, 1000):
    if isArmstrong(so):
        danh_sach_armstrong.append(so)

print(danh_sach_armstrong)


#8.6
def sumPdivisors(n):
    if n < 2:
        return 0
    tong_uoc = 1
    i = 2
    while i * i <= n:
        if n % i == 0:
            tong_uoc = tong_uoc + i
            if i != n // i:
                tong_uoc = tong_uoc + n // i
        i = i + 1
    return tong_uoc

n = int(input("Nhap so nguyen duong de tinh tong uoc thuc su: "))
print("Tong uoc thuc su cua", n, "=", sumPdivisors(n))


#8.7
def is_amicable(a, b):
    return a != b and sumPdivisors(a) == b and sumPdivisors(b) == a

a = int(input("Nhap so thu nhat: "))
b = int(input("Nhap so thu hai : "))
if is_amicable(a, b):
    print(a, "va", b, "la cap so amicable.")
else:
    print(a, "va", b, "khong phai cap so amicable.")


#8.8
mang = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

so_chan = list(filter(lambda x: x % 2 == 0, mang))
so_le   = list(filter(lambda x: x % 2 != 0, mang))

print("Mang goc :", mang)
print("So chan  :", so_chan)
print("So le    :", so_le)


#8.9
lap_phuong = list(map(lambda x: x ** 3, mang))

print("Mang goc     :", mang)
print("Lap phuong   :", lap_phuong)


#8.10
lap_phuong_chan = list(map(lambda x: x ** 3, filter(lambda x: x % 2 == 0, mang)))
binh_phuong_le  = list(map(lambda x: x ** 2, filter(lambda x: x % 2 != 0, mang)))

print("Lap phuong cua so chan:", lap_phuong_chan)
print("Binh phuong cua so le :", binh_phuong_le)