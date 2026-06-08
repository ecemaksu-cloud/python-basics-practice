admin_username = "admin123"
admin_password = "pass123"

user = input("Kullanıcı adını giriniz: ")
passw = input("Şifreyi giriniz: ")

if admin_username == user and admin_password == passw:
    print("Sisteme giriş yaptınız.")
else:
    print("Yanlış giriş yaptınız.")
