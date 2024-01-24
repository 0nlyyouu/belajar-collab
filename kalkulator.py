def tambah(x, y):
  return x + y
def kurang(bil_a, bil_b):
  return bil_a - bil_b
def kali(a, b):
  return a * b
def bagi(ang1, ang2):
  return ang1 / ang2
def modulus(mod1, mod2):
  return mod1 % mod2

print("Pilih Operasi : ")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")
print("5. Sisa Bagi")

pilihan = input("Masukkan pilihan (1/2/3/4/5) : ")

if pilihan in ("1","2","3","4","5"):
  angka1 = int(input("Masukkan bilangan pertama : "))
  angka2 = int(input("Masukkan bilangan kedua : "))

  if pilihan == "1":
    print(angka1, "+", angka2, "=", tambah(angka1, angka2))
  elif pilihan == "2":
    print(angka1, "-", angka2, "=", kurang(angka1, angka2))
  elif pilihan == "3":
    print(angka1, "*", angka2, "=", kali(angka1, angka2))
  elif pilihan == "4":
    print(angka1, ":", angka2, "=", bagi(angka1, angka2))
  elif pilihan == "5":
      print(angka1, "%", angka2, "=", modulus(angka1, angka2))
else:
    print("Pilihan tidak valid")

