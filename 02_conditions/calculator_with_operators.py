# Calculator using operator selection

s1 = int(input("Bir sayı giriniz: "))
sembol = input("Yapılacak işlemin sembolünü giriniz (+, -, *, /): ")
s2 = int(input("Bir sayı giriniz: "))

if sembol == "/":
    sonuc = s1 / s2
elif sembol == "*":
    sonuc = s1 * s2
elif sembol == "-":
    sonuc = s1 - s2
elif sembol == "+":
    sonuc = s1 + s2
else:
    sonuc = None
    print("Hatalı değer girdiniz.")

if sonuc is not None:
    print("Sonuç =", sonuc)
