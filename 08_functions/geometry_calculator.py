#yukarıdaki işlemin geometrik şekil ile
print("********************")
print("* geometrik şekil  *")
print("********************")
print("*    1 kare        *")
print("*    2 dikdörtgen  *")
print("*    3 daire       *")
print("********************")
print("********************")
print("*    4 alan        *")
print("*    5 çevre       *")
print("********************")

def kare_alan(s):
  return s*s

def kare_cevre(s):
  return 4*s

def dikdortgen_alan(a,b):
  return a*b

def dikdortgen_cevre(a,b):
  return 2*(a+b)

def daire_alan(r):
  return math.pi*r*r

def daire_cevre(r):
  return 2*math.pi*r

while True:
  islem=int(input("yapılacak işlemi giriniz"))
  hesap=int(input("HESAPLANACAK İŞLEMİ seçiniz"))

  if islem==1 and hesap==4:
    s1=int(input("kenar uzunluğunu giriniz"))
    print("alan",kare_alan(s1))
    break
  elif islem==1 and hesap==5:
    s1=int(input("kenar uzunluğunu giriniz"))
    print("çevre",kare_cevre(s1))
    break

  elif islem==2 and hesap==4:
    s1=int(input("kısa kenar uzunluğunu giriniz"))
    s2=int(input("uzun kenar uzunluğunu giriniz"))
    print("alan",dikdortgen_alan(s1,s2))
    break

  elif islem==2 and hesap==5:
    s1=int(input("kısa kenar uzunluğunu giriniz"))
    s2=int(input("uzun kenar uzunluğunu giriniz"))
    print("çevre",dikdortgen_cevre(s1,s2))
    break

  elif islem==3 and hesap==4:
    s1=int(input("yarı çapı giriniz"))
    print("alan",daire_alan(s1))
    break

  elif islem==3 and hesap==5:
    s1=int(input("yarı çapı giriniz"))
    print("çevre",daire_cevre(s1))
    break

  else:
    print("yanlış değer girdiniz")
