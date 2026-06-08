gun = input("Günü giriniz: ").lower()

if gun in ["pazartesi", "salı", "çarşamba", "perşembe", "cuma"]:
    print("7:00 alarmını kurdun")
elif gun in ["cumartesi", "pazar"]:
    print("9:30 alarmını kurdun")
else:
    print("Hatalı değer girdiniz")
