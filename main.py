import func

while True:
    print("\nMİNİ Hesap Makinesine Hoş Geldiniz")
    print("1) Toplama")
    print("2) Çıkarma")
    print("0) Çıkış")

    user = input("\nHangi işlemi yapmak istersiniz: ")

    if user == "1":
        num1 = input("Lütfen 1. sayıyı giriniz: ")
        num2 = input("Lütfen 2. sayıyı giriniz: ")
        result = func.topla(int(num1),int(num2))
        print(f"Sonucunuz: {result}")
        while True:
            print("Başka sayı istemiyorsanız * yazınız.")
            num3 = input("Başka sayı giriniz:")
            if num3 == "*":
                break
            else:
                result = func.topla(result, int(num3))
                print(f"Sonucunuz: {result}")

    elif user == "2":
        print("Bu fonksiyon henüz çalışmamaktadır.")
    elif user == "0":
        exit()
    else:
        print("Yanlış rakam girdiniz. Lütfen tekrar deneyin.")