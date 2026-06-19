while True:
    print("\n---yo selamat datang---\n===di kalkulator CLI===\n     press enter")
    hint = input(" ")
    if hint == "":
        print("sekedar info, kalo mau lanjut dimana pun\ntinggal pencet enter aja ya")
    # permision decision
    permision = input(" ")
    if permision == "":
        print("kenapa kau kesini bung?")

    answerList = ["1. karena ingin belajar", "2. karena bosan", "3. karena ingin menghitung"]
    for answer in answerList:
        print(answer)

    userAnswer = input("(1/2/3): ")
    if userAnswer == "1":
        print("\nlah tumben.")
    elif userAnswer == "2":
        print("\naku sudah menduganya.")
    elif userAnswer == "3":
        print("\nkayak yang iya aja -_-.")
    else:
        print("\nyang bener mpruy ;(.")
        continue

    delay = input(" ")
    if delay == "":
        print("yaudah daripada lama.\ntuh pilih mau yang mana")

    # masuk ke operasi
    def tambah(x, y):
        return x + y

    def kurang(x, y):
        return x - y

    def kali(x, y):
        return x * y

    def bagi(x, y):
        if y != 0:
            return x / y
        else:
            print("\npernah belajar gak sih?.")
            return False

    def eksponensial(x, y):
        return x ** y

    aritmetikList = ["1. Penjumlahan", 
                    "2. Pengurangan", 
                    "3. Perkalian",  
                    "4. Pembagian", 
                    "5. Eksponensial", 
                    "6. keluar"]
    for aritmetik in aritmetikList:
        print(aritmetik)    

    # operasi
    pilihOp = int(input("(1/2/3/4/5/6): "))

    if pilihOp == 1: 
        x = float(input("\nmasukan angka pertama: "))
        y = float(input("masukan angka kedua: "))

        print("\nhasil:", int(tambah(x, y)))
    elif pilihOp == 2:
        x = float(input("\nmasukan angka pertama: "))
        y = float(input("masukan angka kedua: "))

        print("\nhasil:", int(kurang(x, y)))
    elif pilihOp == 3:
        x = float(input("\nmasukan angka pertama: "))
        y = float(input("masukan angka kedua: "))

        print("\nhasil:", int(kali(x, y)))
    elif pilihOp == 4:
        x = float(input("\nmasukan angka pertama: "))
        y = float(input("masukan angka kedua: "))

        print("\nhasil:", bagi(x, y))
    elif pilihOp == 5:
        x = float(input("\nmasukan angka pertama: "))
        y = float(input("mau pangkat berapa?: "))
        print("\nhasil:", float(eksponensial(x, y)))
    elif pilihOp == 6:
        print("yaudah, makasih udah mampir.")
        break

    finishInput = input(" ")
    if finishInput == "":
        continue