# angka = 1

# while angka > 0 and angka < 11:
#     angka = int(input("Masukkan bilangan bulat: "))
#     if angka >= 1:
#         print("Bilangan Positif")
#     elif angka < 0:
#         print("Bilangan Negatif")
#     else:
#         print("Bilangan Nol")

while True:
    nama = input("Masukkan nama Anda: ")

    if nama == "x":
        break
    elif nama == "Adi":
        continue

    print("Selamat datang ", nama)
